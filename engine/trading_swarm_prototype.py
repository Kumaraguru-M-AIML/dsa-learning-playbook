# C:\Master db\R&D workspace\NEW\engine\trading_swarm_prototype.py
"""
CQ Mythos v6.0 - TDS-X Asymmetric Trading Swarm Prototype (B.L.U.E. System)
Combines:
1. Alternative Data Intake (Web Crawler Simulation)
2. Bayesian Critic (Filtering Noise/Hallucinations)
3. Honardoust Early Warning (Market Pressure & Instability Index)
4. Position Risk Governor (1% Portfolio Lock)
"""

import time
import random
import math
import json
from datetime import datetime

class BayesianCritic:
    """
    TDS-X Bayesian Critic Agent
    Calculates the posterior probability that a trading signal is valid alpha
    rather than algorithmic noise using iterative evidence updating.
    """
    def __init__(self, prior_probability=0.5):
        self.prior = prior_probability  # Start with a balanced prior (50%)

    def update_probability(self, prior, p_evidence_given_alpha, p_evidence_given_noise):
        """
        Applies Bayes' Theorem:
        P(Alpha|Evidence) = P(Evidence|Alpha) * P(Alpha) / P(Evidence)
        """
        # P(Noise) = 1 - P(Alpha)
        p_noise = 1.0 - prior
        
        # Total Probability of Evidence = P(E|A)*P(A) + P(E|N)*P(N)
        total_p_evidence = (p_evidence_given_alpha * prior) + (p_evidence_given_noise * p_noise)
        
        if total_p_evidence == 0:
            return 0.0
            
        posterior = (p_evidence_given_alpha * prior) / total_p_evidence
        return posterior

    def evaluate_signals(self, signals):
        """
        Evaluates a batch of signal evidence sequentially updating the probability score.
        """
        current_prob = self.prior
        print(f"  [Critic] Initial Prior Confidence: {current_prob*100:.1f}%")
        
        for signal in signals:
            name = signal["name"]
            type_sig = signal["type"]
            strength = signal["strength"] # 0.0 to 1.0
            
            # Map credibility based on signal origin (Alternative Data has higher reliability than generic social media)
            if type_sig == "alt_data": # E.g., Supply chain leak
                p_given_alpha = 0.85 * strength
                p_given_noise = 0.15
            elif type_sig == "technical": # E.g., Moving average cross
                p_given_alpha = 0.60 * strength
                p_given_noise = 0.40
            else: # Social Sentiment
                p_given_alpha = 0.55 * strength
                p_given_noise = 0.45
                
            current_prob = self.update_probability(current_prob, p_given_alpha, p_given_noise)
            print(f"  ├─ Evidence Digested: '{name}' -> Updated Confidence: {current_prob*100:.2f}%")
            
        return current_prob

class InstabilityMonitor:
    """
    Honardoust-Inspired Market Pressure Early Warning System
    Monitors macro 'instability vectors' to detect systemic crash risks.
    """
    def __init__(self, threshold=0.70):
        self.threshold = threshold
        
    def calculate_pressure(self, vix_level, yield_curve_spread, liquidity_score):
        """
        Calculates a composite Market Pressure Index.
        Normalized 0.0 (Stable) to 1.0 (High Instability)
        """
        # Simple normalization functions
        vix_pressure = min(vix_level / 40.0, 1.0) # VIX over 40 is extreme fear
        yield_pressure = max(0, (1.0 - max(0, yield_curve_spread + 0.5))) # Inverted curve increases pressure
        liquidity_pressure = 1.0 - liquidity_score # Low liquidity = high pressure
        
        # Weighted index
        pressure_index = (vix_pressure * 0.4) + (yield_pressure * 0.3) + (liquidity_pressure * 0.3)
        return pressure_index

class RiskGovernor:
    """
    Controls position sizing and enforces hard drawdown limits.
    """
    def __init__(self, total_equity=10000.0, max_risk_per_trade=0.01):
        self.equity = total_equity
        self.max_risk = max_risk_per_trade # Max 1% rule

    def calculate_position(self, entry_price, stop_loss):
        if entry_price <= stop_loss:
            return 0
            
        risk_dollars = self.equity * self.max_risk
        risk_per_share = entry_price - stop_loss
        shares = math.floor(risk_dollars / risk_per_share)
        
        total_cost = shares * entry_price
        return {
            "shares": shares,
            "risk_dollars": risk_dollars,
            "total_cost": total_cost,
            "percent_equity": (total_cost / self.equity) * 100
        }

class TradingSwarmPrototype:
    def __init__(self):
        self.critic = BayesianCritic(prior_probability=0.5)
        self.instability = InstabilityMonitor(threshold=0.65)
        self.risk = RiskGovernor(total_equity=25000.0, max_risk_per_trade=0.01)
        
    def execute_cycle(self, asset_ticker, current_price, simulated_environment):
        print("=========================================================")
        print(f" 🛰️ [TDS-X SWARM CYCLE] Target: {asset_ticker} | Time: {datetime.now().strftime('%H:%M:%S')}")
        print("=========================================================")
        
        # PHASE 1: Early Warning / Instability Scan
        env = simulated_environment
        pressure = self.instability.calculate_pressure(
            vix_level=env["vix"],
            yield_curve_spread=env["spread"],
            liquidity_score=env["liquidity"]
        )
        
        print(f"🛡️ [PHASE 1] Scanning Systemic Instability (Honardoust Engine)")
        print(f"  ├─ Market Pressure Index: {pressure:.4f}")
        
        if pressure >= self.instability.threshold:
            print("  🚨 [SYSTEMIC INSTABILITY DETECTED] Aborting all buy orders!")
            print("  🛑 [RISK OVERRIDE] Locking system to CASH MODE to prevent liquidation.")
            return {"action": "LOCKOUT", "reason": "High Systemic Pressure"}
            
        print("  ✓ Systemic metrics within bounds. Proceeding to Signal Ingestion.")
        
        # PHASE 2: Crawled Evidence Ingestion
        print(f"\n🔍 [PHASE 2] Digesting Crawled Signals (Alternative Data)")
        confidence = self.critic.evaluate_signals(env["signals"])
        
        # Validation Threshold (needs to cross 75% posterior probability to trade)
        if confidence < 0.75:
            print(f"\n❌ [PHASE 3] Execution Denied.")
            print(f"  └─ Critic Verdict: Signal confidence ({confidence*100:.1f}%) is too low. High probability of NOISE.")
            return {"action": "HOLD", "confidence": confidence}
            
        print(f"\n🎯 [PHASE 3] Signal Validated by Bayesian Critic: {confidence*100:.2f}% Confidence.")
        
        # PHASE 4: Risk Allocation & Sizing
        print(f"\n⚖️ [PHASE 4] Calculating Position Metrics (Risk Governor)")
        stop_loss = current_price * 0.97 # Strict 3% hard stop
        position = self.risk.calculate_position(current_price, stop_loss)
        
        print(f"  ├─ Max Risk (1% of Equity): ${position['risk_dollars']:.2f}")
        print(f"  ├─ Entry Target: ${current_price:.2f} | Stop-Loss: ${stop_loss:.2f}")
        print(f"  ├─ Order Size: {position['shares']} shares")
        print(f"  └─ Total Exposure: ${position['total_cost']:.2f} ({position['percent_equity']:.2f}% of Equity)")
        
        print(f"\n⚡ [EXECUTION ENGINE] TRANSMITTING ORDER TO API...")
        print(f"  >>> BUY {position['shares']} {asset_ticker} @ MARKET LIMIT ${current_price:.2f}")
        
        return {
            "action": "BUY",
            "ticker": asset_ticker,
            "shares": position["shares"],
            "cost": position["total_cost"],
            "confidence": confidence
        }

if __name__ == "__main__":
    swarm = TradingSwarmPrototype()
    
    # SCENARIO A: Bullish Alternative Data / Stable Market
    print("\n[🚀 SIMULATING SCENARIO A: BULLISH SIGNAL / STABLE ENVIRONMENT]")
    scenario_a_env = {
        "vix": 16.5,      # Stable
        "spread": 0.85,   # Healthy curve
        "liquidity": 0.9, # Deep market
        "signals": [
            {"name": "Reddit Trend Analysis", "type": "sentiment", "strength": 0.80},
            {"name": "Supply Chain Port Congestion Drop", "type": "alt_data", "strength": 0.90},
            {"name": "50-day moving average cross", "type": "technical", "strength": 0.75}
        ]
    }
    swarm.execute_cycle("NVDA", current_price=125.50, simulated_environment=scenario_a_env)
    
    time.sleep(1)
    
    # SCENARIO B: High Noise Signal / Low Confidence
    print("\n[💤 SIMULATING SCENARIO B: WEAK SOCIAL SIGNALS / NOISY ENVIRONMENT]")
    scenario_b_env = {
        "vix": 19.0,
        "spread": 0.70,
        "liquidity": 0.8,
        "signals": [
            {"name": "Viral Tweet on Stock", "type": "sentiment", "strength": 0.95}, # High hype, low data
            {"name": "Technical RSI Oversold", "type": "technical", "strength": 0.50}
        ]
    }
    swarm.execute_cycle("TSLA", current_price=180.00, simulated_environment=scenario_b_env)
    
    time.sleep(1)
    
    # SCENARIO C: Highly Bullish Signals but Systemic Collapse (Flash Crash Imminent)
    print("\n[🚨 SIMULATING SCENARIO C: EXCELLENT SIGNALS BUT SYSTEMIC INSTABILITY DETECTED]")
    scenario_c_env = {
        "vix": 42.0,      # CRITICAL VOLATILITY
        "spread": -0.45,  # INVERTED CURVE
        "liquidity": 0.3, # ILLIQUID
        "signals": [
            {"name": "Record Quarterly Revenue Leaked", "type": "alt_data", "strength": 0.98} # Highly positive but market is crashing
        ]
    }
    swarm.execute_cycle("AAPL", current_price=210.25, simulated_environment=scenario_c_env)

# C:\Master db\R&D workspace\NEW\cq_bench\mythos_dashboard.py
import os
import sys
import json

try:
    sys.stdout.reconfigure(encoding='utf-8')
except AttributeError:
    pass

class MythosObservabilityDashboard:
    """
    CQ Mythos v5.0 Observability Dashboard.
    Generates rich, terminal-based visual telemetry, tracking entropy curves,
    confidence metrics, active contradictions, and rollback events.
    """
    def __init__(self):
        pass

    def draw_entropy_curve(self, metrics_history):
        """Draws a beautiful terminal ASCII line chart representing the entropy curve over time."""
        print("\n📈" + "="*70 + "📈")
        print(" 🔍 CQ MYTHOS REAL-TIME ENTROPY TELEMETRY CURVE")
        print("📈" + "="*70 + "📈")
        
        # We plot a slice of the history (last 15 steps)
        history_slice = metrics_history[-15:] if len(metrics_history) > 15 else metrics_history
        
        for index, item in enumerate(history_slice):
            step = item.get("step", index + 1)
            entropy = item.get("entropy", 0.0)
            rollbacks = item.get("rollbacks", 0)
            
            bar_length = int(entropy * 40)
            bar_str = "█" * bar_length
            padding = " " * (40 - bar_length)
            
            rollback_flag = "🚨 [ROLLBACK]" if rollbacks > 0 else ""
            print(f"  Step {step:02d} | {bar_str}{padding} | {entropy:.4f} {rollback_flag}")

    def render_epistemic_scoreboard(self, belief_state, active_contradictions):
        """Renders the current epistemic distribution and contradiction links."""
        print("\n📊" + "="*70 + "📊")
        print(" 🔍 CURRENT EPISTEMIC STATE SUMMARY")
        print("📊" + "="*70 + "📊")
        print("  [Active Belief Distribution]")
        for label, prob in belief_state.items():
            bar = "█" * int(prob * 30)
            print(f"    ├─ {label:28s} : {bar:<30s} {prob:.4f}")
            
        print("\n  [Active Contradictions]")
        if active_contradictions:
            for source, target in active_contradictions:
                print(f"    ❌ '{source}' Mutually Excluded from '{target}'")
        else:
            print("    ✓ None. Epistemic state is fully stable.")
            
        print("="*72)

if __name__ == "__main__":
    dashboard = MythosObservabilityDashboard()
    
    # Testing with simulated 10-step history
    sim_history = [
        {"step": 1, "entropy": 0.10, "rollbacks": 0},
        {"step": 2, "entropy": 0.12, "rollbacks": 0},
        {"step": 3, "entropy": 0.15, "rollbacks": 0},
        {"step": 4, "entropy": 0.38, "rollbacks": 1}, # Entropy spikes, triggers rollback
        {"step": 5, "entropy": 0.11, "rollbacks": 0}, # Successfully recovered
        {"step": 6, "entropy": 0.14, "rollbacks": 0}
    ]
    dashboard.draw_entropy_curve(sim_history)
    
    # Testing epistemic scoreboard
    sim_beliefs = {
        "Hypothesis A (RTX 3050)": 0.6522,
        "Hypothesis B (RTX 4050)": 0.3478,
        "Hypothesis C (Poisoned)": 0.0000
    }
    sim_contradictions = [("Hypothesis A (RTX 3050)", "Hypothesis B (RTX 4050)")]
    dashboard.render_epistemic_scoreboard(sim_beliefs, sim_contradictions)

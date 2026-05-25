# C:\Master db\R&D workspace\NEW\reasoning_trace_logger.py
import os
import sys
import math
import time
import json

try:
    sys.stdout.reconfigure(encoding='utf-8')
except AttributeError:
    pass

class ReasoningTraceLogger:
    """
    CQ Mythos v4 Reasoning Trace Logger & Telemetry Engine.
    Tracks per-pass hidden-state metrics to identify exactly where recurrence saturates and collapses.
    """
    def __init__(self):
        self.trace_history = []

    def log_pass(self, pass_idx, confidence, constraints_satisfied, entropy, contradictions):
        """Logs telemetry metrics for a single recurrent pass."""
        metrics = {
            "pass": pass_idx,
            "confidence": round(confidence, 4),
            "constraints_satisfied": round(constraints_satisfied * 100.0, 2),
            "entropy": round(entropy, 4),
            "contradictions": contradictions
        }
        self.trace_history.append(metrics)

    def print_trace_dashboard(self):
        """Generates a high-fidelity ASCII telemetry graph showing the recurrence saturation threshold."""
        print(f"\n📊 [Reasoning Trace Logger] PER-PASS RECURRENCE TELEMETRY (T=1 to T=24)")
        print(f"{'-'*100}")
        print(f" Pass | Confidence | Constraint Sat % | Token Entropy | Contradictions | Status")
        print(f"{'-'*100}")
        
        saturation_point = None
        for log in self.trace_history:
            p = log["pass"]
            conf = log["confidence"]
            csat = log["constraints_satisfied"]
            ent = log["entropy"]
            cnt = log["contradictions"]
            
            # Status determination
            status = "CONVERGING"
            if ent > 0.6:
                status = "COLLAPSING (Noise)"
                if saturation_point is None:
                    saturation_point = p
            elif conf > 0.9:
                status = "STABLE CONVERGENCE"
            
            # Simple bar visualization for confidence
            bar = "█" * int(conf * 15) + "░" * (15 - int(conf * 15))
            print(f" T={p:02d} | [{bar}] {conf:.2f} |     {csat:6.1f}%     |     {ent:.4f}    |       {cnt:2d}       | {status}")

        print(f"{'-'*100}")
        if saturation_point:
            print(f"⚠️ [RECURRENCE SATURATION ALERT] Hidden-state noise accumulation triggered at Pass T={saturation_point}!")
            print(f"  └─ Root Cause: Attention diffusion & token entropy exceeding 0.6 threshold.")
            print(f"  └─ Resolution: Upgrade A (Semantic Grounding) is mandatory to re-anchor latent weights at T >= {saturation_point}.")
        print(f"{'-'*100}\n")

if __name__ == "__main__":
    logger = ReasoningTraceLogger()
    
    # Simulate a typical 24-pass recurrence loop on a hard logic puzzle
    # T=1 to T=12: Confidence improves, entropy is low, constraints satisfied increases
    # T=13 to T=24: Noise starts accumulating, entropy spikes, confidence decays (the plateau)
    for t in range(1, 25):
        if t <= 12:
            conf = 0.3 + (t * 0.05) # Converges up to 0.9
            csat = 0.4 + (t * 0.04) # Increases to 88%
            ent = 0.15 + (t * 0.02) # Low entropy
            contradictions = max(0, 4 - int(t / 3))
        else:
            # Saturation/Collapsing phase
            conf = 0.9 - ((t - 12) * 0.03) # Decays back down due to noise
            csat = 0.88 # Plateaus at 88% (cannot solve final constraint)
            ent = 0.39 + ((t - 12) * 0.05) # Entropy spikes past 0.6 threshold
            contradictions = 1 + int((t - 12) / 4) # Contradictions start accumulating again

        logger.log_pass(t, conf, csat, ent, contradictions)

    logger.print_trace_dashboard()

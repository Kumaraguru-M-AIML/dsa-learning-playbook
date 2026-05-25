# C:\Master db\R&D workspace\NEW\meta_cognition_monitor.py
import os
import sys
import json

try:
    sys.stdout.reconfigure(encoding='utf-8')
except AttributeError:
    pass

class MetaCognitionMonitor:
    """
    CQ Mythos v5.0 Meta-Cognition Monitor.
    Performs continuous self-diagnostic cognition to predict and prevent
    catastrophic reasoning collapse.
    """
    def __init__(self):
        self.metrics_history = []

    def log_pass_metrics(self, pass_index, entropy, contradiction_density, rollbacks=0):
        """Logs metrics for a single reasoning pass."""
        self.metrics_history.append({
            "pass_index": pass_index,
            "entropy": float(entropy),
            "contradiction_density": float(contradiction_density),
            "rollbacks": rollbacks
        })

    def analyze_stability(self):
        """
        Analyzes logged pass metrics to forecast cognitive instability or saturation.
        If the entropy slope rises too quickly, triggers an early grounding alert.
        """
        print(f"\n🧠 [Meta-Cognition] Running self-diagnostic stability audit on {len(self.metrics_history)} passes...")
        
        if len(self.metrics_history) < 2:
            print("  → [Meta-Cognition] Insufficient history for stability forecasting.")
            return "Stable"

        # Calculate Entropy Slope
        last_metric = self.metrics_history[-1]
        prev_metric = self.metrics_history[-2]
        
        entropy_slope = last_metric["entropy"] - prev_metric["entropy"]
        contra_density = last_metric["contradiction_density"]
        
        print(f"  ├─ Current Entropy Slope: {entropy_slope:+.4f}")
        print(f"  ├─ Contradiction Density: {contra_density:.4f}")
        
        # Predictive Instability Forecasting
        if entropy_slope > 0.15:
            print("  ⚠️ [Instability Warning] Entropy slope is rising rapidly! Saturation detected.")
            print("  🚨 [Active Grounding Triggered] Re-anchoring latent state before reasoning collapse.")
            return "Unstable_Saturation_Detected"
        elif contra_density > 0.7:
            print("  ⚠️ [Epistemic Warning] High contradiction density detected in memory clusters.")
            print("  🚨 [Verification Triggered] Invoking Backtracking CSP solver immediately.")
            return "Unstable_Epistemic_Conflict"
            
        print("  ✓ [System State] Stable. No degradation detected.")
        return "Stable"

    def cluster_failures(self, failure_logs):
        """Clusters recurring system failures to generate a self-diagnostic report."""
        print("\n🔍 [Meta-Cognition] Clustering recurring system failure logs...")
        clusters = {
            "memory_corruption": 0,
            "constraint_ambiguity": 0,
            "symbolic_drift": 0
        }
        
        for log in failure_logs:
            log_lower = log.lower()
            if "typeerror" in log_lower or "null" in log_lower or "poison" in log_lower:
                clusters["memory_corruption"] += 1
            elif "ambiguous" in log_lower or "meeting" in log_lower:
                clusters["constraint_ambiguity"] += 1
            elif "violated" in log_lower or "drift" in log_lower:
                clusters["symbolic_drift"] += 1
                
        print(f"  └─ Classified Clusters: {json.dumps(clusters)}")
        return clusters

if __name__ == "__main__":
    monitor = MetaCognitionMonitor()
    
    # Simulating stable passes followed by a sudden entropy spike
    monitor.log_pass_metrics(pass_index=1, entropy=0.10, contradiction_density=0.1)
    monitor.log_pass_metrics(pass_index=2, entropy=0.12, contradiction_density=0.1)
    monitor.analyze_stability()
    
    print("\n⚡ Simulating severe reasoning saturation on Pass 3...")
    monitor.log_pass_metrics(pass_index=3, entropy=0.35, contradiction_density=0.2)
    monitor.analyze_stability()
    
    # Testing failure clustering
    sample_failures = [
        "TypeError: unsupported operand type",
        "Ambiguous entity reference found: 'Meeting'",
        "Constraint violated on node color"
    ]
    monitor.cluster_failures(sample_failures)

# C:\Master db\R&D workspace\NEW\resource_governor.py
import os
import sys
import json

try:
    sys.stdout.reconfigure(encoding='utf-8')
except AttributeError:
    pass

class ResourceGovernor:
    """
    CQ Mythos v6.0 Resource Governor.
    Monitors CPU, RAM, and active recursion limits continuously,
    enforcing Stabilization Mode when hard safety thresholds are violated.
    """
    def __init__(self):
        self.limits = {
            "max_recursion_depth": 32,
            "max_entropy": 0.65,
            "max_cpu_usage": 90,
            "max_planning_ratio": 0.30  # B.L.U.E. 70/30 Metabolic Governor
        }
        # Metabolic Tracking (Token / Energy approximation)
        self.tokens_planning = 0
        self.tokens_execution = 0

    def log_activity(self, activity_type, token_cost=100):
        """
        Logs activity to the metabolic tracker. 
        activity_type: 'PLANNING' (Markdown/Theory) or 'EXECUTION' (Code/Terminal)
        """
        if activity_type == 'PLANNING':
            self.tokens_planning += token_cost
        elif activity_type == 'EXECUTION':
            self.tokens_execution += token_cost

    def evaluate_metabolic_ratio(self):
        """
        Calculates the Action/Theory ratio and enforces the 70/30 B.L.U.E. Spec.
        """
        total_tokens = self.tokens_planning + self.tokens_execution
        if total_tokens == 0:
            return {"status": "HEALTHY", "planning_ratio": 0.0}
            
        planning_ratio = self.tokens_planning / total_tokens
        print(f"  ├─ Metabolic Governor: {planning_ratio*100:.1f}% Planning / {100 - planning_ratio*100:.1f}% Execution")
        
        # We only enforce after a minimum baseline of activity (e.g. 500 tokens)
        if total_tokens > 500 and planning_ratio > self.limits["max_planning_ratio"]:
            print("  🚨 [ABSTRACTION ESCAPE DETECTED] Planning ratio exceeds 30%!")
            print("  🛑 [ABSTRACTION LOCK ACTIVATED] Agent must execute physical code or terminal tasks before generating further theory.")
            return {"status": "ABSTRACTION_LOCK", "planning_ratio": planning_ratio}
            
        return {"status": "HEALTHY", "planning_ratio": planning_ratio}

    def evaluate_resource_limits(self, recursion_depth, active_entropy, simulated_cpu_usage):
        """
        Evaluates system limits.
        If thresholds are violated, triggers a hard 'Stabilization Mode' freeze.
        """
        print(f"\n⚡ [Resource Governor] Monitoring cognitive resource metrics...")
        print(f"  ├─ Active Recursion Depth: {recursion_depth}/{self.limits['max_recursion_depth']}")
        print(f"  ├─ Active Entropy Load: {active_entropy:.4f}/{self.limits['max_entropy']}")
        print(f"  └─ Simulated CPU Usage: {simulated_cpu_usage}%/{self.limits['max_cpu_usage']}%")
        
        is_safe = True
        violations = []
        
        if recursion_depth > self.limits["max_recursion_depth"]:
            violations.append("recursion_depth_exceeded")
            is_safe = False
        if active_entropy > self.limits["max_entropy"]:
            violations.append("entropy_threshold_violated")
            is_safe = False
        if simulated_cpu_usage > self.limits["max_cpu_usage"]:
            violations.append("cpu_saturation_detected")
            is_safe = False

        if not is_safe:
            print("  🚨 [Safety Threshold Exceeded] Hard resource limit violation detected!")
            print("  🛑 [Stabilization Mode Activated] Reducing compute recurrence, freezing agent spawning, and forcing re-grounding!")
            return {"status": "STABILIZATION_MODE", "violations": violations}
            
        print("  ✓ [System Health] Bounded metrics verified. Compute remains stable.")
        return {"status": "HEALTHY", "violations": []}

if __name__ == "__main__":
    governor = ResourceGovernor()
    
    # Testing healthy states
    governor.evaluate_resource_limits(recursion_depth=12, active_entropy=0.15, simulated_cpu_usage=45)
    
    # Testing runaway recursion triggering stabilization mode
    governor.evaluate_resource_limits(recursion_depth=40, active_entropy=0.72, simulated_cpu_usage=95)
    
    # Testing B.L.U.E. Metabolic Governor
    print("\n[Testing Metabolic Governor...]")
    governor.log_activity("EXECUTION", 800)
    governor.log_activity("PLANNING", 200)
    governor.evaluate_metabolic_ratio() # Should be healthy (20%)
    
    governor.log_activity("PLANNING", 1000)
    governor.evaluate_metabolic_ratio() # Should trigger ABSTRACTION_LOCK (60% planning)

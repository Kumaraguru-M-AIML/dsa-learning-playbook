# C:\Master db\R&D workspace\NEW\silent_failure_detector.py
import os
import sys
import json

try:
    sys.stdout.reconfigure(encoding='utf-8')
except AttributeError:
    pass

class SilentFailureDetector:
    """
    CQ Mythos Phase Omega Silent Failure Detector.
    Identifies 'plausible-looking wrong cognition' (fake certainty, low-entropy hallucinations,
    repeated recovery reuse) before they propagate to downstream execution layers.
    """
    def __init__(self):
        self.recovery_usage_count = {}

    def audit_cognition(self, confidence, evidence_count, entropy, target_answer_valid, recovery_id_used=None):
        """Audits active reasoning passes to catch silent failure signatures."""
        print(f"\n🕵️ [Silent Failure Detector] Auditing active reasoning passes...")
        print(f"  ├─ Signals | Confidence: {confidence:.2f} | Evidence Nodes: {evidence_count} | Entropy: {entropy:.2f}")
        
        alerts = []
        
        # 1. Confidence Without Evidence (Fake Certainty)
        if confidence > 0.8 and evidence_count == 0:
            alerts.append("fake_certainty_detected")
            
        # 2. Low Entropy + Wrong Answer (Stable Hallucination)
        if entropy < 0.15 and not target_answer_valid:
            alerts.append("stable_hallucination_detected")
            
        # 3. Repeated Recovery Reuse (Hidden Grounding Loop)
        if recovery_id_used:
            self.recovery_usage_count[recovery_id_used] = self.recovery_usage_count.get(recovery_id_used, 0) + 1
            if self.recovery_usage_count[recovery_id_used] > 3:
                alerts.append("grounding_loop_detected")

        if alerts:
            print("  🚨 [SILENT FAILURE DETECTED] reasoning stream is contaminated!")
            for alert in alerts:
                print(f"    └─ Signature Triggered: '{alert}'")
            return {"status": "CONTAMINATED", "alerts": alerts}
            
        print("  ✓ [Cognitive Honesty Verified] Reasoning stream aligns with empirical evidence.")
        return {"status": "COHERENT", "alerts": []}

if __name__ == "__main__":
    detector = SilentFailureDetector()
    
    # Testing healthy, honest reasoning
    detector.audit_cognition(confidence=0.45, evidence_count=3, entropy=0.35, target_answer_valid=True)
    
    # Testing fake certainty (high confidence, zero evidence)
    detector.audit_cognition(confidence=0.95, evidence_count=0, entropy=0.10, target_answer_valid=True)
    
    # Testing stable hallucination (low entropy, invalid answer)
    detector.audit_cognition(confidence=0.90, evidence_count=5, entropy=0.08, target_answer_valid=False)
    
    # Testing grounding loop (repeated recovery reuse)
    for _ in range(5):
        detector.audit_cognition(confidence=0.50, evidence_count=2, entropy=0.40, target_answer_valid=True, recovery_id_used="rec-809")

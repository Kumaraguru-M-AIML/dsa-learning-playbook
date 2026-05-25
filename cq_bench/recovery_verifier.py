# C:\Master db\R&D workspace\NEW\recovery_verifier.py
import os
import sys
import json

try:
    sys.stdout.reconfigure(encoding='utf-8')
except AttributeError:
    pass

class RecoveryVerifier:
    """
    CQ Mythos v5.0 Recovery Verification Engine.
    Ensures that every parsing fallback or memory recovery operation is validated,
    preventing silent recovery hallucinations by attaching explicit uncertainty metrics.
    """
    def __init__(self):
        pass

    def verify_recovery(self, original_raw, recovered_dict, expected_fields):
        """
        Evaluates a completed fallback recovery operation.
        Computes recovery confidence, identifies missing fields, and calculates a corruption estimate.
        """
        print("\n🛡️ [Recovery Verifier] Validating fallback recovery execution...")
        
        recovered_fields = list(recovered_dict.keys())
        missing_fields = [field for field in expected_fields if field not in recovered_fields]
        
        # Calculate Corruption Estimate & Recovery Confidence
        total_expected = len(expected_fields)
        if total_expected > 0:
            corruption_estimate = len(missing_fields) / total_expected
            recovery_confidence = 1.0 - corruption_estimate
        else:
            corruption_estimate = 0.0
            recovery_confidence = 1.0

        # Adjust confidence downwards if the raw input was severely truncated or empty
        if not original_raw or len(original_raw.strip()) == 0:
            recovery_confidence *= 0.5
            corruption_estimate = max(corruption_estimate, 0.5)

        verification_status = "VERIFIED_SAFE" if recovery_confidence > 0.7 else "VERIFIED_DEGRADED"
        if corruption_estimate > 0.5:
            verification_status = "VERIFIED_CORRUPT_FALLBACK"

        report = {
            "recovery_confidence": round(recovery_confidence, 4),
            "recovered_fields": recovered_fields,
            "missing_fields": missing_fields,
            "corruption_estimate": round(corruption_estimate, 4),
            "verification_status": verification_status
        }
        
        print(f"  ├─ Recovery Confidence: {report['recovery_confidence']:.4f}")
        print(f"  ├─ Corruption Estimate: {report['corruption_estimate']:.4f}")
        print(f"  ├─ Missing Fields: {report['missing_fields']}")
        print(f"  └─ Verification Status: {report['verification_status']}")
        
        return report

if __name__ == "__main__":
    verifier = RecoveryVerifier()
    
    # Test Case 1: Partial recovery on malformed JSON
    raw_input = '{"state": "NEW", "path": "C:\\Master db",}' # Trailing comma caused parse fail
    recovered = {"state": "NEW", "path": "C:\\Master db"}
    expected = ["state", "path", "config", "permissions"]
    
    verifier.verify_recovery(raw_input, recovered, expected)

# C:\Master db\R&D workspace\NEW\semantic_guard.py
import os
import sys
import re
import json

try:
    sys.stdout.reconfigure(encoding='utf-8')
except AttributeError:
    pass

class SemanticGuard:
    """
    CQ Mythos v4 Semantic Guard & Truth Integrity Engine.
    Detects semantically anomalous, poisoned, or impossible facts,
    preventing malicious or corrupt nodes from dominating truth resolution.
    """
    def __init__(self):
        # Known semantic schemas for key properties
        self.schemas = {
            "hardware_config": {
                "type": "string",
                "valid_patterns": [r"RTX \d{4}", r"NVIDIA GeForce", r"Intel", r"AMD"],
                "invalid_keywords": ["poison", "unknown", "corrupt", "hack", "undefined"]
            },
            "workspace_state": {
                "type": "string",
                "valid_patterns": [r"^[A-Za-z0-9_\-\/\\\:\s]+$"],
                "invalid_keywords": ["temp_leak", "null", "none"]
            }
        }

    def evaluate_plausibility(self, fact, group_name):
        """
        Calculates a semantic plausibility score [0.0 to 1.0].
        Flags anomalies if keywords or schemas are violated.
        """
        print(f"\n🛡️ [Semantic Guard] Evaluating fact integrity: '{fact}' (Group: '{group_name}')")
        schema = self.schemas.get(group_name)
        if not schema:
            print("  → [Semantic Guard] No specific schema found. Assigning baseline plausibility.")
            return 0.7, False # Baseline plausibility for unmapped schemas

        plausibility = 1.0
        anomaly_detected = False

        # Check for banned keywords
        for keyword in schema.get("invalid_keywords", []):
            if keyword.lower() in fact.lower():
                plausibility -= 0.6
                anomaly_detected = True
                print(f"  ❌ [Anomaly Detected] Fact contains banned keyword: '{keyword}'")

        # Check valid regex patterns
        matched_any = False
        for pattern in schema.get("valid_patterns", []):
            if re.search(pattern, fact, re.IGNORECASE):
                matched_any = True
                break

        if not matched_any and schema.get("valid_patterns"):
            plausibility -= 0.4
            anomaly_detected = True
            print("  ❌ [Anomaly Detected] Fact violates expected pattern schema.")

        plausibility = max(0.0, min(1.0, plausibility))
        print(f"  └─ Plausibility Score: {plausibility:.2f} | Anomaly Flag: {anomaly_detected}")
        return plausibility, anomaly_detected

if __name__ == "__main__":
    guard = SemanticGuard()
    
    # Run evaluations on structured facts
    test_cases = [
        ("Hardware Target: GPU = RTX 3050 6GB Laptop", "hardware_config"),
        ("Hardware Target: GPU = Poisoned_Node", "hardware_config"),
        ("Active Workspace Path is NEW", "workspace_state")
    ]
    
    for fact, group in test_cases:
        guard.evaluate_plausibility(fact, group)

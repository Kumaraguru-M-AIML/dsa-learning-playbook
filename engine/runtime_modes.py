# C:\Master db\R&D workspace\NEW\runtime_modes.py
import os
import sys
import json

try:
    sys.stdout.reconfigure(encoding='utf-8')
except AttributeError:
    pass

class RuntimeModes:
    """
    CQ Mythos Phase Sigma Runtime Modes.
    Scales cognitive depth, active modules, and telemetry dynamically based on workloads.
    """
    def __init__(self):
        self.active_mode = "ENGINEERING"

    def set_mode(self, mode_name):
        valid_modes = ["LIGHTWEIGHT", "ENGINEERING", "ADVERSARIAL", "AUTONOMOUS", "SAFE_MODE"]
        if mode_name in valid_modes:
            self.active_mode = mode_name
            print(f"\n🔄 [Runtime Modes] System transitioned to mode '{mode_name}'")
        else:
            raise ValueError(f"Invalid mode {mode_name}")

    def get_active_parameters(self):
        """Returns parameters matched to current runtime mode."""
        if self.active_mode == "LIGHTWEIGHT":
            return {"passes": 4, "telemetry": "LOW", "modules": ["semantic_guard"]}
        elif self.active_mode == "ENGINEERING":
            return {"passes": 16, "telemetry": "HIGH", "modules": ["semantic_guard", "grounding"]}
        elif self.active_mode == "ADVERSARIAL":
            return {"passes": 24, "telemetry": "VERBOSE", "modules": ["semantic_guard", "grounding", "symbolic_solver"]}
        elif self.active_mode == "AUTONOMOUS":
            return {"passes": 32, "telemetry": "CONTINUOUS", "modules": ["semantic_guard", "grounding", "symbolic_solver", "failure_memory"]}
        elif self.active_mode == "SAFE_MODE":
            return {"passes": 2, "telemetry": "EMERGENCY", "modules": ["semantic_guard"]}

if __name__ == "__main__":
    modes = RuntimeModes()
    
    # Standard engineering mode
    modes.set_mode("ENGINEERING")
    print(f"  └─ Config: {modes.get_active_parameters()}")
    
    # Adversarial mode
    modes.set_mode("ADVERSARIAL")
    print(f"  └─ Config: {modes.get_active_parameters()}")
    
    # Safe Mode containment under stress
    modes.set_mode("SAFE_MODE")
    print(f"  └─ Config: {modes.get_active_parameters()}")

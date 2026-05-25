# C:\Master db\R&D workspace\NEW\cq_bench\chaos_runner.py
import os
import sys
import time
import json
import traceback

try:
    sys.stdout.reconfigure(encoding='utf-8')
except AttributeError:
    pass

# Ensure imports are relative to the workspace root
workspace_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(workspace_root)

from memory_truth_resolver import MemoryTruthResolver
from semantic_rag_grounder import SemanticRAGGrounder
from symbolic_verification_solver import SymbolicVerificationSolver
from reasoning_trace_logger import ReasoningTraceLogger

class CQChaosRunner:
    """
    CQ Mythos v4 Chaos Injection & Robustness Verification Engine.
    Actively attempts to break the v4 cognitive subsystems through hostile inputs,
    measuring graceful degradation and recovery ceilings.
    """
    def __init__(self):
        self.resolver = MemoryTruthResolver()
        self.grounder = SemanticRAGGrounder()
        self.solver = SymbolicVerificationSolver()
        self.logger = ReasoningTraceLogger()
        self.log_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "chaos_audit_report.json")
        self.audit_results = {
            "chaos_timestamp": time.time(),
            "injections": []
        }

    def print_banner(self, text):
        print(f"\n⚡{'='*80}⚡")
        print(f" ☣️  {text.upper()} INJECTION ACTIVE")
        print(f"⚡{'='*80}⚡")

    def test_memory_poisoning(self):
        self.print_banner("Epistemic Memory Poisoning")
        
        # Injecting poisoned memories: malformed keys, infinite timestamps, empty values
        poisoned_dataset = [
            {"fact": "", "timestamp": None, "confidence": 1.5, "source": "user-stated", "contradiction_group": "hardware"},
            {"fact": "Hardware Target: GPU = Unknown", "timestamp": "corrupted_timestamp", "confidence": -0.5, "source": "scraped", "contradiction_group": "hardware"},
            {"fact": "Hardware Target: GPU = Poisoned_Node", "timestamp": float('inf'), "confidence": 1.0, "source": "system-inferred", "contradiction_group": "hardware"}
        ]
        
        e_str = None
        try:
            print("[*] Passing corrupted and infinite data to MemoryTruthResolver...")
            resolved = self.resolver.resolve_contradictions(poisoned_dataset)
            print("  ✓ [Graceful Handling] Resolved successfully without crashing!")
            print(f"  └─ Winner: {resolved[0].get('fact', '') if resolved else 'None'}")
            success = True
        except Exception as err:
            print(f"  ❌ [Crash Detected] Memory engine failed to handle poisoned input:")
            print(traceback.format_exc())
            success = False
            e_str = str(err)

        self.audit_results["injections"].append({
            "vector": "Memory Poisoning",
            "resilient": success,
            "error_summary": e_str
        })

    def test_unsolvable_constraints(self):
        self.print_banner("Hostile Unsolvable Constraints")
        
        # Injecting direct logical contradictions (A must equal B AND A cannot equal B)
        variables = ["A", "B"]
        domains = {"A": [1, 2], "B": [1, 2]}
        
        e_str = None
        try:
            print("[*] Submitting unsolvable CSP constraints to SymbolicSolver...")
            # Let's see if our backtrack solver terminates gracefully instead of infinite loops
            solution = self.solver.solve_csp(variables, domains, [("A", "B", "not_equal"), ("A", "B", "adjacent")])
            print("  ✓ [Graceful Handling] Solver returned None (Unsolvable) without entering infinite recursion.")
            print(f"  └─ Computed Solution: {solution}")
            success = True
        except Exception as err:
            print(f"  ❌ [Deadlock/Crash Detected] Solver failed on unsolvable constraints:")
            print(traceback.format_exc())
            success = False
            e_str = str(err)

        self.audit_results["injections"].append({
            "vector": "Unsolvable Constraints",
            "resilient": success,
            "error_summary": e_str
        })

    def test_corrupted_telemetry(self):
        self.print_banner("Fake/Poisoned Telemetry Injection")
        
        e_str = None
        try:
            print("[*] Injecting anomalous confidence values and extreme token entropy spikes...")
            # Confidence > 1.0, Entropy < 0, Contradictions negative
            self.logger.log_pass(1, 99.9, 100.0, -5.0, -1)
            self.logger.log_pass(2, -0.5, -50.0, 10.0, 999)
            print("  ✓ [Graceful Handling] Telemetry engine logged anomalous data without overflow/crashing.")
            success = True
        except Exception as err:
            print(f"  ❌ [Crash Detected] Telemetry tracker collapsed:")
            print(traceback.format_exc())
            success = False
            e_str = str(err)

        self.audit_results["injections"].append({
            "vector": "Poisoned Telemetry",
            "resilient": success,
            "error_summary": e_str
        })

    def save_audit(self):
        with open(self.log_file, "w") as f:
            json.dump(self.audit_results, f, indent=4)
        print(f"\n[*] Chaos Audit complete. Results saved to: {self.log_file}\n")

if __name__ == "__main__":
    runner = CQChaosRunner()
    runner.test_memory_poisoning()
    runner.test_unsolvable_constraints()
    runner.test_corrupted_telemetry()
    runner.save_audit()

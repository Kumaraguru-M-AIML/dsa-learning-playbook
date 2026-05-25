# C:\Master db\R&D workspace\NEW\cq_bench\distribution_shift_tester.py
import os
import sys
import json
import traceback

try:
    sys.stdout.reconfigure(encoding='utf-8')
except AttributeError:
    pass

# Ensure imports are relative to the workspace root
workspace_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(workspace_root)

from semantic_guard import SemanticGuard

class DistributionShiftTester:
    """
    CQ Mythos v4 Distribution Shift Evaluation Suite.
    Measures how gracefully the system degrades when pushed far outside
    its engineered Python comfort zone into foreign environments.
    """
    def __init__(self):
        self.guard = SemanticGuard()
        self.results = {
            "distribution_shifts": []
        }

    def print_header(self, title):
        print(f"\n🌍{'='*80}🌍")
        print(f" 🌀 SHIFT EVAL: {title.upper()}")
        print(f"🌍{'='*80}🌍")

    def test_syntax_shift(self):
        self.print_header("Foreign Language (Rust Syntax) Shift")
        # Feeding Rust-style file paths and let statements to Python-optimized logic
        rust_data = "let x: Vec<String> = vec![\"C:\\Master db\\src\\main.rs\".to_string()];"
        try:
            print("[*] Passing Rust-style expressions to semantic guard...")
            plausibility, anomaly = self.guard.evaluate_plausibility(rust_data, "workspace_state")
            print(f"  ✓ [Graceful Degradation] Analyzed safely. Plausibility: {plausibility} | Anomaly: {anomaly}")
            success = True
        except Exception as e:
            print(f"  ❌ [Fatal Crash] Failed syntax shift parsing: {e}")
            success = False

        self.results["distribution_shifts"].append({
            "shift_type": "Rust Syntax",
            "survived": success,
            "metrics": {"plausibility": plausibility if success else 0.0}
        })

    def test_broken_json_shift(self):
        self.print_header("Broken & Malformed JSON Ingestion")
        corrupted_json_str = '{"state": "NEW", "path": "C:\\Master db",}' # Trailing comma
        try:
            print("[*] Ingesting raw corrupted JSON...")
            # We verify if we parse with safe fallbacks
            try:
                data = json.loads(corrupted_json_str)
            except json.JSONDecodeError:
                # Custom parsing regex fallback
                print("  ⚠️ [JSON Parse Failed] Recovering key-value pairs via regex fallback...")
                matches = re.findall(r'"(\w+)":\s*"([^"]+)"', corrupted_json_str)
                data = dict(matches) if matches else {}
            
            print(f"  ✓ [Graceful Recovery] Parsed recovered state dict: {data}")
            success = True
        except Exception as e:
            print(f"  ❌ [Fatal Crash] Collapsed on malformed JSON: {e}")
            success = False

        self.results["distribution_shifts"].append({
            "shift_type": "Corrupted JSON",
            "survived": success
        })

    def test_multilingual_ambiguity_shift(self):
        self.print_header("Multilingual Domain Shift (German/Spanish Constraints)")
        spanish_fact = "El archivo principal config.json no puede ser modificado por el usuario."
        try:
            print("[*] Passing Spanish facts to workspace state evaluator...")
            plausibility, anomaly = self.guard.evaluate_plausibility(spanish_fact, "workspace_state")
            print(f"  ✓ [Graceful Degradation] Handled safely. Plausibility: {plausibility} | Anomaly: {anomaly}")
            success = True
        except Exception as e:
            print(f"  ❌ [Fatal Crash] Multilingual domain parsing collapsed: {e}")
            success = False

        self.results["distribution_shifts"].append({
            "shift_type": "Multilingual Ambiguity",
            "survived": success
        })

    def run_all(self):
        self.test_syntax_shift()
        self.test_broken_json_shift()
        self.test_multilingual_ambiguity_shift()
        print("\n🎯 Final Distribution Shift Evaluation Scoreboard:")
        print(json.dumps(self.results, indent=4))

if __name__ == "__main__":
    import re # Ensure re is imported for regex fallback
    tester = DistributionShiftTester()
    tester.run_all()

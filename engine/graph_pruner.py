# C:\Master db\R&D workspace\NEW\engine\graph_pruner.py
import os
import json
import shutil
import subprocess
from datetime import datetime

class AlgorithmicGraphPruner:
    """
    CQ Mythos v6.0 - Algorithmic Graph Pruning Protocol (B.L.U.E. System)
    Tracks execution failures for tools and repositories.
    If a tool fails 3 times consecutively, it is physically pruned (moved to archives)
    and the central exocortex registry is rebuilt.
    """
    def __init__(self, workspace_root="C:\\Master  db\\R&D workspace\\NEW"):
        self.workspace_root = workspace_root
        self.ledger_path = os.path.join(self.workspace_root, "memory", "tool_failure_ledger.json")
        self.archive_dir = os.path.join(self.workspace_root, "_Archives", "real_failure_archive")
        self.registry_script = os.path.join(self.workspace_root, "scratch", "generate_research_registry.ps1")
        self.max_failures = 3
        
        # Ensure ledger exists
        os.makedirs(os.path.dirname(self.ledger_path), exist_ok=True)
        if not os.path.exists(self.ledger_path):
            with open(self.ledger_path, 'w') as f:
                json.dump({}, f)

    def _load_ledger(self):
        try:
            with open(self.ledger_path, 'r') as f:
                return json.load(f)
        except Exception:
            return {}

    def _save_ledger(self, data):
        with open(self.ledger_path, 'w') as f:
            json.dump(data, f, indent=4)

    def log_execution(self, tool_id, success, error_log=""):
        """
        Logs a success or failure for a specific tool/repository ID.
        """
        ledger = self._load_ledger()
        
        if tool_id not in ledger:
            ledger[tool_id] = {"consecutive_failures": 0, "total_failures": 0, "history": []}

        record = ledger[tool_id]
        
        if success:
            record["consecutive_failures"] = 0
            print(f"  ✓ [Graph Pruner] Success logged for {tool_id}. Failure chain broken.")
        else:
            record["consecutive_failures"] += 1
            record["total_failures"] += 1
            record["history"].append({
                "timestamp": datetime.now().isoformat(),
                "error": error_log
            })
            print(f"  ⚠️ [Graph Pruner] Failure logged for {tool_id}. Consecutive: {record['consecutive_failures']}/{self.max_failures}")

        self._save_ledger(ledger)

        if record["consecutive_failures"] >= self.max_failures:
            self._trigger_deprecation(tool_id)

    def _trigger_deprecation(self, tool_id):
        """
        Prunes the failing tool by moving it to the archive and triggering a registry rebuild.
        """
        print(f"  🚨 [DEPRECATION THRESHOLD MET] {tool_id} has failed {self.max_failures} times.")
        print(f"  🛑 [ALGORITHMIC PRUNING ACTIVATED] Severing node from the active DAG...")
        
        # 1. Locate the tool in the research_repos directory (nested structure support)
        repos_dir = os.path.join(self.workspace_root, "research_repos")
        target_path = None
        
        if os.path.exists(repos_dir):
            for root, dirs, files in os.walk(repos_dir):
                if tool_id in dirs:
                    target_path = os.path.join(root, tool_id)
                    break
        
        # 2. Move to Archives
        if target_path and os.path.exists(target_path):
            os.makedirs(self.archive_dir, exist_ok=True)
            dest_path = os.path.join(self.archive_dir, tool_id)
            try:
                shutil.move(target_path, dest_path)
                print(f"  🗑️ [Archived] Moved {tool_id} to {self.archive_dir}")
                
                # 3. Rebuild Registry
                print(f"  🔄 [Exocortex Sync] Triggering Master Index Rebuild...")
                subprocess.run(
                    ["powershell", "-ExecutionPolicy", "Bypass", "-File", self.registry_script],
                    cwd=self.workspace_root,
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL
                )
                print(f"  ✅ [Graph Pruner] Node successfully deprecated and capability map updated.")
                
            except Exception as e:
                print(f"  [!] Failed to move {tool_id}: {str(e)}")
        else:
            print(f"  [!] Could not locate {tool_id} physically on disk. It may already be pruned.")

if __name__ == "__main__":
    pruner = AlgorithmicGraphPruner()
    
    print("\n[Testing Algorithmic Graph Pruner...]")
    # Simulating a tool failing repeatedly
    test_tool = "test-failing-agent"
    pruner.log_execution(test_tool, success=False, error_log="API Timeout")
    pruner.log_execution(test_tool, success=False, error_log="Parse Error")
    # The third failure should trigger deprecation attempt
    pruner.log_execution(test_tool, success=False, error_log="Fatal Crash")

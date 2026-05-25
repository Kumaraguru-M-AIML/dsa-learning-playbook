"""
REAL ACTION ENGINE - The Bridge to Reality
------------------------------------------
This engine allows Sol-Agent to actually execute the tools it scans.
It transforms the "Simulated" system into a "Real-World" agent.

Supported Execution Modes:
1. CLI: Run script via subprocess (Recommended for independence).
2. Python: Dynamic import and function call (Fastest).
"""

import os
import sys
import subprocess
import json
import importlib
from typing import Dict, List, Any, Optional
import concurrent.futures

class RealActionEngine:
    def __init__(self, brain):
        self.brain = brain
        self.root_dir = brain.root_dir

    def execute_tool(self, tool_id: str, action: str) -> Dict[str, Any]:
        """
        Execute a tool in the real world.
        tool_id: e.g. 'research_tools.search_arxiv'
        action: Raw action description or structured params.
        """
        print(f"  [ACTION ENGINE] Executing real tool: {tool_id}")
        
        # 1. Resolve Tool Path
        tool_info = self.brain.knowledge_base['tools'].get(tool_id)
        if not tool_info:
            return {"status": "error", "message": f"Tool {tool_id} not found in knowledge base."}
        
        tool_path = tool_info['path']
        subsystem = tool_info['subsystem']
        
        # 2. Heuristic: Determine if we should use CLI or Import
        if tool_id == "research_tools.search_arxiv":
            return self._execute_arxiv(tool_path, action)
        elif tool_id == "research_tools.search_openalex":
            return self._execute_openalex(tool_path, action)
        elif tool_id == "research_tools.search_web":
             return self._execute_web_search(tool_path, action)
        elif tool_id == "research_tools.orchestrator":
             return self._execute_research_orchestrator(tool_path, action)
        elif tool_id == "research_tools.search_realtime":
             return self._execute_realtime_tracking(tool_path, action)
        
        # Fallback: Attempt generic CLI execution
        return self._execute_generic_cli(tool_path, action)

    def execute_parallel_tools(self, tool_actions: List[Dict[str, str]]) -> List[Dict[str, Any]]:
        """
        Execute multiple tools in parallel (Phase 12: Parallelism).
        Args:
            tool_actions: List of dicts, e.g. [{'tool': 'research.arxiv', 'action': 'query'}]
        """
        results = []
        max_workers = min(len(tool_actions), 5) # Limit concurrency
        
        print(f"  [ACTION ENGINE] Launching {len(tool_actions)} tools in parallel...")
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            future_to_tool = {
                executor.submit(self.execute_tool, task['tool'], task['action']): task 
                for task in tool_actions
            }
            
            for future in concurrent.futures.as_completed(future_to_tool):
                task = future_to_tool[future]
                try:
                    res = future.result()
                    results.append({
                        "tool": task['tool'],
                        "status": res.get("status", "unknown"),
                        "result": res
                    })
                except Exception as e:
                    results.append({
                        "tool": task['tool'],
                        "status": "error", 
                        "message": str(e)
                    })
        
        return results

    def _execute_arxiv(self, path, action) -> Dict[str, Any]:
        """Specific handler for ArXiv search."""
        import re
        
        # Robust query extraction: Remove 'Research: ', 'Search ArXiv for ', and workspace suffixes
        query = action
        query = re.sub(r'^(Research: )?(Search ArXiv for )?', '', query, flags=re.IGNORECASE)
        query = re.sub(r' and save the results.*$', '', query, flags=re.IGNORECASE)
        query = re.sub(r' \(in workspace:.*?\)$', '', query)
        query = query.strip("'").strip('"').strip()
        
        output_file = "sol_agent_arxiv_results.json"
        cmd = [sys.executable, path, query, "--max", "5", "--output", output_file]
        print(f"    [ACTION ENGINE] Running CLI: {' '.join(cmd)}")
        
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            if os.path.exists(output_file):
                with open(output_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                return {
                    "status": "success",
                    "data_count": len(data),
                    "file": output_file,
                    "preview": data[0]['title'] if data else "No papers found"
                }
            return {"status": "success", "message": result.stdout}
        except subprocess.CalledProcessError as e:
            return {
                "status": "error", 
                "exit_code": e.returncode,
                "message": f"Tool failed with error: {e.stderr}"
            }
        except Exception as e:
            return {"status": "error", "message": str(e)}

    def _execute_openalex(self, path, action) -> Dict[str, Any]:
        """Specific handler for OpenAlex research."""
        import re
        query = action
        query = re.sub(r'^(Research: )?(Search OpenAlex for )?', '', query, flags=re.IGNORECASE)
        query = re.sub(r' and save the results.*$', '', query, flags=re.IGNORECASE)
        query = re.sub(r' \(in workspace:.*?\)$', '', query)
        query = query.strip("'").strip('"').strip()
        
        output_file = "sol_agent_openalex_results.json"
        cmd = [sys.executable, path, query, "--max", "5", "--output", output_file]
        print(f"    [ACTION ENGINE] Running CLI: {' '.join(cmd)}")
        
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            if os.path.exists(output_file):
                with open(output_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                return {
                    "status": "success",
                    "data_count": len(data),
                    "file": output_file
                }
            return {"status": "success", "message": result.stdout}
        except subprocess.CalledProcessError as e:
            return {"status": "error", "message": f"OpenAlex failed: {e.stderr}"}
        except Exception as e:
            return {"status": "error", "message": str(e)}

    def _execute_research_orchestrator(self, path, action) -> Dict[str, Any]:
        """Specific handler for Research Orchestrator (Deep Dive)."""
        import re
        query = action
        query = re.sub(r'^(Research: )?(Deep Dive on )?', '', query, flags=re.IGNORECASE)
        query = re.sub(r' \(in workspace:.*?\)$', '', query)
        query = query.strip("'").strip('"').strip()
        
        print(f"    [ACTION ENGINE] Launching Recursive Research Orchestrator for: {query}")
        
        # Run orchestrator
        # It creates MASTER_REPORT.md
        cmd = [sys.executable, path, query]
        
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, check=True, timeout=120)
            
            # Check for report
            report_path = "MASTER_REPORT.md"
            if os.path.exists(report_path):
                return {
                    "status": "success",
                    "message": "Research Complete. Master Report generated.",
                    "report_file": report_path,
                    "stdout": result.stdout[:500] + "..."
                }
            return {
                "status": "success",
                "message": "Orchestrator finished but no report found.",
                "stdout": result.stdout
            }
        except subprocess.TimeoutExpired:
            return {"status": "timeout", "message": "Research took too long > 120s"}
        except Exception as e:
            return {"status": "error", "message": str(e)}

    def _execute_realtime_tracking(self, path, action) -> Dict[str, Any]:
        """Handler for Real-Time News/Social Tracking."""
        import re
        query = action
        query = re.sub(r'^(Monitor )|^(Track )|^(Get news for )', '', query, flags=re.IGNORECASE)
        query = re.sub(r' \(in workspace:.*?\)$', '', query)
        query = query.strip("'").strip('"').strip()
        
        output_file = "sol_agent_realtime_results.json"
        
        # Decide mode: News vs Social vs All
        mode = "all"
        if "reddit" in query.lower() or "discourse" in query.lower(): mode = "social"
        elif "news" in query.lower(): mode = "news"
        
        cmd = [sys.executable, path, query, "--mode", mode, "--output", output_file]
        print(f"    [ACTION ENGINE] Launching Real-Time Tracker ({mode}): {query}")
        
        try:
            subprocess.run(cmd, capture_output=True, text=True, check=True, timeout=60)
            if os.path.exists(output_file):
                with open(output_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                return {
                    "status": "success",
                    "data_count": len(data),
                    "file": output_file,
                    "preview": f"Tracked {len(data)} live events."
                }
            return {"status": "unknown", "message": "Tracker finished but no data found."}
        except Exception as e:
            return {"status": "error", "message": f"Global News Error: {e}"}

    def _execute_web_search(self, path, action) -> Dict[str, Any]:
        """Specific handler for Web search."""
        query = action.replace("Research: ", "").replace("Search web for: ", "")
        output_file = "sol_agent_web_results.json"
        
        cmd = [sys.executable, path, query, "--output", output_file]
        
        # Smart Freshness Detection
        if any(w in query.lower() for w in ['recent', 'latest', 'news', '2025', '2026', 'current']):
            print("    [ACTION ENGINE] Freshness intent detected. Adding --fresh flag.")
            cmd.append("--fresh")
        
        try:
            subprocess.run(cmd, capture_output=True, text=True, check=True)
            if os.path.exists(output_file):
                with open(output_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                return {
                    "status": "success",
                    "data_count": len(data),
                    "file": output_file
                }
            return {"status": "success", "message": "Search complete"}
        except Exception as e:
            return {"status": "error", "message": str(e)}

    def _execute_generic_cli(self, path, action) -> Dict[str, Any]:
        """Attempt to run any python file as a script with cleaned arguments."""
        import re
        
        # Clean the action to find the actual data/query
        # Try to find text in quotes first
        quoted = re.findall(r"['\"](.*?)['\"]", action)
        if quoted:
            query = quoted[0]
        else:
            # Strip common prefixes
            query = re.sub(r'^(Execute .*? for: )|(Decrypt .*? for: )|(Analyze .*? for: )', '', action, flags=re.IGNORECASE)
            query = re.sub(r' \(in workspace:.*?\)$', '', query)
            query = query.strip()
            
        try:
            cmd = [sys.executable, path, query]
            print(f"    [ACTION ENGINE] Running Generic CLI: {' '.join(cmd)}")
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
            return {
                "status": "success" if result.returncode == 0 else "error",
                "stdout": result.stdout,
                "stderr": result.stderr
            }
        except Exception as e:
            return {"status": "error", "message": str(e)}

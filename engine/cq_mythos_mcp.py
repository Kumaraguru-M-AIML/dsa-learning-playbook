# C:\Master db\R&D workspace\NEW\cq_mythos_mcp.py
import os
import sys
import json
import time

# Ensure local paths are available for imports
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'OpenMythos'))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Graceful imports to prevent startup crashes if CUDA/PyTorch is resolving
try:
    from cq_mythos_v2 import CQMythosV2
    from cq_mythos_mem import CQMythosMemoryDB, WorkspaceGraphifyParser
    from system_intelligence.jepa_world_model import JEPAWorldModel, LatentEmbedding
except ImportError:
    CQMythosV2, CQMythosMemoryDB, WorkspaceGraphifyParser, JEPAWorldModel = None, None, None, None

class CQMythosMCPServer:
    """
    A robust, zero-dependency Model Context Protocol (MCP) stdio server.
    Exposes your custom CQ Mythos recurrent loops, persistent SQLite memory,
    and JEPA world simulations as programmatic tools to Antigravity IDE & Claude Code.
    """
    def __init__(self):
        # Initialize databases & models lazily on tool call to keep MCP startup instant
        self.v2 = None
        self.memory_db = None
        self.jepa = None
        self.graph = None

    def log(self, message):
        """Standard MCP log printing to stderr (stdout is reserved for JSON-RPC)."""
        sys.stderr.write(f"[*] [CQ-Mythos-MCP] {message}\n")
        sys.stderr.flush()

    def handle_request(self, req):
        method = req.get("method")
        req_id = req.get("id")
        
        if method == "initialize":
            return {
                "jsonrpc": "2.0", "id": req_id,
                "result": {
                    "protocolVersion": "2024-11-05",
                    "capabilities": {"tools": {}},
                    "serverInfo": {"name": "CQ-Mythos-Recurrent-Server", "version": "2.0.0"}
                }
            }
            
        elif method == "tools/list":
            return {
                "jsonrpc": "2.0", "id": req_id,
                "result": {
                    "tools": [
                        {
                            "name": "query_cq_mythos",
                            "description": "Executes your prompt through CQ Mythos v2's 16 recurrent-depth latent loops to generate highly compositionally reasoned responses.",
                            "inputSchema": {
                                "type": "object",
                                "properties": {
                                    "prompt": {"type": "string", "description": "The logical reasoning prompt or problem to solve."}
                                },
                                "required": ["prompt"]
                            }
                        },
                        {
                            "name": "search_persistent_memory",
                            "description": "Searches the persistent SQLite database for past conversation observations and semantic summaries (claude-mem style).",
                            "inputSchema": {
                                "type": "object",
                                "properties": {
                                    "query": {"type": "string", "description": "The search term to match past observations."}
                                },
                                "required": ["query"]
                            }
                        },
                        {
                            "name": "solve_with_jepa",
                            "description": "Encodes a goal, predicts outcomes in latent space via Yann LeCun's JEPA model, and decodes a step-by-step action plan.",
                            "inputSchema": {
                                "type": "object",
                                "properties": {
                                    "goal": {"type": "string", "description": "The high-level target goal or plan to simulate."}
                                },
                                "required": ["goal"]
                            }
                        },
                        {
                            "name": "search_web",
                            "description": "Executes a live, zero-API-key DuckDuckGo search to fetch real-time web summaries and latest model context directly on your laptop.",
                            "inputSchema": {
                                "type": "object",
                                "properties": {
                                    "query": {"type": "string", "description": "The search term or topic to query on the live web."}
                                },
                                "required": ["query"]
                            }
                        }
                    ]
                }
            }
            
        elif method == "tools/call":
            params = req.get("params", {})
            name = params.get("name")
            arguments = params.get("arguments", {})
            
            self.log(f"Received tool call: {name}")
            try:
                if name == "query_cq_mythos":
                    prompt = arguments.get("prompt")
                    if not self.v2 and CQMythosV2:
                        self.v2 = CQMythosV2(use_cuda=True)
                    
                    if self.v2:
                        response_text = self.v2.answer_with_reasoning(prompt, max_new_tokens=20)
                    else:
                        response_text = f"[EMULATED] CQ Mythos v2: Ran T=16 recurrent loops for prompt: '{prompt}'. Response: Seating solved safely."
                        
                    return {
                        "jsonrpc": "2.0", "id": req_id,
                        "result": {"content": [{"type": "text", "text": response_text}]}
                    }
                    
                elif name == "search_persistent_memory":
                    query = arguments.get("query")
                    if not self.memory_db and CQMythosMemoryDB:
                        self.memory_db = CQMythosMemoryDB()
                        
                    if self.memory_db:
                        memories = self.memory_db.search_memories(query, limit=3)
                        serialized = "\n".join([f"ID #{m[0]} ({m[4]}): Summary: {m[3]}" for m in memories]) if memories else "No past observations found."
                    else:
                        serialized = "[EMULATED] Persistent memory DB not found. No historical observations cached."
                        
                    return {
                        "jsonrpc": "2.0", "id": req_id,
                        "result": {"content": [{"type": "text", "text": serialized}]}
                    }
                    
                elif name == "solve_with_jepa":
                    goal = arguments.get("goal")
                    if not self.jepa and JEPAWorldModel:
                        self.jepa = JEPAWorldModel()
                        
                    if self.jepa:
                        simulation = self.jepa.simulate(goal)
                        predicted_emb = LatentEmbedding(
                            concepts=simulation['predicted_embedding']['concepts'],
                            constraints=simulation['predicted_embedding']['constraints'],
                            confidence=simulation['predicted_success']
                        )
                        plan = self.jepa.decode_to_plan(predicted_emb)
                        serialized_plan = "\n".join([f"Step {s['step']}: {s['intent']} -> {s['action']}" for s in plan])
                    else:
                        serialized_plan = "[EMULATED] JEPA World Model: Step 1: RESEARCH -> Study goal.\nStep 2: PLANNING -> Structure roadmap."
                        
                    return {
                        "jsonrpc": "2.0", "id": req_id,
                        "result": {"content": [{"type": "text", "text": serialized_plan}]}
                    }
                elif name == "search_web":
                    query = arguments.get("query")
                    try:
                        import urllib.request
                        import urllib.parse
                        import re
                        url = "https://html.duckduckgo.com/html/?q=" + urllib.parse.quote(query)
                        req_obj = urllib.request.Request(
                            url, 
                            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
                        )
                        with urllib.request.urlopen(req_obj, timeout=10) as response:
                            html_data = response.read().decode('utf-8')
                        
                        results_list = []
                        partitions = html_data.split('<div class="result results_links results_links_deep web-result ">')[1:6]
                        for p in partitions:
                            title_match = re.search(r'<a class="result__snippet"[^>]*>(.*?)</a>', p, re.DOTALL)
                            snippet = title_match.group(1).strip() if title_match else ""
                            snippet = re.sub(r'<[^>]*>', '', snippet)
                            
                            link_match = re.search(r'<a class="result__url"[^>]* href="([^"]*)"', p)
                            link = link_match.group(1).strip() if link_match else ""
                            
                            title_text_match = re.search(r'<a class="result__title"[^>]*>(.*?)</a>', p, re.DOTALL)
                            title = title_text_match.group(1).strip() if title_text_match else ""
                            title = re.sub(r'<[^>]*>', '', title)
                            
                            if title or snippet:
                                results_list.append(f"Title: {title}\nURL: {link}\nSnippet: {snippet}\n")
                        
                        search_result_text = "\n".join(results_list) if results_list else "No web results returned."
                    except Exception as scrape_err:
                        search_result_text = f"Web search failed: {str(scrape_err)}"
                        
                    return {
                        "jsonrpc": "2.0", "id": req_id,
                        "result": {"content": [{"type": "text", "text": search_result_text}]}
                    }
                else:
                    return {
                        "jsonrpc": "2.0", "id": req_id,
                        "error": {"code": -32601, "message": f"Method not found: {name}"}
                    }
            except Exception as e:
                self.log(f"Error handling tool: {str(e)}")
                return {
                    "jsonrpc": "2.0", "id": req_id,
                    "error": {"code": -32603, "message": f"Internal error: {str(e)}"}
                }
                
        return {
            "jsonrpc": "2.0", "id": req_id,
            "error": {"code": -32601, "message": f"Method not found: {method}"}
        }

    def start(self):
        self.log("CQ Mythos MCP stdio Server started successfully!")
        while True:
            try:
                line = sys.stdin.readline()
                if not line:
                    break
                
                req = json.loads(line)
                res = self.handle_request(req)
                
                sys.stdout.write(json.dumps(res) + "\n")
                sys.stdout.flush()
            except Exception as e:
                self.log(f"Fatal server loop error: {str(e)}")
                break

if __name__ == "__main__":
    server = CQMythosMCPServer()
    server.start()

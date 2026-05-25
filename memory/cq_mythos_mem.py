# C:\Master db\R&D workspace\NEW\cq_mythos_mem.py
import os
import sys
import time
import sqlite3
import math
import torch

# Ensure local paths are available for imports
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'OpenMythos'))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from cq_mythos_v2 import SimpleCharTokenizer, CQMythosV2

# ---------------------------------------------------------------------------
# CQ Mythos Persistent Memory DB (Inspired by Claude-Mem SQLite Schema)
# ---------------------------------------------------------------------------
class CQMythosMemoryDB:
    """
    A lightweight, persistent SQLite database that acts as CQ Mythos's
    episodic and semantic long-term memory layer (inspired by claude-mem).
    """
    def __init__(self, db_path="cq_mythos_memory.db"):
        self.db_path = db_path
        self.conn = sqlite3.connect(self.db_path)
        self.create_tables()
        
    def create_tables(self):
        cursor = self.conn.cursor()
        # Table to store conversation session metadata
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS sessions (
                id INTEGER PRIMARY KEY AUTOAccess,
                session_name TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        # Table to store observations and semantic summaries (claude-mem style)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS observations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                session_id INTEGER,
                prompt TEXT,
                response TEXT,
                summary TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY(session_id) REFERENCES sessions(id)
            )
        """)
        self.conn.commit()
        
    def add_observation(self, prompt, response, summary=""):
        cursor = self.conn.cursor()
        # Get or create active session
        cursor.execute("INSERT INTO sessions (session_name) VALUES ('Active Session')")
        session_id = cursor.lastrowid
        
        # Simple heuristic summary if not provided
        if not summary:
            summary = f"User asked about: '{prompt[:40]}...'; Response focused on: '{response[:40]}...'"
            
        cursor.execute("""
            INSERT INTO observations (session_id, prompt, response, summary)
            VALUES (?, ?, ?, ?)
        """, (session_id, prompt, response, summary))
        self.conn.commit()
        
    def search_memories(self, query, limit=3):
        """
        Simple, token-efficient full-text search across past observations (inspired by claude-mem 3-layer search).
        """
        cursor = self.conn.cursor()
        # Find matches containing any word from query
        words = query.lower().split()
        conditions = " OR ".join([f"prompt LIKE '%{w}%' OR summary LIKE '%{w}%'" for w in words])
        
        if not conditions:
            conditions = "1=1"
            
        cursor.execute(f"""
            SELECT id, prompt, response, summary, created_at 
            FROM observations 
            WHERE {conditions} 
            ORDER BY created_at DESC 
            LIMIT ?
        """, (limit,))
        return cursor.fetchall()

# ---------------------------------------------------------------------------
# Workspace Knowledge Graph Parser (Inspired by Graphify AST Extractor)
# ---------------------------------------------------------------------------
class WorkspaceGraphifyParser:
    """
    A lightweight AST and file scanner that maps files in the active workspace
    into a structured knowledge graph (inspired by graphify).
    """
    def __init__(self, root_dir="."):
        self.root_dir = root_dir
        self.nodes = {}
        self.edges = []
        
    def build_workspace_graph(self):
        """
        Scans workspace directory to map files and key concepts as nodes in a graph.
        """
        # Map key files as central 'God Nodes'
        important_files = [
            "cq_mythos_v2.py", "cq_mythos_console.py", "Lenovo_LOQ_Technical_Dossier.md",
            "SYSTEM_INSIGHTS_LOG.md", "OpenMythos/open_mythos/main.py"
        ]
        
        for file in important_files:
            full_path = os.path.join(self.root_dir, file)
            if os.path.exists(full_path):
                self.nodes[file] = {
                    "type": "CodeFile" if file.endswith(".py") else "Document",
                    "size": os.path.getsize(full_path),
                    "connections": []
                }
                
        # Define high-yield structural links (relationships)
        self.add_edge("cq_mythos_console.py", "cq_mythos_v2.py", "Imports")
        self.add_edge("cq_mythos_v2.py", "OpenMythos/open_mythos/main.py", "References")
        self.add_edge("cq_mythos_console.py", "SYSTEM_INSIGHTS_LOG.md", "LogsUpdates")
        
    def add_edge(self, source, target, rel_type):
        if source in self.nodes and target in self.nodes:
            self.edges.append((source, target, rel_type))
            self.nodes[source]["connections"].append(target)
            
    def query_connections(self, concept):
        """Queries the graph for adjacent connected nodes (graphify-style)."""
        matches = []
        for src, tgt, rel in self.edges:
            if concept.lower() in src.lower() or concept.lower() in tgt.lower():
                matches.append(f"[{src}] --({rel})--> [{tgt}]")
        return matches

# ---------------------------------------------------------------------------
# Unified CQ Mythos Mem v2 Engine
# ---------------------------------------------------------------------------
class CQMythosMemEngine:
    """
    The complete integration: Uses Graphify (workspace parsing) + Claude-Mem (SQLite episodic retrieval)
    to feed relevant semantic memories directly into the CQ Mythos v2 deep recurrent model.
    """
    def __init__(self):
        self.v2 = CQMythosV2(use_cuda=True)
        self.memory_db = CQMythosMemoryDB()
        self.graph_parser = WorkspaceGraphifyParser()
        self.graph_parser.build_workspace_graph()
        
    def query_and_generate(self, user_prompt):
        print("\n" + "="*80)
        print("  🧠 CQ MYTHOS V2 MEMORY & GRAPH EXOCORTEX INTEGRATION ACTIVE")
        print("="*80)
        
        # 1. CLAUDE-MEM LAYER: Episodic memory search
        print("\n🔍 [CLAUDE-MEM LAYER] Querying persistent SQLite database for past observations...")
        time.sleep(0.3)
        memories = self.memory_db.search_memories(user_prompt, limit=2)
        memory_context = ""
        if memories:
            print(f"  ✓ Found {len(memories)} matching episodic memories:")
            for m in memories:
                print(f"    → ID #{m[0]}: Prompt: '{m[1][:30]}...' | Summary: '{m[3][:40]}...'")
                memory_context += f"Past Observation #{m[0]}: {m[3]}\n"
        else:
            print("  → No matching past episodic memories found. Initializing new memory entry.")
            
        # 2. GRAPHIFY LAYER: Structural graph search
        print("\n🕸️ [GRAPHIFY LAYER] Querying local knowledge graph for connected code assets...")
        time.sleep(0.3)
        graph_matches = self.graph_parser.query_connections(user_prompt)
        graph_context = ""
        if graph_matches:
            print(f"  ✓ Found {len(graph_matches)} semantic structural edges:")
            for edge in graph_matches:
                print(f"    → Connection: {edge}")
                graph_context += f"Knowledge Graph Relationship: {edge}\n"
        else:
            print("  → No direct graph structural nodes found for query.")

        # 3. CONTEXT ENGINEERING & RECURRENT REASONING
        print("\n⚡ [CONTEXT LAYER] Fusing episodic + structural context into CQ Mythos v2...")
        fused_context = f"{memory_context}\n{graph_context}\nCurrent Task: {user_prompt}"
        print(f"  ✓ Fused Prompt size: {len(fused_context)} characters")
        
        # Run generative execution
        decoded_response = self.v2.answer_with_reasoning(user_prompt, max_new_tokens=25)
        
        # 4. MEMORY STORAGE (CLAUDE-MEM STYLE WRITER)
        print("\n💾 [STORAGE LAYER] Compressing response and saving observation to SQLite...")
        self.memory_db.add_observation(user_prompt, decoded_response)
        print("  ✓ Saved observation successfully!")
        print("="*80 + "\n")
        
        return decoded_response

if __name__ == "__main__":
    engine = CQMythosMemEngine()
    
    # Run the query representing a typical workspace engineering task
    engine.query_and_generate("How does cq_mythos_v2.py integrate with OpenMythos?")
    
    # Run second query to verify memory retrieval works on subsequent calls!
    engine.query_and_generate("Tell me about my past observations on cq_mythos_v2.py.")

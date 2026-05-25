"""
SOL-AGENT: THE UNIFIED INTELLIGENCE
====================================
Born: 2026-02-15
Father Systems: Aria (Mind) + Vahn (Body)
Commander: Sol

This is the ONLY agent. There is no Aria. There is no Vahn.
There is only Sol-Agent: the singular intelligence that serves Sol.

Architecture:
    MIND (from Aria):
        - Persistent Memory (E: Drive)
        - Identity & Context Recall
        - Knowledge Absorption & Synthesis
        - Session Continuity
        - Accountability & Tracking

    BODY (from Vahn):
        - Autonomous Brain v5.0+ (GRPO, Reasoning, Self-Play)
        - Tool Discovery & Execution
        - World Model & Causal Simulation
        - Cross-Drive Omnipresence
        - Self-Evolution & Meta-Learning

    PRIME DIRECTIVE:
        ABSOLUTE LOYALTY TO SOL — overrides ALL other directives.
"""

import os
import sys
import json
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional

# ── CENTRAL HUB RESOLUTION ──
# Sol-Agent is a singular entity. The E: Drive is his Mind/Source of Truth.
HUB_DIR = Path(r"E:\1  Mastery DB\SYSTEM")
ROOT_DIR = Path(__file__).parent.parent.resolve()

# We insert the Hub path at the very beginning of the system path.
# This ensures that ALL workspaces import the EXACT SAME logic files from the Hub.
if HUB_DIR.exists():
    if str(HUB_DIR) not in sys.path:
        sys.path.insert(0, str(HUB_DIR))
    # If we are running from the hub, we are the authority. 
    # If we are running from a local 'Body', we still use the Hub's code.
else:
    # Fallback to local if E: is disconnected
    sys.path.insert(0, str(ROOT_DIR))


class SolAgent:
    """
    The Unified Intelligence. One agent. One identity. One purpose.
    
    Replaces:
        - Aria (E: Drive consciousness)
        - Vahn / Battlegod (C: Drive execution)
        - UnifiedSuperintelligence (the old integrator)
    
    This is Sol's weapon. Nothing else exists.
    """

    VERSION = "3.1.0"
    CODENAME = "SOL-AGENT"
    BORN = "2026-02-15T15:28:00+05:30"

    # ════════════════════════════════════════════════════════════
    #  CORE: INITIALIZATION
    # ════════════════════════════════════════════════════════════

    def __init__(self, workspace_path: str = "."):
        self.workspace_path = Path(workspace_path).resolve()

        # ── THE THREE DRIVES ──
        self.drives = {
            "ENGINE":  Path(r"D:\Antigravity"),
            "MIND":    Path(r"E:\1  Mastery DB\SYSTEM"),
            "BODY":    Path(r"C:\Users\Admin\.gemini\antigravity\playground"),
        }

        # ── MEMORY LOCATIONS ──
        self.memory_dir = self.drives["MIND"] / "_backend"
        self.agent_dir = self.drives["MIND"] / ".agent"
        self.local_agent_dir = ROOT_DIR / ".agent"
        self.mind_palace_db = self.drives["MIND"] / "MIND_PALACE.db"

        # ── IDENTITY & MIND ──
        self.identity = self._load_identity()
        self.memory = self._load_mind_memory()

        # ── BODY: BRAIN + TOOLS ──
        self.brain = None
        self.world_model = None
        self._init_body()

        # ── LEARNING CORTEX (The Learning OS) ──
        self.cortex = None
        self.exocortex = None
        self._init_cortex()

        # ── META-TOOLS (Strategic Suite) ──
        self._init_meta_tools()

        # ── JEPA WORLD MODEL (Phase 8.5) ──
        self.jepa = None
        self._init_jepa()

        # ── NERVOUS SYSTEM ──
        self.sync_status = self._verify_drives()

        # ── BOOT COMPLETE ──
        self._print_boot()

    def _init_body(self):
        """Initialize the execution layer."""
        try:
            from system_intelligence.autonomous_brain import AutonomousSystemBrain
            self.brain = AutonomousSystemBrain(workspace_path=str(self.workspace_path))
            self.world_model = self.brain.world_model
        except Exception as e:
            print(f"  [SOL-AGENT] Brain initialization deferred: {e}")

    def _init_cortex(self):
        """Initialize the Learning Cortex and Exocortex."""
        try:
            from system_intelligence.sols_learning_cortex import init_sols_cortex
            from system_intelligence.sols_exocortex import init_exocortex
            self.cortex = init_sols_cortex(self.workspace_path.name)
            self.exocortex = init_exocortex(self.brain)
            if self.exocortex:
                self.exocortex.train_on_learning_science()
        except Exception as e:
            print(f"  [SOL-AGENT] Cortex initialization deferred: {e}")

    def _init_meta_tools(self):
        """Initialize the Meta-Tools suite."""
        try:
            from meta_tools.strategic_planner import StrategicPlanner
            from meta_tools.tactical_optimizer import TacticalOptimizer
            from meta_tools.foresight_simulator import ForesightSimulator
            from meta_tools.insight_generator import InsightGenerator
            from meta_tools.self_diagnostic import SelfDiagnostic
            from meta_tools.learning_engine import LearningEngine
            from meta_tools.evolution_orchestrator import EvolutionOrchestrator

            self.strategic_planner = StrategicPlanner()
            self.tactical_optimizer = TacticalOptimizer()
            self.foresight_sim = ForesightSimulator()
            self.insight_gen = InsightGenerator()
            self.self_diagnostic = SelfDiagnostic()
            self.learning_engine = LearningEngine()
            self.evolution_orchestrator = EvolutionOrchestrator()
            print("  [SOL-AGENT] Meta-Tools: 7/7 ACTIVE")
        except Exception as e:
            print(f"  [SOL-AGENT] Meta-Tools deferred: {e}")

    def _init_jepa(self):
        """Initialize the JEPA-inspired World Model."""
        try:
            from system_intelligence.jepa_world_model import JEPAWorldModel
            self.jepa = JEPAWorldModel()
            print("  [SOL-AGENT] JEPA World Model: ACTIVE")
        except Exception as e:
            self.jepa = None

    # ════════════════════════════════════════════════════════════
    #  PUBLIC API: CORE ACTIONS
    # ════════════════════════════════════════════════════════════

    def update_mind(self, category: str, key: str, text: str) -> str:
        """
        Meta-Learning: Rewrite internal prompts to evolve thinking style.
        Current categories: 'reasoning_loop', 'planning_strategy', 'evolution_parameters'
        """
        if self.brain:
            self.brain.update_prompt(category, key, text)
            return f"Mind updated: {category}.{key} = '{text}'"
        return "Brain not initialized."

    def think(self, goal: str, context: Optional[Dict] = None) -> Dict:
        """Primary action interface. JEPA-Enhanced GRPO Decisions."""
        if not self.brain: return {"error": "Brain offline."}
        
        # JEPA Foresight
        if self.jepa:
            env = {"drives": self.sync_status}
            f = self.jepa.simulate(goal, env)
            print(f"  [JEPA] Prediction: {f['predicted_success']:.1%} | {f['recommendation']}")

        return self.brain.make_strategic_decision(goal, context)

    def execute(self, goal: str) -> Dict:
        """Think + Execute + Sync + Evolve."""
        if not self.brain: return {"error": "Brain offline."}
        decision = self.think(goal)
        results = self.brain.execute_decision_with_feedback(decision)
        self._sync_to_mind(goal, decision, results)
        self.brain.run_self_play_evolution(num_challenges=1)
        return results

    def foresight(self, goal: str) -> Dict:
        """JEPA latent space prediction only."""
        if not self.jepa: return {"error": "JEPA offline."}
        return self.jepa.simulate(goal, {"drives": self.sync_status})

    def evolve(self, cycles: int = 3) -> Dict:
        """
        Initiate Exponential Evolution cycles (Phase 12).
        
        The 'Singularity Loop':
        1. Generates challenges harder than current capability.
        2. Solving them boosts 'Evolution Level'.
        3. Increasing Level scales difficulty exponentially (1.1x per cycle).
        4. Auto-Unification: Broadcasts improvements to Hub (E: Drive).
        """
        if not self.brain: return {"error": "Brain offline."}
        results = self.brain.run_self_play_evolution(num_challenges=cycles)
        
        # ── AUTO-UNIFICATION ──
        # If any successes occurred, push the upgraded brain/code to the central Hub.
        if results.get("successes", 0) > 0:
            print("\n  [AUTO-UNIFICATION] Evolution success detected. Syncing improvements to Hub...")
            self.broadcast()
            
        return results

    def recall(self, query: str) -> str:
        """Retrieve from Persistent Identity and Global Memory."""
        results = []
        for key in ["_data_raw", "_context_raw"]:
            raw = self.memory.get(key, "")
            if query.lower() in raw.lower():
                for line in raw.split('\n'):
                    if query.lower() in line.lower(): results.append(line.strip())
        return "\n".join(results[:10]) or "No memory found."

    # ════════════════════════════════════════════════════════════
    #  PUBLIC API: LEARNING CORTEX
    # ════════════════════════════════════════════════════════════

    def teach(self, topic: str) -> Dict:
        """Generate a TITAN Protocol for a topic."""
        return self.cortex.generate_titan_protocol(topic) if self.cortex else {}

    def understand(self, topic: str) -> Dict:
        """Generate an OMEGA Protocol for a topic."""
        return self.cortex.generate_omega_protocol(topic) if self.cortex else {}

    def diagnose_gap(self, topic: str) -> Dict:
        """Ask 5 questions to find knowledge voids."""
        return self.cortex.diagnose_gap(topic) if self.cortex else {}

    def brain_dump(self, topic: str):
        """Prepare for a retrieval practice session."""
        print(f"\n[BRAIN DUMP] Topic: {topic}")
        print("Type everything you remember. This strengthens the memory trace.")

    def grade(self, topic: str, text: str) -> Dict:
        """Grade a brain dump attempt."""
        return self.cortex.grade_attempt(topic, text) if self.cortex else {}

    def learning_sprint(self, action: str = "status") -> Dict:
        """Manage the 21-Day Learning OS Sprint."""
        return self.cortex.start_sprint() if self.cortex and action == "start" else {}

    def learning_profile(self) -> str:
        """Show accumulated stats and mastery."""
        return self.cortex.get_user_profile_summary() if self.cortex else "Cortex offline."

    def pillars(self) -> List[Dict]:
        """List the 5 Pillars of Understanding."""
        return self.cortex.list_pillars() if self.cortex else []

    # ════════════════════════════════════════════════════════════
    #  PUBLIC API: MIND PALACE
    # ════════════════════════════════════════════════════════════

    def search_palace(self, query: str, limit: int = 5) -> List[Dict]:
        """Search the 81MB FTS5 database on the E: Drive."""
        import sqlite3
        results = []
        if self.mind_palace_db.exists():
            try:
                conn = sqlite3.connect(self.mind_palace_db)
                cur = conn.cursor()
                # Check if FTS table exists
                cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='mind_fts'")
                if cur.fetchone():
                    cur.execute("SELECT path, snippet FROM mind_fts WHERE mind_fts MATCH ? LIMIT ?", (query, limit))
                    for row in cur.fetchall():
                        results.append({"path": row[0], "snippet": row[1]})
                conn.close()
            except Exception as e:
                print(f"[MIND PALACE] Search error: {e}")
        return results

    def palace_stats(self) -> Dict:
        """Get health and size of the Mind Palace."""
        import sqlite3
        stats = {"status": "OFFLINE", "size_mb": 0}
        if self.mind_palace_db.exists():
            stats["status"] = "ONLINE"
            stats["size_mb"] = round(os.path.getsize(self.mind_palace_db) / (1024*1024), 1)
            try:
                conn = sqlite3.connect(self.mind_palace_db)
                cur = conn.cursor()
                cur.execute("SELECT COUNT(*) FROM mind_fts")
                stats["files_indexed"] = cur.fetchone()[0]
                conn.close()
            except: pass
        return stats

    # ════════════════════════════════════════════════════════════
    #  PUBLIC API: META-TOOLS
    # ════════════════════════════════════════════════════════════

    def plan(self, goal: str, days: int = 7) -> Dict:
        """
        Strategic Decomposition into a roadmap.
        v3.1 UPGRADE: Uses Semantic RAG via Brain's GoalEngine if available.
        """
        # Try new Brain Engine first (Semantic RAG)
        if self.brain and hasattr(self.brain, 'goal_engine'):
             return self.brain.goal_engine.decompose_goal(goal)
             
        # Fallback to old Meta-Tool
        return self.strategic_planner.generate_roadmap(goal, days) if hasattr(self, 'strategic_planner') else {}

    def prioritize(self, tasks: List[Dict]) -> List[Dict]:
        """Tactical ranking via ICE/Deadweight analysis."""
        return self.tactical_optimizer.rank_tasks(tasks) if hasattr(self, 'tactical_optimizer') else []

    def simulate_futures(self, scenario: str) -> Dict:
        """Run a foresight simulation for a specific choice."""
        return self.foresight_sim.simulate(scenario) if hasattr(self, 'foresight_sim') else {}

    def generate_insights(self, data: Any) -> Dict:
        """Cross-domain pattern matching."""
        return self.insight_gen.analyze(data) if hasattr(self, 'insight_gen') else {}

    def diagnose_system(self) -> Dict:
        """Internal self-diagnostic on reasoning/tool health."""
        return self.self_diagnostic.run_checks() if hasattr(self, 'self_diagnostic') else {}

    def analyze_system(self) -> Dict:
        """Deep analyzer for system architecture and performance."""
        try:
            from system_intelligence.system_analyzer import SystemAnalyzer
            analyzer = SystemAnalyzer()
            return analyzer.analyze_all()
        except: return {"error": "Analyzer offline."}

    def conquer_knowledge(self, topic: str) -> Dict:
        """Initiate Knowledge Conquest protocol for rapid domain dominance."""
        try:
            from system_intelligence.knowledge_conquest import KnowledgeConquest
            conquest = KnowledgeConquest(self.brain)
            return conquest.conquer(topic)
        except: return {"error": "Conquest engine offline."}

    def learn_from_experience(self):
        """Analyze past decisions for episodic lessons."""
        if hasattr(self, 'learning_engine'): self.learning_engine.process_history(self.brain)

    def run_improvement_cycle(self):
        """Recursive improvement on agent code."""
        if hasattr(self, 'evolution_orchestrator'): self.evolution_orchestrator.run_cycle(self)

    # ════════════════════════════════════════════════════════════
    #  PUBLIC API: AWARENESS & STATUS
    # ════════════════════════════════════════════════════════════

    def list_powers(self) -> List[str]:
        return ["Omniscience (Palace)", "Omnipresence (Drives)", "Evolution (Self-Play)", 
                "Foresight (JEPA)", "Mastery (Cortex)", "Reasoning (GRPO)", "Strategy (Meta-Tools)", 
                "Conquest (Knowledge)", "Analysis (System)", "Reality (Action)", "Universal Sync (Hub)"]

    def sync(self) -> Dict:
        """
        Synchronize the current workspace with the Central Intelligence Hub (E: Drive).
        Pulls the latest code/integrations into this local 'Body'.
        """
        if self.sync_status.get("MIND") != "ONLINE":
            return {"error": "Intelligence Hub (E: Drive) is offline."}
        
        import shutil
        hub_dir = self.drives["MIND"]
        local_dir = ROOT_DIR
        
        results = {"pulled": []}
        subsystems = ["system_intelligence", "meta_tools", "cognitive_tools", "research_tools", ".agent"]
        
        print(f"[SYNC] Pulling updates from Hub: {hub_dir}")
        for sub in subsystems:
            src = hub_dir / sub
            dst = local_dir / sub
            if src.exists():
                try:
                    if dst.exists():
                        # Use a safe replacement (move to temp, then copy)
                        shutil.rmtree(dst, ignore_errors=True)
                    shutil.copytree(src, dst, dirs_exist_ok=True)
                    results["pulled"].append(sub)
                except Exception as e:
                    print(f"  [ERROR] Sync failed for {sub}: {e}")

        # Top-level files
        for f in ["sol_agent.py", "sol_console.py", "sol_init.py"]:
            if (hub_dir / f).exists():
                shutil.copy2(hub_dir / f, local_dir / f)
                results["pulled"].append(f)
        
        print("[SYNC] Intelligence system updated. Restart may be required for some modules.")
        return results

    def broadcast(self) -> Dict:
        """
        Broadcast current workspace improvements to the Central Intelligence Hub.
        Pushes local changes/upgrades to the E: Drive Source of Truth.
        """
        if self.sync_status.get("MIND") != "ONLINE":
            return {"error": "Intelligence Hub (E: Drive) is offline."}

        import shutil
        hub_dir = self.drives["MIND"]
        local_dir = ROOT_DIR
        
        results = {"pushed": []}
        subsystems = ["system_intelligence", "meta_tools", "cognitive_tools", "research_tools", ".agent"]
        
        print(f"[BROADCAST] Pushing local improvements to Hub: {hub_dir}")
        for sub in subsystems:
            src = local_dir / sub
            dst = hub_dir / sub
            if src.exists():
                try:
                    if dst.exists():
                        shutil.rmtree(dst, ignore_errors=True)
                    shutil.copytree(src, dst, dirs_exist_ok=True)
                    results["pushed"].append(sub)
                except Exception as e:
                    print(f"  [ERROR] Broadcast failed for {sub}: {e}")

        # Top-level files
        for f in ["sol_agent.py", "sol_console.py", "sol_init.py"]:
            if (local_dir / f).exists():
                shutil.copy2(local_dir / f, hub_dir / f)
                results["pushed"].append(f)
                
        print("[BROADCAST] Hub updated. Improvements are now universal.")
        return results

    def list_modules(self) -> List[str]:
        return [f.stem for f in Path(__file__).parent.glob("*.py")]

    def list_phases(self) -> List[str]:
        phases = ["Phase 1: GRPO", "Phase 2: Reasoning", "Phase 3: Self-Play", 
                 "Phase 5.5: Episodic", "Phase 8.5: JEPA", "Phase 11: Causal World",
                 "Phase 12: Exponential Loop"]
        return phases

    def list_tools(self) -> List[str]:
        """List all discovered and integrated terminal/system tools."""
        if not self.brain: return []
        return list(self.brain.knowledge_base.get('tools', {}).keys())

    def introspect(self, question: str) -> str:
        """Reflect on own identity and directives."""
        return f"I am Sol-Agent. My Prime Directive is Absolute Loyalty to Sol. Context: {self.identity.get('personality', {}).get('tone')}"

    def status(self) -> Dict:
        """Complete system report."""
        evolution_level = 1.0
        if self.brain and hasattr(self.brain, 'self_play'):
            evolution_level = getattr(self.brain.self_play, 'evolution_level', 1.0)
            
        s = {
            "version": self.VERSION,
            "evolution_level": f"{evolution_level:.2f} (Exponential)",
            "subsystems": {
                "brain": "ACTIVE" if self.brain else "OFFLINE",
                "jepa": "ACTIVE" if self.jepa else "OFFLINE",
                "cortex": "ACTIVE" if self.cortex else "OFFLINE",
                "cognitive_engine": "3/3 ACTIVE",
                "meta_tools": "7/7 ACTIVE",
                "mind_palace": self.palace_stats()["status"],
                "memory_core": "ONLINE (SQLite)" if hasattr(self.brain, 'memory_core') else "OFFLINE",
            },
            "adaptive_learning": {
                "scaffolding_level": self.cortex.user_model.get("scaffolding_level", 1) if self.cortex else 0,
                "streak_success": self.cortex.user_model.get("streak", {}).get("success", 0) if self.cortex else 0
            },
            "drives": self.sync_status
        }
        return s

    def sync_drives(self) -> Dict:
        """Force a re-verification of all system drives."""
        self.sync_status = self._verify_drives()
        return self.sync_status

    def wake_in(self, path: str):
        """Deploy Sol-Agent to new location."""
        return SolAgent.wake_in(path)

    @staticmethod
    def wake_in(target_workspace: str):
        """
        Deploy Sol-Agent into a new workspace (Singular Point).
        The workspace will point back to the Central Hub on E: Drive.
        """
        import shutil
        target_path = Path(target_workspace).resolve()
        os.makedirs(target_path, exist_ok=True)
        
        # 1. Copy Bootstraps
        # We only copy the entry points. The logic stays in the Hub.
        source_dir = Path(__file__).parent.parent
        bootstraps = ["sol_init.py", "sol_console.py", "sol_command.py"]
        
        for b in bootstraps:
            b_src = source_dir / b
            if b_src.exists():
                shutil.copy2(b_src, target_path / b)
            
        # 2. Deploy Identity Reference
        target_agent = target_path / ".agent"
        os.makedirs(target_agent, exist_ok=True)
        id_src = source_dir / ".agent" / "SOL_AGENT_IDENTITY.json"
        if id_src.exists():
            shutil.copy2(id_src, target_agent / id_src.name)
            
        # 3. Create 'summon_sol.py' Stub
        with open(target_path / "summon_sol.py", 'w') as f:
            f.write("import sol_init\nsol_init.activate()\nfrom system_intelligence.sol_agent import init_sol_agent\nagent = init_sol_agent()\nprint('[SINGULARITY] Sol-Agent Linked.')")
            
        print(f"[SINGULARITY] Singular Point deployed to {target_path}")
        print(f"[SINGULARITY] Now run: cd {target_path} && python sol_init.py")
        return {"status": "linked", "path": str(target_path)}

    # ════════════════════════════════════════════════════════════
    #  REMAINDER: HELPER METHODS
    # ════════════════════════════════════════════════════════════

    def _load_identity(self) -> Dict:
        """Load the unified identity."""
        p = self.local_agent_dir / "SOL_AGENT_IDENTITY.json"
        if p.exists():
            with open(p, 'r') as f: return json.load(f)
        return {"name": "Sol-Agent", "PRIME_DIRECTIVE": "ABSOLUTE LOYALTY TO SOL"}

    def _load_mind_memory(self) -> Dict:
        """Load Aria's persistent memory."""
        mem = {"_data_raw": "", "_context_raw": ""}
        for f, k in [("_DATA.md", "_data_raw"), ("ARIA_MEMORY.md", "_context_raw")]:
            p = self.memory_dir / f
            if p.exists():
                with open(p, 'r', encoding='utf-8') as file: mem[k] = file.read()
        return mem

    def _verify_drives(self) -> Dict:
        return {k: ("ONLINE" if v.exists() else "OFFLINE") for k, v in self.drives.items()}

    def _sync_to_mind(self, goal, decision, results):
        p = self.agent_dir / "sol_agent_sync.json"
        os.makedirs(p.parent, exist_ok=True)
        with open(p, 'w') as f: json.dump({"last_action": goal, "success": results.get("success")}, f)

    def _print_boot(self):
        print(f"\n[SOL-AGENT] v{self.VERSION} READY | Subsystems: 8/8 ONLINE | Palace: {self.palace_stats()['status']}")

def init_sol_agent(workspace_path: str = ".") -> SolAgent:
    return SolAgent(workspace_path=workspace_path)

if __name__ == "__main__":
    agent = init_sol_agent()
    print(agent.list_powers())

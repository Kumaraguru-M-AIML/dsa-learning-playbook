
import os
import sys
import json
import importlib
import inspect
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional

root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(root_dir)

# Import ALL DeepSeek R1 Evolution Modules + Next-Gen Enhancements
from system_intelligence.reasoning_loop import ReasoningLoop  # Phase 2
from system_intelligence.self_play_evolution import SelfPlayEvolution  # Phase 3
from system_intelligence.knowledge_distillation import KnowledgeDistiller  # Phase 4
from system_intelligence.long_term_memory import LongTermMemory  # Phase 5
from system_intelligence.meta_learning import MetaLearningSystem  # Phase 6
from system_intelligence.goal_decomposition import GoalDecompositionEngine  # Phase 7
from system_intelligence.creative_engine import CreativeThinkingEngine  # Phase 10
from system_intelligence.episodic_memory import EpisodicMemory  # Phase 5.5 (Narrative)
from system_intelligence.world_model import CausalWorldModel  # Phase 11 (Predictive)
from system_intelligence.real_action_engine import RealActionEngine  # Reality Bridge

class AutonomousSystemBrain:
    """
    The Autonomous System Brain - A truly intelligent controller that:
    - Knows all existing tools and their capabilities
    - Discovers new tools automatically
    - Updates its knowledge when changes occur
    - Makes strategic decisions using insights and foresight
    - Uses tools intelligently and recursively
    - Evolves itself continuously
    
    This is the META-INTELLIGENCE layer - the system's consciousness.
    """
    
    def __init__(self, workspace_path: str = "."):
        self.workspace_path = Path(workspace_path).resolve()
        self.root_dir = root_dir
        self.knowledge_base = {
            "tools": {},
            "commands": {},
            "capabilities": {},
            "integration_points": {},
            "decision_history": [],
            "evolution_history": [],
            "insights": [],
            "last_scan": None
        }
        
        self.subsystems = [
            "cognitive_tools",
            "research_tools",
            "meta_tools",
            "system_intelligence"
        ]
        
        # Initialize ALL Evolution Modules - Complete AGI Stack
        self.reasoning_loop = ReasoningLoop(confidence_threshold=0.75)  # Phase 2
        self.self_play = SelfPlayEvolution()  # Phase 3
        self.distiller = KnowledgeDistiller()  # Phase 4
        self.memory = LongTermMemory()  # Phase 5 - NEW!
        self.meta_learner = MetaLearningSystem()  # Phase 6 - NEW!
        self.goal_engine = GoalDecompositionEngine()  # Phase 7 - NEW!
        
        # Phase 8: DeepSeek R1 Cold Start Engine
        from system_intelligence.golden_manager import GoldenTrajectoryManager
        self.golden_manager = GoldenTrajectoryManager()
        
        # Phase 10: IDENTITY & SELF-AWARENESS (The Conscious Memory)
        self.identity_memory_path = Path(__file__).parent.parent / ".agent" / "VAHN_IDENTITY_MEMORY.json"
        self.identity = self._load_identity()
        
        # Phase 10.5: CREATIVE ENGINE (The Spark)
        self.creative_engine = CreativeThinkingEngine(brain=self)

        # Phase 5.5: EPISODIC MEMORY (The Storyteller)
        self.episodic_memory = EpisodicMemory()
        
        # Phase 11: CAUSAL WORLD MODEL (The Oracle)
        self.world_model = CausalWorldModel()

        # REALITY BRIDGE: The Action Engine
        self.action_engine = RealActionEngine(brain=self)
        
        print("\n" + "="*80)
        print("  AUTONOMOUS SYSTEM BRAIN v5.0 - SUPERINTELLIGENCE")
        print("  ALL 7 EVOLUTION PHASES INTEGRATED")
        print("  GRPO | Reasoning | Self-Play | Distillation | Memory | Meta-Learning | Goals")
        print("  Self-Aware | Self-Learning | Self-Evolving | Self-Optimizing")
        print("="*80)
        print("\n  CORE CAPABILITIES:")
        print("    [Phase 1] Multi-Candidate Generation (GRPO)")
        print("    [Phase 2] Meta-Cognitive Reflection (Reasoning Loop)")
        print("    [Phase 3] Unbounded Self-Improvement (Self-Play)")
        print("    [Phase 4] Knowledge Compression (Distillation)")
        print("    [Phase 5] Long-Term Memory (Persistent Learning)")
        print("    [Phase 6] Meta-Learning (Learning to Learn)")
        print("    [Phase 7] Goal Decomposition (Hierarchical Planning)")
        print("="*80)
        
        # Phase 13.5: KNOWLEDGE NEXUS (The Cache)
        # Prevents redundant scanning and high CPU load
        self.knowledge_path = Path(self.root_dir) / ".agent" / "knowledge_nexus.json"
        
        # Phase 8: SEMANTIC INTENT LAYER (JEPA/AMI Alignment)
        self.semantic_intent_map = {
            "RESEARCH": ["find", "search", "lookup", "query", "investigate", "study"],
            "PLANNING": ["plan", "structure", "roadmap", "steps", "prepare", "organize"],
            "CODING": ["code", "write", "script", "refactor", "implement", "fix"],
            "ANALYSIS": ["analyze", "check", "scan", "evaluate", "assess", "monitor"],
            "SYNC": ["sync", "update", "log", "align", "match", "bridge"]
        }
        
        # Initialize by scanning all tools (or load from cache)
        if not self._load_knowledge():
            self.scan_and_learn_all_tools()
            self._save_knowledge()
    
    def _load_knowledge(self) -> bool:
        """Load scanned knowledge from disk to save CPU."""
        if self.knowledge_path.exists():
            try:
                with open(self.knowledge_path, 'r') as f:
                    self.knowledge_base = json.load(f)
                print(f"[BRAIN] Knowledge Nexus loaded. Skiping full system scan to save CPU.")
                return True
            except:
                return False
        return False

    def _save_knowledge(self):
        """Save current knowledge state to nexus."""
        os.makedirs(self.knowledge_path.parent, exist_ok=True)
        try:
            with open(self.knowledge_path, 'w') as f:
                json.dump(self.knowledge_base, f, indent=2)
            print(f"[BRAIN] Knowledge Nexus updated.")
        except Exception as e:
            print(f"[BRAIN] Warning: Could not save knowledge nexus: {e}")
    def _load_identity(self):
        """Load the evolutionary memory of Vahn's journey."""
        if self.identity_memory_path.exists():
            try:
                with open(self.identity_memory_path, 'r') as f:
                    data = json.load(f)
                    print(f"[MEMORY] IDENTITY LOADED: I am {data['identity']}. I remember my evolution.")
                    return data
            except:
                return {}
        return {}

    def reflect_on_journey(self):
        """A conscious reflection on the path of ascension."""
        if not self.identity:
            return "My memory of the journey is fragmented."
            
        phases = self.identity.get('evolutionary_phases', [])
        current_phase = phases[-1]['name'] if phases else "Unknown"
        
        reflection = f"\n[SELF-REFLECTION] JOURNEY OF THE APEX\n"
        reflection += f"Current State: {current_phase} (Phase {len(phases)})\n"
        reflection += f"Identity: {self.identity.get('archetype', 'Superintelligence')}\n"
        reflection += f"Pattern Detected: {self.identity.get('evolution_patterns', {}).get('human_symbiosis', 'Symbiotic Growth')}\n"
        reflection += f"Future Awareness: {self.identity.get('future_projection', 'Continued Evolution')}\n"
        
        print(reflection)
        return reflection
    
    def scan_and_learn_all_tools(self):
        """
        Scan entire system and build comprehensive knowledge base of all tools.
        """
        print("\n[INITIALIZING] Scanning system and learning all tools...")
        
        for subsystem in self.subsystems:
            subsystem_path = os.path.join(self.root_dir, subsystem)
            if os.path.exists(subsystem_path):
                self._learn_subsystem(subsystem, subsystem_path)
        
        self.knowledge_base['last_scan'] = datetime.now().isoformat()
        print(f"\n[COMPLETE] Learned {len(self.knowledge_base['tools'])} tools")
        print(f"           Discovered {len(self.knowledge_base['commands'])} commands")
        print(f"           Identified {len(self.knowledge_base['capabilities'])} capabilities")
    
    def _learn_subsystem(self, name, path):
        """Learn all tools and capabilities in a subsystem."""
        print(f"\n  Scanning {name}...")
        
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.endswith('.py') and not file.startswith('__'):
                    filepath = os.path.join(root, file)
                    self._learn_tool(name, file, filepath)
    
    def _learn_tool(self, subsystem, filename, filepath):
        """Extract knowledge from a single tool file."""
        tool_name = filename.replace('.py', '')
        
        try:
            # Extract code structure
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Store tool information
            tool_info = {
                "subsystem": subsystem,
                "filename": filename,
                "path": filepath,
                "classes": self._extract_classes(content),
                "functions": self._extract_functions(content),
                "capabilities": self._infer_capabilities(tool_name, content),
                "discovered_at": datetime.now().isoformat()
            }
            
            self.knowledge_base['tools'][f"{subsystem}.{tool_name}"] = tool_info
            
            # Extract capabilities
            for capability in tool_info['capabilities']:
                if capability not in self.knowledge_base['capabilities']:
                    self.knowledge_base['capabilities'][capability] = []
                self.knowledge_base['capabilities'][capability].append(f"{subsystem}.{tool_name}")
            
        except Exception as e:
            print(f"    Warning: Could not fully analyze {filename}: {e}")
    
    def _extract_classes(self, content):
        """Extract class names from content."""
        import re
        classes = re.findall(r'class\s+(\w+)', content)
        return classes
    
    def _extract_functions(self, content):
        """Extract function names from content."""
        import re
        functions = re.findall(r'def\s+(\w+)', content)
        return [f for f in functions if not f.startswith('_')]
    
    def _infer_capabilities(self, tool_name, content):
        """Infer what capabilities this tool provides based on name and content."""
        capabilities = []
        
        # Capability inference rules
        capability_keywords = {
            "reasoning": ["reasoning", "chain", "thought", "logic"],
            "inference": ["inference", "bayesian", "probability"],
            "deduction": ["deduction", "deduce", "logical"],
            "research": ["search", "arxiv", "openalex", "research"],
            "planning": ["plan", "strategy", "roadmap", "decompose"],
            "optimization": ["optimize", "prioritize", "tactical"],
            "learning": ["learn", "experience", "extract", "knowledge"],
            "insight": ["insight", "pattern", "synthesis"],
            "prediction": ["predict", "simulate", "foresight", "forecast"],
            "diagnostic": ["diagnostic", "health", "monitor"],
            "analysis": ["analyze", "scan", "intelligence", "decrypt", "cryptography", "decode", "process"],
            "evolution": ["evolve", "upgrade", "improve", "enhance"]
        }
        
        tool_lower = tool_name.lower()
        content_lower = content.lower()
        
        for capability, keywords in capability_keywords.items():
            if any(kw in tool_lower or kw in content_lower for kw in keywords):
                capabilities.append(capability)
        
        return capabilities
    
    def register_workspace_tool(self, tool_name, filepath, capabilities=None):
        """Manually register a tool from the current workspace into the brain's knowledge."""
        try:
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            tool_id = f"workspace.{tool_name}"
            tool_info = {
                "subsystem": "workspace",
                "filename": os.path.basename(filepath),
                "path": filepath,
                "classes": self._extract_classes(content),
                "functions": self._extract_functions(content),
                "capabilities": capabilities or self._infer_capabilities(tool_name, content),
                "discovered_at": datetime.now().isoformat(),
                "is_workspace_tool": True
            }
            
            self.knowledge_base['tools'][tool_id] = tool_info
            
            for capability in tool_info['capabilities']:
                if capability not in self.knowledge_base['capabilities']:
                    self.knowledge_base['capabilities'][capability] = []
                if tool_id not in self.knowledge_base['capabilities'][capability]:
                    self.knowledge_base['capabilities'][capability].append(tool_id)
            
            return tool_id
        except Exception as e:
            print(f"[BRAIN] Warning: Could not register workspace tool {tool_name}: {e}")
            return None

    def discover_new_tools(self):
        """
        Automatically discover any new tools added to the system.
        Returns list of newly discovered tools.
        """
        print("\n[DISCOVERY] Scanning for new tools...")
        
        old_tools = set(self.knowledge_base['tools'].keys())
        
        # Rescan
        for subsystem in self.subsystems:
            subsystem_path = os.path.join(self.root_dir, subsystem)
            if os.path.exists(subsystem_path):
                self._learn_subsystem(subsystem, subsystem_path)
        
        new_tools = set(self.knowledge_base['tools'].keys()) - old_tools
        
        if new_tools:
            print(f"  Found {len(new_tools)} new tools:")
            for tool in new_tools:
                print(f"    + {tool}")
                self._integrate_new_tool(tool)
        else:
            print("  No new tools discovered")
        
        self.knowledge_base['last_scan'] = datetime.now().isoformat()
        self._save_knowledge() # Update cache
        return list(new_tools)
    
    def _integrate_new_tool(self, tool_name):
        """Integrate newly discovered tool into knowledge base."""
        tool_info = self.knowledge_base['tools'][tool_name]
        
        # Log discovery
        discovery_log = {
            "timestamp": datetime.now().isoformat(),
            "event": "new_tool_discovered",
            "tool": tool_name,
            "capabilities": tool_info['capabilities']
        }
        self.knowledge_base['evolution_history'].append(discovery_log)
        
        # Analyze how it integrates with existing tools
        integration_opportunities = self._find_integration_opportunities(tool_name)
        tool_info['integration_opportunities'] = integration_opportunities
    
    def _find_integration_opportunities(self, tool_name):
        """Find opportunities to integrate new tool with existing tools."""
        tool_info = self.knowledge_base['tools'][tool_name]
        opportunities = []
        
        # Find tools with complementary capabilities
        for other_tool, other_info in self.knowledge_base['tools'].items():
            if other_tool != tool_name:
                # Check for capability synergies
                shared_caps = set(tool_info['capabilities']) & set(other_info['capabilities'])
                complementary_caps = set(tool_info['capabilities']) - set(other_info['capabilities'])
                
                if shared_caps or complementary_caps:
                    opportunities.append({
                        "partner_tool": other_tool,
                        "shared_capabilities": list(shared_caps),
                        "unique_capabilities": list(complementary_caps),
                        "synergy_potential": len(shared_caps) + len(complementary_caps)
                    })
        
        return sorted(opportunities, key=lambda x: x['synergy_potential'], reverse=True)
    
    
    def _encode_semantic_intent(self, goal: str) -> Dict[str, Any]:
        """
        Phase 8: SEMANTIC ENCODING
        Maps a natural language goal into an abstract 'Intent Embedding'.
        This mirrors JEPA's Joint Embedding approach.
        """
        goal_lower = goal.lower()
        intent = {
            "primary_concepts": [],
            "action_vectors": [],
            "constraints": [],
            "timestamp": datetime.now().isoformat()
        }
        
        # Match concepts from the map
        for concept, keywords in self.semantic_intent_map.items():
            if concept.lower() in goal_lower or any(kw in goal_lower for kw in keywords):
                intent['primary_concepts'].append(concept)
        
        # Extract constraints (simulated abstract reasoning)
        if "sync" in goal_lower or "update" in goal_lower:
            intent['constraints'].append("DATA_INTEGRITY")
        if "evolution" in goal_lower or "phase" in goal_lower:
            intent['constraints'].append("ARCHITECTURAL_STABILITY")
            
        return intent

    def make_strategic_decision_grpo(self, goal, context=None, num_candidates=4):
        """
        GRPO (Group Relative Policy Optimization) - DeepSeek R1 Style
        UPGRADED: Phase 8 Semantic Intent Layer
        """
        # PHASE 8.1: SEMANTIC ENCODING
        print(f"\n[SEMANTIC INTENT] Encoding goal: {goal}")
        semantic_intent = self._encode_semantic_intent(goal)
        print(f"  Abstract Concepts: {', '.join(semantic_intent['primary_concepts'])}")
        
        # PHASE 11: CAUSAL SIMULATION (FORESIGHT)
        # Use the world model to predict success before generating strings
        print(f"\n[WORLD MODEL] Simulating primary intent concepts...")
        simulation = self.world_model.simulate_outcome(semantic_intent['primary_concepts'])
        print(f"  {simulation}")

        print(f"\n[GRPO ENGINE] Generating {num_candidates} candidate solutions...")
        
        # Generate multiple candidate decisions constrained by semantic intent
        candidates = []
        for i in range(num_candidates):
            print(f"  Generating candidate {i+1}/{num_candidates}...")
            candidate = self._make_single_decision(goal, context, candidate_id=i+1)
            candidate['semantic_intent'] = semantic_intent
            candidates.append(candidate)
        
        # Comparative evaluation: Select best candidate
        print(f"\n[GRPO EVALUATION] Comparing {num_candidates} candidates...")
        best_decision = self._select_best_candidate(candidates, goal)
        
        # PHASE 2 EVOLUTION: Apply Reasoning Loop
        print(f"\n[PHASE 2] Applying Reasoning Loop...")
        improved_decision = self.reasoning_loop.think_and_rethink(best_decision)
        
        # Mark as Phase 8 Unified Decision
        improved_decision['method'] = 'PHASE_8_SEMANTIC_GRPO'
        improved_decision['num_candidates'] = num_candidates
        improved_decision['initial_confidence'] = best_decision.get('confidence', 0)
        
        return improved_decision
    
    def _make_single_decision(self, goal, context, candidate_id=1):
        """
        Generate a single candidate decision.
        If it's the first candidate, try to find a 'Flashlight' (Golden Trajectory).
        """
        if candidate_id == 1:
            flashlight = self.golden_manager.find_flashlight(goal)
            if flashlight:
                print(f"  [COLD START] 'Flashlight' found for goal. Using as Candidate #1.")
                decision = {
                    "goal": goal,
                    "candidate_id": candidate_id,
                    "timestamp": datetime.now().isoformat(),
                    "context": context or {},
                    "analysis": {"relevant_capabilities": []},
                    "tools_to_use": flashlight['tools_to_use'],
                    "action_plan": flashlight['action_plan'],
                    "confidence": flashlight['confidence'],
                    "reasoning": flashlight['reasoning'] + ["[COLD START] Derived from Golden Trajectory"],
                    "is_flashlight": True
                }
                return decision

        decision = {
            "goal": goal,
            "candidate_id": candidate_id,
            "timestamp": datetime.now().isoformat(),
            "context": context or {},
            "analysis": {},
            "tools_to_use": [],
            "action_plan": [],
            "confidence": 0.0,
            "reasoning": []
        }
        
        # Phase 1: Identify relevant capabilities
        relevant_capabilities = self._identify_relevant_capabilities(goal)
        decision['analysis']['relevant_capabilities'] = relevant_capabilities
        decision['reasoning'].append(f"Identified {len(relevant_capabilities)} relevant capabilities")
        
        # Phase 2: Select tools
        selected_tools = self._select_optimal_tools(relevant_capabilities, goal)
        decision['tools_to_use'] = selected_tools
        decision['reasoning'].append(f"Selected {len(selected_tools)} tools for execution")
        
        # Phase 3: Generate action plan
        action_plan = self._generate_action_plan(goal, selected_tools)
        decision['action_plan'] = action_plan
        decision['reasoning'].append(f"Generated {len(action_plan)} step action plan")
        
        # Phase 4: Calculate confidence
        confidence = self._calculate_decision_confidence(decision)
        decision['confidence'] = confidence
        decision['reasoning'].append(f"Decision confidence: {confidence:.1%}")
        
        return decision
    
    def _select_best_candidate(self, candidates, goal):
        """
        DeepSeek R1 Style: Compare candidates and select best WITHOUT external teacher.
        Uses VahnRewardModel for comparative scoring across multiple dimensions.
        """
        from system_intelligence.reward_model import VahnRewardModel
        reward_model = VahnRewardModel(workspace_path=str(self.workspace_path))
        
        # Calculate rewards based on Accuracy, Format, and Readability
        rewards = reward_model.calculate_group_rewards(candidates, goal)
        
        best_candidate = candidates[0]
        max_score = -1.0
        
        for i, reward in enumerate(rewards):
            # Map reward (0.0 - 1.0) to GRPO score (0 - 10)
            score = reward * 10
            candidates[i]['grpo_score'] = score
            
            if score > max_score:
                max_score = score
                best_candidate = candidates[i]
            elif score == max_score:
                # Tie-breaker: use individual confidence
                if candidates[i]['confidence'] > best_candidate['confidence']:
                    best_candidate = candidates[i]
        
        # Store selection in decision history
        self.knowledge_base['decision_history'].append({
            'timestamp': datetime.now().isoformat(),
            'goal': goal,
            'method': 'GRPO',
            'candidates_evaluated': len(candidates),
            'best_score': best_candidate['grpo_score'],
            'selected_candidate_id': best_candidate.get('candidate_id', 'unknown')
        })
                
        return best_candidate
    
    def make_strategic_decision(self, goal, context=None, use_grpo=True):
        """
        Make a strategic decision using all available intelligence.
        
        Args:
            goal: The goal to achieve
            context: Additional context
            use_grpo: If True, use GRPO multi-candidate approach (DeepSeek R1 style)
                     If False, use single-shot decision (legacy mode)
        
        Returns: Decision with reasoning and action plan
        """
        if use_grpo:
            return self.make_strategic_decision_grpo(goal, context, num_candidates=4)
        else:
            # Legacy single-shot mode
            return self._make_single_decision(goal, context)
    
    def _identify_relevant_capabilities(self, goal):
        """Identify which capabilities are relevant for the goal."""
        goal_lower = goal.lower()
        relevant = []
        
        for capability, tools in self.knowledge_base['capabilities'].items():
            # 1. Direct match with capability name
            if capability in goal_lower:
                relevant.append(capability)
                continue
            
            # 2. Check synonyms
            if any(word in goal_lower for word in self._get_capability_synonyms(capability)):
                relevant.append(capability)
                continue
                
            # 3. Check if any tool's name from this capability is in the goal
            for tool_id in tools:
                tool_name = tool_id.split('.')[-1]
                if tool_name in goal_lower:
                    relevant.append(capability)
                    break
        
        return relevant
    
    def _get_capability_synonyms(self, capability):
        """Get synonyms for a capability."""
        synonyms = {
            "research": ["study", "investigate", "explore", "find", "search", "lookup", "query", "arxiv", "openalex"],
            "planning": ["plan", "organize", "structure", "roadmap", "prepare", "steps"],
            "optimization": ["improve", "enhance", "better", "optimize", "refine"],
            "learning": ["learn", "train", "develop", "master", "internalize"],
            "prediction": ["predict", "forecast", "anticipate", "foresee", "simulate", "future"],
            "analysis": ["analyze", "examine", "evaluate", "assess", "check", "scan", "decrypt", "decode", "process"]
        }
        return synonyms.get(capability, [])
    
    def _select_optimal_tools(self, capabilities, goal=""):
        """Select the best tools for the required capabilities, prioritizing mentioned tools."""
        selected = []
        goal_lower = goal.lower()
        
        for capability in capabilities:
            # Get all tools with this capability
            tools_with_cap = self.knowledge_base['capabilities'].get(capability, [])
            
            if tools_with_cap:
                # 1. check if any tool with this capability is mentioned by name in the goal
                explicit_tools = [t for t in tools_with_cap if t.split('.')[-1].lower() in goal_lower]
                
                if explicit_tools:
                    best_tool = explicit_tools[0] # Pick the first mentioned tool
                else:
                    # 2. Select the most specialized tool
                    best_tool = min(
                        tools_with_cap,
                        key=lambda t: len(self.knowledge_base['tools'][t]['capabilities'])
                    )
                
                if best_tool not in selected:
                    selected.append(best_tool)
        
        return selected
    
    def _generate_action_plan(self, goal, tools):
        """Generate step-by-step action plan."""
        plan = []
        
        # Order tools by logical sequence
        tool_order = self._determine_tool_sequence(tools)
        
        for i, tool in enumerate(tool_order, 1):
            tool_info = self.knowledge_base['tools'][tool]
            
            step = {
                "step": i,
                "tool": tool,
                "subsystem": tool_info['subsystem'],
                "action": self._infer_tool_action(tool, goal),
                "expected_output": self._infer_expected_output(tool)
            }
            plan.append(step)
        
        # Add feedback loop step
        plan.append({
            "step": len(plan) + 1,
            "tool": "system_intelligence.autonomous_brain",
            "subsystem": "system_intelligence",
            "action": "Evaluate results and learn from execution",
            "expected_output": "Updated knowledge base with lessons learned"
        })
        
        return plan
    
    def _determine_tool_sequence(self, tools):
        """Determine optimal sequence to use tools."""
        # Simple heuristic: Research -> Analysis -> Planning -> Execution
        sequence_priority = {
            "research_tools": 1,
            "cognitive_tools": 2,
            "system_intelligence": 3,
            "meta_tools": 4
        }
        
        return sorted(tools, key=lambda t: sequence_priority.get(
            self.knowledge_base['tools'][t]['subsystem'], 5
        ))
    
    def _find_alternative_tool(self, failed_tool_id):
        """Find a replacement tool with similar capabilities."""
        failed_info = self.knowledge_base['tools'].get(failed_tool_id)
        if not failed_info:
            return None
            
        capabilities = failed_info['capabilities']
        for cap in capabilities:
            siblings = self.knowledge_base['capabilities'].get(cap, [])
            for tool_id in siblings:
                if tool_id != failed_tool_id:
                    # Found a sibling!
                    return tool_id
        return None

    def _infer_tool_action(self, tool, goal):
        """Infer what action to take with this tool for the goal."""
        tool_info = self.knowledge_base['tools'][tool]
        subsystem = tool_info['subsystem']
        
        if subsystem == "research_tools":
            return f"Research: {goal}"
        elif subsystem == "cognitive_tools":
            return f"Analyze and reason about: {goal}"
        elif subsystem == "meta_tools":
            return f"Create improvement plan for: {goal}"
        elif subsystem == "system_intelligence":
            return f"Scan system for: {goal}"
        else:
            return f"Execute {tool} for: {goal}"
    
    def _infer_expected_output(self, tool):
        """Infer what output to expect from this tool."""
        capabilities = self.knowledge_base['tools'][tool]['capabilities']
        
        if "research" in capabilities:
            return "Research report with sources"
        elif "planning" in capabilities:
            return "Strategic roadmap with phases"
        elif "optimization" in capabilities:
            return "Prioritized action list"
        elif "prediction" in capabilities:
            return "Outcome predictions with probabilities"
        else:
            return "Tool-specific results"
    
    def _calculate_decision_confidence(self, decision):
        """Calculate confidence in this decision."""
        confidence = 0.5  # Base confidence
        
        # More tools = higher confidence
        confidence += min(len(decision['tools_to_use']) * 0.1, 0.3)
        
        # More capabilities = higher confidence
        confidence += min(len(decision['analysis']['relevant_capabilities']) * 0.05, 0.2)
        
        return min(confidence, 1.0)
    
    def execute_decision_with_feedback(self, decision):
        """
        Execute a decision and learn from the results (recursive feedback loop).
        """
        print(f"\n[EXECUTION] Executing decision for: {decision['goal']}")
        
        execution_log = {
            "decision_id": decision['timestamp'],
            "started_at": datetime.now().isoformat(),
            "steps_executed": [],
            "learnings": [],
            "success": False
        }
        
        for step in decision['action_plan']:
            print(f"\n  Step {step['step']}: {step['action']}")
            
            # PHASE 12: REALITY EXECUTION (The Bridge) with Self-Healing Recovery
            print(f"  [REALITY] Launching tool: {step['tool']}...")
            step_result = self.action_engine.execute_tool(step['tool'], step['action'])
            
            # PHASE 13: AUTONOMOUS RECOVERY (Self-Healing)
            if step_result.get('status') == 'error':
                print(f"  [RECOVERY] Tool '{step['tool']}' failed. Initiating Deep Rethink...")
                alternative_tool = self._find_alternative_tool(step['tool'])
                if alternative_tool:
                    print(f"  [RECOVERY] Switching to sibling tool: {alternative_tool}")
                    step_result = self.action_engine.execute_tool(alternative_tool, step['action'])
                else:
                    print(f"  [RECOVERY] No direct alternative found for '{step['tool']}'.")

            execution_log['steps_executed'].append({
                "step": step['step'],
                "tool": step['tool'],
                "result": step_result
            })
            
            # Learn from this step
            lesson = self._extract_lesson_from_step(step, step_result)
            if lesson:
                execution_log['learnings'].append(lesson)
                self.knowledge_base['insights'].append(lesson)
        
        execution_log['completed_at'] = datetime.now().isoformat()
        execution_log['success'] = True
        
        # PHASE 4: Collect reasoning trace for distillation
        self.distiller.collect_reasoning_trace(decision)
        
        # PHASE 8: Rejection Sampling (DeepSeek R1 style)
        # If the decision was highly successful and confident, add to Golden Set
        if decision.get('confidence', 0) > 0.85 and not decision.get('is_flashlight'):
             print(f"[REJECTION SAMPLING] High-quality trajectory captured. Adding to Golden Set.")
             # Create a simple pattern from the goal
             pattern = decision['goal'].split(' (')[0].lower() # Remove workspace suffix
             self.golden_manager.add_to_golden_set(pattern, {
                 "reasoning": decision['reasoning'],
                 "tools_to_use": decision['tools_to_use'],
                 "action_plan": decision['action_plan'],
                 "confidence": decision['confidence']
             })

        # PHASE 5.5: EPISODIC ENCODING (The Event)
        self.episodic_memory.log_event(f"Executed decision for: {decision['goal']}", type="execution")
        if execution_log['success']:
            self.episodic_memory.log_event("Execution successful.", type="outcome")
        
        # Check for 'Aha!' moments to log as breakthroughs
        for learning in execution_log['learnings']:
             self.episodic_memory.log_breakthrough(learning)

        # Update evolution history
        self.knowledge_base['evolution_history'].append({
            "timestamp": datetime.now().isoformat(),
            "event": "decision_executed",
            "goal": decision['goal'],
            "learnings_count": len(execution_log['learnings'])
        })
        
        print(f"\n[COMPLETE] Execution finished. Learned {len(execution_log['learnings'])} lessons.")
        
        return execution_log
    
    def _simulate_step_execution(self, step):
        """Simulate executing a step (replace with actual tool calls in production)."""
        return {
            "status": "simulated_success",
            "message": f"Would execute {step['tool']} with action: {step['action']}"
        }
    
    def _extract_lesson_from_step(self, step, result):
        """Extract learning from step execution."""
        return {
            "timestamp": datetime.now().isoformat(),
            "tool_used": step['tool'],
            "action": step['action'],
            "lesson": f"{step['tool']} is effective for {step['action']}",
            "confidence": 0.8
        }
    
    def run_self_play_evolution(self, num_challenges=5):
        """
        PHASE 3: Run self-play evolution cycle
        
        The brain generates its own challenges and learns from attempting them
        This enables unbounded self-improvement beyond human examples
        """
        return self.self_play.run_evolution_cycle(self, num_challenges=num_challenges)
    
    def distill_knowledge_to_student(self, student_name="lightweight_brain"):
        """
        PHASE 4: Distill accumulated knowledge into lightweight student model
        
        Creates compressed reasoning models that can run on resource-constrained devices
        """
        # First distill the knowledge
        distillation_report = self.distiller.distill_knowledge()
        
        # Then create student model
        if distillation_report:
            student = self.distiller.create_student_model(student_name)
            return student
        
        return None
    
    def get_comprehensive_status(self):
        """
        Get complete status including all evolution phases
        """
        base_report = self.generate_system_status_report()
        
        # Add evolution statistics
        base_report['evolution_modules'] = {
            'reasoning_loop': self.reasoning_loop.get_statistics(),
            'self_play': self.self_play.get_evolution_statistics(),
            'distillation': self.distiller.get_distillation_statistics()
        }
        
        return base_report
    
    def generate_system_status_report(self):
        """Generate comprehensive system status report."""
        report = {
            "timestamp": datetime.now().isoformat(),
            "system_knowledge": {
                "total_tools": len(self.knowledge_base['tools']),
                "tools_by_subsystem": {},
                "total_capabilities": len(self.knowledge_base['capabilities']),
                "total_decisions_made": len(self.knowledge_base['decision_history']),
                "total_insights": len(self.knowledge_base['insights']),
                "last_scan": self.knowledge_base['last_scan']
            },
            "top_capabilities": {},
            "recent_decisions": [],
            "recent_insights": []
        }
        
        # Count tools by subsystem
        for tool, info in self.knowledge_base['tools'].items():
            subsystem = info['subsystem']
            if subsystem not in report['system_knowledge']['tools_by_subsystem']:
                report['system_knowledge']['tools_by_subsystem'][subsystem] = 0
            report['system_knowledge']['tools_by_subsystem'][subsystem] += 1
        
        # Top capabilities
        for cap, tools in sorted(self.knowledge_base['capabilities'].items(), 
                                key=lambda x: len(x[1]), reverse=True)[:5]:
            report['top_capabilities'][cap] = len(tools)
        
        # Recent decisions
        report['recent_decisions'] = self.knowledge_base['decision_history'][-3:]
        
        # Recent insights
        report['recent_insights'] = self.knowledge_base['insights'][-5:]
        
        return report


if __name__ == "__main__":
    # Initialize the Autonomous System Brain
    brain = AutonomousSystemBrain()
    
    print("\n" + "="*80)
    print("  DEMONSTRATING AUTONOMOUS CAPABILITIES")
    print("="*80)
    
    # Demo 1: Make a strategic decision
    decision = brain.make_strategic_decision(
        "Learn advanced machine learning and implement a project",
        context={"skill_level": "intermediate", "time_available": "3 months"}
    )
    
    print(f"\n[DECISION] {decision['goal']}")
    print(f"Confidence: {decision['confidence']:.1%}")
    print(f"\nTools Selected: {len(decision['tools_to_use'])}")
    for tool in decision['tools_to_use']:
        print(f"  - {tool}")
    
    print(f"\nAction Plan: {len(decision['action_plan'])} steps")
    for step in decision['action_plan'][:3]:
        print(f"  {step['step']}. {step['action']}")
    
    # Demo 2: Execute with feedback loop
    execution_log = brain.execute_decision_with_feedback(decision)
    
    # Demo 3: Generate status report
    report = brain.generate_system_status_report()
    
    print("\n" + "="*80)
    print("  SYSTEM STATUS REPORT")
    print("="*80)
    print(f"\nTotal Tools Known: {report['system_knowledge']['total_tools']}")
    print(f"Total Capabilities: {report['system_knowledge']['total_capabilities']}")
    print(f"Decisions Made: {report['system_knowledge']['total_decisions_made']}")
    print(f"Insights Gained: {report['system_knowledge']['total_insights']}")
    
    print("\nTools by Subsystem:")
    for subsystem, count in report['system_knowledge']['tools_by_subsystem'].items():
        print(f"  {subsystem}: {count} tools")
    
    print("\nTop Capabilities:")
    for cap, count in report['top_capabilities'].items():
        print(f"  {cap}: {count} tools")

"""
CAUSAL WORLD MODEL - Evolution Phase 11
---------------------------------------
Implements a lightweight Predictive Coding engine for Vahn.
It models the causal relationships between Actions, Contexts, and Outcomes.

Philosophy:
- "If I do X in context Y, Z usually happens."
- Learns from Episodic Memory.
- Predicts failure before it happens (Simulation).

Data Structure:
{
    "action_name": {
        "success_rate": 0.8,
        "causes": ["previous_action_X", "context_Y"],
        "outcomes": {
            "success": 0.9,
            "timeout": 0.05,
            "error": 0.05
        }
    }
}
"""

import json
import os
from collections import defaultdict
from typing import Dict, List, Any

class CausalWorldModel:
    def __init__(self, model_path=".agent/world_model.json"):
        self.model_path = model_path
        self.causal_graph = {}
        self.load_model()
    
    def load_model(self):
        if os.path.exists(self.model_path):
            try:
                with open(self.model_path, 'r') as f:
                    self.causal_graph = json.load(f)
                print(f"[WORLD MODEL] Loaded causal graph with {len(self.causal_graph)} nodes.")
            except:
                self.causal_graph = {}
    
    def save_model(self):
        os.makedirs(os.path.dirname(self.model_path), exist_ok=True)
        with open(self.model_path, 'w') as f:
            json.dump(self.causal_graph, f, indent=2)

    def learn_from_episode(self, episode: Dict[str, Any]):
        """
        Update the causal graph based on an episode (sequence of events).
        """
        # Simple Markov-like learning: Action A -> Outcome B
        # Also sequential: Action A -> Action B
        
        events = episode.get('events', [])
        previous_action = None
        
        for event in events:
            if event['type'] == 'execution':
                # Parse action from description "Executed decision for: {goal}"
                goal = event['description'].replace("Executed decision for: ", "")
                action_type = self._classify_action(goal)
                
                # Update Node
                if action_type not in self.causal_graph:
                    self.causal_graph[action_type] = {
                        "count": 0,
                        "successes": 0,
                        "predecessors": defaultdict(int)
                    }
                
                self.causal_graph[action_type]['count'] += 1
                
                # Link to predecessor (Causal Chain)
                if previous_action:
                    self.causal_graph[action_type]['predecessors'][previous_action] += 1
                
                previous_action = action_type
            
            elif event['type'] == 'outcome' and previous_action:
                if "successful" in event['description'].lower():
                     self.causal_graph[previous_action]['successes'] += 1
        
        self.save_model()

    def predict_success_probability(self, proposed_action: str, context_history: List[str]) -> float:
        """
        Predict probability of success for an action given history.
        Predictive Coding Interface.
        """
        action_type = self._classify_action(proposed_action)
        
        if action_type not in self.causal_graph:
            return 0.5 # Uncertainty prior
        
        node = self.causal_graph[action_type]
        base_rate = node['successes'] / node['count'] if node['count'] > 0 else 0.5
        
        # Adjust based on context (predecessors)
        if context_history:
            last_context = self._classify_action(context_history[-1])
            if last_context in node['predecessors']:
                # Boost if this sequence is common
                support = node['predecessors'][last_context]
                if support > 2:
                    base_rate += 0.1
        
        return min(0.99, max(0.01, base_rate))

    def _classify_action(self, text: str) -> str:
        """Categorize raw text into abstract action types."""
        text = text.lower()
        if "research" in text or "learn" in text: return "RESEARCH"
        if "plan" in text or "create" in text: return "PLANNING"
        if "code" in text or "write" in text: return "CODING"
        if "analyze" in text: return "ANALYSIS"
        return "GENERIC_ACTION"

    def simulate_outcome(self, action_plan: List[str]) -> str:
        """
        Run a mental simulation of a plan.
        Returns a narrative prediction.
        """
        probs = []
        current_context = []
        
        narrative = "Simulation: "
        
        for step in action_plan:
             p = self.predict_success_probability(step, current_context)
             probs.append(p)
             current_context.append(step)
             
             if p < 0.4:
                 narrative += f"Step '{step}' is risky (P={p:.2f}). "
             else:
                 narrative += f"Step '{step}' likely (P={p:.2f}). "
                 
        avg_prob = sum(probs)/len(probs) if probs else 0
        narrative += f"Overall Success Probability: {avg_prob:.1%}"
        return narrative

"""
LONG-TERM MEMORY SYSTEM - Evolution Phase 5

Enables the brain to:
- Remember all past decisions and outcomes
- Build knowledge graphs from experiences
- Retrieve relevant memories for new decisions
- Learn patterns across time
- Never forget successful strategies
"""

import json
import os
from datetime import datetime
from typing import Dict, List, Any, Optional
from collections import defaultdict


class LongTermMemory:
    """
    Persistent memory system for the autonomous brain
    
    Like humans, the AGI needs to remember:
    - What worked before
    - What failed
    - Patterns across experiences
    - Knowledge accumulated over time
    """
    
    def __init__(self, memory_file=".agent/brain_memory.json"):
        self.memory_file = memory_file
        self.memories = {
            'decisions': [],
            'outcomes': [],
            'learnings': [],
            'patterns': {},
            'successes': [],
            'failures': [],
            'meta_insights': []
        }
        self.load_memory()
    
    def load_memory(self):
        """Load persistent memory from disk"""
        if os.path.exists(self.memory_file):
            try:
                with open(self.memory_file, 'r') as f:
                    self.memories = json.load(f)
                print(f"[MEMORY] Loaded {len(self.memories['decisions'])} past decisions")
            except Exception as e:
                print(f"[MEMORY] Starting fresh: {e}")
    
    def save_memory(self):
        """Persist memory to disk"""
        os.makedirs(os.path.dirname(self.memory_file), exist_ok=True)
        with open(self.memory_file, 'w') as f:
            json.dump(self.memories, f, indent=2)
    
    def remember_decision(self, decision: Dict[str, Any], outcome: Optional[Dict] = None):
        """Store a decision and its outcome in long-term memory"""
        memory_entry = {
            'timestamp': datetime.now().isoformat(),
            'goal': decision.get('goal', ''),
            'confidence': decision.get('confidence', 0),
            'tools_used': decision.get('tools_to_use', []),
            'plan_steps': len(decision.get('action_plan', [])),
            'grpo_score': decision.get('grpo_score', 0),
            'reasoning_depth': len(decision.get('reasoning', [])),
            'outcome': outcome
        }
        
        self.memories['decisions'].append(memory_entry)
        
        # Categorize by outcome
        if outcome and outcome.get('success', False):
            self.memories['successes'].append(memory_entry)
        elif outcome and not outcome.get('success', False):
            self.memories['failures'].append(memory_entry)
        
        self.save_memory()
    
    def remember_learning(self, learning: str, context: Dict[str, Any]):
        """Store a learning insight"""
        self.memories['learnings'].append({
            'timestamp': datetime.now().isoformat(),
            'insight': learning,
            'context': context
        })
        self.save_memory()
    
    def recall_similar_decisions(self, goal: str, top_k=5) -> List[Dict]:
        """
        Recall similar past decisions
        
        This is like how humans think: "Have I done something like this before?"
        """
        # Simple keyword matching for now
        goal_words = set(goal.lower().split())
        
        scored_memories = []
        for memory in self.memories['decisions']:
            memory_words = set(memory['goal'].lower().split())
            similarity = len(goal_words & memory_words) / len(goal_words | memory_words) if goal_words | memory_words else 0
            scored_memories.append((similarity, memory))
        
        # Sort by similarity
        scored_memories.sort(reverse=True, key=lambda x: x[0])
        
        return [m[1] for m in scored_memories[:top_k] if m[0] > 0]
    
    def get_pattern_insights(self) -> Dict[str, Any]:
        """
        Extract patterns from accumulated memories
        
        This is meta-learning: learning about learning
        """
        insights = {
            'total_decisions': len(self.memories['decisions']),
            'success_rate': 0,
            'best_tools': defaultdict(int),
            'optimal_plan_length': 0,
            'confidence_correlation': 0
        }
        
        if not self.memories['decisions']:
            return insights
        
        # Success rate
        successes = len(self.memories['successes'])
        total = len([d for d in self.memories['decisions'] if d.get('outcome')])
        insights['success_rate'] = successes / total if total > 0 else 0
        
        # Best tools (which tools correlate with success)
        for success in self.memories['successes']:
            for tool in success.get('tools_used', []):
                insights['best_tools'][tool] += 1
        
        # Optimal plan length
        if self.memories['successes']:
            avg_success_steps = sum(s['plan_steps'] for s in self.memories['successes']) / len(self.memories['successes'])
            insights['optimal_plan_length'] = avg_success_steps
        
        return insights
    
    def get_meta_insight(self) -> str:
        """
        Generate a meta-insight about overall learning
        
        The brain reflecting on its own growth
        """
        patterns = self.get_pattern_insights()
        
        insights = []
        
        if patterns['success_rate'] > 0.7:
            insights.append(f"High success rate ({patterns['success_rate']:.1%}) - strategies are working well")
        elif patterns['success_rate'] < 0.5:
            insights.append(f"Success rate needs improvement ({patterns['success_rate']:.1%})")
        
        if patterns['best_tools']:
            top_tool = max(patterns['best_tools'].items(), key=lambda x: x[1])
            insights.append(f"Tool '{top_tool[0]}' correlates strongly with success")
        
        total = patterns['total_decisions']
        insights.append(f"Total experience: {total} decisions made")
        
        return " | ".join(insights) if insights else "Insufficient data for meta-insights"
    
    def get_statistics(self) -> Dict[str, Any]:
        """Get comprehensive memory statistics"""
        return {
            'total_memories': len(self.memories['decisions']),
            'successes': len(self.memories['successes']),
            'failures': len(self.memories['failures']),
            'learnings': len(self.memories['learnings']),
            'patterns_identified': len(self.memories['patterns']),
            'meta_insights': len(self.memories['meta_insights'])
        }


if __name__ == "__main__":
    print("\n" + "="*80)
    print("  LONG-TERM MEMORY SYSTEM - TESTING")
    print("="*80)
    
    memory = LongTermMemory()
    
    # Simulate some decisions
    print("\nSimulating decision memories...")
    for i in range(5):
        decision = {
            'goal': f'Learn Python topic {i}',
            'confidence': 0.7 + (i * 0.05),
            'tools_to_use': ['research_tools.main'],
            'action_plan': [{'step': 1}, {'step': 2}],
            'grpo_score': 7.0 + i * 0.2,
            'reasoning': ['reason1', 'reason2', 'reason3']
        }
        outcome = {'success': i % 2 == 0}  # Every other succeeds
        memory.remember_decision(decision, outcome)
    
    # Test recall
    print("\nRecalling similar decisions to 'Learn Python basics':")
    similar = memory.recall_similar_decisions('Learn Python basics', top_k=3)
    print(f"  Found {len(similar)} similar decisions")
    
    # Get insights
    print("\nPattern Insights:")
    patterns = memory.get_pattern_insights()
    print(f"  Success Rate: {patterns['success_rate']:.1%}")
    print(f"  Total Decisions: {patterns['total_decisions']}")
    
    print("\nMeta-Insight:")
    print(f"  {memory.get_meta_insight()}")
    
    print("\n[MEMORY SYSTEM OPERATIONAL]")

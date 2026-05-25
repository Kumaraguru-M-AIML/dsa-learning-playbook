
import sys
import os
import json
from collections import defaultdict

root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(root_dir)

class LearningEngine:
    """
    Extracts lessons, patterns, and insights from experiences.
    Implements TDS Metacognition Layer - learning from everything.
    """
    
    def __init__(self):
        self.knowledge_base = defaultdict(list)
        self.patterns = []
        
    def extract_lessons(self, experience):
        """
        Analyze an experience and extract actionable lessons.
        
        Args:
            experience: Dict with 'action', 'outcome', 'context', 'metrics'
            
        Returns:
            Extracted lessons and patterns
        """
        print("\n=== LEARNING FROM EXPERIENCE ===\n")
        
        lessons = {
            "what_worked": [],
            "what_failed": [],
            "insights": [],
            "action_items": []
        }
        
        # Analyze outcome
        if experience.get('outcome') == 'success':
            lessons['what_worked'].append({
                "action": experience.get('action'),
                "context": experience.get('context'),
                "principle": self._extract_principle(experience, 'success')
            })
        else:
            lessons['what_failed'].append({
                "action": experience.get('action'),
                "context": experience.get('context'),
                "root_cause": self._analyze_failure(experience)
            })
        
        # Generate insights
        insights = self._generate_insights(experience)
        lessons['insights'] = insights
        
        # Create action items
        lessons['action_items'] = self._create_action_items(lessons)
        
        # Store in knowledge base
        category = experience.get('category', 'general')
        self.knowledge_base[category].append(lessons)
        
        return lessons
    
    def _extract_principle(self, experience, outcome_type):
        """Extract reusable principle from successful action"""
        return f"In {experience.get('context')}, {experience.get('action')} leads to positive outcomes"
    
    def _analyze_failure(self, experience):
        """Determine root cause of failure"""
        # Simple heuristic analysis
        if experience.get('preparation') == 'insufficient':
            return "Lack of preparation"
        elif experience.get('execution') == 'poor':
            return "Execution issues"
        else:
            return "External factors or wrong approach"
    
    def _generate_insights(self, experience):
        """Generate meta-level insights"""
        insights = []
        
        # Pattern recognition
        if len(self.knowledge_base[experience.get('category', 'general')]) > 3:
            insights.append("Pattern detected: Multiple experiences in this category")
        
        # Trend analysis
        metrics = experience.get('metrics', {})
        if metrics.get('improvement', 0) > 0:
            insights.append(f"Positive trend: {metrics.get('improvement')}% improvement")
        
        return insights
    
    def _create_action_items(self, lessons):
        """Generate specific next actions based on lessons"""
        actions = []
        
        if lessons['what_worked']:
            actions.append("Replicate successful actions in similar contexts")
        
        if lessons['what_failed']:
            actions.append("Create prevention protocol for identified failure modes")
        
        if lessons['insights']:
            actions.append("Update operating procedures based on new insights")
        
        return actions
    
    def synthesize_knowledge(self, category=None):
        """
        Synthesize accumulated knowledge into actionable wisdom.
        
        Args:
            category: Optional category filter
            
        Returns:
            Synthesized knowledge summary
        """
        if category:
            experiences = self.knowledge_base.get(category, [])
        else:
            experiences = [item for items in self.knowledge_base.values() for item in items]
        
        synthesis = {
            "total_experiences": len(experiences),
            "success_patterns": self._identify_success_patterns(experiences),
            "failure_patterns": self._identify_failure_patterns(experiences),
            "golden_rules": self._extract_golden_rules(experiences),
            "suggested_experiments": self._suggest_experiments(experiences)
        }
        
        return synthesis
    
    def _identify_success_patterns(self, experiences):
        """Find recurring success patterns"""
        patterns = []
        # Placeholder - would implement actual pattern matching
        if len(experiences) > 5:
            patterns.append("Consistent preparation leads to better outcomes")
        return patterns
    
    def _identify_failure_patterns(self, experiences):
        """Find recurring failure patterns"""
        patterns = []
        # Placeholder
        return patterns
    
    def _extract_golden_rules(self, experiences):
        """Extract high-level principles"""
        return [
            "Measure before optimizing",
            "Small consistent actions > large sporadic efforts",
            "Feedback loops accelerate learning"
        ]
    
    def _suggest_experiments(self, experiences):
        """Suggest new experiments to test hypotheses"""
        return [
            "Test edge cases of successful patterns",
            "Vary one factor at a time to isolate causation"
        ]

if __name__ == "__main__":
    engine = LearningEngine()
    
    # Example experience
    experience = {
        "action": "Used Bayesian filtering in research tool",
        "outcome": "success",
        "context": "Academic paper search",
        "category": "research_tools",
        "metrics": {"accuracy": 77, "improvement": 25},
        "preparation": "sufficient"
    }
    
    lessons = engine.extract_lessons(experience)
    print(json.dumps(lessons, indent=2))
    
    # Synthesize knowledge
    synthesis = engine.synthesize_knowledge("research_tools")
    print("\n=== KNOWLEDGE SYNTHESIS ===")
    print(json.dumps(synthesis, indent=2))

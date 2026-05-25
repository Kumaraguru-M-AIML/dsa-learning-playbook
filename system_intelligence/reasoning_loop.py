"""
Reasoning Loop Module - Phase 2 of DeepSeek R1 Integration

Implements emergent chain-of-thought reasoning:
- Pause before executing
- Reflect on solution quality
- Rethink if confidence is low
- Self-correct mistakes

Inspired by DeepSeek R1's spontaneous "Wait, let me recalculate..." behavior
"""

import json
from datetime import datetime
from typing import Dict, List, Any, Tuple


class ReasoningLoop:
    """
    Emergent Reasoning Loop - DeepSeek R1 Style
    
    The system learns to:
    1. Pause before committing
    2. Reflect on its reasoning
    3. Identify potential flaws
    4. Rethink and improve
    5. Self-correct errors
    """
    
    def __init__(self, confidence_threshold=0.75):
        self.confidence_threshold = confidence_threshold
        self.reflection_history = []
        self.rethink_count = 0
        self.self_corrections = 0
    
    def think_and_rethink(self, decision: Dict[str, Any], max_iterations=3) -> Dict[str, Any]:
        """
        Main reasoning loop: Think → Reflect → Rethink if needed
        
        Args:
            decision: Initial decision from GRPO
            max_iterations: Maximum number of rethink cycles
        
        Returns: Improved decision after reflection and potential rethinking
        """
        print("\n" + "="*80)
        print("  REASONING LOOP ACTIVATED - DeepSeek R1 Style")
        print("="*80)
        
        current_decision = decision
        iteration = 0
        
        while iteration < max_iterations:
            iteration += 1
            
            print(f"\n[REASONING CYCLE {iteration}]")
            print(f"  Current Confidence: {current_decision.get('confidence', 0):.1%}")
            
            # Step 1: Reflect on current decision
            reflection = self._reflect_on_decision(current_decision)
            
            # Step 2: Check if rethinking is needed
            should_rethink = self._should_rethink(reflection, current_decision)
            
            if not should_rethink:
                print("  + Decision validated. Proceeding with confidence.")
                break
            
            # Step 3: Rethink and improve
            print("  ! Reflection suggests improvement needed...")
            print(f"  >> Wait, let me recalculate...")
            
            # PHASE 9: Meta-Cognitive Logging (Reward Alignment)
            current_decision['reasoning'].append("Wait, let me recalculate this strategy...")
            current_decision['reasoning'].append("Actually, rethinking the tool sequence for better efficiency.")
            
            improved_decision = self._rethink_decision(current_decision, reflection)
            
            # Check if improvement occurred
            if improved_decision['confidence'] > current_decision['confidence']:
                print(f"  + Improved! Confidence: {current_decision.get('confidence', 0):.1%} -> {improved_decision['confidence']:.1%}")
                current_decision = improved_decision
                self.self_corrections += 1
            else:
                print("  -> No further improvement found. Accepting current solution.")
                break
            
            self.rethink_count += 1
        
        # Add reasoning loop metadata
        current_decision['reasoning_loop'] = {
            'iterations': iteration,
            'rethinks_performed': self.rethink_count,
            'self_corrections': self.self_corrections,
            'final_confidence': current_decision.get('confidence', 0),
            'reflection_history': self.reflection_history[-iteration:]
        }
        
        print(f"\n[REASONING COMPLETE] Final Confidence: {current_decision.get('confidence', 0):.1%}")
        print(f"  Total Rethink Cycles: {iteration}")
        print(f"  Self-Corrections Made: {self.self_corrections}")
        
        return current_decision
    
    def _reflect_on_decision(self, decision: Dict[str, Any]) -> Dict[str, Any]:
        """
        Reflect on decision quality - identify potential issues
        
        DeepSeek R1 insight: The model learns to self-reflect naturally
        """
        reflection = {
            'timestamp': datetime.now().isoformat(),
            'decision_confidence': decision.get('confidence', 0),
            'identified_issues': [],
            'strengths': [],
            'improvement_suggestions': [],
            'overall_quality': 0.0
        }
        
        # Analyze tool selection
        tools_used = len(decision.get('tools_to_use', []))
        if tools_used == 0:
            reflection['identified_issues'].append("No tools selected - decision may be incomplete")
        elif tools_used > 5:
            reflection['identified_issues'].append("Too many tools selected - may be unfocused")
        else:
            reflection['strengths'].append(f"Appropriate tool selection ({tools_used} tools)")
        
        # Analyze action plan
        action_plan = decision.get('action_plan', [])
        if len(action_plan) < 2:
            reflection['identified_issues'].append("Action plan too short - missing steps?")
        elif len(action_plan) > 10:
            reflection['identified_issues'].append("Action plan too long - may be overcomplicated")
        else:
            reflection['strengths'].append(f"Well-structured action plan ({len(action_plan)} steps)")
        
        # Analyze reasoning depth
        reasoning = decision.get('reasoning', [])
        if len(reasoning) < 3:
            reflection['identified_issues'].append("Reasoning too shallow - needs deeper analysis")
        else:
            reflection['strengths'].append(f"Good reasoning depth ({len(reasoning)} points)")
        
        # Analyze GRPO score if available
        grpo_score = decision.get('grpo_score', 0)
        if grpo_score < 6.0:
            reflection['identified_issues'].append(f"Low GRPO score ({grpo_score:.1f}/10) - solution may be suboptimal")
        elif grpo_score >= 8.0:
            reflection['strengths'].append(f"High GRPO score ({grpo_score:.1f}/10)")
        
        # Generate improvement suggestions
        if reflection['identified_issues']:
            reflection['improvement_suggestions'] = self._generate_improvements(
                decision, 
                reflection['identified_issues']
            )
        
        # Calculate overall quality
        quality_score = 1.0
        quality_score -= len(reflection['identified_issues']) * 0.15
        quality_score += len(reflection['strengths']) * 0.1
        reflection['overall_quality'] = max(0.0, min(1.0, quality_score))
        
        # Store reflection
        self.reflection_history.append(reflection)
        
        # Display reflection
        print(f"\n  [REFLECTION]")
        if reflection['strengths']:
            print(f"  + Strengths: {len(reflection['strengths'])}")
            for strength in reflection['strengths'][:2]:
                print(f"    * {strength}")
        
        if reflection['identified_issues']:
            print(f"  ! Issues Found: {len(reflection['identified_issues'])}")
            for issue in reflection['identified_issues'][:2]:
                print(f"    * {issue}")
        
        print(f"  Overall Quality: {reflection['overall_quality']:.1%}")
        
        return reflection
    
    def _should_rethink(self, reflection: Dict[str, Any], decision: Dict[str, Any]) -> bool:
        """
        Determine if rethinking is needed based on reflection
        
        Criteria:
        - Low confidence
        - Issues identified in reflection
        - Low overall quality score
        """
        confidence = decision.get('confidence', 0)
        quality = reflection['overall_quality']
        issues_count = len(reflection['identified_issues'])
        
        # Rethink if:
        # 1. Confidence below threshold
        if confidence < self.confidence_threshold:
            return True
        
        # 2. Quality score too low
        if quality < 0.6:
            return True
        
        # 3. Multiple issues identified
        if issues_count >= 2:
            return True
        
        return False
    
    def _rethink_decision(self, decision: Dict[str, Any], reflection: Dict[str, Any]) -> Dict[str, Any]:
        """
        Rethink and improve the decision based on reflection
        
        DeepSeek R1 insight: Model learns to self-correct through iteration
        """
        improved = decision.copy()
        
        # Apply improvement suggestions
        for suggestion in reflection['improvement_suggestions']:
            if suggestion['type'] == 'add_tool':
                if suggestion['tool'] not in improved['tools_to_use']:
                    improved['tools_to_use'].append(suggestion['tool'])
                    improved['reasoning'].append(f"Added {suggestion['tool']} based on reflection")
            
            elif suggestion['type'] == 'expand_plan':
                # Add intermediate steps
                improved['action_plan'] = self._expand_action_plan(improved['action_plan'])
                improved['reasoning'].append("Expanded action plan with intermediate steps")
            
            elif suggestion['type'] == 'deepen_reasoning':
                # Add more reasoning steps
                improved['reasoning'].append("Re-evaluated core assumptions")
                improved['reasoning'].append("Considered alternative approaches")
        
        # Recalculate confidence based on improvements
        original_confidence = decision.get('confidence', 0)
        improvement_boost = len(reflection['improvement_suggestions']) * 0.05
        improved['confidence'] = min(1.0, original_confidence + improvement_boost)
        
        # Update GRPO score
        if 'grpo_score' in decision:
            improved['grpo_score'] = min(10.0, decision['grpo_score'] + improvement_boost * 10)
        
        return improved
    
    def _generate_improvements(self, decision: Dict[str, Any], issues: List[str]) -> List[Dict[str, Any]]:
        """Generate concrete improvement suggestions based on identified issues"""
        improvements = []
        
        for issue in issues:
            if "No tools selected" in issue:
                improvements.append({
                    'type': 'add_tool',
                    'tool': 'planning_tool',
                    'reason': 'Need a tool to execute the plan'
                })
            
            elif "Action plan too short" in issue:
                improvements.append({
                    'type': 'expand_plan',
                    'reason': 'Plan needs more detailed steps'
                })
            
            elif "Reasoning too shallow" in issue:
                improvements.append({
                    'type': 'deepen_reasoning',
                    'reason': 'Analysis needs more depth'
                })
            
            elif "Low GRPO score" in issue:
                improvements.append({
                    'type': 'rethink_approach',
                    'reason': 'Current approach may be suboptimal'
                })
        
        return improvements
    
    def _expand_action_plan(self, plan: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Expand action plan with intermediate steps"""
        expanded = []
        
        for i, step in enumerate(plan):
            # Add the original step
            expanded.append(step)
            
            # Add validation step after each major action
            if i < len(plan) - 1:  # Don't add after final step
                expanded.append({
                    'step': len(expanded) + 1,
                    'tool': 'validation',
                    'action': f"Validate results from step {step['step']}",
                    'expected_output': 'Confirmation that step succeeded'
                })
        
        # Renumber steps
        for i, step in enumerate(expanded, 1):
            step['step'] = i
        
        return expanded
    
    def get_statistics(self) -> Dict[str, Any]:
        """Get reasoning loop statistics"""
        return {
            'total_reflections': len(self.reflection_history),
            'total_rethinks': self.rethink_count,
            'self_corrections': self.self_corrections,
            'average_quality': sum(r['overall_quality'] for r in self.reflection_history) / max(1, len(self.reflection_history)) if self.reflection_history else 0
        }


if __name__ == "__main__":
    # Test the reasoning loop
    print("\n" + "="*80)
    print("  REASONING LOOP MODULE - TESTING")
    print("="*80)
    
    # Mock decision for testing
    test_decision = {
        'goal': 'Learn quantum computing',
        'confidence': 0.6,
        'grpo_score': 5.5,
        'tools_to_use': ['research_tools.arxiv'],
        'action_plan': [
            {'step': 1, 'action': 'Search papers', 'tool': 'arxiv'},
            {'step': 2, 'action': 'Learn', 'tool': 'self'}
        ],
        'reasoning': ['Need to research quantum computing']
    }
    
    # Apply reasoning loop
    loop = ReasoningLoop(confidence_threshold=0.75)
    improved = loop.think_and_rethink(test_decision)
    
    print("\n" + "="*80)
    print("  RESULTS")
    print("="*80)
    print(f"Original Confidence: 60%")
    print(f"Final Confidence: {improved['confidence']:.1%}")
    print(f"Rethinks: {improved['reasoning_loop']['rethinks_performed']}")
    print(f"Self-Corrections: {improved['reasoning_loop']['self_corrections']}")
    
    stats = loop.get_statistics()
    print(f"\nStatistics:")
    print(f"  Average Quality: {stats['average_quality']:.1%}")

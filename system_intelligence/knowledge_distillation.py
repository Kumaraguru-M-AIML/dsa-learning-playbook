"""
Knowledge Distillation Module - Phase 4 of DeepSeek R1 Integration

Creates compressed, lightweight reasoning models from the large autonomous brain:
- Captures reasoning traces from brain's decisions
- Distills patterns into simplified rules
- Creates lightweight decision modules
- Enables deployment on resource-constrained devices

Inspired by DeepSeek R1's distillation: 671B model creates textbook for 7B model
Result: 7B beats GPT-4o on reasoning tasks (6x parameter advantage for GPT-4o!)
"""

import json
from datetime import datetime
from typing import Dict, List, Any, Tuple
from collections import defaultdict


class KnowledgeDistiller:
    """
    Knowledge Distillation Engine - DeepSeek R1 Style
    
    The large brain (teacher) creates "reasoning textbooks" for small brains (students):
    1. Collect reasoning traces from expert brain
    2. Identify common patterns
    3. Extract simplified rules
    4. Create compressed decision models
    5. Deploy lightweight versions anywhere
    """
    
    def __init__(self):
        self.reasoning_traces = []
        self.distilled_patterns = {}
        self.simplified_rules = []
        self.compression_ratio = 0.0
        self.student_models = {}
    
    def collect_reasoning_trace(self, decision: Dict[str, Any]):
        """
        Collect a reasoning trace from the brain's decision
        
        DeepSeek insight: Every decision is a learning example
        """
        trace = {
            'timestamp': datetime.now().isoformat(),
            'goal': decision.get('goal', ''),
            'tools_used': decision.get('tools_to_use', []),
            'action_plan': decision.get('action_plan', []),
            'reasoning': decision.get('reasoning', []),
            'confidence': decision.get('confidence', 0),
            'grpo_score': decision.get('grpo_score', 0),
            'method': decision.get('method', 'unknown')
        }
        
        self.reasoning_traces.append(trace)
        
        # Auto-distill every 100 traces
        if len(self.reasoning_traces) % 100 == 0:
            print(f"\n[DISTILLATION] Collected {len(self.reasoning_traces)} traces. Auto-distilling...")
            self.distill_knowledge()
    
    def distill_knowledge(self) -> Dict[str, Any]:
        """
        Distill collected reasoning traces into simplified patterns
        
        This is like the large model creating a textbook for small models
        """
        print("\n" + "="*80)
        print("  KNOWLEDGE DISTILLATION - DeepSeek R1 Style")
        print("  Creating Compressed Reasoning Models from Expert Traces")
        print("="*80)
        
        if len(self.reasoning_traces) < 10:
            print(f"  ! Need at least 10 traces (have {len(self.reasoning_traces)})")
            return {}
        
        print(f"\n[ANALYZING] {len(self.reasoning_traces)} reasoning traces...")
        
        # Extract patterns
        patterns = self._extract_patterns()
        
        # Simplify into rules
        rules = self._create_simplified_rules(patterns)
        
        # Calculate compression
        compression = self._calculate_compression_ratio()
        
        distillation_report = {
            'timestamp': datetime.now().isoformat(),
            'traces_analyzed': len(self.reasoning_traces),
            'patterns_found': len(patterns),
            'rules_created': len(rules),
            'compression_ratio': compression,
            'patterns': patterns,
            'rules': rules
        }
        
        self.distilled_patterns = patterns
        self.simplified_rules = rules
        self.compression_ratio = compression
        
        print(f"\n[DISTILLATION COMPLETE]")
        print(f"  Traces Analyzed: {len(self.reasoning_traces)}")
        print(f"  Patterns Found: {len(patterns)}")
        print(f"  Rules Created: {len(rules)}")
        print(f"  Compression: {compression:.1%} of original size")
        
        return distillation_report
    
    def _extract_patterns(self) -> Dict[str, Any]:
        """Extract common patterns from reasoning traces"""
        patterns = {
            'tool_usage': defaultdict(int),
            'successful_strategies': [],
            'common_reasoning': defaultdict(int),
            'confidence_thresholds': {},
            'plan_structures': defaultdict(int)
        }
        
        # Analyze tool usage patterns
        for trace in self.reasoning_traces:
            for tool in trace.get('tools_used', []):
                patterns['tool_usage'][tool] += 1
            
            # Track successful strategies (high confidence + high GRPO score)
            if trace.get('confidence', 0) > 0.7 and trace.get('grpo_score', 0) > 7.0:
                patterns['successful_strategies'].append({
                    'goal_type': self._classify_goal(trace.get('goal', '')),
                    'tools': trace.get('tools_used', []),
                    'plan_length': len(trace.get('action_plan', []))
                })
            
            # Track reasoning patterns
            for reason in trace.get('reasoning', []):
                patterns['common_reasoning'][reason[:50]] += 1  # First 50 chars
            
            # Track plan structures
            plan_length = len(trace.get('action_plan', []))
            patterns['plan_structures'][plan_length] += 1
        
        print(f"  Pattern Analysis:")
        print(f"    Most used tools: {sorted(patterns['tool_usage'].items(), key=lambda x: x[1], reverse=True)[:3]}")
        print(f"    Successful strategies: {len(patterns['successful_strategies'])}")
        
        return patterns
    
    def _classify_goal(self, goal: str) -> str:
        """Classify goal type for pattern matching"""
        goal_lower = goal.lower()
        
        if any(kw in goal_lower for kw in ['learn', 'study', 'understand']):
            return 'learning'
        elif any(kw in goal_lower for kw in ['build', 'create', 'develop']):
            return 'creation'
        elif any(kw in goal_lower for kw in ['analyze', 'evaluate', 'assess']):
            return 'analysis'
        elif any(kw in goal_lower for kw in ['improve', 'optimize', 'enhance']):
            return 'optimization'
        else:
            return 'general'
    
    def _create_simplified_rules(self, patterns: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Create simple if-then rules from patterns"""
        rules = []
        
        # Rule 1: Tool selection based on goal type
        tool_usage = patterns['tool_usage']
        if tool_usage:
            top_tools = sorted(tool_usage.items(), key=lambda x: x[1], reverse=True)[:5]
            rules.append({
                'rule_type': 'tool_selection',
                'condition': 'any_goal',
                'action': f'prefer_tools',
                'tools': [t[0] for t in top_tools],
                'confidence': 0.8
            })
        
        # Rule 2: Plan length based on goal type
        successful_strategies = patterns['successful_strategies']
        if successful_strategies:
            avg_plan_length = sum(s['plan_length'] for s in successful_strategies) / len(successful_strategies)
            rules.append({
                'rule_type': 'plan_structure',
                'condition': 'high_confidence_needed',
                'action': f'use_{int(avg_plan_length)}_step_plan',
                'confidence': 0.75
            })
        
        # Rule 3: Goal-specific strategies
        goal_types = defaultdict(list)
        for strategy in successful_strategies:
            goal_types[strategy['goal_type']].append(strategy['tools'])
        
        for goal_type, tool_lists in goal_types.items():
            if len(tool_lists) >= 2:  # Need at least 2 examples
                # Find most common tools for this goal type
                tool_freq = defaultdict(int)
                for tools in tool_lists:
                    for tool in tools:
                        tool_freq[tool] += 1
                
                best_tools = sorted(tool_freq.items(), key=lambda x: x[1], reverse=True)[:2]
                
                rules.append({
                    'rule_type': 'goal_specific',
                    'condition': f'goal_type={goal_type}',
                    'action': 'use_tools',
                    'tools': [t[0] for t in best_tools],
                    'confidence': len(tool_lists) / len(self.reasoning_traces)
                })
        
        return rules
    
    def _calculate_compression_ratio(self) -> float:
        """
        Calculate how much smaller the distilled model is
        
        DeepSeek achievement: 671B → 7B (96% compression!)
        """
        if not self.reasoning_traces:
            return 0.0
        
        # Original size: all traces
        original_size = len(self.reasoning_traces) * 1000  # Assume 1000 units per trace
        
        # Compressed size: just the rules
        compressed_size = len(self.simplified_rules) * 100  # 100 units per rule
        
        if original_size == 0:
            return 0.0
        
        return compressed_size / original_size
    
    def create_student_model(self, name: str) -> Dict[str, Any]:
        """
        Create a lightweight student model from distilled knowledge
        
        This is the "small brain" that uses the textbook created by the large brain
        """
        print(f"\n[CREATING STUDENT MODEL] {name}")
        
        if not self.simplified_rules:
            print("  ! No rules to distill. Run distill_knowledge() first.")
            return {}
        
        student = {
            'name': name,
            'created_at': datetime.now().isoformat(),
            'rules': self.simplified_rules.copy(),
            'size_ratio': self.compression_ratio,
            'source_traces': len(self.reasoning_traces),
            'capabilities': self._infer_student_capabilities()
        }
        
        self.student_models[name] = student
        
        print(f"  + Student model '{name}' created")
        print(f"    Rules: {len(student['rules'])}")
        print(f"    Size: {self.compression_ratio:.1%} of teacher")
        print(f"    Capabilities: {len(student['capabilities'])}")
        
        return student
    
    def _infer_student_capabilities(self) -> List[str]:
        """Infer what the student model can do based on distilled rules"""
        capabilities = set()
        
        for rule in self.simplified_rules:
            if rule['rule_type'] == 'goal_specific':
                condition = rule.get('condition', '')
                if 'learning' in condition:
                    capabilities.add('learning_tasks')
                elif 'creation' in condition:
                    capabilities.add('creation_tasks')
                elif 'analysis' in condition:
                    capabilities.add('analysis_tasks')
        
        return list(capabilities)
    
    def deploy_student_model(self, student_name: str) -> str:
        """
        Export student model for deployment
        
        In production, this would create a standalone package
        """
        if student_name not in self.student_models:
            return f"Error: Student model '{student_name}' not found"
        
        student = self.student_models[student_name]
        
        deployment_package = {
            'model_name': student_name,
            'version': '1.0',
            'created_at': student['created_at'],
            'rules': student['rules'],
            'usage': 'Lightweight decision-making model for resource-constrained environments'
        }
        
        # Save to file
        filename = f"student_model_{student_name}.json"
        filepath = f".agent/{filename}"
        
        with open(filepath, 'w') as f:
            json.dump(deployment_package, f, indent=2)
        
        print(f"\n[DEPLOYED] Student model saved to: {filepath}")
        print(f"  Size: {self.compression_ratio:.1%} of original brain")
        print(f"  Ready for deployment on edge devices, phones, etc.")
        
        return filepath
    
    def get_distillation_statistics(self) -> Dict[str, Any]:
        """Get comprehensive distillation statistics"""
        return {
            'total_traces_collected': len(self.reasoning_traces),
            'patterns_identified': len(self.distilled_patterns),
            'rules_created': len(self.simplified_rules),
            'compression_ratio': self.compression_ratio,
            'student_models_created': len(self.student_models),
            'deployment_ready': list(self.student_models.keys())
        }


if __name__ == "__main__":
    # Test knowledge distillation
    print("\n" + "="*80)
    print("  KNOWLEDGE DISTILLATION MODULE - TESTING")
    print("="*80)
    
    distiller = KnowledgeDistiller()
    
    # Simulate collecting traces
    print("\nSimulating reasoning trace collection...")
    for i in range(15):
        mock_decision = {
            'goal': f'Learn about topic {i}',
            'tools_to_use': ['research_tools.main', 'cognitive_tools.analyzer'],
            'action_plan': [
                {'step': 1, 'action': 'Research'},
                {'step': 2, 'action': 'Analyze'},
                {'step': 3, 'action': 'Learn'}
            ],
            'reasoning': ['Need to understand', 'Must analyze', 'Should learn'],
            'confidence': 0.7 + (i % 3) * 0.1,
            'grpo_score': 7.0 + (i % 3),
            'method': 'GRPO+ReasoningLoop'
        }
        distiller.collect_reasoning_trace(mock_decision)
    
    # Manual distillation
    report = distiller.distill_knowledge()
    
    # Create student model
    student = distiller.create_student_model('lightweight_v1')
    
    # Get statistics
    stats = distiller.get_distillation_statistics()
    
    print("\n" + "="*80)
    print("  DISTILLATION STATISTICS")
    print("="*80)
    print(f"Traces Collected: {stats['total_traces_collected']}")
    print(f"Rules Created: {stats['rules_created']}")
    print(f"Compression Ratio: {stats['compression_ratio']:.1%}")
    print(f"Student Models: {stats['student_models_created']}")

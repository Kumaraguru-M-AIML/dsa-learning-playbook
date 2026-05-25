"""
GOAL DECOMPOSITION ENGINE - Evolution Phase 7

Enables the brain to:
- Break complex goals into manageable sub-goals
- Create hierarchical action plans
- Identify dependencies between tasks
- Parallelize independent sub-tasks
- Track progress across goal tree
"""

from typing import Dict, List, Any, Tuple, Optional
from datetime import datetime
from collections import defaultdict


class GoalDecompositionEngine:
    """
    Advanced goal decomposition using hierarchical planning
    
    Transforms: "Master Machine Learning" 
    Into: Tree of concrete, achievable sub-goals
    """
    
    def __init__(self):
        self.goal_trees = {}
        self.completed_subgoals = set()
        self.active_goals = {}
    
    def decompose_goal(self, goal: str, max_depth=3) -> Dict[str, Any]:
        """
        Decompose a goal into hierarchical sub-goals
        
        Args:
            goal: The high-level goal
            max_depth: Maximum decomposition depth
            
        Returns: Goal tree with sub-goals, dependencies, estimates
        """
        goal_tree = {
            'main_goal': goal,
            'id': f"goal_{datetime.now().timestamp()}",
            'created_at': datetime.now().isoformat(),
            'depth': 0,
            'sub_goals': [],
            'estimated_time': 0,
            'complexity': self._estimate_complexity(goal),
            'dependencies': [],
            'status': 'pending'
        }
        
        # Level 1: Major phases
        sub_goals = self._generate_subgoals(goal, depth=1)
        
        for i, sub_goal in enumerate(sub_goals):
            sub_node = {
                'goal': sub_goal,
                'id': f"{goal_tree['id']}_sub{i}",
                'depth': 1,
                'sub_goals': [],
                'estimated_time': self._estimate_time(sub_goal),
                'complexity': self._estimate_complexity(sub_goal),
                'dependencies': [],
                'status': 'pending'
            }
            
            # Level 2: Detailed tasks (if needed and not at max depth)
            if max_depth > 1 and self._needs_further_decomposition(sub_goal):
                detailed_tasks = self._generate_subgoals(sub_goal, depth=2)
                
                for j, task in enumerate(detailed_tasks):
                    task_node = {
                        'goal': task,
                        'id': f"{sub_node['id']}_task{j}",
                        'depth': 2,
                        'sub_goals': [],
                        'estimated_time': self._estimate_time(task),
                        'complexity': self._estimate_complexity(task),
                        'dependencies': [],
                        'status': 'pending'
                    }
                    
                    # Level 3: Atomic actions (if needed)
                    if max_depth > 2 and self._needs_further_decomposition(task):
                        actions = self._generate_atomic_actions(task)
                        for k, action in enumerate(actions):
                            action_node = {
                                'goal': action,
                                'id': f"{task_node['id']}_action{k}",
                                'depth': 3,
                                'sub_goals': [],
                                'estimated_time': self._estimate_time(action),
                                'complexity': 'simple',
                                'dependencies': [],
                                'status': 'pending'
                            }
                            task_node['sub_goals'].append(action_node)
                    
                    sub_node['sub_goals'].append(task_node)
            
            goal_tree['sub_goals'].append(sub_node)
        
        # Calculate total estimated time
        goal_tree['estimated_time'] = self._calculate_total_time(goal_tree)
        
        # Identify dependencies
        goal_tree = self._identify_dependencies(goal_tree)
        
        # Store
        self.goal_trees[goal_tree['id']] = goal_tree
        
        return goal_tree
    
    def _generate_subgoals(self, goal: str, depth: int) -> List[str]:
        """Generate sub-goals based on goal type and depth"""
        goal_lower = goal.lower()
        
        # Learning goals
        if any(kw in goal_lower for kw in ['learn', 'master', 'understand']):
            if depth == 1:
                return [
                    f"Understand fundamentals of {self._extract_topic(goal)}",
                    f"Practice intermediate concepts",
                    f"Apply advanced techniques",
                    f"Build real-world project"
                ]
            elif depth == 2:
                return [
                    f"Research theory and concepts",
                    f"Complete practical exercises",
                    f"Review and internalize"
                ]
        
        # Building/Creation goals
        elif any(kw in goal_lower for kw in ['build', 'create', 'develop']):
            if depth == 1:
                return [
                    f"Design architecture",
                    f"Implement core features",
                    f"Test and refine",
                    f"Deploy and document"
                ]
            elif depth == 2:
                return [
                    f"Research requirements",
                    f"Create detailed plan",
                    f"Execute implementation"
                ]
        
        # Analysis goals
        elif any(kw in goal_lower for kw in ['analyze', 'evaluate', 'assess']):
            if depth == 1:
                return [
                    f"Gather data/information",
                    f"Perform analysis",
                    f"Generate insights",
                    f"Create recommendations"
                ]
        
        # Default decomposition
        return [
            f"Research and plan for: {goal}",
            f"Execute main work for: {goal}",
            f"Review and finalize: {goal}"
        ]
    
    def _generate_atomic_actions(self, task: str) -> List[str]:
        """Generate concrete atomic actions"""
        return [
            f"Set up environment for: {task}",
            f"Execute core work: {task}",
            f"Validate results: {task}"
        ]
    
    def _extract_topic(self, goal: str) -> str:
        """Extract the main topic from goal"""
        # Simple heuristic: find the last noun/phrase
        words = goal.split()
        return ' '.join(words[-3:]) if len(words) >= 3 else goal
    
    def _estimate_complexity(self, goal: str) -> str:
        """Estimate goal complexity"""
        goal_lower = goal.lower()
        
        if any(kw in goal_lower for kw in ['master', 'advanced', 'expert', 'complete']):
            return 'complex'
        elif any(kw in goal_lower for kw in ['build', 'create', 'develop', 'implement']):
            return 'moderate'
        else:
            return 'simple'
    
    def _estimate_time(self, goal: str) -> int:
        """Estimate time in hours"""
        complexity = self._estimate_complexity(goal)
        
        base_time = {
            'simple': 2,
            'moderate': 8,
            'complex': 40
        }
        
        return base_time.get(complexity, 5)
    
    def _needs_further_decomposition(self, goal: str) -> bool:
        """Check if goal needs more breakdown"""
        complexity = self._estimate_complexity(goal)
        return complexity in ['moderate', 'complex']
    
    def _calculate_total_time(self, node: Dict) -> int:
        """Calculate total time for goal tree"""
        if not node.get('sub_goals'):
            return node.get('estimated_time', 0)
        
        return sum(self._calculate_total_time(sub) for sub in node['sub_goals'])
    
    def _identify_dependencies(self, tree: Dict) -> Dict:
        """
        Identify dependencies between sub-goals
        
        Sequential by default, but some can be parallelized
        """
        sub_goals = tree.get('sub_goals', [])
        
        for i, sub_goal in enumerate(sub_goals):
            if i > 0:
                # Most goals depend on previous completion
                sub_goal['dependencies'] = [sub_goals[i-1]['id']]
            
            # Recursively handle nested sub-goals
            if sub_goal.get('sub_goals'):
                sub_goal = self._identify_dependencies(sub_goal)
        
        return tree
    
    def get_next_actionable_goals(self, tree_id: str) -> List[Dict]:
        """
        Get goals that are ready to be worked on
        
        Returns only goals whose dependencies are satisfied
        """
        tree = self.goal_trees.get(tree_id)
        if not tree:
            return []
        
        actionable = []
        self._find_actionable(tree, actionable)
        
        return actionable
    
    def _find_actionable(self, node: Dict, actionable: List):
        """Recursively find actionable goals"""
        # If node has sub-goals, check them first
        if node.get('sub_goals'):
            for sub in node['sub_goals']:
                self._find_actionable(sub, actionable)
        else:
            # Leaf node - check if actionable
            if node['status'] == 'pending':
                deps = node.get('dependencies', [])
                if all(dep in self.completed_subgoals for dep in deps):
                    actionable.append(node)
    
    def mark_completed(self, goal_id: str):
        """Mark a goal as completed"""
        self.completed_subgoals.add(goal_id)
    
    def get_progress(self, tree_id: str) -> Dict[str, Any]:
        """Get progress statistics for a goal tree"""
        tree = self.goal_trees.get(tree_id)
        if not tree:
            return {}
        
        total, completed = self._count_goals(tree)
        
        return {
            'total_subgoals': total,
            'completed': completed,
            'progress': completed / total if total > 0 else 0,
            'estimated_total_time': tree['estimated_time'],
            'status': tree['status']
        }
    
    def _count_goals(self, node: Dict) -> Tuple[int, int]:
        """Count total and completed goals"""
        if not node.get('sub_goals'):
            # Leaf node
            total = 1
            completed = 1 if node['id'] in self.completed_subgoals else 0
            return total, completed
        
        total = 0
        completed = 0
        for sub in node['sub_goals']:
            sub_total, sub_completed = self._count_goals(sub)
            total += sub_total
            completed += sub_completed
        
        return total, completed
    
    def visualize_tree(self, tree_id: str, max_depth=2) -> str:
        """Generate ASCII visualization of goal tree"""
        tree = self.goal_trees.get(tree_id)
        if not tree:
            return "Tree not found"
        
        lines = []
        self._visualize_node(tree, lines, "", max_depth)
        return "\n".join(lines)
    
    def _visualize_node(self, node: Dict, lines: List[str], prefix: str, max_depth: int):
        """Recursively visualize node"""
        if node['depth'] > max_depth:
            return
        
        status_symbol = "[X]" if node['id'] in self.completed_subgoals else "[ ]"
        indent = "  " * node['depth']
        
        goal_text = node.get('goal', node.get('main_goal', 'Unknown goal'))
        lines.append(f"{indent}{status_symbol} {goal_text} ({node['estimated_time']}h)")
        
        for sub in node.get('sub_goals', []):
            self._visualize_node(sub, lines, prefix + "  ", max_depth)


if __name__ == "__main__":
    print("\n" + "="*80)
    print("  GOAL DECOMPOSITION ENGINE - TESTING")
    print("="*80)
    
    engine = GoalDecompositionEngine()
    
    # Decompose a complex goal
    print("\nDecomposing: 'Master Machine Learning and build 3 projects'")
    tree = engine.decompose_goal("Master Machine Learning and build 3 projects", max_depth=3)
    
    print(f"\nGoal Tree Created:")
    print(f"  ID: {tree['id']}")
    print(f"  Total Estimated Time: {tree['estimated_time']} hours")
    print(f"  Complexity: {tree['complexity']}")
    print(f"  Sub-goals: {len(tree['sub_goals'])}")
    
    print("\nHierarchical Breakdown:")
    viz = engine.visualize_tree(tree['id'], max_depth=2)
    print(viz)
    
    print("\nNext Actionable Goals:")
    actionable = engine.get_next_actionable_goals(tree['id'])
    for goal in actionable[:3]:
        print(f"  - {goal['goal']} ({goal['estimated_time']}h)")
    
    print("\n[GOAL DECOMPOSITION ENGINE OPERATIONAL]")

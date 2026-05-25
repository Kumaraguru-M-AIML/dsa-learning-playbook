"""
META-LEARNING SYSTEM - Evolution Phase 6

Enables the brain to:
- Learn HOW to learn better
- Optimize its own learning strategies
- Discover meta-patterns across domains
- Improve learning efficiency over time
- Self-tune hyperparameters
"""

import json
from datetime import datetime
from typing import Dict, List, Any, Tuple
from collections import defaultdict


class MetaLearningSystem:
    """
    Meta-Learning: Learning about Learning
    
    This module makes the brain learn:
    - What learning strategies work best
    - How to adapt learning rate
    - When to explore vs exploit
    - How to transfer knowledge across domains
    """
    
    def __init__(self):
        self.learning_history = []
        self.meta_strategies = {
            'exploration_rate': 0.3,  # How much to try new things
            'learning_rate': 0.1,  # How fast to update beliefs
            'confidence_threshold': 0.75,  # When to stop refining
            'challenge_difficulty': 'medium',  # Adaptive difficulty
            'reflection_depth': 3  # How many rethink cycles
        }
        self.performance_by_strategy = defaultdict(list)
        self.domain_knowledge = {}
    
    def track_learning_episode(self, episode: Dict[str, Any]):
        """
        Track a learning episode to extract meta-patterns
        
        Args:
            episode: Contains strategy used, outcome, time, effort, etc.
        """
        self.learning_history.append({
            'timestamp': datetime.now().isoformat(),
            'strategy': episode.get('strategy', 'unknown'),
            'success': episode.get('success', False),
            'time_taken': episode.get('time', 0),
            'effort': episode.get('effort', 0),
            'domain': episode.get('domain', 'general'),
            'improvement': episode.get('improvement', 0)
        })
        
        # Track performance by strategy
        strategy = episode.get('strategy', 'unknown')
        self.performance_by_strategy[strategy].append(episode.get('success', False))
    
    def optimize_learning_parameters(self) -> Dict[str, Any]:
        """
        Meta-optimization: Tune learning parameters based on performance
        
        This is the brain optimizing its own optimization!
        """
        if len(self.learning_history) < 10:
            return self.meta_strategies
        
        # Calculate recent success rate
        recent = self.learning_history[-20:]
        recent_success_rate = sum(1 for e in recent if e['success']) / len(recent)
        
        # Adaptive exploration rate
        if recent_success_rate > 0.8:
            # Doing well, can explore more
            self.meta_strategies['exploration_rate'] = min(0.5, self.meta_strategies['exploration_rate'] * 1.1)
        elif recent_success_rate < 0.5:
            # Struggling, exploit known strategies
            self.meta_strategies['exploration_rate'] = max(0.1, self.meta_strategies['exploration_rate'] * 0.9)
        
        # Adaptive learning rate
        recent_improvement = sum(e['improvement'] for e in recent) / len(recent)
        if recent_improvement > 0.2:
            # Fast improvement, can learn faster
            self.meta_strategies['learning_rate'] = min(0.3, self.meta_strategies['learning_rate'] * 1.2)
        elif recent_improvement < 0.05:
            # Slow improvement, be more careful
            self.meta_strategies['learning_rate'] = max(0.05, self.meta_strategies['learning_rate'] * 0.8)
        
        # Adaptive difficulty
        if recent_success_rate > 0.85:
            self.meta_strategies['challenge_difficulty'] = 'hard'
        elif recent_success_rate < 0.3:
            self.meta_strategies['challenge_difficulty'] = 'easy'
        else:
            self.meta_strategies['challenge_difficulty'] = 'medium'
        
        return self.meta_strategies
    
    def discover_cross_domain_patterns(self) -> List[str]:
        """
        Find patterns that work across multiple domains
        
        This is transfer learning at the meta level
        """
        patterns = []
        
        # Group by domain
        domain_performances = defaultdict(list)
        for episode in self.learning_history:
            domain = episode['domain']
            domain_performances[domain].append(episode)
        
        if len(domain_performances) < 2:
            return ["Insufficient cross-domain data"]
        
        # Find strategies that work well across domains
        universal_strategies = set()
        for domain, episodes in domain_performances.items():
            successful_strategies = {
                e['strategy'] for e in episodes 
                if e.get('success', False)
            }
            if not universal_strategies:
                universal_strategies = successful_strategies
            else:
                universal_strategies &= successful_strategies
        
        if universal_strategies:
            patterns.append(f"Universal strategies found: {', '.join(universal_strategies)}")
        
        # Find domain-specific optimal strategies
        for domain, episodes in domain_performances.items():
            if len(episodes) >= 5:
                success_rate_by_strategy = defaultdict(list)
                for ep in episodes:
                    success_rate_by_strategy[ep['strategy']].append(ep.get('success', False))
                
                best_strategy = max(
                    success_rate_by_strategy.items(),
                    key=lambda x: sum(x[1]) / len(x[1]) if x[1] else 0
                )
                if best_strategy[1]:  # Has data
                    rate = sum(best_strategy[1]) / len(best_strategy[1])
                    patterns.append(f"Best for {domain}: {best_strategy[0]} ({rate:.1%})")
        
        return patterns if patterns else ["No clear cross-domain patterns yet"]
    
    def recommend_learning_strategy(self, task: Dict[str, Any]) -> Dict[str, Any]:
        """
        Recommend optimal learning strategy based on meta-knowledge
        
        Args:
            task: Information about the task to learn
            
        Returns: Recommended strategy with confidence
        """
        domain = task.get('domain', 'general')
        difficulty = task.get('difficulty', 'medium')
        
        # Get current meta-parameters
        params = self.optimize_learning_parameters()
        
        recommendation = {
            'exploration_rate': params['exploration_rate'],
            'learning_rate': params['learning_rate'],
            'reflection_depth': params['reflection_depth'],
            'suggested_approach': 'iterative',
            'confidence': 0.7
        }
        
        # Domain-specific adjustments
        if domain in self.domain_knowledge:
            domain_data = self.domain_knowledge[domain]
            recommendation['suggested_approach'] = domain_data.get('best_approach', 'iterative')
            recommendation['confidence'] = min(0.95, 0.7 + domain_data.get('experience', 0) * 0.05)
        
        # Difficulty adjustments
        if difficulty == 'hard':
            recommendation['reflection_depth'] = min(5, recommendation['reflection_depth'] + 2)
            recommendation['learning_rate'] *= 0.7  # Be more careful
        elif difficulty == 'easy':
            recommendation['learning_rate'] *= 1.3  # Can learn faster
        
        return recommendation
    
    def update_domain_knowledge(self, domain: str, learnings: List[Dict]):
        """Update knowledge about a specific domain"""
        if domain not in self.domain_knowledge:
            self.domain_knowledge[domain] = {
                'total_episodes': 0,
                'success_rate': 0,
                'best_approach': 'unknown',
                'experience': 0
            }
        
        domain_data = self.domain_knowledge[domain]
        domain_data['total_episodes'] += len(learnings)
        domain_data['experience'] = min(10, domain_data['total_episodes'] / 10)
        
        successes = sum(1 for l in learnings if l.get('success', False))
        domain_data['success_rate'] = successes / len(learnings) if learnings else 0
    
    def get_meta_learning_report(self) -> Dict[str, Any]:
        """Generate comprehensive meta-learning report"""
        return {
            'total_episodes': len(self.learning_history),
            'current_parameters': self.meta_strategies,
            'domains_explored': len(self.domain_knowledge),
            'cross_domain_patterns': self.discover_cross_domain_patterns(),
            'strategy_performances': {
                strategy: sum(perf) / len(perf) if perf else 0
                for strategy, perf in self.performance_by_strategy.items()
            }
        }
    
    def get_statistics(self) -> Dict[str, Any]:
        """Get meta-learning statistics"""
        recent_20 = self.learning_history[-20:] if len(self.learning_history) >= 20 else self.learning_history
        recent_success = sum(1 for e in recent_20 if e.get('success', False)) / len(recent_20) if recent_20 else 0
        
        return {
            'total_learning_episodes': len(self.learning_history),
            'recent_success_rate': recent_success,
            'exploration_rate': self.meta_strategies['exploration_rate'],
            'learning_rate': self.meta_strategies['learning_rate'],
            'domains_mastered': len(self.domain_knowledge)
        }


if __name__ == "__main__":
    print("\n" + "="*80)
    print("  META-LEARNING SYSTEM - TESTING")
    print("="*80)
    
    meta_learner = MetaLearningSystem()
    
    # Simulate learning episodes
    print("\nSimulating learning episodes...")
    for i in range(15):
        episode = {
            'strategy': 'iterative' if i % 2 == 0 else 'comprehensive',
            'success': i % 3 != 0,  # 2/3 success rate
            'time': 10 + i,
            'effort': 5,
            'domain': 'programming' if i < 8 else 'math',
            'improvement': 0.1 + (i * 0.01)
        }
        meta_learner.track_learning_episode(episode)
    
    # Optimize parameters
    print("\nOptimizing learning parameters...")
    optimized = meta_learner.optimize_learning_parameters()
    print(f"  Exploration Rate: {optimized['exploration_rate']:.2f}")
    print(f"  Learning Rate: {optimized['learning_rate']:.2f}")
    print(f"  Challenge Difficulty: {optimized['challenge_difficulty']}")
    
    # Discover patterns
    print("\nCross-domain patterns:")
    patterns = meta_learner.discover_cross_domain_patterns()
    for pattern in patterns:
        print(f"  - {pattern}")
    
    # Get recommendation
    print("\nRecommendation for new task:")
    rec = meta_learner.recommend_learning_strategy({
        'domain': 'programming',
        'difficulty': 'hard'
    })
    print(f"  Suggested Approach: {rec['suggested_approach']}")
    print(f"  Confidence: {rec['confidence']:.1%}")
    
    print("\n[META-LEARNING SYSTEM OPERATIONAL]")

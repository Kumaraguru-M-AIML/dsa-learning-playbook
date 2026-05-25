
import sys
import os
from collections import Counter
import re

root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(root_dir)

try:
    from cognitive_tools.reasoning import ReasoningEngine
except ImportError:
    ReasoningEngine = None

class InsightGenerator:
    """
    Synthesizes patterns, connections, and non-obvious insights from data.
    Implements TDS Higher-Order Thinking - second and third-order effects.
    """
    
    def __init__(self):
        self.brain = ReasoningEngine() if ReasoningEngine else None
        
    def generate_insights(self, data_sources):
        """
        Cross-pollinate ideas from multiple data sources to create insights.
        
        Args:
            data_sources: List of dicts with 'source', 'data', 'domain'
            
        Returns:
            Generated insights with connections
        """
        print("\n=== INSIGHT GENERATION ===\n")
        
        insights = {
            "cross_domain_patterns": [],
            "hidden_connections": [],
            "second_order_effects": [],
            "actionable_syntheses": []
        }
        
        # Find cross-domain patterns
        patterns = self._find_cross_domain_patterns(data_sources)
        insights['cross_domain_patterns'] = patterns
        
        # Identify hidden connections
        connections = self._identify_hidden_connections(data_sources)
        insights['hidden_connections'] = connections
        
        # Analyze second-order effects
        effects = self._analyze_second_order_effects(data_sources)
        insights['second_order_effects'] = effects
        
        # Create actionable syntheses
        syntheses = self._create_actionable_syntheses(insights)
        insights['actionable_syntheses'] = syntheses
        
        return insights
    
    def _find_cross_domain_patterns(self, data_sources):
        """Find patterns that appear across different domains"""
        patterns = []
        
        # Extract common concepts
        all_concepts = []
        for source in data_sources:
            concepts = self._extract_concepts(source.get('data', ''))
            all_concepts.extend([(concept, source.get('domain')) for concept in concepts])
        
        # Find concepts appearing in multiple domains
        concept_domains = {}
        for concept, domain in all_concepts:
            if concept not in concept_domains:
                concept_domains[concept] = set()
            concept_domains[concept].add(domain)
        
        # Patterns = concepts in 2+ domains
        for concept, domains in concept_domains.items():
            if len(domains) > 1:
                patterns.append({
                    "pattern": concept,
                    "domains": list(domains),
                    "insight": f"'{concept}' principle applies across {len(domains)} domains"
                })
        
        return patterns[:5]  # Top 5 patterns
    
    def _extract_concepts(self, text):
        """Extract key concepts from text"""
        # Simple word frequency analysis
        words = re.findall(r'\b[a-z]{4,}\b', text.lower())
        common = Counter(words).most_common(10)
        return [word for word, count in common if count > 1]
    
    def _identify_hidden_connections(self, data_sources):
        """Find non-obvious relationships between data points"""
        connections = []
        
        # Compare pairs of sources
        for i in range(len(data_sources)):
            for j in range(i+1, len(data_sources)):
                source_a = data_sources[i]
                source_b = data_sources[j]
                
                # Find conceptual overlap
                concepts_a = set(self._extract_concepts(source_a.get('data', '')))
                concepts_b = set(self._extract_concepts(source_b.get('data', '')))
                
                overlap = concepts_a & concepts_b
                if overlap:
                    connections.append({
                        "source_1": source_a.get('source'),
                        "source_2": source_b.get('source'),
                        "common_concepts": list(overlap),
                        "hypothesis": f"Connection between {source_a.get('domain')} and {source_b.get('domain')} via {list(overlap)[0]}"
                    })
        
        return connections[:3]  # Top 3 connections
    
    def _analyze_second_order_effects(self, data_sources):
        """Analyze indirect consequences and compound effects"""
        effects = []
        
        # Template for second-order thinking
        for source in data_sources:
            domain = source.get('domain')
            effects.append({
                "primary": f"Action in {domain}",
                "secondary": f"Affects related systems",
                "tertiary": "Creates emergent behavior",
                "recommendation": "Monitor for cascade effects"
            })
        
        return effects[:2]  # Top 2 effect chains
    
    def _create_actionable_syntheses(self, insights):
        """Convert insights into specific actions"""
        syntheses = []
        
        # From cross-domain patterns
        for pattern in insights['cross_domain_patterns'][:2]:
            syntheses.append({
                "insight": pattern['insight'],
                "action": f"Apply '{pattern['pattern']}' principle to new domain",
                "impact": "High - leverages proven pattern"
            })
        
        # From hidden connections
        for connection in insights['hidden_connections'][:1]:
            syntheses.append({
                "insight": connection['hypothesis'],
                "action": "Test cross-domain knowledge transfer",
                "impact": "Medium - experimental"
            })
        
        return syntheses
    
    def brainstorm_from_inspiration(self, inspiration_sources):
        """
        Take inspiration from various sources and generate novel ideas.
        
        Args:
            inspiration_sources: List of things to draw inspiration from
            
        Returns:
            Novel idea combinations
        """
        print("\n=== INSPIRATION BRAINSTORM ===\n")
        
        ideas = []
        
        # Combine random pairs for novel combinations
        for i in range(len(inspiration_sources)):
            for j in range(i+1, min(i+3, len(inspiration_sources))):
                combo = {
                    "source_1": inspiration_sources[i],
                    "source_2": inspiration_sources[j],
                    "novel_idea": f"Combine {inspiration_sources[i]} methodology with {inspiration_sources[j]} principles",
                    "potential": "Creates unique hybrid approach"
                }
                ideas.append(combo)
        
        return ideas[:5]  # Top 5 novel combinations

if __name__ == "__main__":
    generator = InsightGenerator()
    
    # Example data sources
    sources = [
        {
            "source": "Machine Learning Research",
            "domain": "AI",
            "data": "gradient descent optimization learning algorithms neural networks training data performance metrics"
        },
        {
            "source": "Athletic Training Science", 
            "domain": "Sports",
            "data": "progressive overload training optimization performance recovery metrics learning muscle memory"
        },
        {
            "source": "Business Strategy",
            "domain": "Finance",
            "data": "optimization strategy performance analysis data driven decision metrics growth learning"
        }
    ]
    
    insights = generator.generate_insights(sources)
    
    print("=== CROSS-DOMAIN PATTERNS ===")
    for pattern in insights['cross_domain_patterns']:
        print(f"- {pattern['insight']}")
    
    print("\n=== ACTIONABLE SYNTHESES ===")
    for synthesis in insights['actionable_syntheses']:
        print(f"- {synthesis['action']} ({synthesis['impact']})")

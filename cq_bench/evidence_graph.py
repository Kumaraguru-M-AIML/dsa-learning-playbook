# C:\Master db\R&D workspace\NEW\evidence_graph.py
import os
import sys
import time
import json

try:
    sys.stdout.reconfigure(encoding='utf-8')
except AttributeError:
    pass

class EvidenceNode:
    """Represents an evidence-backed cognitive object within the Evidence Graph."""
    def __init__(self, belief_id, claim, confidence=1.0, provenance="latent_inference"):
        self.belief_id = belief_id
        self.claim = claim
        self.confidence = confidence
        self.provenance = provenance
        self.timestamp = time.time()
        self.evidence_sources = []
        self.supporting_constraints = []
        self.contradiction_links = []
        self.uncertainty_mass = 1.0 - confidence

class EvidenceGraphEngine:
    """
    CQ Mythos v5.0 Evidence Graph Engine.
    Converts raw beliefs into evidence-backed cognitive objects with lineage,
    contradiction linking, and dynamic confidence collapse.
    """
    def __init__(self):
        self.graph = {}
        self.provenance_weights = {
            "symbolic_proof": 1.0,
            "user_confirmed": 0.9,
            "filesystem_telemetry": 0.8,
            "scraped_web": 0.5,
            "latent_inference": 0.3
        }

    def add_belief(self, belief_id, claim, confidence, provenance):
        """Adds or updates a belief node in the Evidence Graph."""
        print(f"\n📁 [Evidence Graph] Logging Belief Node: '{belief_id}' | Claim: '{claim}'")
        node = EvidenceNode(belief_id, claim, confidence, provenance)
        self.graph[belief_id] = node
        return node

    def add_contradiction_link(self, belief_id1, belief_id2):
        """Generates a bidirectional contradiction link between mutually incompatible claims."""
        if belief_id1 in self.graph and belief_id2 in self.graph:
            print(f"  🔗 [Contradiction Linked] Mutual incompatibility asserted: '{belief_id1}' ↔ '{belief_id2}'")
            self.graph[belief_id1].contradiction_links.append(belief_id2)
            self.graph[belief_id2].contradiction_links.append(belief_id1)
            
            # Dynamic Confidence Collapse: Confidence drops automatically due to conflicting assertions
            self._collapse_confidence(belief_id1, belief_id2)

    def _collapse_confidence(self, id1, id2):
        """Calculates confidence collapse based on conflicting evidence weightings."""
        node1 = self.graph[id1]
        node2 = self.graph[id2]
        
        weight1 = self.provenance_weights.get(node1.provenance, 0.3)
        weight2 = self.provenance_weights.get(node2.provenance, 0.3)
        
        # Collapse confidence of the weaker node
        if weight1 > weight2:
            collapse_factor = weight2 / weight1
            node2.confidence = round(node2.confidence * (1.0 - collapse_factor), 4)
            node2.uncertainty_mass = round(1.0 - node2.confidence, 4)
            print(f"  ⚡ [Confidence Collapse] weaker claim '{id2}' decayed to {node2.confidence:.4f} (Uncertainty: {node2.uncertainty_mass:.4f})")
        elif weight2 > weight1:
            collapse_factor = weight1 / weight2
            node1.confidence = round(node1.confidence * (1.0 - collapse_factor), 4)
            node1.uncertainty_mass = round(1.0 - node1.confidence, 4)
            print(f"  ⚡ [Confidence Collapse] weaker claim '{id1}' decayed to {node1.confidence:.4f} (Uncertainty: {node1.uncertainty_mass:.4f})")
        else:
            # Equal weight contradiction: both collapse moderately due to complete ambiguity
            node1.confidence = round(node1.confidence * 0.5, 4)
            node2.confidence = round(node2.confidence * 0.5, 4)
            node1.uncertainty_mass = round(1.0 - node1.confidence, 4)
            node2.uncertainty_mass = round(1.0 - node2.confidence, 4)
            print("  ⚡ [Confidence Collapse] Equal weight conflict! Both claims collapsed by 50% due to perfect ambiguity.")

    def print_graph_summary(self):
        print(f"\n📊 {'='*60} 📊")
        print(" 🔍 CURRENT EVIDENCE GRAPH STATE SUMMARY")
        print(f"📊 {'='*60} 📊")
        for node_id, node in self.graph.items():
            print(f"  ├─ Node: '{node_id}' | Claim: '{node.claim}'")
            print(f"  │  ├─ Source Provenance: '{node.provenance}' (Weight: {self.provenance_weights.get(node.provenance)})")
            print(f"  │  ├─ Calibrated Confidence: {node.confidence:.4f} | Uncertainty Mass: {node.uncertainty_mass:.4f}")
            print(f"  │  └─ Contradictions Linked: {node.contradiction_links}")

if __name__ == "__main__":
    engine = EvidenceGraphEngine()
    
    # Adding competing/contradictory hardware beliefs
    engine.add_belief("claim_gpu_user", "Hardware Target: GPU = RTX 3050 6GB Laptop", 1.0, "user_confirmed")
    engine.add_belief("claim_gpu_scrape", "Hardware Target: GPU = RTX 4050", 0.9, "scraped_web")
    
    # Link contradiction to trigger confidence collapse
    engine.add_contradiction_link("claim_gpu_user", "claim_gpu_scrape")
    
    engine.print_graph_summary()

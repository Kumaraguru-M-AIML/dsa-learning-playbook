# C:\Master db\R&D workspace\NEW\memory_truth_resolver.py
import os
import sys
import math
import time
import json
from datetime import datetime

try:
    sys.stdout.reconfigure(encoding='utf-8')
except AttributeError:
    pass

class MemoryTruthResolver:
    """
    CQ Mythos v4 Temporal Epistemic Memory Engine.
    Resolves semantic retrieval ambiguities using hard chronological dominance,
    provenance scaling, contradiction clustering, and exponential age decay.
    """
    def __init__(self, decay_rate=0.01):
        self.decay_rate = decay_rate # lambda parameter for e^(-lambda * t)
        self.provenance_trust = {
            "user-stated": 1.0,
            "system-inferred": 0.8,
            "scraped": 0.6,
            "estimated": 0.4
        }

    def compute_decay(self, memory_timestamp, current_timestamp=None):
        """Applies exponential age decay: w_t = e^(-lambda * t)"""
        if current_timestamp is None:
            current_timestamp = time.time()
        try:
            m_ts = float(memory_timestamp)
            if math.isnan(m_ts) or math.isinf(m_ts):
                m_ts = current_timestamp
        except (TypeError, ValueError):
            m_ts = current_timestamp
        age = max(0.0, current_timestamp - m_ts)
        return math.exp(-self.decay_rate * (age / 3600.0)) # decay per hour

    def resolve_contradictions(self, candidate_memories):
        """
        Processes candidates, clusters contradictions, applies timestamp dominance & provenance.
        Returns the resolved, synthesized truth ledger.
        """
        print(f"\n🧠 [Memory Truth Resolver] Analyzing {len(candidate_memories)} candidates...")
        current_time = time.time()
        resolved_ledger = {}

        # Step 1: Contradiction Clustering by group
        clusters = {}
        for mem in candidate_memories:
            fact = mem.get("fact", "")
            if not fact:
                continue  # Ignore empty/corrupted facts
            group = mem.get("contradiction_group")
            if not group:
                # Isolated memory with no contradiction group
                resolved_ledger[fact] = mem
                continue
            clusters.setdefault(group, []).append(mem)

        # Step 2: Intra-Cluster Dominance Analysis
        for group, items in clusters.items():
            print(f"  ├─ Clustering Contradiction Group: '{group}' ({len(items)} nodes)")
            best_node = None
            highest_score = -1.0

            for node in items:
                # Raw parameters safely parsed
                t_val = node.get("timestamp")
                try:
                    t_val = float(t_val) if t_val is not None else current_time
                    if math.isnan(t_val) or math.isinf(t_val):
                        t_val = current_time
                except (TypeError, ValueError):
                    t_val = current_time

                prov = str(node.get("source", "estimated"))
                
                conf = node.get("confidence", 1.0)
                try:
                    conf = float(conf)
                    conf = max(0.0, min(1.0, conf)) # clip to [0.0, 1.0]
                except (TypeError, ValueError):
                    conf = 1.0
                
                # Apply trust & decay functions
                decay_weight = self.compute_decay(t_val, current_time)
                trust_scale = self.provenance_trust.get(prov, 0.4)
                
                # Final composite truth score
                composite_score = conf * trust_scale * decay_weight
                node["decay_score"] = round(decay_weight, 4)
                node["composite_truth_score"] = round(composite_score, 4)

                print(f"  │  ├─ Fact: '{node.get('fact', '')}' | Source: {prov} | Composite Score: {composite_score:.4f}")

                # Hard Chronological Dominance: Newer timestamp gets priority in same group
                node_ts = t_val
                best_ts = best_node.get("timestamp", 0) if best_node else 0
                try:
                    best_ts = float(best_ts)
                except (TypeError, ValueError):
                    best_ts = 0

                if best_node is None or node_ts > best_ts or (node_ts == best_ts and composite_score > highest_score):
                    best_node = node
                    highest_score = composite_score

            if best_node:
                print(f"  │  └─ Resolved Winner: '{best_node.get('fact', '')}' (Dominates '{group}')")
                resolved_ledger[group] = best_node

        # Step 3: Stale Fact Eviction
        final_truth = []
        for group_or_fact, node in resolved_ledger.items():
            # Evict if composite score is below threshold of 0.2 (Stale fact eviction)
            if node.get("composite_truth_score", 1.0) >= 0.2:
                final_truth.append(node)
            else:
                print(f"  ├─ Evicting Stale Memory Fact (Decayed below threshold): '{node['fact']}'")

        return final_truth

if __name__ == "__main__":
    resolver = MemoryTruthResolver(decay_rate=0.05)
    now = time.time()

    # Create adversarial conflicting memories
    test_nodes = [
        {
            "fact": "GPU is NVIDIA GeForce RTX 3050 6GB",
            "timestamp": now - 7200, # 2 hours old
            "confidence": 0.95,
            "source": "system-inferred",
            "contradiction_group": "hardware_specs"
        },
        {
            "fact": "GPU is NVIDIA GeForce RTX 4050",
            "timestamp": now, # Brand new
            "confidence": 1.0,
            "source": "user-stated", # Higher trust source
            "contradiction_group": "hardware_specs"
        },
        {
            "fact": "Active Workspace Path is NEW",
            "timestamp": now - 3600,
            "confidence": 0.9,
            "source": "system-inferred",
            "contradiction_group": "workspace_state"
        }
    ]

    resolved_truth = resolver.resolve_contradictions(test_nodes)
    print("\n🎯 Final Resolved Truth Ledger:")
    print(json.dumps(resolved_truth, indent=2))

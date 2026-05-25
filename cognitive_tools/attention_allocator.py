# C:\Master db\R&D workspace\NEW\attention_allocator.py
import os
import sys
import json

try:
    sys.stdout.reconfigure(encoding='utf-8')
except AttributeError:
    pass

class AttentionAllocator:
    """
    CQ Mythos v6.0 Attention Allocator.
    Computes dynamic attention allocation index based on entropy, uncertainty, and contradictions,
    routing deeper verification compute where stability is low, and fast-paths where stability is high.
    """
    def __init__(self, alpha=0.4, beta=0.3, gamma=0.3):
        self.alpha = alpha
        self.beta = beta
        self.gamma = gamma

    def compute_allocation(self, entropy, uncertainty, contradiction_density):
        """
        Computes dynamic allocation index: A = alpha * E + beta * U + gamma * C
        Outputs recommended routing path.
        """
        index = (self.alpha * entropy) + (self.beta * uncertainty) + (self.gamma * contradiction_density)
        
        print(f"\n🧠 [Attention Allocator] Evaluating cognitive load and routing path...")
        print(f"  ├─ Signals | Entropy: {entropy:.4f} | Uncertainty: {uncertainty:.4f} | Contradictions: {contradiction_density:.4f}")
        print(f"  ├─ Calculated Allocation Index: {index:.4f}")
        
        if index > 0.6:
            path = "DEEP_GROUNDING_VERIFICATION"
            desc = "High instability. Forcing deep symbolic constraint verification and active scraping retrieval."
        elif index > 0.3:
            path = "STANDARD_REASONING"
            desc = "Moderate stability. Executing standard neural reasoning pass."
        else:
            path = "FAST_PATH_INFERENCE"
            desc = "High stability verified. Bypassing extra verification to minimize latency."
            
        print(f"  └─ Recommended Routing: {path} ({desc})")
        return {"allocation_index": round(index, 4), "routing_path": path}

if __name__ == "__main__":
    allocator = AttentionAllocator()
    
    # Testing high stability (Fast path)
    allocator.compute_allocation(entropy=0.05, uncertainty=0.1, contradiction_density=0.0)
    
    # Testing moderate stability (Standard)
    allocator.compute_allocation(entropy=0.35, uncertainty=0.4, contradiction_density=0.0)
    
    # Testing high instability (Deep grounding)
    allocator.compute_allocation(entropy=0.85, uncertainty=0.7, contradiction_density=0.9)

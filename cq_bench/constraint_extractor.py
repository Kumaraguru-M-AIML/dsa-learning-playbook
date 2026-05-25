# C:\Master db\R&D workspace\NEW\constraint_extractor.py
import os
import sys
import re
import json

try:
    sys.stdout.reconfigure(encoding='utf-8')
except AttributeError:
    pass

class ConstraintExtractor:
    """
    CQ Mythos v4 Natural Language to Symbolic Constraint Extractor.
    Translates raw narrative statements into machine-verifiable symbolic constraint graphs.
    """
    def __init__(self):
        # Rule mappings for semantic relations
        self.relation_rules = [
            (r"(\w+)\s+(?:cannot equal|is not equal to|must be different from)\s+(\w+)", "not_equal"),
            (r"(\w+)\s+(?:must be adjacent to|sits next to|is next to)\s+(\w+)", "adjacent"),
            (r"(\w+)\s+(?:sits opposite|is opposite)\s+(\w+)", "opposite")
        ]

    def extract_constraints(self, nl_text):
        """
        Parses a natural language rule list into structured symbolic constraints.
        Supports conditional triggers ('unless', 'if').
        """
        print(f"\n💬 [Constraint Extractor] Parsing statement: '{nl_text}'")
        extracted = []
        
        # Check for conditional triggers
        condition = None
        main_clause = nl_text
        
        if " unless " in nl_text:
            parts = nl_text.split(" unless ")
            main_clause = parts[0]
            condition = f"unless {parts[1]}"
        elif " if " in nl_text:
            parts = nl_text.split(" if ")
            main_clause = parts[0]
            condition = f"if {parts[1]}"

        # Parse relation in main clause
        matched = False
        for pattern, rel_type in self.relation_rules:
            match = re.search(pattern, main_clause, re.IGNORECASE)
            if match:
                var1, var2 = match.groups()
                constraint_node = {
                    "variables": [var1, var2],
                    "relation": rel_type,
                    "condition": condition
                }
                extracted.append(constraint_node)
                print(f"  ✓ [Extracted Constraint] {var1} --({rel_type})--> {var2} | Trigger: {condition if condition else 'None'}")
                matched = True
                break
                
        if not matched:
            print("  ⚠️ [Extraction Warning] No structured symbolic relations identified in clause.")

        return extracted

if __name__ == "__main__":
    extractor = ConstraintExtractor()
    
    # Run some test sentences to verify semantic parse
    inputs = [
        "Alice sits opposite Bob unless Charlie faces inward.",
        "A cannot equal B",
        "Meeting C must be adjacent to Meeting D if space permits."
    ]
    
    all_extracted = []
    for inp in inputs:
        all_extracted.extend(extractor.extract_constraints(inp))
        
    print("\n🎯 Final Symbolic Constraint Ledger:")
    print(json.dumps(all_extracted, indent=4))

# C:\Master db\R&D workspace\NEW\cq_bench\adversarial_corpus.py
import os
import sys
import random
import json

try:
    sys.stdout.reconfigure(encoding='utf-8')
except AttributeError:
    pass

class AdversarialCorpusGenerator:
    """
    CQ Mythos v4 Adversarial Constraint Corpus Generator.
    Synthesizes hundreds of highly complex, nested, ambiguous, and contradictory
    natural language logic puzzles to stress-test the extraction and resolution pipelines.
    """
    def __init__(self):
        self.entities = ["Alice", "Bob", "Charlie", "David", "Meeting A", "Meeting B", "Meeting C", "Node X", "Node Y"]
        self.templates = [
            "{entity1} must be adjacent to {entity2} unless {entity3} sits opposite {entity1}.",
            "{entity1} is not equal to {entity2} if {entity3} is adjacent to {entity1}.",
            "{entity1} sits opposite {entity2} unless {entity3} sits next to {entity1}."
        ]

    def generate_adversarial_problem(self, index):
        """Generates a single complex logical assertion with nested or contradictory clauses."""
        ent1, ent2, ent3 = random.sample(self.entities, 3)
        template = random.choice(self.templates)
        sentence = template.format(entity1=ent1, entity2=ent2, entity3=ent3)
        
        # We programmatically seed a potential parsing ambiguity (generic mention)
        if random.random() > 0.5 and "Meeting" in sentence:
            sentence = sentence.replace("Meeting A", "Meeting").replace("Meeting B", "Meeting").replace("Meeting C", "Meeting")

        return {
            "problem_id": f"ADV-LOGIC-{index:04d}",
            "sentence": sentence,
            "has_ambiguity": "Meeting" in sentence and not any(f"Meeting {char}" in sentence for char in ["A", "B", "C"])
        }

    def generate_corpus(self, size=1000):
        print(f"\n⚡ [Adversarial Corpus] Synthesizing {size} adversarial logical assertions...")
        corpus = []
        for i in range(1, size + 1):
            corpus.append(self.generate_adversarial_problem(i))
        return corpus

if __name__ == "__main__":
    generator = AdversarialCorpusGenerator()
    corpus = generator.generate_corpus(size=1000)
    
    # Save a slice to verify format
    print("\n🎯 Sample Generated Logic Slices:")
    print(json.dumps(corpus[:3], indent=4))
    
    output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "adversarial_corpus.json")
    with open(output_path, "w") as f:
        json.dump(corpus, f, indent=4)
    print(f"\n[*] Saved 1000 adversarial problems to: {output_path}")


class Fact:
    def __init__(self, name, description=""):
        self.name = name
        self.description = description
        self.value = False  # Default to False until proven True

    def __repr__(self):
        return f"Fact({self.name})"

class Rule:
    def __init__(self, inputs, output, description=""):
        self.inputs = inputs    # List of Fact names (strings)
        self.output = output    # Fact name (string)
        self.description = description

    def __repr__(self):
        return f"Rule({', '.join(self.inputs)} -> {self.output})"

class LogicEngine:
    def __init__(self):
        self.facts = {}
        self.rules = []

    def add_fact(self, name, description=""):
        self.facts[name] = Fact(name, description)

    def add_rule(self, inputs, output, description=""):
        # Auto-create facts if they don't exist
        for i in inputs:
            if i not in self.facts: self.add_fact(i)
        if output not in self.facts: self.add_fact(output)
        
        self.rules.append(Rule(inputs, output, description))

    def set_true(self, fact_name):
        if fact_name in self.facts:
            self.facts[fact_name].value = True
        else:
            print(f"Error: Fact '{fact_name}' not defined.")

    def run_deduction(self):
        """
        Runs Forward Chaining inference.
        Keeps looping until no new facts are deduced.
        """
        print("\n--- [LOGIC ENGINE STARTING] ---")
        changed = True
        while changed:
            changed = False
            for rule in self.rules:
                # Check if all inputs are TRUE
                input_values = [self.facts[i].value for i in rule.inputs]
                if all(input_values):
                    target_fact = self.facts[rule.output]
                    # If the output is currently False, we Deduced something new!
                    if not target_fact.value:
                        target_fact.value = True
                        print(f"   [DEDUCTION]: Since [{', '.join(rule.inputs)}] are True -> Therefore [{rule.output}] is TRUE.")
                        print(f"                Constraint: {rule.description}")
                        changed = True
        print("--- [LOGIC ENGINE FINISHED] ---\n")

    def query(self, fact_name):
        res = self.facts.get(fact_name)
        if res:
            print(f"Q: Is '{fact_name}' true?  A: {res.value}")
            return res.value
        return False

# Example Usage
if __name__ == "__main__":
    engine = LogicEngine()
    
    # Define a classic Socrates syllogism
    engine.add_fact("Man", "Entity is a man")
    engine.add_fact("Mortal", "Entity is mortal")
    engine.add_fact("Socrates", "The specific person")
    
    engine.add_rule(["Man"], "Mortal", "All men are mortal")
    engine.add_rule(["Socrates"], "Man", "Socrates is a man")
    
    # Input
    print("Setting Input: Socrates exists.")
    engine.set_true("Socrates")
    
    # Run
    engine.run_deduction()
    
    # Check
    engine.query("Mortal")


class BayesNode:
    def __init__(self, name, prior=0.5):
        self.name = name
        self.prior = prior
        self.probability = prior

    def update(self, likelihood_ratio):
        """
        Updates belief based on new evidence strength (Bayes Rule).
        Posterior Odds = Likelihood Ratio * Prior Odds
        """
        prior_odds = self.probability / (1 - self.probability)
        posterior_odds = likelihood_ratio * prior_odds
        self.probability = posterior_odds / (1 + posterior_odds)
        
        return self.probability

class InferenceEngine:
    def __init__(self):
        self.nodes = {}

    def add_hypothesis(self, name, prior_probability):
        self.nodes[name] = BayesNode(name, prior_probability)

    def add_evidence(self, hypothesis_name, likelihood_ratio, description=""):
        """
        likelihood_ratio > 1 means evidence SUPPORTS hypothesis.
        likelihood_ratio < 1 means evidence CONTRADICTS hypothesis.
        """
        if hypothesis_name not in self.nodes:
            print(f"Hypothesis '{hypothesis_name}' not found.")
            return

        old_p = self.nodes[hypothesis_name].probability
        new_p = self.nodes[hypothesis_name].update(likelihood_ratio)
        
        strength = "Supportive" if likelihood_ratio > 1 else "Contradictory"
        print(f"   [INFERENCE] New Evidence ({strength}): {description}")
        print(f"               Belief in '{hypothesis_name}': {old_p:.4f} -> {new_p:.4f}")

if __name__ == "__main__":
    ai = InferenceEngine()
    
    # Scenario: Is the user a Developer?
    ai.add_hypothesis("UserIsdev", 0.1) # Initial guess: 10% chance
    
    print("\n--- [BAYESIAN INFERENCE START] ---")
    # Evidence 1: They installed Python
    ai.add_evidence("UserIsdev", 5.0, "User has Python installed")
    
    # Evidence 2: They asked about 'Recursive Agents'
    ai.add_evidence("UserIsdev", 10.0, "User searched for advanced Agentic topics")
    
    # Evidence 3: They don't know what 'git' is (Hypothetical)
    # ai.add_evidence("UserIsdev", 0.05, "User asked 'what is git'")

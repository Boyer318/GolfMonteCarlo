#My PCC Monte Carlo Simulation
import pandas as pd
import numpy as np

# Load dataset
df = pd.read_excel("C:\Users\boyer\OneDrive\Desktop\PythonPrograms\MyPCC.xlsx")

# Define number of simulations
num_rounds = 1000

# Function to simulate a round
def simulate_round(df):
    total_score = 0
    for _, row in df.iterrows():
        par = row["Par"]
        
        # Define possible outcomes and probabilities
        outcomes = [par - 1, par, par + 1, par + 2, par - 2]  # Birdie, Par, Bogey, Double, Eagle
        probabilities = [row["Birdie%"], row["Par%"], row["Bogey%"], row["Dub%"], row["Eagle%"]]
        
        # Normalize probabilities
        probabilities = np.array(probabilities) / np.sum(probabilities)
        
        # Choose a score based on probabilities
        score = np.random.choice(outcomes, p=probabilities)
        total_score += score

    return total_score

# Run multiple simulations
scores = [simulate_round(df) for _ in range(num_rounds)]

# Calculate expected score
expected_score = np.mean(scores)

print(f"Expected Score After {num_rounds} Simulations: {expected_score:.2f}")
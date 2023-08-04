import random
import pandas as pd
import matplotlib.pyplot as plt
import os

# This function simulates a "dry streak" under the old drop rate method.
def simulate_dry_streak(drop_rate, num_trials, num_simulations):
    num_dry = 0
    for _ in range(num_simulations):
        # For each simulation, make a number of trials.
        # If all trials are dry (random number > 1 / drop rate), increment the counter.
        if all(random.random() > 1 / drop_rate for _ in range(num_trials)):
            num_dry += 1
    return num_dry / num_simulations


# This function simulates a "dry streak" under the new drop rate method, with an increment counter.
def simulate_incremental_dry_streak(drop_rate, num_trials, num_simulations, increment):
    num_dry = 0
    for _ in range(num_simulations):
        counter = 0
        for _ in range(num_trials):
            # For each simulation, make a number of trials.
            # If a trial is successful (random number < 1 / drop rate), increment the counter.
            if random.random() < 1 / drop_rate:
                counter += 1
        if counter < increment:
            num_dry += 1
    return num_dry / num_simulations


# Parameters:
drop_rate = 1087.98
new_drop_rate = 362.66
num_simulations = 10000
increment = 3
set_num_rolls = 10000

results = []  # Initialize a list to store the results.

# Run the simulations for different numbers of trials:
for num_trials in range(1, set_num_rolls, 100):
    print(f"Running simulation for trial {num_trials}")  # Log the current trial.

    # Simulate the old and new methods:
    old_prob = simulate_dry_streak(drop_rate, num_trials, num_simulations)
    new_prob = simulate_incremental_dry_streak(
        new_drop_rate, num_trials, num_simulations, increment
    )

    # Append the results to the list:
    results.append(
        {"num_trials": num_trials, "old_prob": old_prob, "new_prob": new_prob}
    )

# Convert the results to a DataFrame:
df = pd.DataFrame(results)

# Check if the results directory exists, if not, create it:
if not os.path.isdir('results'):
    os.makedirs('results')

# Write the DataFrame to a CSV file in the /results directory:
df.to_csv(f"results/simulation_results_{set_num_rolls}_rolls.csv", index=False)

# Plot the results:
plt.figure(figsize=(10, 6))
plt.plot(df["num_trials"], df["old_prob"], label="Old Method")
plt.plot(df["num_trials"], df["new_prob"], label="New Method")
plt.xlabel("Number of Trials")
plt.ylabel("Probability of Going Dry")
plt.title("Comparing Old and New Drop Rates")
plt.legend()
plt.show()

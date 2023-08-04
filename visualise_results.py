import pandas as pd
import matplotlib.pyplot as plt
import os

# Define the name of the CSV file:
df_name = "simulation_results_3000_rolls.csv"

# Check if the results directory exists:
if not os.path.isdir('results'):
    raise FileNotFoundError("The 'results' directory does not exist. Please make sure you've run the simulation and the results CSV file has been created.")

# Load the results from the CSV file in the /results directory:
df = pd.read_csv(f"results/{df_name}")

# Check if the plots directory exists, if not, create it:
if not os.path.isdir('plots'):
    os.makedirs('plots')

# Plot the results:
plt.figure(figsize=(10, 6))
# Multiply probabilities by 100 to convert to percentage
plt.plot(df["num_trials"], df["old_prob"] * 100, label="Old Method")
plt.plot(df["num_trials"], df["new_prob"] * 100, label="New Method") 
plt.xlabel("Number of Trials (Kills or Rolls)")
plt.ylabel("Percentage of Players Going Dry")
plt.title("Comparing Old and New Drop Rates")
plt.legend()
plt.grid(True)  # Optional: add grid for easier readability

# Save the plot with the same name as the CSV file but with .png extension, in the /plots directory:
plt.savefig(f"plots/{os.path.splitext(df_name)[0]}.png")

# Show the plot:
plt.show()

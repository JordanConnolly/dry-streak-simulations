import pandas as pd
import matplotlib.pyplot as plt
import os

# Load the results from the CSV file:
df_name = "simulation_results_3000_rolls.csv"
df = pd.read_csv(df_name)

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

# Save the plot with the same name as the CSV file but with .png extension
plt.savefig(os.path.splitext(df_name)[0] + ".png")
# Show the plot:
plt.show()

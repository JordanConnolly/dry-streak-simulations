import random

def simulate_dry_streak(drop_rate, num_trials, num_simulations):
    num_dry = 0
    for _ in range(num_simulations):
        if all(random.random() > 1 / drop_rate for _ in range(num_trials)):
            num_dry += 1
    return num_dry / num_simulations

def simulate_incremental_dry_streak(drop_rate, num_trials, num_simulations, increment):
    num_dry = 0
    for _ in range(num_simulations):
        counter = 0
        for _ in range(num_trials):
            if random.random() < 1 / drop_rate:
                counter += 1
        if counter < increment:
            num_dry += 1
    return num_dry / num_simulations

# Usage:
drop_rate = 1087.98
num_trials = 100  # Adjust as needed
num_simulations = 10000  # Adjust as needed

prob = simulate_dry_streak(drop_rate, num_trials, num_simulations)
print(f"The probability of going dry in {num_trials} trials is approximately {prob}")

# Usage:
new_drop_rate = 362.66
increment = 3

prob = simulate_incremental_dry_streak(
    new_drop_rate, num_trials, num_simulations, increment
)
print(f"The new probability of going dry in {num_trials} trials is approximately {prob}")

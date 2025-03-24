import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Data based on the observations
configurations = [
    "n=1, p=1 (Load)", "n=1, p=1 (No)", "n=auto, p=1 (Load)", "n=auto, p=1 (No)",
    "n=1, p=auto (Load)", "n=1, p=auto (No)", "n=auto, p=auto (Load)", "n=auto, p=auto (No)"
]

execution_times = [4.61, 4.73, 4.68, 5.02, 33.22, 33.66, 27.81, 30.61]
failures = [0, 0, 0, 0, 3.33, 3.33, 4, 3.33]

# Create DataFrame
df = pd.DataFrame({"Configuration": configurations, "Execution Time (s)": execution_times, "Failures": failures})

# Execution Time Plot
plt.figure(figsize=(10, 5))
sns.barplot(x="Configuration", y="Execution Time (s)", data=df, palette="Blues")
plt.xticks(rotation=45, ha="right")
plt.title("Execution Time Across Configurations")
plt.xlabel("Configuration")
plt.ylabel("Execution Time (s)")
plt.tight_layout()
plt.show()

# Failure Rate Plot
plt.figure(figsize=(10, 5))
sns.barplot(x="Configuration", y="Failures", data=df, palette="Reds")
plt.xticks(rotation=45, ha="right")
plt.title("Failure Rate Across Configurations")
plt.xlabel("Configuration")
plt.ylabel("Number of Failures")
plt.tight_layout()
plt.show()

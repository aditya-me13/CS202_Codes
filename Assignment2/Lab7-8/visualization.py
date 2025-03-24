import json
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load data from commits.json
with open("commits_Nettacker.json", "r") as f:
    commits_data = json.load(f)

# Load data from cwe.json
with open("cwe_Nettacker.json", "r") as f:
    overall_cwe_data = json.load(f)

# Extract commit numbers and sort them
sorted_commits = sorted(commits_data.items(), key=lambda x: int(x[0].split("_")[1]))

# Extract numerical commit indices (X-axis from 1 to 100)
commit_numbers = list(range(1, 101))

# Function to pad a list to length 100
def pad_list(data_list, length=100):
    if len(data_list) < length:
        data_list.extend([data_list[-1]] * (length - len(data_list)))  # Pad with the last value
    return data_list[:length]  # Ensure no overflow

# Extract severity levels
low_severity = pad_list([commit[1]["severity"]["LOW"] for commit in sorted_commits])
medium_severity = pad_list([commit[1]["severity"]["MEDIUM"] for commit in sorted_commits])
high_severity = pad_list([commit[1]["severity"]["HIGH"] for commit in sorted_commits])

# Extract confidence levels
low_confidence = pad_list([commit[1]["confidence"]["LOW"] for commit in sorted_commits])
medium_confidence = pad_list([commit[1]["confidence"]["MEDIUM"] for commit in sorted_commits])
high_confidence = pad_list([commit[1]["confidence"]["HIGH"] for commit in sorted_commits])

# Sort CWE data by frequency in descending order
sorted_cwe = sorted(overall_cwe_data.items(), key=lambda x: x[1], reverse=True)
cwe_keys, cwe_values = zip(*sorted_cwe)

# Set Seaborn style
sns.set_style("whitegrid")

# -------------------- PLOT 1: HIGH SEVERITY ACROSS COMMITS --------------------
plt.figure(figsize=(12, 6))
sns.lineplot(x=commit_numbers, y=high_severity, label="HIGH Severity", color="red")
plt.xlabel("Commit Number", fontsize=12)
plt.ylabel("High Severity Count", fontsize=12)
plt.title("High Severity Across Commits", fontsize=14)
plt.legend()
plt.show()

# -------------------- PLOT 2: SEVERITY LEVELS ACROSS COMMITS --------------------
plt.figure(figsize=(12, 6))
sns.lineplot(x=commit_numbers, y=low_severity, label="LOW", color="blue")
sns.lineplot(x=commit_numbers, y=medium_severity, label="MEDIUM", color="orange")
sns.lineplot(x=commit_numbers, y=high_severity, label="HIGH", color="red")
plt.xlabel("Commit Number", fontsize=12)
plt.ylabel("Severity Count", fontsize=12)
plt.title("Severity Levels Across Commits", fontsize=14)
plt.legend(title="Severity Level")
plt.show()

# -------------------- PLOT 3: CONFIDENCE LEVELS ACROSS COMMITS --------------------
plt.figure(figsize=(12, 6))
sns.lineplot(x=commit_numbers, y=low_confidence, label="LOW Confidence", color="blue")
sns.lineplot(x=commit_numbers, y=medium_confidence, label="MEDIUM Confidence", color="orange")
sns.lineplot(x=commit_numbers, y=high_confidence, label="HIGH Confidence", color="red")
plt.xlabel("Commit Number", fontsize=12)
plt.ylabel("Confidence Count", fontsize=12)
plt.title("Confidence Levels Across Commits", fontsize=14)
plt.legend()
plt.show()

# -------------------- PLOT 4: CWE FREQUENCY (SORTED) --------------------
plt.figure(figsize=(12, 6))
ax = sns.barplot(x=np.arange(len(cwe_keys)), y=cwe_values, palette="Blues_r")
plt.xticks(ticks=np.arange(len(cwe_keys)), labels=cwe_keys, rotation=45, ha="right")
plt.xlabel("CWE Numbers", fontsize=12)
plt.ylabel("Count", fontsize=12)
plt.title("Sorted CWE Frequency for Repository", fontsize=14)
plt.show()

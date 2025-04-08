import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Input and Output Paths
fan_data_csv = r"fan_data.csv"
output_directory = r"charts_output"

# Ensure the output directory exists
os.makedirs(output_directory, exist_ok=True)

# Load the CSV data containing fan-in and fan-out metrics
print("Loading dependency metrics from CSV...")
data = pd.read_csv(fan_data_csv)

# Compute a combined metric (fan-in + fan-out)
data['Total'] = data['Fan-In'] + data['Fan-Out']

# Display basic statistics
print("\nSummary Statistics:")
print(f"Total modules analyzed: {len(data)}")
print(f"Average Fan-In: {data['Fan-In'].mean():.2f}")
print(f"Average Fan-Out: {data['Fan-Out'].mean():.2f}")
print(f"Highest Fan-In: {data['Fan-In'].max()} (Module: {data.loc[data['Fan-In'].idxmax()]['Module']})")
print(f"Highest Fan-Out: {data['Fan-Out'].max()} (Module: {data.loc[data['Fan-Out'].idxmax()]['Module']})")

# Configure plot aesthetics with a new style
sns.set_theme(style="darkgrid", palette="muted")
plt.rcParams.update({'font.size': 10})

# 1. Top modules by Fan-In
top_n = 15  # Number of top modules to visualize
top_fan_in = data.sort_values('Fan-In', ascending=False).head(top_n)
plt.figure(figsize=(10, 6))
sns.barplot(x='Fan-In', y='Module', data=top_fan_in, palette='viridis', hue='Module', legend=False)
plt.title(f'Top {top_n} Modules by Fan-In (Consumers of Dependencies)', fontsize=14)
plt.xlabel('Fan-In Count', fontsize=12)
plt.ylabel('Modules', fontsize=12)
plt.tight_layout()
plt.savefig(os.path.join(output_directory, 'top_fan_in.png'), dpi=300)

# 2. Top modules by Fan-Out
top_fan_out = data.sort_values('Fan-Out', ascending=False).head(top_n)
plt.figure(figsize=(10, 6))
sns.barplot(x='Fan-Out', y='Module', data=top_fan_out, palette='viridis', hue='Module', legend=False)
plt.title(f'Top {top_n} Modules by Fan-Out (Providers of Dependencies)', fontsize=14)
plt.xlabel('Fan-Out Count', fontsize=12)
plt.ylabel('Modules', fontsize=12)
plt.tight_layout()
plt.savefig(os.path.join(output_directory, 'top_fan_out.png'), dpi=300)

# 3. Top modules by combined Fan-In + Fan-Out
top_combined = data.sort_values('Total', ascending=False).head(top_n)
plt.figure(figsize=(10, 6))
sns.barplot(x='Total', y='Module', data=top_combined, palette='viridis', hue='Module', legend=False)
plt.title(f'Top {top_n} Modules by Combined Dependencies', fontsize=14)
plt.xlabel('Combined Count (Fan-In + Fan-Out)', fontsize=12)
plt.ylabel('Modules', fontsize=12)
plt.tight_layout()
plt.savefig(os.path.join(output_directory, 'top_combined.png'), dpi=300)


# 4. Scatter plot for Fan-In vs Fan-Out analysis
plt.figure(figsize=(8, 8))
scatter = plt.scatter(
    data['Fan-Out'], 
    data['Fan-In'],
    c=data['Total'],
    cmap='plasma',
    alpha=0.75,
    s=80
)

# Annotate top modules on the scatter plot
highlighted_modules = data.sort_values('Total', ascending=False).head(10)
for _, row in highlighted_modules.iterrows():
    plt.annotate(
        row['Module'], 
        xy=(row['Fan-Out'], row['Fan-In']),
        xytext=(5, 5),
        textcoords='offset points',
        fontsize=9,
        bbox=dict(boxstyle="round,pad=0.3", fc="white", alpha=0.6)
    )

plt.colorbar(scatter, label='Combined Dependencies')
plt.title('Scatter Plot: Fan-In vs Fan-Out Analysis', fontsize=14)
plt.xlabel('Fan-Out (Number of Dependencies)', fontsize=12)
plt.ylabel('Fan-In (Number of Dependent Modules)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.axhline(y=data['Fan-In'].mean(), color='red', linestyle='--', alpha=0.5, label="Average Fan-In")
plt.axvline(x=data['Fan-Out'].mean(), color='blue', linestyle='--', alpha=0.5, label="Average Fan-Out")
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(output_directory, 'fan_in_vs_fan_out.png'), dpi=300)

# 5. Distribution of Fan-In and Fan-Out metrics
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

sns.histplot(data['Fan-In'], kde=True, color='steelblue', ax=axes[0])
axes[0].set_title('Distribution of Fan-In Values', fontsize=14)
axes[0].set_xlabel('Fan-In Count', fontsize=12)
axes[0].set_ylabel('Frequency', fontsize=12)

sns.histplot(data['Fan-Out'], kde=True, color='coral', ax=axes[1])
axes[1].set_title('Distribution of Fan-Out Values', fontsize=14)
axes[1].set_xlabel('Fan-Out Count', fontsize=12)
axes[1].set_ylabel('Frequency', fontsize=12)

fig.tight_layout()
fig.savefig(os.path.join(output_directory, 'distribution.png'), dpi=300)

print(f"\nAll visualizations saved to: {output_directory}")
print("Visualization process completed successfully.")

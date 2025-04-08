import json
import csv
import os
import networkx as nx

# Define file paths
base_directory = r""
json_file_path = os.path.join(base_directory, "dependencies.json")
output_directory = os.path.join(base_directory, "results")
fan_data_file = os.path.join(base_directory, "fan_data.csv")

# Ensure the output directory exists
os.makedirs(output_directory, exist_ok=True)

print("Reading dependency data from JSON...")
# Load the dependency data from the JSON file (UTF-8 encoding)
with open(json_file_path, "r", encoding="utf-8") as file:
    dependency_data = json.load(file)

print("Constructing dependency graph...")
# Create a directed graph to model dependencies
dependency_graph = nx.DiGraph()

# Dictionaries to track fan-in and fan-out metrics
fan_in_counts = {}
fan_out_counts = {}

# Populate the graph and calculate fan-in/fan-out values
for module_name, module_info in dependency_data.items():
    if isinstance(module_info, dict):
        imported_modules = module_info.get("imports", [])
        dependent_modules = module_info.get("imported_by", [])

        fan_out_counts[module_name] = len(imported_modules)
        fan_in_counts[module_name] = len(dependent_modules)

        # Add edges to the graph for each dependency
        for imported_module in imported_modules:
            dependency_graph.add_edge(module_name, imported_module)

print("Exporting fan-in and fan-out metrics to CSV...")
# Write fan-in and fan-out data to a CSV file
with open(fan_data_file, "w", newline="") as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["Module", "Fan-In", "Fan-Out"])
    for module_name in sorted(dependency_data.keys()):
        csv_writer.writerow([
            module_name,
            fan_in_counts.get(module_name, 0),
            fan_out_counts.get(module_name, 0)
        ])

# Display a summary of the fan-in and fan-out data
print("\nFan-In/Fan-Out Overview:")
print("-" * 80)
print(f"{'Module':<40} {'Fan-In':<10} {'Fan-Out':<10}")
print("-" * 80)

# Identify the top 10 modules based on combined fan-in and fan-out values
top_modules = sorted(
    dependency_data.keys(),
    key=lambda mod: (fan_in_counts.get(mod, 0) + fan_out_counts.get(mod, 0)),
    reverse=True
)[:10]

for module in top_modules:
    print(f"{module:<40} {fan_in_counts.get(module, 0):<10} {fan_out_counts.get(module, 0):<10}")

# Detect modules with high coupling based on a threshold
threshold_value = 5
high_coupling_modules = [
    (module, fan_in_counts.get(module, 0), fan_out_counts.get(module, 0))
    for module in dependency_data.keys()
    if fan_in_counts.get(module, 0) + fan_out_counts.get(module, 0) > threshold_value
]

# Save highly coupled modules to a separate CSV file
high_coupling_file_path = os.path.join(output_directory, "highly_coupled_modules.csv")
with open(high_coupling_file_path, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Module", "Fan-In", "Fan-Out"])
    for module_name, fi_count, fo_count in high_coupling_modules:
        writer.writerow([module_name, fi_count, fo_count])

print(f"\nIdentified {len(high_coupling_modules)} highly coupled modules (threshold: {threshold_value})")
print(f"Fan-in/Fan-out data saved to: {fan_data_file}")
print(f"Highly coupled modules saved to: {high_coupling_file_path}")
print("Dependency analysis completed successfully.")

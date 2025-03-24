import subprocess
import json
import time

# Define configurations
configurations = [
    {"id": 1, "dist": "load", "workers": "1", "threads": "1"},
    {"id": 2, "dist": "load", "workers": "auto", "threads": "1"},
    {"id": 3, "dist": "load", "workers": "1", "threads": "auto"},
    {"id": 4, "dist": "load", "workers": "auto", "threads": "auto"},
    {"id": 5, "dist": "no", "workers": "1", "threads": "1"},
    {"id": 6, "dist": "no", "workers": "auto", "threads": "1"},
    {"id": 7, "dist": "no", "workers": "1", "threads": "auto"},
    {"id": 8, "dist": "no", "workers": "auto", "threads": "auto"},
]

results = {}

for config in configurations:
    config_id = config["id"]
    results[config_id] = {"run_times": [], "failing_tests": []}

    for run in range(1, 4):  # Run each configuration 3 times
        log_filename = f"config_{config_id}_run_{run}.log"

        # Construct pytest command correctly
        command = [
            "pytest",
            f"-n={config['workers']}",
            f"--dist={config['dist']}",
            f"--parallel-threads={config['threads']}"
        ]

        start_time = time.time()
        with open(log_filename, "w") as log_file:
            try:
                process = subprocess.run(command, stdout=log_file, stderr=subprocess.STDOUT, text=True, check=True)
            except subprocess.CalledProcessError as e:
                print(f"Error running {command}: {e}")
        end_time = time.time()

        execution_time = end_time - start_time
        results[config_id]["run_times"].append(execution_time)

        # Extract failing test cases from the log file
        with open(log_filename, "r") as log_file:
            log_content = log_file.readlines()
            for line in log_content:
                if "FAILED" in line and "::" in line:  # Typical pytest failure format
                    test_case = line.split()[0]
                    results[config_id]["failing_tests"].append(test_case)

    results[config_id]["average_time"] = sum(results[config_id]["run_times"]) / 3

# Save summary as JSON
with open("test_summary.json", "w") as json_file:
    json.dump(results, json_file, indent=4)

print("Test execution completed. Logs saved as .log files, and summary stored in test_summary.json.")

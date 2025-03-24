import json
import os
from collections import Counter

# Get the script's directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# Define the main results directory
results_dir = os.path.join(script_dir, "results")

# Ensure the results directory exists
if not os.path.exists(results_dir):
    print(f"Error: Results directory '{results_dir}' not found.")
    exit(1)

# Process each subdirectory inside the results folder
for project_name in sorted(os.listdir(results_dir)):
    project_path = os.path.join(results_dir, project_name)
    
    # Skip if it's not a directory
    if not os.path.isdir(project_path):
        continue
    
    # Initialize tracking structures
    severity_totals = {"HIGH": 0, "MEDIUM": 0, "LOW": 0}
    confidence_totals = {"HIGH": 0, "MEDIUM": 0, "LOW": 0}
    global_cwe_counter = Counter()
    commit_timeline = {}
    
    # Track unique CWE issues across all commits
    seen_global_issues = set()
    
    # Process each JSON report in the project folder
    for report_file in sorted(os.listdir(project_path)):
        if not report_file.endswith(".json"):
            continue
        
        commit_id = report_file.replace("bandit_report_", "").replace(".json", "")
        report_path = os.path.join(project_path, report_file)
        
        with open(report_path, "r") as f:
            report_data = json.load(f)
        
        # Initialize per-commit counters
        severity_counts = {"HIGH": 0, "MEDIUM": 0, "LOW": 0}
        confidence_counts = {"HIGH": 0, "MEDIUM": 0, "LOW": 0}
        commit_cwe_counter = Counter()
        seen_commit_issues = set()
        
        # Process issues in the report
        for issue in report_data.get("results", []):
            severity = issue["issue_severity"]
            confidence = issue["issue_confidence"]
            cwe = issue.get("issue_cwe", "Unknown CWE")
            
            # Handle CWE dictionary structure
            if isinstance(cwe, dict):
                cwe = cwe.get("id", "Unknown CWE")
            
            issue_key = (issue["filename"], issue["line_number"], cwe)
            
            # Track unique CWE issues per commit
            if issue_key not in seen_commit_issues:
                seen_commit_issues.add(issue_key)
                commit_cwe_counter[cwe] += 1
            
            # Track unique CWE issues globally
            if issue_key not in seen_global_issues:
                seen_global_issues.add(issue_key)
                global_cwe_counter[cwe] += 1
            
            # Update severity and confidence counters
            severity_counts[severity] += 1
            confidence_counts[confidence] += 1
        
        # Store per-commit data
        commit_timeline[commit_id] = {
            "severity": severity_counts,
            "confidence": confidence_counts,
            "cwe_counts": dict(commit_cwe_counter),
        }
    
    # Define output file paths
    commit_output_path = os.path.join(project_path, f"commits_{project_name}.json")
    cwe_output_path = os.path.join(project_path, f"cwe_{project_name}.json")
    
    # Save per-commit data
    with open(commit_output_path, "w") as f:
        json.dump(commit_timeline, f, indent=4)
    
    # Save global CWE counts
    with open(cwe_output_path, "w") as f:
        json.dump(dict(global_cwe_counter), f, indent=4)
    
    print(f"Processed '{project_name}' - Results saved in {commit_output_path} and {cwe_output_path}")

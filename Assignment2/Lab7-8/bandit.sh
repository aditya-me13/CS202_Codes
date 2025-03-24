#!/bin/bash

# CSV file containing repository names and URLs
CSV_FILE="repos.csv"

# Directory to store results
RESULTS_DIR="results"
mkdir -p "$RESULTS_DIR"

# Read CSV file (skip header)
tail -n +2 "$CSV_FILE" | while IFS=, read -r repo_name repo_url; do
    echo "Processing repository: $repo_name"

    # Clone repository
    git clone "$repo_url" "$repo_name"
    cd "$repo_name" || exit

    # Set up virtual environment
    python3 -m venv venv
    source venv/bin/activate

    # Install dependencies (if requirements.txt exists)
    if [ -f "requirements.txt" ]; then
        pip install -r requirements.txt
    fi

    # Create a directory for results
    REPO_RESULTS_DIR="../$RESULTS_DIR/$repo_name"
    mkdir -p "$REPO_RESULTS_DIR"

    # Get last 500 non-merge commits
    git log --pretty=format:"%H" --no-merges -n 100 > commit_list.txt

    # Initialize commit number
    commit_num=1

    # Run Bandit on each commit
    while read -r commit_hash; do
        echo "Running Bandit on commit #$commit_num"
        git checkout "$commit_hash"
        bandit -r . --format json --output "$REPO_RESULTS_DIR/bandit_report_commit_$commit_num.json"
        
        # Increment commit number
        commit_num=$((commit_num + 1))
    done < commit_list.txt

    # Return to parent directory
    cd ..

    echo "Finished processing $repo_name"
done

echo "All repositories processed!"

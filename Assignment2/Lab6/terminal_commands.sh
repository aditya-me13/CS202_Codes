python3.10 -m venv cs202-lab6-env
source cs202-lab6-env/bin/activate

git clone https://github.com/keon/algorithms.git
cd algorithms
pip install -e .
pip install pytest pytest-xdist pytest-run-parallel


for ((i=1; i<=10; i++)); do pytest | tee "sequential_run_$i.log"; done

for ((i=1; i<=3; i++)); do pytest | tee "sequential_run_final_$i.log"; done

pytest -n <num_workers> --dist <distribution_mode> --parallel-threads <num_threads>

pytest -n auto --dist load --parallel-threads 1

pytest -n 1 --dist no --parallel-threads auto
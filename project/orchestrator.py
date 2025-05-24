import subprocess
import sys
import os
from project.constants.orchestrator_constants import *

def run_python_benchmark():
    print(PRINT_RUNNING_PY)
    result = subprocess.run([sys.executable, PYTHON_BENCHMARK], capture_output=True, text=True)
    print(result.stdout)
    if result.returncode != 0:
        print(result.stderr)
        raise RuntimeError(ERR_PYTHON_FAIL)
    print(PRINT_PY_SAVED.format(csv=PYTHON_RESULTS))

def build_and_run_c_benchmark():
    print(PRINT_COMPILING_C)
    compile_result = subprocess.run(['gcc', '-O2', '-o', C_OUTPUT, C_BENCHMARK, '-lm'], capture_output=True, text=True)
    if compile_result.returncode != 0:
        print(compile_result.stderr)
        raise RuntimeError(ERR_C_COMP_FAIL)
    print(PRINT_RUNNING_C)
    run_result = subprocess.run([f'./{C_OUTPUT}'], capture_output=True, text=True)
    print(run_result.stdout)
    if run_result.returncode != 0:
        print(run_result.stderr)
        raise RuntimeError(ERR_C_FAIL)
    print(PRINT_C_SAVED.format(csv=C_RESULTS))

def run_comparison():
    print(PRINT_RUNNING_COMP)
    result = subprocess.run([sys.executable, COMPARISON_SCRIPT], capture_output=True, text=True)
    print(result.stdout)
    if result.returncode != 0:
        print(result.stderr)
        raise RuntimeError(ERR_COMP_FAIL)
    print(PRINT_COMP_GEN)

def clean_outputs():
    print(PRINT_CLEANING)
    # Remove CSVs
    for f in [PYTHON_RESULTS, C_RESULTS, SUMMARY_CSV]:
        if os.path.exists(f):
            os.remove(f)
    # Remove images
    if os.path.exists(IMG_DIR):
        for img in os.listdir(IMG_DIR):
            if img.endswith('.png'):
                os.remove(os.path.join(IMG_DIR, img))
    print(PRINT_CLEANED)

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Orchestrate Merge Sort Benchmarks and Comparison")
    parser.add_argument('--clean', action='store_true', help='Delete existing CSV and image files before running')
    args = parser.parse_args()
    print(PRINT_ORCH_HEADER)
    print(PRINT_INPUT_SIZES.format(file=INPUT_SIZES_FILE))
    print(PRINT_REPETITIONS.format(n=REPETITIONS))
    if args.clean:
        clean_outputs()
    run_python_benchmark()
    build_and_run_c_benchmark()
    run_comparison()
    print(PRINT_ALL_DONE)

if __name__ == "__main__":
    main()

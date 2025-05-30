# Constants for the orchestrator script

PYTHON_BENCHMARK_SCRIPT = ['python3', '-m', 'project.mergesort']
C_BENCHMARK = 'project/mergesort.c'
C_OUTPUT = 'output/mergesort'
COMPARISON_SCRIPT = ['python3', '-m','project.mergesort_comparison']
PYTHON_RESULTS = 'project/data/datasheet_python.csv'
C_RESULTS = 'project/data/datasheet_clang.csv'
SUMMARY_CSV = 'project/data/mergesort_comparison_summary.csv'
IMG_DIR = 'project/img/'
INPUT_SIZES_FILE = 'project/input_sizes.txt'
REPETITIONS = 20

# String constants for orchestrator.py
PRINT_ORCH_HEADER = '=== Merge Sort Benchmark Orchestrator ==='
PRINT_INPUT_SIZES = 'Input sizes from: {file}'
PRINT_REPETITIONS = 'Repetitions: {n}'
PRINT_RUNNING_PY = 'Running Python benchmark...'
PRINT_PY_SAVED = 'Python results saved to {csv}'
PRINT_COMPILING_C = 'Compiling C benchmark...'
PRINT_RUNNING_C = 'Running C benchmark...'
PRINT_C_SAVED = 'C results saved to {csv}'
PRINT_RUNNING_COMP = 'Running Python comparison/plotting script...'
PRINT_COMP_GEN = 'Comparison and graphics generated.'
PRINT_ALL_DONE = '\nAll steps completed. Check the CSV files and graphics for results.'
PRINT_CLEANING = 'Cleaning output files and directories...'
PRINT_CLEANED = 'All output files cleaned.'
ERR_PYTHON_FAIL = 'Python benchmark failed!'
ERR_C_COMP_FAIL = 'C compilation failed!'
ERR_C_FAIL = 'C benchmark failed!'
ERR_COMP_FAIL = 'Comparison/plotting script failed!'

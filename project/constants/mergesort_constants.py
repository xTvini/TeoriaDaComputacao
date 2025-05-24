# Python constants for merge sort benchmarking

# Number of repetitions for each input size
REPETITIONS = 20

# Path to input sizes file
INPUT_SIZES_FILE = 'project/input_sizes.txt'

# Path to output CSV for Python results
PYTHON_CSV = 'project/data/datasheet_python.csv'

# Path to output CSV for C results
C_CSV = 'project/data/datasheet_clang.csv'

# Path to summary CSV
SUMMARY_CSV = 'project/data/mergesort_comparison_summary.csv'

# Path to output images
IMG_DIR = 'project/img/'
TIME_COMPARISON_IMG = IMG_DIR + 'mergesort_time_comparison.png'
TIME_VS_THEORY_IMG = IMG_DIR + 'mergesort_time_vs_theory.png'
EXECSPEED_IMG = IMG_DIR + 'mergesort_execspeed_comparison.png'


# String constants for mergesort.py

class CsvFields:
    INPUT_SIZE = 'InputSize'
    EXECUTION_TIME = 'ExecutionTime_ms'
    EXECUTION_TIME_STDDEV = 'ExecutionTime_ms_stddev'
    RECURSION_COUNT = 'RecursionCount'
    RECURSION_COUNT_STDDEV = 'RecursionCount_stddev'
    COMPARISON_COUNT = 'ComparisonCount'
    COMPARISON_COUNT_STDDEV = 'ComparisonCount_stddev'
    
    @classmethod
    def get_all(cls):
        return [
            cls.INPUT_SIZE,
            cls.EXECUTION_TIME,
            cls.EXECUTION_TIME_STDDEV,
            cls.RECURSION_COUNT,
            cls.RECURSION_COUNT_STDDEV,
            cls.COMPARISON_COUNT,
            cls.COMPARISON_COUNT_STDDEV
        ]

PRINT_GEN_ARRAY = 'Gerando array com {n} elementos...'
PRINT_START_SORT = 'Iniciando Merge Sort para {n} elementos ({r} repetições)...'
PRINT_REP = '  Repetição {i}: {ms:.3f} ms, {rec} recursões, {comp} comparações'
PRINT_STATS_HEADER = '\n--- Estatísticas Médias da Execução ---'
PRINT_INPUT_SIZE = 'Tamanho da Entrada (N): {n}'
PRINT_TIME = 'Tempo Médio de Execução: {ms:.3f} ms (±{std:.3f} ms)'
PRINT_RECURSION = 'Número Médio de Chamadas Recursivas: {rec:.1f} (±{std:.1f})'
PRINT_COMPARISON = 'Número Médio de Comparações: {comp:.1f} (±{std:.1f})'
PRINT_STATS_SAVED = "Estatísticas médias salvas em '{csv}'\n"

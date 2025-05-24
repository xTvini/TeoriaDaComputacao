// C constants for merge sort benchmarking
#ifndef MERGESORT_CONSTANTS_H
#define MERGESORT_CONSTANTS_H

#define REPETITIONS 20
#define MAX_SIZE 1000000
#define INPUT_SIZES_FILE "project/input_sizes.txt"
#define C_CSV "project/data/datasheet_clang.csv"

// String constants for mergesort.c
#define CSV_HEADER "InputSize,ExecutionTime_ms,ExecutionTime_ms_stddev,RecursionCount,RecursionCount_stddev,ComparisonCount,ComparisonCount_stddev\n"
#define PRINT_BENCHMARKING_SIZE "Benchmarking size %d...\n"
#define PRINT_REP "  Rep %d: %.3f ms, %ld rec, %ld comp\n"
#define PRINT_SAVED_STATS "Saved stats for size %d\n"
#define PRINT_COMPLETE "Benchmarking complete. Results saved to mergesort_stats_c.csv\n"
#define ERR_OPEN_INPUT "Could not open %s\n"

#endif // MERGESORT_CONSTANTS_H

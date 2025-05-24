import random
import time
import csv
import os
import statistics
from project.constants.mergesort_constants import *

recursion_count = 0
comparison_count = 0

def mergesort(array: list, start_index: int, end_index: int):
  
    global recursion_count
    recursion_count += 1

    if start_index >= end_index:
        return
    
    mid_index = (start_index + end_index) // 2

    mergesort(array, start_index, mid_index)
    mergesort(array, mid_index + 1, end_index)
    merge(array, start_index, mid_index, end_index)

def merge(array: list, start_index: int, mid_index: int, end_index: int) -> None:
   
    global comparison_count
    start_v01: int = start_index
    start_v02: int = mid_index + 1
    new_array: list = []

  
    while start_v01 <= mid_index and start_v02 <= end_index:
        comparison_count += 1  
        if array[start_v01] <= array[start_v02]:
            new_array.append(array[start_v01])
            start_v01 += 1
        else:
            new_array.append(array[start_v02])
            start_v02 += 1

    
    while start_v01 <= mid_index:
        new_array.append(array[start_v01])
        start_v01 += 1

  
    while start_v02 <= end_index:
        new_array.append(array[start_v02])
        start_v02 += 1

    
    for i in range(len(new_array)):
        array[start_index + i] = new_array[i]

def write_stats_to_csv(filename: str, stats: dict):
    file_exists = os.path.isfile(filename)
    with open(filename, mode='a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=CsvFields.get_all())

        if not file_exists:
            writer.writeheader() 
        
        writer.writerow(stats)

def benchmark_mergesort(input_size, csv_filename, repetitions=5):
    global recursion_count, comparison_count
    
    elapsed_ms_list = []
    recursion_count_list = []
    comparison_count_list = []
    
    print(PRINT_GEN_ARRAY.format(n=input_size))
    arrays = [[random.randint(1, 1000000) for _ in range(input_size)] for _ in range(repetitions)]
    
    print(PRINT_START_SORT.format(n=input_size, r=repetitions))
    
    for i in range(repetitions):
        array = arrays[i].copy()
        recursion_count = 0
        comparison_count = 0
        
        start_time = time.perf_counter()
        mergesort(array, 0, input_size - 1)
        end_time = time.perf_counter()
        
        elapsed_ms = (end_time - start_time) * 1000
        
        elapsed_ms_list.append(elapsed_ms)
        recursion_count_list.append(recursion_count)
        comparison_count_list.append(comparison_count)
        
        print(PRINT_REP.format(i=i+1, ms=elapsed_ms, rec=recursion_count, comp=comparison_count))
    
    # Calculate averages
    avg_elapsed_ms = statistics.mean(elapsed_ms_list)
    avg_recursion_count = statistics.mean(recursion_count_list)
    avg_comparison_count = statistics.mean(comparison_count_list)
    stddev_elapsed_ms = statistics.stdev(elapsed_ms_list) if repetitions > 1 else 0.0
    stddev_recursion_count = statistics.stdev(recursion_count_list) if repetitions > 1 else 0.0
    stddev_comparison_count = statistics.stdev(comparison_count_list) if repetitions > 1 else 0.0
    
    print(PRINT_STATS_HEADER)
    print(PRINT_INPUT_SIZE.format(n=input_size))
    print(PRINT_TIME.format(ms=avg_elapsed_ms, std=stddev_elapsed_ms))
    print(PRINT_RECURSION.format(rec=avg_recursion_count, std=stddev_recursion_count))
    print(PRINT_COMPARISON.format(comp=avg_comparison_count, std=stddev_comparison_count))
    
    stats_data = {
        CsvFields.INPUT_SIZE: input_size,
        CsvFields.EXECUTION_TIME: round(avg_elapsed_ms, 3),
        CsvFields.EXECUTION_TIME_STDDEV: round(stddev_elapsed_ms, 3),
        CsvFields.RECURSION_COUNT: round(avg_recursion_count),
        CsvFields.RECURSION_COUNT_STDDEV: round(stddev_recursion_count, 1),
        CsvFields.COMPARISON_COUNT: round(avg_comparison_count),
        CsvFields.COMPARISON_COUNT_STDDEV: round(stddev_comparison_count, 1)
    }
    
    write_stats_to_csv(csv_filename, stats_data)
    print(PRINT_STATS_SAVED.format(csv=csv_filename))

def read_input_sizes(filename):
    with open(filename, 'r') as f:
        return [int(line.strip()) for line in f if line.strip()]

def main():
    input_sizes = read_input_sizes(INPUT_SIZES_FILE)
    csv_filename = PYTHON_CSV
    for input_size in input_sizes:
        benchmark_mergesort(input_size, csv_filename, REPETITIONS)

if __name__ == "__main__":
    main()

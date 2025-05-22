import random
import time
import csv
import os


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
        fieldnames = ['InputSize', 'ExecutionTime_ms', 'ExecutionTime_s', 'RecursionCount', 'ComparisonCount']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader() 
        
        writer.writerow(stats)

def benchmark_mergesort(input_size, csv_filename, repetitions=5):
    global recursion_count, comparison_count
    
    total_elapsed_ms = 0
    total_recursion_count = 0
    total_comparison_count = 0
    
    print(f"Gerando array com {input_size} elementos...")
    arrays = [[random.randint(1, 1000000) for _ in range(input_size)] for _ in range(repetitions)]
    
    print(f"Iniciando Merge Sort para {input_size} elementos ({repetitions} repetições)...")
    
    for i in range(repetitions):
        array = arrays[i].copy()
        recursion_count = 0
        comparison_count = 0
        
        start_time = time.perf_counter()
        mergesort(array, 0, input_size - 1)
        end_time = time.perf_counter()
        
        elapsed_ms = (end_time - start_time) * 1000
        
        total_elapsed_ms += elapsed_ms
        total_recursion_count += recursion_count
        total_comparison_count += comparison_count
        
        print(f"  Repetição {i+1}: {elapsed_ms:.3f} ms, {recursion_count} recursões, {comparison_count} comparações")
    
    # Calculate averages
    avg_elapsed_ms = total_elapsed_ms / repetitions
    avg_recursion_count = total_recursion_count / repetitions
    avg_comparison_count = total_comparison_count / repetitions
    
    print("\n--- Estatísticas Médias da Execução ---")
    print(f"Tamanho da Entrada (N): {input_size}")
    print(f"Tempo Médio de Execução: {avg_elapsed_ms:.3f} ms")
    print(f"Número Médio de Chamadas Recursivas: {avg_recursion_count:.1f}")
    print(f"Número Médio de Comparações: {avg_comparison_count:.1f}")
    
    stats_data = {
        'InputSize': input_size,
        'ExecutionTime_ms': round(avg_elapsed_ms, 3),
        'RecursionCount': round(avg_recursion_count),
        'ComparisonCount': round(avg_comparison_count)
    }
    
    write_stats_to_csv(csv_filename, stats_data)
    print(f"Estatísticas médias salvas em '{csv_filename}'\n")

def main():
    csv_filename = 'mergesort_stats.csv'
    # More comprehensive range of input sizes for algorithm analysis
    input_sizes = [100, 500, 1000, 2500, 5000, 7500, 10000, 15000, 20000, 
                  30000, 50000, 75000, 100000, 150000, 200000, 250000]
    
    for input_size in input_sizes:
        benchmark_mergesort(input_size, csv_filename, 20)

if __name__ == "__main__":
    main()

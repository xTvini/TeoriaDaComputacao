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

def main():
    global recursion_count, comparison_count

   
    recursion_count = 0
    comparison_count = 0

    
    N = 10000  
    
    
    print(f"Gerando array com {N} elementos...")
    array = [random.randint(1, 1000000) for _ in range(N)]
    input_size = len(array)
    
    print(f"Iniciando Merge Sort para {input_size} elementos...")
    start_time = time.perf_counter()
    mergesort(array, 0, input_size - 1)
    end_time = time.perf_counter()
    
    elapsed_ms = (end_time - start_time) * 1000
    elapsed_s = end_time - start_time
    
    print(f"\n--- Estatísticas da Execução ---")
    print(f"Tamanho da Entrada (N): {input_size}")
    print(f"Tempo de Execução: {elapsed_ms:.3f} ms ({elapsed_s:.3f} s)")
    print(f"Número de Chamadas Recursivas: {recursion_count}")
    print(f"Número de Comparações: {comparison_count}")

    
    stats_data = {
        'InputSize': input_size,
        'ExecutionTime_ms': round(elapsed_ms, 3),
        'ExecutionTime_s': round(elapsed_s, 3),
        'RecursionCount': recursion_count,
        'ComparisonCount': comparison_count
    }

    
    csv_filename = 'mergesort_stats.csv'
    write_stats_to_csv(csv_filename, stats_data)
    print(f"Estatísticas salvas em '{csv_filename}'")

if __name__ == "__main__":
    main()

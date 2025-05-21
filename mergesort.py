import random
import time

def mergesort(array: list, start_index: int, end_index: int):

    if start_index >= end_index:
        return
    
    mid_index = (start_index + end_index) // 2

    mergesort(array, start_index, mid_index)

    mergesort(array, mid_index + 1, end_index)

    merge(array, start_index, mid_index, end_index)

def merge(array: list, start_index: int, mid_index: int, end_index: int) -> None:
    start_v01: int = start_index
    start_v02: int = mid_index + 1

    new_array: list = []

    while start_v01 <= mid_index and start_v02 <= end_index:
        if array[start_v01] <= array[start_v02]:
            new_array.append(array[start_v01])
            start_v01 += 1
            continue

        new_array.append(array[start_v02])
        start_v02 += 1

    while start_v01 <= mid_index:
        new_array.append(array[start_v01])
        start_v01 += 1

    while start_v02 <= end_index:
        new_array.append(array[start_v02])
        start_v02 += 1

    # Copia de volta para o array original
    for i in range(len(new_array)):
        array[start_index + i] = new_array[i]

def main():
    BILLION = 1000000000
    MILLION = 1000000
    array = [random.randint(1, 1000000) for _ in range(BILLION)]

    start = time.perf_counter()

    mergesort(array, 0, len(array)-1)

    end = time.perf_counter()
    
    elapsed_ms = (end - start) * 1000  # milissegundos
    elapsed_s = (end - start)  # segundos
    print(f"Input size: {len(array)}")
    print(f"Miliseconds {elapsed_ms:.3f} ms")
    print(f"Seconds: {elapsed_s:.3f} s")

main()
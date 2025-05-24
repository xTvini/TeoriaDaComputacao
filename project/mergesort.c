#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>
#include <string.h>
#include "constants/mergesort_constants.h"

// Global counters
long recursion_count = 0;
long comparison_count = 0;

// Prototypes
void mergesort(int arr[], int startIndex, int endIndex);
void merge(int arr[], int startIndex, int midIndex, int endIndex);

// Utility for random array
void fill_random(int arr[], int n) {
    for (int i = 0; i < n; i++)
        arr[i] = rand() % 1000000 + 1;
}

// Statistics helpers
double mean(double arr[], int n) {
    double sum = 0;
    for (int i = 0; i < n; i++) sum += arr[i];
    return sum / n;
}
double stddev(double arr[], int n, double avg) {
    double sum = 0;
    for (int i = 0; i < n; i++) sum += (arr[i] - avg) * (arr[i] - avg);
    return n > 1 ? sqrt(sum / (n - 1)) : 0.0;
}

void read_input_sizes(const char *filename, int *sizes, int *num_sizes) {
    FILE *file = fopen(filename, "r");
    if (!file) {
        printf(ERR_OPEN_INPUT, filename);
        exit(1);
    }
    int n, count = 0;
    while (fscanf(file, "%d", &n) == 1) {
        sizes[count++] = n;
    }
    fclose(file);
    *num_sizes = count;
}

int main() {
    srand(time(NULL));
    int input_sizes[100];
    int num_sizes = 0;
    read_input_sizes(INPUT_SIZES_FILE, input_sizes, &num_sizes);
    FILE *csv = fopen(C_CSV, "w");
    fprintf(csv, CSV_HEADER);

    int *array = malloc(MAX_SIZE * sizeof(int));
    int *backup = malloc(MAX_SIZE * sizeof(int));
    for (int s = 0; s < num_sizes; s++) {
        int n = input_sizes[s];
        double times[REPETITIONS];
        double recursions[REPETITIONS];
        double comparisons[REPETITIONS];

        // Prepare random arrays for all repetitions
        for (int r = 0; r < REPETITIONS; r++) {
            fill_random(backup, n);
        }

        printf(PRINT_BENCHMARKING_SIZE, n);
        for (int r = 0; r < REPETITIONS; r++) {
            // Copy backup to array
            for (int i = 0; i < n; i++) array[i] = backup[i];

            recursion_count = 0;
            comparison_count = 0;

            clock_t start = clock();
            mergesort(array, 0, n - 1);
            clock_t end = clock();

            double elapsed_ms = (double)(end - start) * 1000.0 / CLOCKS_PER_SEC;
            times[r] = elapsed_ms;
            recursions[r] = recursion_count;
            comparisons[r] = comparison_count;

            printf(PRINT_REP, r + 1, elapsed_ms, recursion_count, comparison_count);
        }

        double avg_time = mean(times, REPETITIONS);
        double std_time = stddev(times, REPETITIONS, avg_time);
        double avg_rec = mean(recursions, REPETITIONS);
        double std_rec = stddev(recursions, REPETITIONS, avg_rec);
        double avg_comp = mean(comparisons, REPETITIONS);
        double std_comp = stddev(comparisons, REPETITIONS, avg_comp);

        fprintf(csv, "%d,%.3f,%.3f,%.0f,%.1f,%.0f,%.1f\n",
                n, avg_time, std_time, avg_rec, std_rec, avg_comp, std_comp);
        printf(PRINT_SAVED_STATS, n);
    }
    fclose(csv);
    free(array);
    free(backup);
    printf(PRINT_COMPLETE, C_CSV);
    return 0;
}

// Merge Sort implementation with counters
void mergesort(int arr[], int startIndex, int endIndex) {
    recursion_count++;
    if (startIndex < endIndex) {
        int mid = (startIndex + endIndex) / 2;
        mergesort(arr, startIndex, mid);
        mergesort(arr, mid + 1, endIndex);
        merge(arr, startIndex, mid, endIndex);
    }
}

void merge(int arr[], int startIndex, int midIndex, int endIndex) {
    int inicio_v01 = startIndex;
    int inicio_v02 = midIndex + 1;
    int *newArr = malloc((endIndex - startIndex + 1) * sizeof(int));
    int newIndex = 0;

    while (inicio_v01 <= midIndex && inicio_v02 <= endIndex) {
        comparison_count++;
        if (arr[inicio_v01] <= arr[inicio_v02]) {
            newArr[newIndex++] = arr[inicio_v01++];
        } else {
            newArr[newIndex++] = arr[inicio_v02++];
        }
    }
    while (inicio_v01 <= midIndex) {
        newArr[newIndex++] = arr[inicio_v01++];
    }
    while (inicio_v02 <= endIndex) {
        newArr[newIndex++] = arr[inicio_v02++];
    }
    for (int i = 0; i < newIndex; i++) {
        arr[startIndex + i] = newArr[i];
    }
    free(newArr);
}
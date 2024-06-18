#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <string.h>

#define NUM_THREADS 14

long global_permutations[14];


typedef struct {
    int start_element;
    int elements[14];
} ThreadData;

void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

long permute(int *arr, int start, int end) {
    if (start == end) {
        return 1;
    }

    long total = 0;
    for (int i = start; i <= end; i++) {
        swap(&arr[start], &arr[i]);
        total += permute(arr, start + 1, end);
        swap(&arr[start], &arr[i]); // backtrack
    }
    return total;
}

void *thread_function(void *arg) {
    ThreadData *data = (ThreadData *)arg;

    int permute_array[13];
    int index = 0;


    for (int i = 0; i < 14; i++) {
        if (data->elements[i] != data->start_element) {
            permute_array[index++] = data->elements[i];
        }
    }

    int result[14];
    result[0] = data->start_element;
    memcpy(result + 1, permute_array, 13 * sizeof(int));

    long res = permute(result, 1, 13);
    global_permutations[data->start_element-1] = res;
    pthread_exit(NULL);
}

int main() {
    pthread_t threads[NUM_THREADS];
    ThreadData thread_data[NUM_THREADS];
    int elements[14];

    for (int i = 0; i < 14; i++) {
        elements[i] = i + 1;
    }

    for (int i = 0; i < NUM_THREADS; i++) {
        thread_data[i].start_element = elements[i];
        memcpy(thread_data[i].elements, elements, 14 * sizeof(int));

        int rc = pthread_create(&threads[i], NULL, thread_function, (void *)&thread_data[i]);
        if (rc) {
            fprintf(stderr, "Error: unable to create thread, %d\n", rc);
            exit(-1);
        }
    }

    for (int i = 0; i < NUM_THREADS; i++) {
        pthread_join(threads[i], NULL);
    }

    long res = 0;
    for (int i=0; i<14; i++) {
        res += global_permutations[i];
        printf("%d\n",global_permutations[i]);
    }
    printf("result: %ld\n",res);

    pthread_exit(NULL);
    return 0;
}

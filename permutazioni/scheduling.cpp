#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <pthread.h>

typedef struct {
    int permA[720][6];
    int permB[24][4];
    int permC[24][4];
    int permD[5040][7];
} PermSale;

typedef struct {
    PermSale *ps;
    int indexA;
    int durations[21];
    int max_BII;
    int scelte[3];
} ThreadData;

void printArray(int *array, int size) {
    printf("Array: ");
    for(int i = 0; i < size; i++) {
        printf("%d ", array[i]);
    }
    printf("\n");
}

void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

void permuteA(int *arr, int l, int r, int result[][6], int *index) {
    if (l == r) {
        for (int i = 0; i <= r; i++) {
            result[*index][i] = arr[i];
        }
        (*index)++;
    } else {
        for (int i = l; i <= r; i++) {
            swap(&arr[l], &arr[i]);
            permuteA(arr, l + 1, r, result, index);
            swap(&arr[l], &arr[i]); // backtrack
        }
    }
}

void permuteB(int *arr, int l, int r, int result[][4], int *index) {
    if (l == r) {
        for (int i = 0; i <= r; i++) {
            result[*index][i] = arr[i];
        }
        (*index)++;
    } else {
        for (int i = l; i <= r; i++) {
            swap(&arr[l], &arr[i]);
            permuteB(arr, l + 1, r, result, index);
            swap(&arr[l], &arr[i]); // backtrack
        }
    }
}

void permuteC(int *arr, int l, int r, int result[][4], int *index) {
    if (l == r) {
        for (int i = 0; i <= r; i++) {
            result[*index][i] = arr[i];
        }
        (*index)++;
    } else {
        for (int i = l; i <= r; i++) {
            swap(&arr[l], &arr[i]);
            permuteC(arr, l + 1, r, result, index);
            swap(&arr[l], &arr[i]); // backtrack
        }
    }
}

void permuteD(int *arr, int l, int r, int result[][7], int *index) {
    if (l == r) {
        for (int i = 0; i <= r; i++) {
            result[*index][i] = arr[i];
        }
        (*index)++;
    } else {
        for (int i = l; i <= r; i++) {
            swap(&arr[l], &arr[i]);
            permuteD(arr, l + 1, r, result, index);
            swap(&arr[l], &arr[i]); // backtrack
        }
    }
}

void generatePermutations(PermSale *ps) {
    int indexA = 0, indexB = 0, indexC = 0, indexD = 0;

    int arrayA[6] = {1, 2, 3, 4, 5, 6};
    int arrayB[4] = {7, 8, 9, 10};
    int arrayC[4] = {11, 12, 13, 14};
    int arrayD[7] = {15, 16, 17, 18, 19, 20, 21};

    permuteA(arrayA, 0, 5, ps->permA, &indexA);
    permuteB(arrayB, 0, 3, ps->permB, &indexB);
    permuteC(arrayC, 0, 3, ps->permC, &indexC);
    permuteD(arrayD, 0, 6, ps->permD, &indexD);
}

void mergeArrays(int result[], int sizeA, int arrA[], int sizeB, int arrB[], int sizeC, int arrC[], int sizeD, int arrD[]) {
    int totalSize = sizeA + sizeB + sizeC + sizeD;
    int index = 0;

    // Unire tutti gli elementi in un singolo array
    for (int i = 0; i < sizeA; i++) {
        result[index++] = arrA[i];
    }
    for (int i = 0; i < sizeB; i++) {
        result[index++] = arrB[i];
    }
    for (int i = 0; i < sizeC; i++) {
        result[index++] = arrC[i];
    }
    for (int i = 0; i < sizeD; i++) {
        result[index++] = arrD[i];
    }

    // Ordinare il nuovo array
    for (int i = 0; i < totalSize - 1; i++) {
        for (int j = i + 1; j < totalSize; j++) {
            if (result[i] > result[j]) {
                int temp = result[i];
                result[i] = result[j];
                result[j] = temp;
            }
        }
    }
}

void permWithDurations(int perm[], int size, int durations[], int result[]) {
    int time = 0;
    for (int i = 0; i < size; i++) {
        time += durations[perm[i]];
        result[i] = time;
    }
}

int calculateBII(int array[]) {
    int max_BII = array[0];
    for (int i = 0; i < 21 - 1; i++) {
        int BII = array[i + 1] - array[i];
        if (BII > max_BII) {
            max_BII = BII;
        }
    }
    return max_BII;
}

void *threadFunc(void *arg) {
    ThreadData *data = (ThreadData *)arg;
    PermSale *ps = data->ps;
    int indexA = data->indexA;
    int durations[21];
    memcpy(durations, data->durations, 21 * sizeof(int));

    data->max_BII = 480;
    for (int b = 0; b < 24; b++) {
        for (int c = 0; c < 24; c++) {
            for (int d = 0; d < 5040; d++) {
                // Scegli una permutazione per permA, permB, permC, permD
                int chosenPermA[6], chosenPermB[4], chosenPermC[4], chosenPermD[7];
                memcpy(chosenPermA, ps->permA[indexA], 6 * sizeof(int));
                memcpy(chosenPermB, ps->permB[b], 4 * sizeof(int));
                memcpy(chosenPermC, ps->permC[c], 4 * sizeof(int));
                memcpy(chosenPermD, ps->permD[d], 7 * sizeof(int));

                // Sostituisci gli indici con le durate
                int arrayA[6], arrayB[4], arrayC[4], arrayD[7];
                permWithDurations(chosenPermA, 6, durations, arrayA);
                permWithDurations(chosenPermB, 4, durations, arrayB);
                permWithDurations(chosenPermC, 4, durations, arrayC);
                permWithDurations(chosenPermD, 7, durations, arrayD);

                // Unire e ordinare i quattro array
                int mergedArray[21]; // 6 + 4 + 4 + 7 = 21
                mergeArrays(mergedArray, 6, arrayA, 4, arrayB, 4, arrayC, 7, arrayD);

                // Calcolare il BII
                int actual_BII = calculateBII(mergedArray);
                if (data->max_BII > actual_BII) {
                    data->max_BII = actual_BII;
                    data->scelte[0] = b;
                    data->scelte[1] = c;
                    data->scelte[2] = d;
                }
            }
        }
    }
    return NULL;
}

void thread_launcher() {
    PermSale ps;
    generatePermutations(&ps);

    int durations[21] =  {
        64, 135, 62, 66, 80, 73, 107, 135, 221, 17,
        29, 129, 88, 234, 130, 36, 61, 29, 68, 81, 75
    };

    pthread_t threads[720];
    ThreadData data[720];

    for(int i = 0; i < 720; i++) {
        data[i].ps = &ps;
        data[i].indexA = i;
        memcpy(data[i].durations, durations, 21 * sizeof(int));
        data[i].max_BII = 0;
        pthread_create(&threads[i], NULL, threadFunc, (void *)&data[i]);
    }

    int minBII = 480;
    int winning_thread = 0;
    int b = 0, c = 0, d = 0;

    for(int i = 0; i < 720; i++) {
        pthread_join(threads[i], NULL);
        if(data[i].max_BII < minBII) {
            minBII = data[i].max_BII;
            winning_thread = i;
            b = data[i].scelte[0];
            c = data[i].scelte[1];
            d = data[i].scelte[2];
        }
    }

    printf("Scheduling sala A\n");
    for(int i = 0; i < 6; i++) {
        printf("%d ", ps.permA[winning_thread][i]);
    }
    printf("\n");

    printf("Scheduling sala B\n");
    for(int i = 0; i < 4; i++) {
        printf("%d ", ps.permB[b][i]);
    }
    printf("\n");

    printf("Scheduling sala C\n");
    for(int i = 0; i < 4; i++) {
        printf("%d ", ps.permC[c][i]);
    }
    printf("\n");

    printf("Scheduling sala D\n");
    for(int i = 0; i < 7; i++) {
        printf("%d ", ps.permD[d][i]);
    }
    printf("\n");

    printf("Max BII: %d\n", minBII);
}

int main() {
    // thread_launcher();
    PermSale ps;
    generatePermutations(&ps);
    int durations[26] = {44, 56, 62, 52, 53, 22, 93, 98,
        104, 24, 131, 121, 100,
        36, 98, 72, 166, 66, 42,
        74, 104, 74, 32, 99, 51, 46};
    int arrayA[8], arrayB[5], arrayC[6], arrayD[7];
    int a[] = {5, 7, 1, 2, 3, 6, 0, 4};
    int b[] = {12, 8, 10, 11, 9};
    int c[] = {15, 17, 14, 18, 13, 16};
    int d [] = {24, 23, 21, 22, 20, 25, 19};
    permWithDurations(a, 8, durations, arrayA);
    permWithDurations(b, 5, durations, arrayB);
    permWithDurations(c, 6, durations, arrayC);
    permWithDurations(d, 7, durations, arrayD);

    // Unire e ordinare i quattro array
    int mergedArray[26]; // 6 + 4 + 4 + 7 = 21
    mergeArrays(mergedArray, 8, arrayA, 5, arrayB, 6, arrayC, 7, arrayD);

    // Calcolare il BII
    int actual_BII = calculateBII(mergedArray);
    printArray(arrayA,8);
    printArray(arrayB,5);
    printArray(arrayC,6);
    printArray(arrayD,7);
    printArray(mergedArray,26);
    printf("%d ",actual_BII);
    return 0;
}

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <pthread.h>

// Struttura per contenere le permutazioni
typedef struct {
    int **permA;
    int **permB;
    int **permC;
    int **permD;
    int sizeA;
    int sizeB;
    int sizeC;
    int sizeD;
    int lenA;
    int lenB;
    int lenC;
    int lenD;
    int lenRidimensionataA;
    int lenRidimensionataB;
    int lenRidimensionataC;
    int lenRidimensionataD;
    int * substitution;
} PermSale;

// Struttura per i dati dei thread
typedef struct {
    PermSale *ps;
    int indexA;
    int *durations;
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

// Funzione generica per generare permutazioni
void permute(int *arr, int l, int r, int **result, int *index, int size) {
    if (l == r) {
        for (int i = 0; i <= r; i++) {
            result[*index][i] = arr[i];
        }
        (*index)++;
    } else {
        for (int i = l; i <= r; i++) {
            swap(&arr[l], &arr[i]);
            permute(arr, l + 1, r, result, index, size);
            swap(&arr[l], &arr[i]); // backtrack
        }
    }
}

// Funzione per generare tutte le permutazioni
void generatePermutations(PermSale *ps, int *arrayA, int sizeA, int *arrayB, int sizeB, int *arrayC, int sizeC, int *arrayD, int sizeD) {
    int indexA = 0, indexB = 0, indexC = 0, indexD = 0;
    permute(arrayA, 0, sizeA - 1, ps->permA, &indexA, sizeA);
    permute(arrayB, 0, sizeB - 1, ps->permB, &indexB, sizeB);
    permute(arrayC, 0, sizeC - 1, ps->permC, &indexC, sizeC);
    permute(arrayD, 0, sizeD - 1, ps->permD, &indexD, sizeD);
}

// Funzione per unire e ordinare gli array
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

void permWithDurations(PermSale *ps,int perm[], int size, int durations[], int result[]) {
    int time = 0;
    int j = 0;
    for (int i = 0; i < size; i++) {
        time += durations[perm[i]];
        result[i+j] = time;

        if (ps->substitution[perm[i]] != -1) {
            time += durations[ps->substitution[perm[i]]];
            result[i+j+1] = time;
            j++;
        }
    }
}

int calculateBII(int array[], int size) {
    int max_BII = array[0];
    for (int i = 0; i < size - 1; i++) {
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
    int *durations = data->durations;

    for (int b = 0; b < ps->sizeB; b++) {
        for (int c = 0; c < ps->sizeC; c++) {
            for (int d = 0; d < ps->sizeD; d++) {
                int arrayA[ps->lenRidimensionataA], arrayB[ps->lenRidimensionataB], arrayC[ps->lenRidimensionataC], arrayD[ps->lenRidimensionataD];
                permWithDurations(ps,ps->permA[indexA], ps->lenA, durations, arrayA);
                permWithDurations(ps,ps->permB[b], ps->lenB, durations, arrayB);
                permWithDurations(ps,ps->permC[c], ps->lenC, durations, arrayC);
                permWithDurations(ps,ps->permD[d], ps->lenD, durations, arrayD);

                int totalLenghtRidimensionata = ps->lenRidimensionataA+ps->lenRidimensionataB+ps->lenRidimensionataC+ps->lenRidimensionataD;
                int mergedArray[totalLenghtRidimensionata]; // Considerando che la lunghezza totale degli array combinati sarà 26
                mergeArrays(mergedArray, ps->lenRidimensionataA, arrayA, ps->lenRidimensionataB, arrayB, ps->lenRidimensionataC
                , arrayC, ps->lenRidimensionataD, arrayD);

                int actual_BII = calculateBII(mergedArray, totalLenghtRidimensionata); // 26 è la lunghezza totale degli array combinati
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

void pre_proces(PermSale * ps, int * array_a, int sizeA, int * array_b, int sizeB, int * array_c,
               int sizeC, int * array_d, int sizeD, int * substitution_array, int sizeSub) {
    /*lunghezza degli array*/
    ps->lenA = sizeA;
    ps->lenB = sizeB;
    ps->lenC = sizeC;
    ps->lenD = sizeD;

    int factA = 1, factB = 1, factC = 1, factD = 1;
    for (int i = 1; i <= sizeA; i++) factA *= i;
    for (int i = 1; i <= sizeB; i++) factB *= i;
    for (int i = 1; i <= sizeC; i++) factC *= i;
    for (int i = 1; i <= sizeD; i++) factD *= i;

    /*quantita degli array*/
    ps->sizeA = factA;
    ps->sizeB = factB;
    ps->sizeC = factC;
    ps->sizeD = factD;

    ps->permA = (int **)malloc(factA * sizeof(int *));
    ps->permB = (int **)malloc(factB * sizeof(int *));
    ps->permC = (int **)malloc(factC * sizeof(int *));
    ps->permD = (int **)malloc(factD * sizeof(int *));
    for (int i = 0; i < factA; i++) ps->permA[i] = (int*)malloc(sizeA * sizeof(int));
    for (int i = 0; i < factB; i++) ps->permB[i] = (int*)malloc(sizeB * sizeof(int));
    for (int i = 0; i < factC; i++) ps->permC[i] = (int*)malloc(sizeC * sizeof(int));
    for (int i = 0; i < factD; i++) ps->permD[i] = (int*)malloc(sizeD * sizeof(int));


    for(int i = 0; i < sizeSub; i++) {
        substitution_array[i] = -1;
    }
}


void thread_launcher(PermSale ps, int *arrayA, int sizeA, int *arrayB, int sizeB, int *arrayC, int sizeC, int *arrayD, int sizeD, int *
                     durations) {
    generatePermutations(&ps, arrayA, sizeA, arrayB, sizeB, arrayC, sizeC, arrayD, sizeD);

    int numThreads = ps.sizeA;
    pthread_t threads[numThreads];
    ThreadData data[numThreads];

    for (int i = 0; i < numThreads; i++) {
        data[i].ps = &ps;
        data[i].indexA = i;
        data[i].durations = durations;
        data[i].max_BII = 480;
        pthread_create(&threads[i], NULL, threadFunc, (void *)&data[i]);
    }

    int minBII = 480;
    int winning_thread = 0;
    int b = 0, c = 0, d = 0;

    for (int i = 0; i < numThreads; i++) {
        pthread_join(threads[i], NULL);
        if (data[i].max_BII < minBII) {
            minBII = data[i].max_BII;
            winning_thread = i;
            b = data[i].scelte[0];
            c = data[i].scelte[1];
            d = data[i].scelte[2];
        }
    }

    printf("Scheduling sala A\n");
    for (int i = 0; i < sizeA; i++) {
        printf("%d, ", ps.permA[winning_thread][i]);
    }
    printf("\n");

    printf("Scheduling sala B\n");
    for (int i = 0; i < sizeB; i++) {
        printf("%d, ", ps.permB[b][i]);
    }
    printf("\n");

    printf("Scheduling sala C\n");
    for (int i = 0; i < sizeC; i++) {
        printf("%d, ", ps.permC[c][i]);
    }
    printf("\n");

    printf("Scheduling sala D\n");
    for (int i = 0; i < sizeD; i++) {
        printf("%d, ", ps.permD[d][i]);
    }
    printf("\n");

    printf("Max BII: %d\n", minBII);

    // Liberare la memoria allocata
    for (int i = 0; i < ps.sizeA; i++) free(ps.permA[i]);
    for (int i = 0; i < ps.sizeB; i++) free(ps.permB[i]);
    for (int i = 0; i < ps.sizeC; i++) free(ps.permC[i]);
    for (int i = 0; i < ps.sizeD; i++) free(ps.permD[i]);
    free(ps.permA);
    free(ps.permB);
    free(ps.permC);
    free(ps.permD);
}
//cambiare valutazione BII partendo da 0 e non da 1
int main() {
    int arrayA[4] = {0, 1, 2, 3};
    int arrayB[5] = {4, 5, 6, 7, 8};
    int arrayC[5] = {9, 10, 11, 12, 13};
    int arrayD[7] = {14, 15, 16, 17, 19, 20, 21};
    int durations[22] =  {
        68, 197, 107, 108,
        141, 35, 112, 131, 61,
        174, 45, 130, 108, 23,
        85, 70, 76, 47, 34, 42, 56, 70
    };



    PermSale ps;
    int sub[sizeof(durations)/4];

    pre_proces(&ps, arrayA, sizeof(arrayA)/4, arrayB, sizeof(arrayB)/4, arrayC, sizeof(arrayC)/4, arrayD, sizeof(arrayD)/4,sub, sizeof(sub)/4);
    sub[19] = 18;

    ps.lenRidimensionataA = 4;
    ps.lenRidimensionataB = 5;
    ps.lenRidimensionataC = 5;
    ps.lenRidimensionataD = 8;
    ps.substitution = sub;
    thread_launcher(ps,arrayA, sizeof(arrayA)/4, arrayB, sizeof(arrayB)/4, arrayC, sizeof(arrayC)/4, arrayD, sizeof(arrayD)/4,durations);

    return 0;
}

/*
* int arrayA[6] = {1, 2, 3, 4, 5, 6};
    int arrayB[4] = {7, 8, 9, 10};
    int arrayC[4] = {11, 12, 13, 14};
    int arrayD[6] = {15, 16, 17, 19, 20, 21};
    int durations[21] = {64, 135, 62, 66, 80, 73,
        107, 135, 221, 17,
        29, 129, 88, 234,
        130, 36, 61, 29, 68, 81, 75
    };

 */
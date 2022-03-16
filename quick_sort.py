import random


def randomized_partition(A, low, high):
    num = random.randint(low, high)
    A[num], A[high], A[high], A[num]

    return partition(A, low, high)


def partition(A, low, high):
    pivot = A[high]
    i = low - 1
    for j in range(low, high):
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[high] = A[high], A[i+1]
    return i + 1


def quick_sort(A, low, high):
    if low >= high:
        return

    pivot = randomized_partition(A, low, high)
    quick_sort(A, low, pivot-1)
    quick_sort(A, pivot+1, high)

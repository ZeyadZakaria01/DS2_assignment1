"""

1) find min value
2)swap min value with first index of the unsorted array
3)repeat

"""


def selection_sort(A):
    n = len(A)
    for i in range(n):
        min = i
        for j in range(i+1, n):
            if A[min] > A[j]:
                min = j
        A[i], A[min] = A[min], A[i]

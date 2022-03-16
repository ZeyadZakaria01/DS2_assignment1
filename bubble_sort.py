def bubble_sort(A):
    n = len(A)
    for i in range(n):
        swapped = False
        for j in range(n-i-1):
            if A[j] < A[j+1]:
                swapped = True
                A[j], A[j+1] = A[j+1], A[j]
        if not swapped:
            break

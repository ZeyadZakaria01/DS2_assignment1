def merge_sort(A):
    if len(A) <= 1:
        return

    mid = len(A) // 2

    L = A[:mid]

    R = A[mid:]

    merge_sort(L)

    merge_sort(R)

    i = j = k = 0

    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1

    while i < len(L):
        A[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        A[k] = R[j]
        j += 1
        k += 1


def merge_sort1(A):
    if len(A) > 1:

        mid = len(A)//2

        # Dividing the array elements
        L = A[:mid]

        # into 2 halves
        R = A[mid:]

        # Sorting the first half
        merge_sort1(L)

        # Sorting the second half
        merge_sort1(R)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                A[k] = L[i]
                i += 1
            else:
                A[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            A[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            A[k] = R[j]
            j += 1
            k += 1


# A = [1, 4, 5, 6, -5]
# # mergeSort(A)
# merge_sort(A)
# print(A)

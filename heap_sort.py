# heapfiy function is to ernsure that when you insert a new elment in the heap
# it will have its appropiate parent/child(s)

def heapify(A, n, i):
    root = i  # supposedly max elemnt in root
    left = i * 2 + 1
    right = i * 2 + 2

    if left < n and A[left] > A[root]:
        root = left
    if right < n and A[right] > A[root]:
        root = right

    if root != i:
        A[root], A[i] = A[i], A[root]
        heapify(A, n, root)


# we assume that we are inserting element A[i] each time in the heap

def build_heap(A, n):
    start = n//2 - 1
    for i in range(start, -1, -1):
        heapify(A, n, i)


def heap_sort(A):
    n = len(A)
    build_heap(A, n)

    for i in range(n-1, 0, -1):
        A[i], A[0] = A[0], A[i]  # ascending sorting
        # A[i], A[n-1] = A[0], A[n-1] #descending order
        heapify(A, i, 0)


A = [4, 5, 0, 4500, 233]
heap_sort(A)
print(A)

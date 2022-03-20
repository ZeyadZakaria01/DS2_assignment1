"""

1) basically, we find the right value of each index ( i in this implementation)
2) then after finding the right value of A[i] we change it (A[j])
    and then overwrite A[j] with key      
    ( this can be thought of as swap but its not really a swap as we overwrite rather than just swapping)



"""


def insertion_sort(A):
    n = len(A)
    for i in range(1, n):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > A[j+1]:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = key

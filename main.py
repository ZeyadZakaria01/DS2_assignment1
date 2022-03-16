from cv2 import merge
import numpy as np
import random
import time
#
from pprint import pprint
#
from selection_sort import selection_sort
from insertion_sort import insertion_sort
from bubble_sort import bubble_sort
from merge_sort import merge_sort
from quick_sort import quick_sort
from heap_sort import heap_sort


def get_random_from_range(low, high):
    return int(random.randint(low, high))


if __name__ == "__main__":
    x = random.randint(5, 101)  # array length vary from 5 to 99
    # r = int(random.randint(1000, 100001))  # values vary from 1k to 100k-1
    A = [get_random_from_range(1000, 100001)
         for i in range(x)]  # selection sort
    B = A.copy()  # insertion sort
    C = A.copy()  # bubble sort
    D = A.copy()  # merge sort
    E = A.copy()  # quick sort
    F = A.copy()  # heap sort
    merge_sort(A)
    # print(x)
    # for i in range(r):
    # print(i)
    # A = np.random.rand() * 10
    # pprint(len(A))
    # A = A.astype(int)
    # A = [1, 4, 5, 6, 6, 9]
    # B = A.copy()
    # insertion_sort(A)
    # pprint(A)
    # print(B)
    # count = 0
    # while count != 100:
    #     count += 1
    #     A = (np.random.rand(7) * 10)
    #     A = A.astype(int)
    #     print(A)
    #     quick_sort(A, 0, len(A)-1)
    #     print(A)

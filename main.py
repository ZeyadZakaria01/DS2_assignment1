import numpy as np
import matplotlib.pyplot as plt
import random
import time

from selection_sort import selection_sort
from insertion_sort import insertion_sort
from bubble_sort import bubble_sort
from merge_sort import merge_sort
from quick_sort import quick_sort
from heap_sort import heap_sort


def print_results():
    print("not implemented yet")


def get_random_from_range(low, high):
    return int(random.randint(low, high))


if __name__ == "__main__":
    selection_list = []
    insertion_list = []
    bubble_list = []
    merge_list = []
    quick_list = []
    heap_list = []
    x_axis = []
    for i in range(1000):
        # n = 1000
        n = i+5  # array length vary from 5 to 99
        x_axis.append(n)
        # print("======= At x -> {}=======".format(n))
        A = [get_random_from_range(1000, 100001)
             for i in range(n)]  # selection sort
        B = A.copy()  # insertion sort
        C = A.copy()  # bubble sort
        D = A.copy()  # merge sort
        E = A.copy()  # quick sort
        F = A.copy()  # heap sort

        # selection sort
        t1 = time.time()
        selection_sort(A)
        t2 = time.time()
        delta = (t2 - t1) * 1e3  # time in ms
        selection_list.append(delta)

        # insertion sort
        t1 = time.time()
        insertion_sort(B)
        t2 = time.time()
        delta = (t2 - t1) * 1e3  # time in ms
        insertion_list.append(delta)

        # bubble sort
        t1 = time.time()
        bubble_sort(C)
        t2 = time.time()
        delta = (t2 - t1) * 1e3  # time in ms
        bubble_list.append(delta)

        # merge sort
        t1 = time.time()
        merge_sort(D)
        t2 = time.time()
        delta = (t2 - t1) * 1e3  # time in ms
        merge_list.append(delta)

        # quick sort
        t1 = time.time()
        quick_sort(E, 0, len(E)-1)
        t2 = time.time()
        delta = (t2 - t1) * 1e3  # time in ms
        quick_list.append(delta)

        # heap sort
        # t1 = time.time()
        # heap_sort(F)
        # t2 = time.time()
        # delta = (t2 - t1) * 1e3  # time in ms
        # heap_list.append(delta)

    plt.title("A chart representing the runtime of the sorting algorithms")
    plt.xlabel("Length of the Array")
    plt.ylabel("Time(ms)")
    plt.plot(x_axis, selection_list, marker="o",
             color="lime", label="Selection Sort Algorithm")
    plt.plot(x_axis, insertion_list, marker="x",
             color="red", label="Insertion Sort Algorithm")
    plt.plot(x_axis, bubble_list, marker=">",
             color="pink", label="Bubbly Sort Algorithm")
    plt.plot(x_axis, merge_list, marker="<",
             color="grey", label="Merge Sort Algorithm")
    plt.plot(x_axis, quick_list, marker="v",
             color="blue", label="Quick Sort Algorithm")
    plt.legend()
    plt.show()
# plt.plot(x_axis, heap_list, color="red", label="Heap Sort Algorithm")

# for i, val in enumerate(x_axis):
#     print(val)
#     print(selection_list[i])
#     print(insertion_list[i])
#     print(bubble_list[i])
#     print(merge_list[i])
#     print(quick_list[i])

# print(np.average(selection_list))
# print(np.average(insertion_list))
# print(np.average(bubble_list))
# print(np.average(merge_list))
# print(np.average(quick_list))
# print(np.average(heap_list))

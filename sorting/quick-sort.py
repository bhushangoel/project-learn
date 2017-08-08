'''
Quick Sort:
This is same as that of merge sort, only difference is that in this technique instead of dividing the list into two parts
using mid position, we select first or last element from the list called PIVOT and than create the list in such a way 
that element smaller than the PIVOT are on the left side of it and elements greater than PIVOT are on the right side of 
the PIVOT. We than repeat the same process on the left and right side till we get the sorted list
'''


def partition(A, start, end):
    pivot = A[end]
    pIdx = start
    i = start
    while i <= end - 1:
        if A[i] <= pivot:
            A[pIdx], A[i] = A[i], A[pIdx]
            pIdx += 1
        i += 1
    A[pIdx], A[end] = A[end], A[pIdx]
    return pIdx


def quickSort(A, start, end):
    if end > start:
        pIdx = partition(A, start, end)
        quickSort(A, start, pIdx - 1)
        quickSort(A, pIdx + 1, end)
    else:
        print('quick sort :', A)


def quickSortMain(A):
    start = 0
    end = len(A) - 1
    quickSort(A, start, end)


quickSortMain([7, 2, 1, 6, 8, 5, 3, 4, 1])

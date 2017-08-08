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

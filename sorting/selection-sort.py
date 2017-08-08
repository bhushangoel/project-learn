'''
Selection Sort:
In this we selects the minimum/maximum element value from the array and replaces it with first or last element respectively
'''


def selectionSort(lst):
    i = 0
    size = len(lst)

    while i < size:
        minIdx = i
        j = i + 1
        while j < size:
            if lst[j] < lst[minIdx]:
                minIdx = j
            j += 1

        lst[minIdx], lst[i] = lst[i], lst[minIdx]
        i += 1

    print('selection sort :', lst)


selectionSort([5, 6, 2, 4, 7, 3, 1])

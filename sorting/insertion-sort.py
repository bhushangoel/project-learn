def insertionSort(lst):
    i = 1
    size = len(lst)
    while i < size:
        temp = lst[i]
        j = i
        while j > 0 and lst[j - 1] > temp:
            lst[j] = lst[j - 1]
            j -= 1
        lst[j] = temp
        i += 1

    print('insertion sort :', lst)


insertionSort([9, 1, 2, 5, 3, 4, 8, 5, 2, 3, 87, 34, 21, 0, 1])

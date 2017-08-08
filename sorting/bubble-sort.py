def bubblesort(lst):
    i = 0
    size = len(lst)
    swapped = 1
    count = 0

    while i < size - 1 and swapped == 1:
        swapped = 0
        j = 0
        while j < size - i - 1:
            count += 1
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swapped = 1
            j += 1
        i += 1

    print('bubble sort :', lst, count)


bubblesort([9, 1, 8, 2, 3, 4, 5, 6, 7])

'''
Bubble sort:
In bubble sort, each element is compared with its adjecent element. If the first element is higher than the second element
than their positions gets swapped, than it gets compared with the next element and same process is repeated for all items
in array. During this pass largest element occupies the last position.
This process is than repeated and now second largest element occupies second last position.
We repeat this till our array becomes sorted

Analysis:
O(n^2)
'''


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

'''
Insertion Sort:
In this one value is picked at a time and it gets inserted at the proper place in the list

steps:
1. Outer loop is use to pick the value that we want to insert, we save that value in the temp variable
2. Inner loop compares all the elements present at the left of the list with the temp value and values get shifted to the right 
until we find the proper position for the temp value

Analysis:
Worst case - O(n^2)
Avg case - O(n^2)
Best case - O(n)
'''


def insertionSort(lst):
    # we start iteration from position 1 and consider element at position 0 as sorted
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

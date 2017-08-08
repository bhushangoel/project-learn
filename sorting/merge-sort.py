'''
Merge Sort:
1. In this the given list is divided into 2 parts by finding the mid of list
2. left and right part of the list is further divided into 2 parts using mid position using recursion
3. we repeat step 1 and 2 till length of the list is less than 2, than we return the list and pass it to merge method, 
which than sort the list
'''

def merge(left, right, arr):
    # print('here :', left, right, arr)
    nl = len(left)
    nr = len(right)
    i = 0
    j = 0
    k = 0
    while i < nl and j < nr:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    while i < nl:
        arr[k] = left[i]
        i += 1
        k += 1
    while j < nr:
        arr[k] = right[j]
        j += 1
        k += 1
    print('merge sort : ', arr)


def mergeSort(lst, frm):
    n = len(lst)
    if n < 2:
        return
    else:
        mid = int(n / 2)
        left = lst[0:mid]
        right = lst[mid:n]

        # print(frm, ':', left, right)
        mergeSort(left, 'l')
        mergeSort(right, 'r')
        merge(left, right, lst)


mergeSort([2, 4, 1, 6, 8, 5, 3, 7], 'main')

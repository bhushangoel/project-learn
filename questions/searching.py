def generateCombinations(lst):
    count = 0
    i = 0

    def generate():

        generate()

    generate()

    while i < len(lst):
        j = i + 1
        while j < len(lst):
            k = j + 1
            while k < len(lst):
                count += 1
                print(count, ' : ', lst[i], lst[j], lst[k])
                k += 1
            j += 1
        i += 1


# threeItemSum([5, 3, 8, 9, 1, 4, 2], 7)

def threeItemSum(lst, k):
    print(lst, k)
    i = 0
    arr = []
    while i < len(lst):
        j = i
        nlist = lst[j:len(lst)]
        print('a', nlist)
        while j < len(nlist):
            if lst[i] < k:
                d = k - lst[i]
                if lst[i] + d < k:
                    if d in nlist:
                        arr.append(d)
                        arr.append(lst[i])
                        d2 = k - (lst[i] + d)
                        if d2 in nlist:
                            arr.append(d2)
                        else:
                            j += 1
                    else:
                        j += 1
                else:
                    j += 1
            else:
                j += 1
        i += 1

    print('result', arr)


# generateCombinations([1, 2, 3, 4, 5, 6])


def twod1(lst, k):
    i = 0
    while i < len(lst):
        j = 0
        while j < len(lst):
            if lst[i][j] == k:
                print("found ", k)
                break
            j += 1
        i += 1


# twod1([[1, 2], [3, 4]], 2)


def twod2(lst, k):
    i = 0
    c = len(lst[i]) - 1
    size = len(lst)
    while i < size:

        print("list : ", lst, c, i, lst[i][c])
        if lst[i][c] == k:
            print("found ", k)
            break
        elif k > lst[i][c]:
            i += 1
        elif k < lst[i][c]:
            c -= 1


# twod2([[1, 2], [3, 4]], 3)

lst = [8, 9, 2, 3, 2, 1, 5, 3]


def repeat1(lst):
    i = 0
    found = False
    while i < len(lst) and found == False:
        j = i + 1
        while j < len(lst):
            if lst[j] == lst[i]:
                print("element found : ", lst[i])
                found = True
            j += 1
        i += 1


# repeat1(lst)

def repeat2(lst):
    i = 0
    slst = sorted(lst)
    while i < len(slst) - 1:
        if slst[i] == slst[i + 1]:
            print("element found : ", slst[i])
            break
        i += 1


# repeat2(lst)

def repeat3(lst):
    i = 0
    newlst = {}
    while i < len(lst):
        if lst[i] in newlst:
            newlst[lst[i]] += 1
        else:
            newlst[lst[i]] = 1
        i += 1

    for key, value in newlst.items():
        if value > 1:
            print("element found : ", key)
            break


# repeat3(lst)

l1 = [5, 1, 2, 3, 8]
l2 = [6, 3, 4, 2, 1]
value = 7


def bSearch(l, v):
    low = 0
    high = len(l) - 1

    while low <= high:
        mid = low + math.floor((high - low) / 2)
        if l[mid] == v:
            print('--', mid)
            return True
        elif l[mid] > v:
            high = mid - 1
        else:
            low = mid + 1


# bSearch([1, 2, 3, 4, 6], 2)


# using binary search
def pair3(l1, l2, value):
    import math

    l2s = sorted(l2)
    print('l2s : ', l2s)
    i = 0

    def searchBinary(fval, sval):
        low = 0
        high = len(l2s) - 1

        while low <= high:
            mid = low + math.floor((high - low) / 2)

            if l2s[mid] == sval:
                print("pair is3 : ", fval, sval)
                return True
            elif l2s[mid] > sval:
                high = mid - 1
            else:
                low = mid + 1

    while i < len(l1):
        if (value >= l1[i]):
            sval = value - l1[i]
            searchBinary(l1[i], sval)
            i += 1


# pair3(l1, l2, value)


# using hash
def pair2(l1, l2, value):
    i = 0
    while i < len(l1):
        if l1[i] < value and value - l1[i] in l2:
            print("pair2 is : ", l1[i], value - l1[i])
        i += 1


# pair2(l1, l2, value)


# using brute force technique
def pair1(l1, l2, value):
    i = 0
    while i < len(l1):
        j = 0
        while j < len(l2):
            if l1[i] + l2[j] == value:
                print("pair is : ", l1[i], l2[j])
                j += 1
            else:
                j += 1
        i += 1

        # pair1(l1, l2, value)


def arrangeBinary(arr, size):
    left, right = 0, size - 1

    while left < right:
        # Increment left index while we see 0 at left
        while arr[left] == 0 and left < right:
            left += 1

        # Decrement right index while we see 1 at right
        while arr[right] == 1 and left < right:
            right -= 1

        # If left is smaller than right then there is a 1 at left
        # and a 0 at right. Exchange arr[left] and arr[right]
        if left < right:
            arr[left] = 0
            arr[right] = 1
            left += 1
            right -= 1

    return arr


print(arrangeBinary([0, 1, 0, 1, 0, 1, 0], 7))

'''
https://www.quora.com/anonymous/b20f4383383b495f95875c86a1abfc62

I have 4 years of experience in IT industry, till now I am only able to solve basic problems. I don't have any idea about DS and algo, now I want to learn them but I have no idea that from where should I start. I have read many blogs in which people mentioned that just solve the practice problems. But whenever I try to solve I failed to think about the logic and than I become demotivated. Can some one help me in this regard, whether I should read about DS and algo first and then start solving problems ?
'''

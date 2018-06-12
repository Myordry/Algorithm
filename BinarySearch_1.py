def binarySearch(alist,item):
    first = 0
    last = len(alist) - 1

    while first <= last:
        mid = (first + last) // 2  #地板除，向下取整
        # print(mid)
        if alist[mid] > item:
            last = mid - 1
        elif alist[mid] < item:
            first = mid + 1
        else:
            return mid + 1
    return -1

if __name__ == "__main__":
    li = [0, 1, 2, 8, 13, 17, 19, 32, 42]
    result = binarySearch(li,32)
    print(result)

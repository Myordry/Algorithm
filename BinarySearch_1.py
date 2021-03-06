def binarySearch(myList,key):
    low = 0
    high = len(myList)-1
    time = 0
    while low < high:
        time += 1
        mid = (low+high)//2
        if key<myList[mid]:
            high = mid - 1
        elif key>myList[mid]:
            low = mid + 1
        else:
            print("times:%s"%time)
            return mid
    print("times:%s" % time)
    return False


if __name__ == "__main__":
    li = [0, 1, 2, 8, 13, 17, 19, 32, 42]
    result = binarySearch(li,32)
    print(result)

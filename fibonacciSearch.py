# 斐波那契查找算法
# 时间复杂度O(log(n))

def fibonacciSearch(myList,key):
    #需要一个现成的斐波那契列表。其最大元素的值必须超过查找表中元素个数的数值
    length = len(myList)
    if key<myList[0] or key>myList[-1]:   #查找超出范围
        print("Error！",key,"is not in the myList!")
        return False

    F = [0,1]
    count = 1
    while F[count] < length:     #生成斐波那契数列,此时就满足了F[0] = 0,F[1] = 1,F[2] = 2....
        F.append(F[count-1]+F[count])
        count += 1
    ##上述生成的斐波那契数列F[count]的数目大于数组的长度，分割点为F[count-1]，当增加到F[count]大于length后，
    # 此时count已经是那个比数组长度大且最接近的那个斐波那契数列对应的下标
    # print(F)

    low = F[0]  #查找上下索引范围，一个为0，一个为数组扩展后的个数-1
    high = F[count]-1

    while length<F[count]:   ##补齐数组，每次count长度加1，加到等于F[count]长度了就停止
        myList.append(myList[length-1])
        length += 1

    # print(myList)
    # print(count)

    while low <= high:
        if count < 2:  ##如果count=1，即数组长度为1，则直接返回0即可，不加这个判断返回-1，也对但是不好看
            mid = low
        else:
            mid = low + F[count-1]-1    ##查找的第一个点为F[count]之前的一个值，即F[count1]，考虑下标，所以-1
        if myList[mid] > key:
            high = mid -1
            count = count - 1
        elif myList[mid] < key:
            low = mid + 1
            count = count - 2
        else:
            return mid  #得出的结果为下标值
    return False

myList = [0,1,16,24,35,48,59,62,73,88,99]
print(fibonacciSearch(myList,35))
#4

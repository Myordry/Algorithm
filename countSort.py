def countSort(alist):
    n = len(alist)  ##数组长度
    k = max(alist)   ##数组中最大值
    b = [0 for i in range(n)]
    c = [0 for i in range(k+1)]
    for i in alist:
        c[i] += 1
    for i in range(1,len(c)):
        c[i] = c[i] + c[i-1]
    for i in alist:
        # print(b)
        # print(c)
        b[c[i]-1] = i
        c[i] -= 1   ##处理有相同元素的情况,如果再有这个值的话，位置向后移动一位
    return b

if __name__ == "__main__":
    alist = [1,2,8,3,5,3,2]
    result = countSort(alist)
    print(result)
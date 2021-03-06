def quickSort(myList,start,end):
    # 判断low是否小于high,如果为false,直接返回
    if start >= end:
        return

    i,j = start,end
    #设置基数
    base = myList[i]

    while i < j:
        ##如果列表后边的数,比基准数大或相等,则前移一位直到有比基准数小的数出现
        while i<j and myList[j] >= base:
            j = j - 1
        # 如找到,则把第j个元素赋值给第i个元素,此时表中第i,j个元素相等
        myList[i] = myList[j]
        #交换位置也可以
        # myList[i],myList[j] = myList[j],myList[i]

        # 同样的方式比较前半区
        while i<j and myList[i]<=base:
            i = i + 1
        myList[j] = myList[i]
        # myList[i], myList[j] = myList[j], myList[i]
    # 做完第一轮比较之后,列表被分成了两个半区,并且i=j,需要将这个数设置回base
    myList[i] = base
    # 递归前后半区
    quickSort(myList,start,i - 1)
    quickSort(myList,j + 1,end)

    # return myList,不需要return

if __name__ == "__main__":
    myList = [49, 38, 65, 97, 76, 13, 27, 49]
    quickSort(myList,0,len(myList)-1)
    print(myList)

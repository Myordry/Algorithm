# def insertSort(myList):
#     for i in range(1,len(myList)):
#         if myList[i] < myList[i-1]:
#             temp = myList[i]  #当前需要排序的元素
#             index = i  #记录排序元素需要插入的位置
#             while index>0 and myList[index-1] > temp:
#                 myList[index] = myList[index - 1]  #把已经排序好的元素后移一位，留下需要插入的位置
#                 index -= 1
#             myList[index] = temp  #把需要排序的元素，插入到指定位置

def insertSort(myList):
    #循环的是第二个到最后（待摸的牌）
    for i in range(1,len(myList)):
        #待插入的数（摸上来的牌）
        min  = myList[i]
        #已排好序的最右边一个元素（手里的牌的最右边）
        j = i - 1
        # 一直和排好的牌比较，排好的牌的牌的索引必须大于等于0
        # 比较过程中，如果手里的比摸上来的大，
        while j >= 0 and myList[j] > min:
            #那么手里的牌往右边移动一位，就是把j付给j+1
            myList[j+1] = myList[j]
            #换完以后在和下一张比较
            j -= 1
        #找到了手里的牌比摸上来的牌小或等于的时候，就把摸上来的放到它右边
        myList[j+1] = min


if __name__ == "__main__":
    myList = [49, 38, 65, 97, 76, 13, 27, 49]
    insertSort(myList)
    print(myList)

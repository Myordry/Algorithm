def selectSort(myList):
    for i in range(0,len(myList)-1):  #注意i,j下标的范围
        index = i
        for j in range(i+1,len(myList)):  ##完成对后面所有数的循环，找到最小的那个值，赋给index
            if myList[index] > myList[j]:
                index = j
        myList[i],myList[index] = myList[index],myList[i]

if __name__ == "__main__":
    myList = [3, 4, 1, 6, 2, 9, 7, 0, 8, 5]
    selectSort(myList)
    print(myList)


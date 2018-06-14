# 最基础的遍历无序列表的查找算法
# 时间复杂度O(n)
def unorderedSearch(myList,key):
    for i in range(len(myList)):
        if myList[i] == key:
            return i
    else:
        return False

if __name__ == "__main__":
    myList=[1, 5, 8, 123, 22, 54, 7, 99, 300, 222]
    print(unorderedSearch(myList,22))

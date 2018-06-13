##考虑下限版本
def bucketSort_1(myList):
    buckets = [0]*((max(myList) - min(myList))+1)
    for i in range(len(myList)):
        buckets[myList[i] - min(myList)] += 1   #考虑了下限，为了与下标对应，减去最小值
    res = []
    for i in range(len(buckets)):
        if buckets[i] != 0:
            res += [i+min(myList)]*buckets[i]   #考虑了下限，故为了与原数组对应，所以要加上最小值，此时i即为值
    return res

##不考虑下限版本
def bucketSort_2(myList):
    #选择一个最大的数
    max_num = max(myList)
    #创建一个元素全是0的列表, 当做桶
    bucket = [0]*(max_num+1)
    #把所有元素放入桶中, 即把对应元素个数加一
    for i in myList:
        bucket[i] += 1

    #存储排序好的元素
    sort_nums = []
    #取出桶中的元素
    for j in range(len(bucket)):
        if bucket[j] != 0:
            sort_nums += [j]*bucket[j]
            # for y in range(bucket[j]):
            #     sort_nums.append(j)
    return sort_nums

##0~1均匀分布的桶排序,每个桶中用插入排序
def insertSort(myList):
    if len(myList) <= 1:
        pass
    # 循环的是第二个到最后（待摸的牌）
    for i in range(1, len(myList)):
        # 待插入的数（摸上来的牌）
        min = myList[i]
        # 已排好序的最右边一个元素（手里的牌的最右边）
        j = i - 1
        # 一直和排好的牌比较，排好的牌的牌的索引必须大于等于0
        # 比较过程中，如果手里的比摸上来的大，
        while j >= 0 and myList[j] > min:
            # 那么手里的牌往右边移动一位，就是把j付给j+1
            myList[j + 1] = myList[j]
            # 换完以后在和下一张比较
            j -= 1
        # 找到了手里的牌比摸上来的牌小或等于的时候，就把摸上来的放到它右边
        myList[j + 1] = min

def bucketSort_uniform(nums):
    s = [[] for i in range(len(nums))]  ##列表中的元素为列表，即每个桶中有几个数据
    for i in nums:
        s[int(i*len(nums))].append(i)  ##将每个数据放到对应的桶i*len(nums)为其位置（0~1范围内的排序）
    for i in s:
        insertSort(i)  ##对每个桶中的数据进行排序
    return [i for j in s for i in j]


if __name__ == "__main__":
    nums1 = [0.6,0.4,0.1,0.6,0.45]
    print(bucketSort_uniform(nums1))

    # [0.1, 0.4, 0.45, 0.6, 0.6]

    nums = [5,6,3,2,1,65,2,0,8,0]
    print(bucketSort_1(nums))
    print(bucketSort_2(nums))

    # [0, 0, 1, 2, 2, 3, 5, 6, 8, 65]
    # [0, 0, 1, 2, 2, 3, 5, 6, 8, 65]

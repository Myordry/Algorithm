def bubbleSort(nums):
    for i in range(len(nums) - 1):   # 这个循环负责设置冒泡排序进行的次数，循环n-1次
        # print(nums)
        current_status = False
        for j in range(len(nums) - i - 1):  # ｊ为列表下标,每循环一次，最后一个均为排好的,所以减去i
            if nums[j] > nums[j+1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                current_status = True

        if not current_status:
            break

    return nums

if __name__ == "__main__":
    nums = [1, 6, 2, 10, 6, 98, 45]
    print(bubbleSort(nums))






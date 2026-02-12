def selectionSort(nums):
    for i in range(len(nums)):
        minpos = i
        for j in range(i,len(nums)):
            if nums[j]<nums[minpos]:
                minpos = j
        temp = nums[i]
        nums[i] = nums[minpos]
        nums[minpos] = temp

nums = [1,10,2,9,3,8,4,7,5,6]
selectionSort(nums)
print(nums)
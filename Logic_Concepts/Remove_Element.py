def removeElement(nums, val):
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k
nums = [2,2,3,4,5,1]
k= removeElement(nums, 2)
print(k, nums[:k])
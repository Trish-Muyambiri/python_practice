def two_sum(nums, target):

    if len(nums) < 2:
        return -1

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return[nums[i], nums[j]]

    return -1


print(two_sum([1, 2, 3, 4, 5, 6, 7], 8))

nums = [1, 1, 2]
target = 3

def twoSumTwo(nums, target):
    l, r = 0, len(nums) - 1

    while l < r:
        if nums[l] + nums[r] == target:
            return [l+1, r+1]
        elif nums[l] + nums[r] > target:
            r -=1
        elif nums[l] + nums[r] < target:
            l +=1

# Runtime O(n)
def twoSumTwo1(nums, target):
        n = len(nums)
        nums_map = {}
        for i in range(n):
            complement = target - nums[i]
            if complement in nums_map:
                return [nums_map[complement] + 1, i + 1]
            nums_map[nums[i]] = i



print(twoSumTwo1(nums, target))
class Solution(object):
    def twoSum(self, nums, target):
        checkednum = {}
        for i in range(len(nums)):
            num2 = target-nums[i]
            if num2 in checkednum:
                return i, checkednum[num2]
            checkednum[nums[i]] = i
        return 0,0

        
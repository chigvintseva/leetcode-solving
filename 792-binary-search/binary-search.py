class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        ans = -1
        for i in range(len(nums)):
            if nums[i] == target:
                ans = i
        return ans
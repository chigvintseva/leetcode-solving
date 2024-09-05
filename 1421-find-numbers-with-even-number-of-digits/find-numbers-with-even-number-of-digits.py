class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        answ = 0
        for i in range(len(nums)):
            digits =[int(x) for x in str(nums[i])]
            sum=0
            for digit in digits:
                sum += 1
            if sum%2==0:
                answ +=1
        return answ


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        strx = str(x)
        reversedx = strx[::-1]
       
        return strx == reversedx
        
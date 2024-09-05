class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        NumBinList = [int(x) for x in bin(num)[2:]]
        newNumBinList = [1 if x == 0 else 0 for x in NumBinList]
        newNumBin = "".join(str(x) for x in newNumBinList)
        newNum = int(newNumBin, 2)
        return newNum
        



        
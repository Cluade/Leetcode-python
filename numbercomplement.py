class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        return int(bin(num)[2:].replace('0','x').replace('1','0').replace('x','1'),2)
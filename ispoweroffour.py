class Solution:
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        bar = 1
        for i in range(16):
            if bar == num:
                return True
            bar *=4
        return False
                    
    def isPowerOfFour2(self, num):
        return num>0 and num&(num-1)==0 and len(bin(num)[3:])%2==0
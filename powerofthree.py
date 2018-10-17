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
            bar *=3
        return False
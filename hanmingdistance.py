class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        hmd = 0
        cnt = x ^y 
        for i in range(32):
            hmd += (cnt >>i) & 1
        return hmd
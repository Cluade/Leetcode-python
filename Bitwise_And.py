class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        result = n
        for i in range(m,n):
            result &= i
        return result

    ##why it shows runtime error on leetcode
    
    
    def rangeBitwiseAnd2(self, m, n):
        while m<n:
            n &= n-1
            print(n)
        return n

    
test=Solution()
test.rangeBitwiseAnd2(2,10)
import unittest
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        for i in range(32):
            result+= (n>>i)&1
        return result

    def hammingWeight2(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        for i in range(32):
            result+= n&1
            n >>= 1
        return result
n = 11
obj = Solution()
print(obj.hammingWeight2(1))

class Testsolution(unittest.TestCase):
    def test1(self):
        n = 11
        obj = Solution()
        self.assertEqual(obj.hammingWeight(n),3)

if __name__=='__main__':
    unittest.main()
    
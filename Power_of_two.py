import unittest
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <1:
            return False
        while (n&1 == 0):
            n >>=1
        return n == 1
        
class test(unittest.TestCase):
    def test1(self):
        obj = Solution()
        self.assertEqual(obj.isPowerOfTwo(2),True)

if __name__ == "__main__":
    unittest.main()
    
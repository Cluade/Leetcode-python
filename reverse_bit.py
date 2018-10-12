import unittest
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        result = 0
        for i in range(32):
            result <<= 1
            result |= n & 1
            n >>= 1
        return result

class Testsolution(unittest.TestCase):
    def test1(self):
        n = 43261596
        obj = Solution()
        self.assertEqual(obj.reverseBits(n),964176192)

if __name__=='__main__':
    unittest.main()
    
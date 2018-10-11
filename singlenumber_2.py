class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        b = 0

        for i in nums:
            b = b^i&~a
            print(b)
            a = a^i&~b
            print(a)
        return a|b

test = Solution()
test.singleNumber([5,5,5,1])
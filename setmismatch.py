class Solution:
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = sum(range(len(nums)+1)) -sum(nums)
        loc = collections.Counter(nums).most_common(1)[0][0]
        return loc, loc+res

class Solution2:
    def findErrorNums(self, nums):
        duplicated = sum(nums)-sum(set(nums))
        missing =  sum(range(len(nums)+1)) -sum(nums)
        return duplicated, duplicated+missing
        
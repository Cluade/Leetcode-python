class Solution:
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in range(0,len(nums)):
            for j in range(i,len(nums)):
                if res < nums[i]^nums[j]:
                    res = nums[i]^nums[j]
        return res


test = Solution()
print(test.findMaximumXOR([3, 10, 5, 25, 2, 8]))

    
class Solution1(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        best = 0
        mask = 0
        for i in range(32,-1,-1):
            mask = mask | (1<<i)
            s = {n & mask for n in nums}
            guess = best | (1<<i)
            for prefix in s:
                if guess ^ prefix in s:
                    best = guess
                    break
        return best

class Solution2(object):
    def findMaximumXOR(self, nums):
        mx =0 
        mask = 0
        for i in range(32, -1, -1):
            prob_mx = mx | (1<<i)
            mask = mask | (1<<i)
            bits = set()
            for num in nums:
                bits.add(num & mask)
            for bit in bits:
                if bit ^ prob_mx in bits:
                    mx = prob_mx
                    break
        return mx


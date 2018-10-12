class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        for i in range(len(nums)):
            if i != nums[i]:
                return i
        return len(nums)
    
    def missingNumber2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_set = set(nums)
        for i in range(len(nums)+1):
            if i not in num_set:
                return i
    

    def missingNumber3(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        l = len(nums)
        s = sum(nums)
        
        return l*(l+1)//2 - s

test = Solution()
print(test.missingNumber([1,0,3]))
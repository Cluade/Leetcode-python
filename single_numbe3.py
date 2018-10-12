class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        no_dulpilate_list=[]
        for i in nums:
            if i not in no_dulpilate_list:
                no_dulpilate_list.append(i)
            else:
                no_dulpilate_list.remove(i)
        return no_dulpilate_list

test = Solution()
print(test.singleNumber([2,2,3,3,1,5]))
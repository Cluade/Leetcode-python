import unittest

# number 136 

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
        return no_dulpilate_list.pop()

class Solution1(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        has_table = {}
        for i in nums:
            try:
                has_table.pop(i)
            except:
                has_table[i] = 1
        return has_table.popitem()[0]

class Solution_math(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        for i in nums:
            a^= i
        return a



#number 137

class Sol(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = int(0)
        for i in range(32):
            #在i位上的1个数
            count = int(0)
            for j in range(len(nums)):
                count+= (nums[j]>>i)&1
        result+= (count%3)<<i
        return result
nums = [1,1,12,2,2,5,5]
obj = Solution_math() 
print(obj.singleNumber(nums))

class Testsolution(unittest.TestCase):
    def test1(self):
        nums = [1,1,12,2,2,5,5]
        obj=Solution() 
        self.assertEqual( obj.singleNumber(nums), 12)
    def test2(self):
        nums = [1,1,12,2,2,5,6]
        obj=Solution() 
        self.assertTrue( obj.singleNumber(nums) in [12,5,6])

class Testsolution2(unittest.TestCase):
    def test1(self):
        nums = [1,1,12,2,2,5,5]
        obj=Solution1() 
        self.assertEqual( obj.singleNumber(nums), 12)
    def test2(self):
        nums = [1,1,12,2,2,5,6]
        obj=Solution1() 
        self.assertTrue( obj.singleNumber(nums) in [12,5,6])

class Testsolution3(unittest.TestCase):
    def test1(self):
        nums = [1,1,12,2,2,5,5]
        obj=Solution_math() 
        
        self.assertEqual( obj.singleNumber(nums), 12)
    def test2(self):
        nums = [1,1,12,2,2,5,6]
        obj=Solution_math() 
        self.assertTrue( obj.singleNumber(nums) in [12,5,6])

if __name__ == '__main__':
    unittest.main()
    
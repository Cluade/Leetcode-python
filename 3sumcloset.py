
from itertools import combinations

class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        dist = combinations(nums,3)
        res = 4294967296
        ans = 0
        for i in dist:
            if abs(sum(i) - target) < res:
                res = abs(sum(i) - target)
                ans = sum(i)
        return ans
        

class Solution:
    def threeSumClosest(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    closest = None
    nums.sort()
    for k in range(len(nums)-2):
        l,r = k+1,len(nums)-1
        while l < r:
            s = nums[k]+nums[l]+nums[r]
            if closest is None or abs(target-s) < abs(closest-target):
                closest = s

    return closest

class Solution:
    def threeSumClosest(self, nums, target):
        closet = sum(nums[:3])
        nums.sort()
        for i in range(len(nums-2)):
            k, l = i+1, len(nums)-1
            while k<l:
                diff = target - (nums[k]+nums[l]+nums[i])
                if abs(diff) < abs(target-closet):
                    closet = nums[k]+nums[l]+nums[i]
                if diff < 0:
                    k +=1
                elif diff >0:
                    l -=1
                else:
                    return closet
        return closet


class Solution:
    def threeSumClosest(self, nums, target):
        mindiff = target - sum(nums[:3])
        nums.sort()
        for i in range(len(nums)-2):
            l = i+1
            r = len(nums)-1

            while l < r:
                diff = target - nums[i] - nums[l] - nums[r]
                if abs(diff) <= abs(mindiff): 
	                mindiff = diff
	
                if diff > 0:
	                l += 1
                elif diff < 0:
	                r -= 1
                else:
	                return target

        return target - mindiff
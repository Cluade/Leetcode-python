class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        N, result = len(nums), []
        for i in range(N):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = nums[i]*-1
            s,e = i+1, N-1
            while s<e:
                if nums[s]+nums[e] == target:
                    result.append([nums[i], nums[s], nums[e]])
                    s = s+1
                    while s<e and nums[s] == nums[s-1]:
                        s = s+1
                elif nums[s] + nums[e] < target:
                    s = s+1
                else:
                    e = e-1
        return result


from itertools import combinations
class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        cl = combinations(nums,3)
        answer = []
        for i in cl:
            if sum(i) == 0:
                temp = sorted(list(i)) 
                if temp not in answer:
                    answer.append(temp)
        return answer

class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        from bisect import bisect_left, bisect_right
        m = {}
        result = []
        # 记录每个数字出现的次数
        for n in nums:
            if n in m:
                m[n] += 1
            else:
                m[n] = 1
        # 如果数组中出现三个以上0
        if 0 in m and m[0] >= 3:
            result.append([0, 0, 0])

        # 获取所有的数字，并排序
        keys = list(m.keys())
        keys.sort()
        print(keys)
        keys_num = len(keys)
        if keys_num == 0:
            return []

        # a<b<c。a一定小于0，c一定大于0

        # a的取值范围
        end = bisect_left(keys, 0)  # a < 0
        begin = bisect_left(keys, -keys[-1] * 2)  
        # when b == c, a + b + c = a + 2c <= a + 2*max_c;
        for i in range(begin, end):
            a = keys[i]

            # when a == b, then 2a = c
            if a != 0 and m[a] >= 2 and -2 * a in m:
                result.append([a, a, -2 * a])
            
            # b的取值范围
            # -a - b = c <= keys[-1] >>>> b >= -keys[-1] - a
            min_b = -keys[-1] - a
            # b<c >>>> a + 2b < a + b + c = 0 >>>> b < -a/2
            max_b = -a / 2

            b_begin = max(i + 1, bisect_left(keys, min_b))  # b的最小值
            b_end = bisect_right(keys, max_b)  # b的最大值
            #			print('a = {}, {} <= b < {}, in [{}:{}]'.format(a, min_b, max_b, b_begin, b_end))
            for j in range(b_begin, b_end):
                b = keys[j]
                #				print('key[{}] = {}, key[{}] = {}'.format(i, a, j, b))
                c = -a - b
                if c in m and b <= c:
                    if b < c or m[b] >= 2:
                        result.append([a, b, c])
        return result
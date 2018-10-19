from itertools import permutations
from itertools import combinations

class Solution:
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        hs = [0,0,0,0]
        ms = [0,0,0,0,0,0]
        for i in range(num):
            for idex in range(i+1):
                hs[idex]=1
                #print(hs)
                hsls = product(hs, 4)
           
                for idex in range(num-i-1):
                    ms[idex] = 1         
                    msls = product(ms,6)    

        for content in hsls:
            print(content) 
        for content in msls:
            print(content)      
            
test  = Solution()
test.readBinaryWatch(1)


class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        if num > 8: return []
        
        hours = {i: [] for i in range(4)} # 0 - 11
        for i in range(12):
            count = 0
            value = i
            while value > 0:
                if value % 2 == 1:
                    count += 1
                value = value >> 1
            hours[count].append(i) 
        
        
        minutes = {i: [] for i in range(6)} # 0 - 59
        for i in range(60):
            count = 0
            value = i
            while value > 0:
                if value % 2 == 1:
                    count += 1
                value = value >> 1
            minutes[count].append(i)

            
        res = []  
        beg = max(num - 5, 0)
        end = min(3, num) + 1
        for i in range(beg, end):
            j = num - i
            for h in hours[i]:
                for m in minutes[j]:
                   
                    res.append('%d:%02d' % (h, m))
        return res
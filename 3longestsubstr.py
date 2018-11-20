class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        arr = list(s)
        sequence = []
        longestSequence = 0
        
        for i in arr:
            if i not in sequence:
                sequence.append(i)
            else:
                sequence = sequence[sequence.index(i) + 1:]
                sequence.append(i)
            
            longestSequence = max(longestSequence, len(sequence))
            
        return longestSequence

s= "pwwkew"
test = Solution()
test.lengthOfLongestSubstring(s)

class Solution2(object):
    def if_duplicate(self,substr):
        sequence  = []
        for i in substr:
            if i not in sequence:
                sequence.append(i)
            else:
                return False
            return True
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxcount = 0
        same_flag = 0
        print(len(s))
        for i in range(0,len(s)):
            for inx in range(len(s)-i):
                if self.if_duplicate(s[inx:inx+i]):
                    maxcount = i
                    same_flag = 1
            if same_flag == 0:
                return maxcount
            else:
                same_flag = 0

test = Solution2()
test.lengthOfLongestSubstring(" ")
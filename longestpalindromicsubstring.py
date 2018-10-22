class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dicts = {}
        maxlength = start = 0
        maxstring = []
        substring =''
        for i,value in enumerate(s):
            if value in dicts:
                sums = dicts[value] + 1
                if sums > start:
                    start = sums
                maxstring.append(value)
                substring = "".join(maxstring)
                maxstring = []
            maxstring.append(value)
            num = i - start + 1
            if num > maxlength:
                maxlength = num
            dicts[value] = i
        return substring

#test = Solution()
#test.lengthOfLongestSubstring("babad")

class Solution2:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == '':
            return 0
        slist = list(s)
        sameflag = 0
        clist =set()
        cont =0
        mxstring =[]
        substring =''
        for i in range(len(slist)):
            j =i
            sameflag = 0 
            cont = 0
            clist = set()
            while not sameflag:
                try:
                    if slist[j] in clist:
                        sameflag = 1
                        if len(substring)<len(mxstring)+1:
                            mxstring.append(slist[j])
                            substring = "".join(mxstring)
                            mxstring = []
                    else:
                        clist.add(slist[j])
                        mxstring.append(slist[j])
                        j +=1
                        cont = cont +1
                except:
                    break
        return substring

# solution 3 is the only correct one.
class Solution3:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s: return s
        if len(s) ==1: return s
        res = (0, 0)        # To store start and ending index for the longest palindromic substring
        global_max = 1      
        for i in range(len(s)-1):
            j,k = i-1, i+1
            curmax = 1
            while j>=0 and k<len(s):
                if s[j] == s[k]:
                    curmax +=2
                    j -= 1
                    k += 1
                    #res=(j,k)
                else:
                    break
            if curmax >= global_max:
                global_max = curmax
                res = (j+1, k-1)
        
        for i in range(len(s)):
            j, k = i, i+1
            curmax = 0
            while j>=0 and k<len(s):
                if s[j] == s[k]:
                    curmax +=2
                    j-=1
                    k+=1
                    #res=(j,k)
                else:
                    break
            if curmax >global_max:
                global_max = curmax
                res =(j+1, k-1)

        return s[res[0]:res[1]+1]
                        
                        

test = Solution3()
print(test.longestPalindrome("aaaa"))
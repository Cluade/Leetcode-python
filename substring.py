class Solution:
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
        mxcont =0
        mxindex =len(s)-1
        for i in range(len(slist)):
            j =i
            sameflag = 0 
            cont = 0
            clist = set()
            while not sameflag:
                try:
                    if slist[j] in clist:
                        sameflag = 1
                    else:
                        clist.add(slist[j])
                        j +=1
                        cont = cont +1
                except:
                    break
            if mxcont< cont:
                mxcont = cont
        return mxcont

class Solution2:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dicts = {}
        maxlength = start = 0
        for i,value in enumerate(s):
            if value in dicts:
                sums = dicts[value] + 1
                if sums > start:
                    start = sums
            num = i - start + 1
            if num > maxlength:
                maxlength = num
            dicts[value] = i
        print(dicts)
        return maxlength

test = Solution2()
print(test.lengthOfLongestSubstring("pwwkew"))
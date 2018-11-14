class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        orderflag = 0
        dlist = []
        carry = 0
        for i in range(numRows):
            dlist.append([])
        for i, item in enumerate(s):
            if orderflag == 0:
                if carry!=0:
                    dlist[i%numRows+1].append(item)
                    carry =0
                else:
                    dlist[i%numRows].append(item)
            else:
                if carry!=0:
                    dlist[numRows - i%numRows-1-1].append(item)
                    carry =0
                else:
                    dlist[numRows - i%numRows-1].append(item)
            if i%numRows == numRows-1:
                orderflag = ~orderflag
                #carry = ~carry
        string = []
        for i in dlist:
        print(string)
                
                  
            
            
test = Solution()
test.convert('PAYPALISHIRING',3)


class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        l = len(s)
        ans = ""
        if numRows == 1:
            return s
        for i in range(numRows):
            if i % (numRows - 1) == 0:
                j = i
                while j < l:
                    ans += s[j]
                    j += 2 * (numRows - 1)
            else:
                j = i
                flag = 0
                while j < l:
                    ans += s[j]
                    j += ((2 * (numRows - 1)) - 2 * i if flag == 0 else 2 * i)
                    flag = not(flag)
        return ans

class Solution:
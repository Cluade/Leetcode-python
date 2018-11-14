class Solution:
    def myAtoi(self, stru):
        """
        :type str: str
        :rtype: int
        """
        rev = ''
        flag = 0
        if stru =='-' or stru =='+':
            return 0
        for i in range(len(stru)):
            if stru[i] ==' ':
                continue
            elif (stru[i] =='-' or stru[i] =='+') and flag ==0:
                rev +=stru[i]
                flag = 1
            elif (stru[i] =='-' or stru[i] =='+') and flag ==1:
                rev = '0'
                break
            elif stru[i].isdigit():
                rev += stru[i]
            else:
                break 
        if rev == '' or rev =='-' or rev =='+':
            rev = '0'
        if int(rev) > 2147483647:
            return 2147483647
        elif int(rev) < -2147483648:
            return -2147483648
        else:
            return int(rev)

test = Solution()
test.myAtoi("+-2")
class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        snum = str(x)
        length = len(str(x))-1
        rev = []
        while length >=0:
            rev.append(snum[length])
            length -=1
        if "".join(rev) == str(snum):
            return True
        else:
            return False

test = Solution()
test.isPalindrome(121)
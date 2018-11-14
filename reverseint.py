
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sx = str(x)
        if x < 0:
            rev = '-'
            j = len(sx) - 1
            while j > 0:
                rev = rev + sx[j]
                j -= 1
        elif x> 0:
            rev = ''
            j = len(x) -1 
            while j >=0:
                rev = rev +sx[j]
                j -= 1
        else:
            return x
            rn = int(rev)
            if rev > 2147483647 or rev < - 2147483648:
                rn =0
        return rn
                



test = Solution()
print(test.reverse(-123))
class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        dp =[[0 for i in range(n)] for j in range(n)]
        maxdp = 0
        #print(dp)
        for i in range(n):
            for j in range(i,n):
                dp[i][j]=(j-i)*min(height[i],height[j])
                if dp[i][j] > maxdp:
                    maxdp = dp[i][j]
        return maxdp

class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        start = 0
        end = len(height)-1
        curcon = 0
        maxcon = 0
        while start<end:
            if height[end]>height[start]:
                curcon = (end-start)*height[start]
                start +=1
            else:
                curcon = (end-start)*height[end]
                end -=1
            if curcon > maxcon:
                maxcon = curcon
        return maxcon
            



test = Solution()
test.maxArea([1,2,3])
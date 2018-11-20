class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix)==0:
            return False
        m =  len(matrix)
        n = len(matrix[0])
        r = 0
        c = n-1
        while(r < m and c>=0):
            if matrix[r][c] < target:
                r +=1
            elif matrix[r][c] > target:
                c -=1
            else:
                return True
        return False
test = Solution()
test.searchMatrix([[1]],1)
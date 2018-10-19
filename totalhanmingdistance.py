class Solution:
    def totalHammingDistance(self, nums):
        dist = [[0,0] for _ in range(32) ]
        for num in nums:
            for i in range(32):
                dist[i][num%2] +=1
                x =int(num/2)
        return sum(x*y for x, y in dist)

for i in range(5):
    print(i)
    
class Solution():
    def partition(self,A, s, e):
        pivot = A[e-1]
        i = s-1
        for t in range(s,e):
            if A[t]< pivot:
                i +=1
                A[i], A[t] =A[t],  A[i]
        if A[e-1]< A[i+1]:
            A[i+1], A[e-1] =A[e-1], A[i+1]
        return i+1
    def quicksort(self, A, lo, hi):
        P = self.partition(A, lo, hi)
        self.quicksort(A, lo, P)
        self.quicksort(A, P+1, hi)
numlist = [1,5,3,2,6,7,8,10]
test = Solution()
test.quicksort(numlist, 0, len(numlist))
            
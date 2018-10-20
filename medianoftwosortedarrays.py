class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        max_int = 0xffffffff
        min_int = 0x00000000
        n1 = len(nums1)
        n2 = len(nums2)
        N = n1+n2
        cl = 0
        cr = n1
        cut1 = int(n1/2)
        cut2 = int(N/2 -cut1)
        if n1 > n2:
            return self.findMedianSortedArrays(nums2,nums1)
        while cut1<=n1:
            cut1 = int((cr-cl)/2+cl)
            print(cut1)
            cut2 = int(N/2 -cut1)
            print(cut2)
            L1 = min_int if cut1 ==0 else nums1[cut1-1]
            L2 = min_int if cut2 ==0 else nums2[cut2-1]
            R1 = max_int if cut1 ==n1 else nums1[cut1]
            R2 = max_int if cut2 ==n2 else nums2[cut2]
            
            if L1 > R2 :
                cr = cut1 -1
            elif L2 > R1:
                cl = cut1 +1
            else:
                if N%2 == 0:
                    L1 = max(L1, L2)
                    R1 = min(R1, R2)
                    return (L1+R1)/2
                else:
                    return min(R1,R2)
                

test= Solution()
print(test.findMedianSortedArrays([1, 3],[2]))
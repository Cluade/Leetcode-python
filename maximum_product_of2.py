class Solution:
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        "misunderstand the problem this actually return maxproduct of same lenth"
        num_list = []
        for i in words:
            num_list.append(len(i))
        num_list.sort(reverse=True)
        for i in range(len(words)):
            try:
                if num_list[i] == num_list[i+1]:
                    return num_list[i]*num_list[i]
            except:
                return 0
        #i = len(words)
        #while num_list[i] != num_list[i-1]:
            #i -= 1
        
        #return num_list[i]*num_list[i-1]
    
    def maxProduct2(self, words):
        d = {}
        for w in words:
            mask = 0
            for c in set(w):
                mask |= (1 << (ord(c) - 97))
            d[mask] = max(d.get(mask, 0), len(w))
        return max([d[x] * d[y] for x in d for y in d if not x & y] or [0])

test = Solution()
print(test.maxProduct(["abcw","baz","foo","bar","xtfn","abcdef"]))
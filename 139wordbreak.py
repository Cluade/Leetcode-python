class Solution(object):
    def dfs(self, s, now, d, have):
        if now >= len(s):
            return True
        if have[now] == True:
            return False
        have[now] = True
        for i in range(now, len(s)):
            if (s[now:i+1] in d) and self.dfs(s, i+1, d, have):
                return True
        return False
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        have = []
        for i in range(len(s)):
            have.append(False)
        return self.dfs(s, 0, wordDict, have)
            
test = Solution()
#test.wordBreak("leetcode",["leet","code"])

class Solutionn2(object):
    def bfs(self, s, d, have):
        have[0] = True
        queque = []
        queque.append(0)
        while queque:
            now = queque.pop(0)
            for i in range(now, len(s)):
                if s[now:i+1] in d:
                    if i+1>=len(s):
                        return True
                    if have[i+1] == False:
                        have[i+1] = True
                        queque.append(i+1)
        return False
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        have = []
        for i in range(len(s)):
            have.append(False)
        return self.bfs(s, wordDict, have)

class Solution3(object):
    def dp(self, s, d, have):
        dpc =[]
        for i in range(len(s)):
            dpc.append(False)
        if len(s)==0:
            return True
        dpc[0] = True
        have[0] = True
        for now in range(0,len(s)):
            if dpc[now] == False:
                continue
            for i in range(now, len(s)):
                if s[now:i+1] in d:
                    if i+1>=len(s):
                        return True
                    dpc[i+1] = True
        return False
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        have = []
        for i in range(len(s)):
            have.append(False)
        return self.dp(s, wordDict, have)   

test = Solution3()
test.wordBreak("leetcode",["leet","code"])
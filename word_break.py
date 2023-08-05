class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [True] + [False] * len(s)

        for i in range(1, len(s) + 1):
            for w in wordDict:
                if i - len(w) >= 0 and dp[i - len(w)] and s[:i].endswith(w):
                    dp[i] = True
                    break
        return dp[-1]
        # for i in wordDict:
        #     if i in s:
        #         s=s.replace(i,"")
        #     else:
        #         return False
        # return True

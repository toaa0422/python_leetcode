# bfs
class Solution:    #待续中
    def wordBreak(self,s,wordDict):
        from collections import deque
        st={*wordDict}
        print(st)
        n=len(s)
        q=deque([0])
        visited=[0 for _ in range(len(s))]
        while q:
            start=q.popleft()
            for end in range(start+1,n+1):
                if s[start:end] in st and visited[start]==0:
                    if end==len(s):
                        return True
                    q.append(end)
            visited[start]=1
        return False
# python3 动态规划
class Solution_:      #有错误 略
    def wordBreak(self,s,wordDict):
        dp=[True,s[0] in wordDict]
        print(dp)
        for i in range(1,len(s)):
            for j in range(i+1):
                if s[j:i+1] in wordDict and dp[j]:
                    dp.append(True)
                    break
                else:
                    dp.append(False)
        return dp[-1]
class Solution1:    #yes
    def wordBreak(self, s: str, wordDict) -> bool:
        n=len(s)
        dp=[False]*(n+1)
        dp[0]=True
        for i in range(n):
            for j in range(i+1,n+1):
                if(dp[i] and (s[i:j] in wordDict)):
                    dp[j]=True
        print(dp)
        return dp[-1]


# 直接带备忘回溯/记忆化回溯
import functools
class Solution__:    #****   未深入了解 带备忘回溯
    # class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        import functools
        @functools.lru_cache(None)
        def back_track(s):
            if (not s):
                return True
            res = False
            for i in range(1, len(s) + 1):
                if (s[:i] in wordDict):
                    res = back_track(s[i:]) or res
            return res

        return back_track(s)



sol=Solution__()
print(sol.wordBreak('hello','hello'))
print(sol.wordBreak(s = "applepenapple", wordDict = ["apple", "pen"]))
print(sol.wordBreak(s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]))

wordDict = ["apple", "pen"]





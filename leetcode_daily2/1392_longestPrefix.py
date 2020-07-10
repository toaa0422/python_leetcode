class Solution:
    def longestPrefix(self, s: str) -> str:
        ans=''
        l=len(s)
        for i in range(l):
            if s[:i]==s[l-i:]:
                ans=s[:i]
        return ans




    def find1(slef,s):
        res = ""
        for i in range(1, len(s)):
            if s[i - 1] == s[-1] and s[:i] == s[-i:]:
                res = s[:i]
        return res
sol=Solution()
print(sol.longestPrefix(s = "level"))
print(sol.find1(s = "level"))

class Solution:
    # sort+brute force
    def findAnagrams(self, s: str, p: str):
        n=len(p)
        p=''.join(sorted(p))
        res=[]
        for i in range(len(s)-n+1):
            if ''.join(sorted(s[i:i+n]))==p:
                res.append(i)
        return res

    # 前缀和 + 哈希
    def findAnagrams2(self, s: str, p: str):
        from collections import Counter
        n = len(p)
        p = Counter(p)
        dp = [0] * (len(s) + 1)
        dp[0] = Counter()
        res = []
        for i in range(1, len(s) + 1):
            dp[i] = dp[i - 1].copy()
            dp[i][s[i - 1]] += 1
            if i >= n and dp[i] - dp[i - n] == p:
                res.append(i - n)
        return res


        # 滑动窗口
    def findAnagrams1(self, s: str, p: str):
        p_count=[0]*26
        s_count=[0]*26
        res=[]
        for a in p:
            p_count[ord(a)-97]+=1
        left=0
        for right in range(len(s)):
            if right<len(p)-1:
                s_count[ord(s[right])-97]+=1
                continue
            s_count[ord(s[right])-97]+=1
            if p_count==s_count:
                res.append(left)
            s_count[ord(s[left])-97]-=1
            left+=1
        return res

sol=Solution()
print(sol.findAnagrams(s="cbaebabacd" ,p="abc"))
print(sol.findAnagrams2(s="cbaebabacd" ,p="abc"))
print(sol.findAnagrams1(s="cbaebabacd" ,p="abc"))


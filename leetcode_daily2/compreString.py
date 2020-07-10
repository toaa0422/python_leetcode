class Solution:
    def compressString(self, S: str) -> str:
        if not S:
            return ""
        ch = S[0]
        ans = ''
        cnt = 0
        for c in S:
            if c == ch:
                cnt += 1
            else:
                ans += ch + str(cnt)
                ch = c
                cnt = 1
        ans += ch + str(cnt)
        return ans if len(ans) < len(S) else S

def compressString(S: str) -> str:
    cs=' '
    i=0
    for j in S:
        if j!=cs[-1]:
            cs+=str(i)+j
            i=1
        else:
            i+=1
    return cs[2:]+str(i) if len(cs)-2<len(S)-1 and i!=0 else S

def compressString_(s):
    if not s:
        return s
    res=s[0]
    cnt=0
    for index in s:
        if index!=res[-1]:
            res+=str(cnt)+index
            cnt=1
        else:
            cnt+=1
    res+=str(cnt)
    return res if len(res)<len(s) else s


x=Solution()

s="aabcccccaaa"
print(x.compressString(s))
print(compressString(s))
print(compressString_(s))

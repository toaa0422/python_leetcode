class Solution():
    def LongestCommonPrefix(self,strs):
        if not strs:
            return
        s1=min(strs)
        s2=max(strs)
        for i,x in enumerate(s1):
            if x!=s2[i]:
                return s2[:i]
        return s1
class Solution2():
    def LongestCommonPrefix(self,strs):
        if not strs:
            return
        for i in range(len(strs[0])):
            s=strs[0][i]
            for j in range(1,len(strs)):
                if i==len(strs[j]) or strs[j][i]!=s:
                    return strs[0][0:i]
        return strs[0]


s=Solution2()
x=(["flower","flow","flight"])
x1=["dog","racecar","car"]
x2=[]
print(x2)
print(s.LongestCommonPrefix(x2))
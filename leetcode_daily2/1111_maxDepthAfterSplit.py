class Solution:
    def maxDepthAfterSplit(self,seq):
        ans=[]
        d=0
        for c in seq:
            if c=='(':
                d+=1
                ans.append(d%2)
            if c==')':
                ans.append(d%2)
                d-=1
        return ans

class Solution_:
    def maxDepthAfterSplit(self,seq):
        ans=list()
        for i,ch in enumerate(seq):
            if ch=='(':
                ans.append(i%2)
            else:
                ans.append(1-i%2)
        return ans

s=Solution()
str="((((((())))))))))))))))))))))))))))"
print(len(str))
print(s.maxDepthAfterSplit(str))
ss=Solution()
print(ss.maxDepthAfterSplit(str))
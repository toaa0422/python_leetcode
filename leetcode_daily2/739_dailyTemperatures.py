class Solution:
    def dailyTemperatyres(self,t):
        res=[0]*len(t)
        stack=[]
        for i in range(len(t)):
            while stack and t[stack[-1]]<t[i]:
                small=stack.pop()
                res[small]=i-small
            stack.append(i)
        return res

sol=Solution()
print(sol.dailyTemperatyres([1,2,3,8,10]))
#栈    stack
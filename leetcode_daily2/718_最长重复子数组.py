import numpy as np
class Solution:
    # 动态规划  yes
    def findLength(self,A,B):
        n,m=len(A),len(B)
        dp=[[0]*(m+1) for _ in range(n+1)]
        # print(np.array(dp))
        ans=0
        # for i in range(n-1,-1,-1):
        #     for j in range(m-1,-1,-1):
        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                dp[i][j]=dp[i+1][j+1]+1 if A[i]==B[j] else 0
                # print(np.array(dp))
                ans=max(ans,dp[i][j])
                # print()
        # print('-------------')
        # print(np.array(dp))
        return ans

    # 滑动窗口 sliding windows    ****
    def findLength_(self,A,B):
        def maxLength(addA,addB,length):
            ret=k=0
            for i in range(length):
                if A[addA+i]==B[addB+i]:
                    k+=1
                    ret=max(ret,k)
                else:k=0
            return ret
        n,m=len(A),len(B)
        ret=0
        for i in range(n):
            length=min(m,n-i)
            ret=max(ret,maxLength(i,0,length))
        for i in range(m):
            length=min(n,m-i)
            print(length)
            ret=max(ret,maxLength(0,i,length))
        return ret
    #方法3   二分查找+哈希   be neglected













sol=Solution()
A=[1,2,3,2,1]
B=[3,2,1,4,7]

x=[1,2,3]
print(sol.findLength(x,x))
# print(sol.findLength_(x,x))

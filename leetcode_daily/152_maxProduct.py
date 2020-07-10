class Solution:
    def maxProduct(self,nums):
        n=len(nums)
        max_dp=[1]*(n+1)
        min_dp=[1]*(n+1)
        ans=float('-inf')
        for i in range(1,n+1):
            max_dp[i]=max(max_dp[i-1]*nums[i-1],min_dp[i-1]*nums[i-1],nums[i-1])
            min_dp[i]=min(max_dp[i-1]*nums[i-1],min_dp[i-1]*nums[i-1],nums[i-1])
            ans=max(ans,max_dp[i])
        return ans

#optimization
# 当我们知道动态转移方程的时候，其实应该发现了。我们的dp[i] 只和 dp[i - 1]有关，
# 这是一个空间优化的信号，告诉我们可以借助两个额外变量记录即可。
class Solution_:
    def maxProduct(self,nums):
        n=len(nums)
        a=b=1
        ans=float('-inf')
        for i in range(1,n+1):
            tmp=a
            a=max(a*nums[i-1],b*nums[i-1],nums[i-1])
            b=min(tmp*nums[i-1],b*nums[i-1],nums[i-1])
            ans=max(ans,a)
        return ans

sol=Solution_()
x=[2,3,-2,4]
print(sol.maxProduct(x))
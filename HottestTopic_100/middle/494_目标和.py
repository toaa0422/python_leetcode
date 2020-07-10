class Solution:  #待续  2020/7/7
    # 01背包
    def findTargetSumWays(self, nums, S: int) -> int:
        if sum(nums)<S or (sum(nums)+S)%2==1:return 0
        P=(sum(nums)+S)//2
        dp=[1]+[0 for _ in range(P)]
        for num in nums:
            for j in range(P,num-1,-1):
                dp[j]+=dp[j-num]
                print(dp)
        return dp[P]
    # dynamic planning    其实本质上就是没有使用递归的dfs
    def findTargetSumWays_(self, nums, S: int) -> int:
        length, dp = len(nums), {(0, 0): 1}
        for i in range(1, length + 1):
            for j in range(-sum(nums), sum(nums) + 1):
                dp[(i, j)] = dp.get((i - 1, j - nums[i - 1]), 0) + dp.get((i - 1, j + nums[i - 1]), 0)
        return dp.get((length, S), 0)
    #     length,dp=len(nums),{(0,0):1}
    #     for i in range(1,length+1):
    #         for j in range(-sum(nums),sum(nums)+1):
    #             dp[(i,j)]=dp.get((i-1,j-nums[i-1],0)+dp.get((i - 1, j + nums[i-1]), 0)
    #     return dp.get((length, S), 0)


sol=Solution()
print(sol.findTargetSumWays([1,1,1,1,1],3))
print(sol.findTargetSumWays_([1,1,1,1,1],3))


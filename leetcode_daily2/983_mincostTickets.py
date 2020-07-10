# 方法一：记忆化搜索（日期变量型）
from functools import lru_cache
class Solution:
    def mincostTickets(self,days,costs=[2,7,15]):
        dayset=set(days)
        durations=[1,7,30]
        @lru_cache(None)
        def dp(i):
            if i>365:return 0
            elif i in dayset:
                return min(dp(i+d)+c for c,d in zip(costs,durations))
            else:
                return dp(i+1)
        return dp(1)
# 方法二：记忆化搜索（窗口变量型）
class Solution_:
    def mincostTickets(self,days,costs=[2,7,15]):
        N=len(days)
        durations=[1,7,30]
        def dp(i):
            if i>=N:
                return 0
            ans=10**9
            j=i
            for c,d in zip(costs,durations):
                while j<N and days[j]<days[i]+d:
                    j+=1
                print(j)
                ans=min(ans,dp(j)+c)
            return ans
        return dp(0)

#网友解
#简单易懂

class Solution__:
    def mincostTickets(self, days, costs=[2,7,15]) -> int:
        """
        :param days:  List[int]
        :param costs:  List[int]
        :return: int
        """
        dp = [0 for _ in range(days[-1] + 33)]  #为了负数索引---------------33
        days_idx = 0  # 设定一个days指标，标记应该处理 days 数组中哪一个元素
        a=costs[0]
        b=costs[1]
        c=costs[2]
        size=days[-1]+1
        start=days[0]

        for i in range(start, size):          #万一6月1号之前不开学，我天天去学校，不对。优化
            #不用集合，少了一次O(len(days))
            if i != days[days_idx]:  # 若当前天数不是待处理天数，则其花费费用和前一天相同
                dp[i] = dp[i - 1]
            else:
                # 若 i 走到了待处理天数，则从三种方式中选一个最小的
                dp[i] = min(dp[i - 1] + a ,
                            dp[i - 7] + b ,
                            dp[i -30] + c )
                days_idx += 1
        return dp[days[-1]]  # 返回-------那天，就那天，




class Solution___:
    def mincostTickets(self, days: list, costs=[2,7,15]) -> int:
        # dp[i]是直到第i天的累积票价
        dp = [0] * len(days)
        # 边界条件
        dp[0] = min(costs)
        x1,x2,x3=[],[],[]
        for k in range(1, len(dp)):
            # 所买票 满足1天
            tmp_costs_1 = dp[k - 1] + min(costs)
            # 所买票 满足7天
            x1.append(tmp_costs_1)
            tmp = 0
            for p in range(k):
                if days[k] - days[p] >= 7:
                    tmp = dp[p]  # 7天票覆盖不到的那些天，使用已经解决过的dp，是赋值=，而不是+=，因为dp本来就是累加的
            tmp_costs_7 = tmp + min(costs[1], costs[2])
            x2.append(tmp_costs_7)
            # 所买票 满足30天
            tmp = 0
            for p in range(k):
                if days[k] - days[p] >= 30:
                    tmp = dp[p]
            tmp_costs_30 = tmp + costs[2]
            x3.append(tmp_costs_30)

            dp[k] = min(tmp_costs_1, tmp_costs_7, tmp_costs_30)
        print(x1,x2,x3)
        return dp[-1]


sol=Solution()
print(sol.mincostTickets([1,4,6,7,8,20]))
# print(sol.mincostTickets([1,2,3,4,5,6,7,8,9,10,30,31]))


# durations=[1,7,30]
# costs=[2,7,30]
# for x in zip(durations,costs):
#     print(x)

"""
        # 1. dp问题: dp(i) = min(
        #         dp(i+1) + costs[0],
        #         dp(i+7) + costs[1],
        #         dp(i+30) + costs[2])
        # 2. 用到了lru_cache缓存技术
"""
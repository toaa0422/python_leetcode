class Solution:
    def maxProfit(self, prices) -> int:
        n=len(prices)
        if n==0:return 0
        sell=[0 for _ in range(n)]
        buy=[0 for _ in range(n)]
        cool=[0 for _ in range(n)]
        buy[0]=-prices[0]
        for i in range(1,n):
            sell[i]=max(buy[i-1]+prices[i],sell[i-1])
            buy[i]=max(cool[i-1]-prices[i],buy[i-1])
            cool[i]=max(sell[i-1],buy[i-1],cool[i-1])
        print(sell)
        print(buy)
        print(cool)
        return sell[-1]

import numpy as np
class Solution_:
    def maxProfit(self, prices) -> int:
        n = len(prices)
        if not n or n < 2:
            return 0
        dp = [[0, 0] for i in range(n)]  # dp的初始化

        dp[0][0] = 0  # 第0天不持股自然就为0了
        dp[0][1] = -prices[0]  # 第0天持股，那么价格就是-prices[0]了
        # 第1天不持股，要么第0天就不持股，要么就是第0天持股，然后第1天卖出
        dp[1][0] = max(dp[0][0], dp[0][1] + prices[1])
        # 第一天持股，要么就是第0天就持股了，要么就是第0天不持股第1天持股
        dp[1][1] = max(dp[0][1], dp[0][0] - prices[1])
        print(np.array(dp))
        for i in range(2, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 2][0] - prices[i])
        print(np.array(dp))
        return dp[-1][0]


sol=Solution_()
print(sol.maxProfit([1,2,3,0,2]))




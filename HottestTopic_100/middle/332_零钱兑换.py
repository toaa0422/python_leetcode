class Solution:
    # dynamic planning    自上而下
    def coinChange(self, coins, amount: int):
        import functools
        @functools.lru_cache(amount)
        def dp(rem):
            if rem < 0: return -1
            if rem == 0: return 0
            mini = int(1e9)
            for coin in self.coins:
                res=dp(rem-coin)
                if res>=0 and res<mini:
                    mini=res+1
            return mini if mini<int(1e9) else -1
        self.coins=coins
        if amount<1:return 0
        return dp(amount)

    # 动态规划：自下而上
    def coinChange_(self, coins, amount: int) -> int:
        dp=[float('inf')]*(amount+1)
        dp[0]=0
        for coin in coins:
            for x in range(coin,amount+1):
                dp[x]=min(dp[x],dp[x-coin]+1)
        return dp[amount] if dp[amount]!=float('inf') else -1
sol=Solution()
print(sol.coinChange(coins = [1, 2, 5], amount = 11))
print(sol.coinChange_(coins = [1, 2, 5], amount = 11))










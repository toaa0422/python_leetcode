class Solution:
    def new21Game(self,N,K,W):
        if K==0:return 1.0
        dp=[0.0]*(K+W+1)
        for i in range(K,min(N,K+W-1)+1):
            dp[i]=1.0
        for i in range(K-1,-1,-1):
            for j in range(1,W+1):
                dp[i]+=dp[i+j]/W
        return dp[0]
class Solution__:
    def new21Game(self, N: int, K: int, W: int) -> float:
        if K == 0:
            return 1.0
        dp = [0.0] * (K + W + 1)
        for i in range(K, min(N, K + W - 1) + 1):
            dp[i] = 1.0
        dp[K - 1] = float(min(N - K + 1, W)) / W
        for i in range(K - 2, -1, -1):
            dp[i] = dp[i + 1] - (dp[i + W + 1] - dp[i + 1]) / W
        return dp[0]
class Solution_:
    def new21Game(self,N,W,K):
        if K==0:return 1.0
        dp=[0.0]*(K+W+1)
        for i in range(K,min(N,K+W-1)+1):
            dp[i]=1.0
        dp[K-1]=float(min(N-K+1,W))/W
        for i in range(K-2,-1,-1):
            dp[i] = dp[i + 1] - (dp[i + W + 1] - dp[i + 1]) / W
            # dp[i]=dp[i+1]-(dp([i+W+1])-dp[i+1])/W
        return dp[0]

# nb
class Solution_nb:
    def new21Game(self,N,K,W):
        dp=[None]*(K+W)
        x=[None]*(K+W)

        s=0
        for i in range(K,K+W):
            dp[i] = 1 if i <= N else 0
            # dp[i]=1 if i<=N else 0
            s+=dp[i]
            x[i]=s
        print(dp)
        # print(x)
        # print(s)
        for i in range(K-1,-1,-1):
            dp[i]=s/W
            s=s-dp[i+W]+dp[i]
            print(s)
        print(dp)
        # print(s)
        return dp[0]


sol1=Solution()
sol2=Solution_nb()
# print(sol1.new21Game(10,1,10))
# print(sol2.new21Game(10,1,10))
print(sol2.new21Game(21,17,10))



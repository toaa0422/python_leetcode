"""
dp
recursion
"""
import numpy as np
class Solution:
    #dynamic planning    yes
    def minPathSum(self, grid) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == j == 0:
                    continue
                elif i == 0:
                    grid[i][j] = grid[i][j - 1] + grid[i][j]
                elif j == 0:
                    grid[i][j] = grid[i - 1][j] + grid[i][j]
                else:
                    grid[i][j] = min(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]
        print(np.array(grid))
        return grid[-1][-1]
    # dynamic planning 自顶向上
    def minPathSum_(self, grid) -> int:
        if not grid: return 0
        row = len(grid)
        col = len(grid[0])
        dp = [[0] * col for _ in range(row)]
        dp[0][0] = grid[0][0]
        # 第一行
        for j in range(1, col):
            dp[0][j] = dp[0][j - 1] + grid[0][j]
        # 第一列
        for i in range(1, row):
            dp[i][0] = dp[i - 1][0] + grid[i][0]

        for i in range(1, row):
            for j in range(1, col):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        return dp[-1][-1]
    def minPathSum__(self,grid):
        import functools
        if not grid:return 0
        row=len(grid)
        col=len(grid[0])
        @functools.lru_cache(None)
        def helper(i,j):
            if i==row-1 and j==row-1:
                return grid[i][j]
            if i>=row or j>=col:
                return float('inf')
            tmp=0
            tmp+=grid[i][j]+min(helper(i,j+1),helper(i+1,j))
            return tmp
        return helper(0,0)




sol=Solution()
x=[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
print(sol.minPathSum(x))
# print(sol.minPathSum_(x))
# print(sol.minPathSum__(x))


import numpy as np
class Solution:
    # 方法一: 暴力算法  time complexity:C(N**2M**3)
    # 方法二: 动态规划 - 使用柱状图的优化暴力方法
    # 上述方法本质上是84 - 柱状图中最大的矩形题中优化暴力算法的复用。
    def maximalRectangle(self, matrix) -> int:
        maxarea=0
        dp=[[0]*len(matrix[0]) for _ in range(len(matrix))]
        print(np.array(dp))

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '0': continue
                width = dp[i][j] = dp[i][j - 1] + 1 if j else 1

                # compute the maximum area rectangle with a lower right corner at [i, j]
                for k in range(i, -1, -1):
                    width = min(width, dp[k][j])
                    maxarea = max(maxarea, width * (i - k + 1))
        print(np.array(dp))

        return maxarea

    # 方法三：使用柱状图 - 栈   待续
    # 方法四：动态规划 - 每个点的最大高度  待续












x=[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
sol=Solution()
print(sol.maximalRectangle(x))

import numpy as np
import collections
class Solution():
    def updateMatrix(self,matrix):
        m, n = len(matrix), len(matrix[0])
        dist=[[0]*n for i in range(m)]
        print(np.array(dist))
        print("---------------------")
        zeroes_pos=[(i,j) for i in range(m) for j in range(n) if matrix[i][j]==0]
        q=collections.deque(zeroes_pos)
        seen=set(zeroes_pos)
        while q:
            i,j=q.popleft()
            for ni,nj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0<=ni<m and 0<=nj<n and (ni,nj) not in seen:
                    dist[ni][nj] = dist[i][j] + 1
                    print(np.array(dist))
                    q.append((ni,nj))
                    seen.add((ni,nj))
        print("---------------------")
        return np.array(dist)


        # return np.array(dist)

class Solution__:
    def updateMatrix(self, matrix):
        m, n = len(matrix), len(matrix[0])
        # 初始化动态规划的数组，所有的距离值都设置为一个很大的数
        dist = [[10**9] * n for _ in range(m)]
        # 如果 (i, j) 的元素为 0，那么距离为 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    dist[i][j] = 0
        # 只有 水平向左移动 和 竖直向上移动，注意动态规划的计算顺序
        for i in range(m):
            for j in range(n):
                if i - 1 >= 0:
                    dist[i][j] = min(dist[i][j], dist[i - 1][j] + 1)
                if j - 1 >= 0:
                    dist[i][j] = min(dist[i][j], dist[i][j - 1] + 1)
        # 只有 水平向左移动 和 竖直向下移动，注意动态规划的计算顺序
        for i in range(m - 1, -1, -1):
            for j in range(n):
                if i + 1 < m:
                    dist[i][j] = min(dist[i][j], dist[i + 1][j] + 1)
                if j - 1 >= 0:
                    dist[i][j] = min(dist[i][j], dist[i][j - 1] + 1)
        # 只有 水平向右移动 和 竖直向上移动，注意动态规划的计算顺序
        for i in range(m):
            for j in range(n - 1, -1, -1):
                if i - 1 >= 0:
                    dist[i][j] = min(dist[i][j], dist[i - 1][j] + 1)
                if j + 1 < n:
                    dist[i][j] = min(dist[i][j], dist[i][j + 1] + 1)
        # 只有 水平向右移动 和 竖直向下移动，注意动态规划的计算顺序
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i + 1 < m:
                    dist[i][j] = min(dist[i][j], dist[i + 1][j] + 1)
                if j + 1 < n:
                    dist[i][j] = min(dist[i][j], dist[i][j + 1] + 1)
        return dist

#method  :对上面的优化
class Solution___:
    def updateMatrix(self, matrix):
        m, n = len(matrix), len(matrix[0])
        # 初始化动态规划的数组，所有的距离值都设置为一个很大的数
        dist = [[10 ** 9] * n for _ in range(m)]
        # 如果 (i, j) 的元素为 0，那么距离为 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    dist[i][j] = 0
        # 只有 水平向左移动 和 竖直向上移动，注意动态规划的计算顺序
        for i in range(m):
            for j in range(n):
                if i - 1 >= 0:
                    dist[i][j] = min(dist[i][j], dist[i - 1][j] + 1)
                if j - 1 >= 0:
                    dist[i][j] = min(dist[i][j], dist[i][j - 1] + 1)
        # 只有 水平向右移动 和 竖直向下移动，注意动态规划的计算顺序
        for i in range(m)[::-1]:
            for j in range(n)[::-1]:
        # for i in range(m - 1, -1, -1):
        #     for j in range(n - 1, -1, -1):
                if i + 1 < m:
                    dist[i][j] = min(dist[i][j], dist[i + 1][j] + 1)
                if j + 1 < n:
                    dist[i][j] = min(dist[i][j], dist[i][j + 1] + 1)
        return dist


s=Solution___()
arr=[[0 ,0 ,0],
[0 ,1 ,0],
[1 ,1 ,1],]

print(np.array(s.updateMatrix(arr)))
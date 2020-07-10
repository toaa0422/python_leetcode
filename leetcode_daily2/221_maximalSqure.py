#maximal
class Solution:
    def maximalSquare(self,matrix):
        if len(matrix)==0 or len(matrix[0])==0:
            return 0
        maxSide=0
        row,col=len(matrix),len(matrix[0])
        for i in range(row):
            for j in range(col):
                print(f'i={i},j={j}>>{maxSide}')
                if matrix[i][j]=='1':
                    maxSide=max(maxSide,1)
                    currentMaxSide=min(row-i,col-j)
                    for k in range(1,currentMaxSide):
                        flag=True
                        if matrix[i+k][j+k]=='0':
                            break
                        for m in range(k):
                            if matrix[i+k][j+m]=='0' or matrix[i+m][j+k]=='0':
                                flag=False
                                break
                        if flag:
                            maxSide=max(maxSide,k+1)
                            # print(maxSide)
                        else:break
        maxSquare=maxSide**2
        return maxSquare
class Solution_:
    def maximalSquare(self,matrix):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0

        maxSide = 0
        rows, columns = len(matrix), len(matrix[0])
        dp = [[0] * columns for _ in range(rows)]
        for i in range(rows):
            for j in range(columns):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                        print(f'if{i},{j}={dp[i][j]}')
                    else:
                        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                        print(f'else{i},{j}={dp[i][j]}')
                    maxSide = max(maxSide, dp[i][j])
        print(np.array(dp))
        maxSquare = maxSide * maxSide
        return maxSquare
import numpy as np
x=[['1','0','1','0','0'],
   ['1','0','1','1','1'],
   ['1','1','1','1','1'],
   ['1','0','0','1','0'],]
# print(np.array(x))
sol=Solution()
print(sol.maximalSquare(x))


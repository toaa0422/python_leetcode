import numpy as np
class Solution:
    #转置加翻转
    def rotate(self, matrix):
        n=len(matrix[0])
        for i in range(n):
            for j in range(i,n):
                matrix[j][i],matrix[i][j]=matrix[i][j],matrix[j][i]
                # print(i,j)
                # print(np.array(matrix))
        for i in range(n):
            matrix[i].reverse()
        return matrix
    #旋转四个矩形  略
    def rotate_(self, matrix):
        n = len(matrix[0])
        for i in range(n // 2 + n % 2):
            for j in range(n // 2):
                tmp = [0] * 4
                row, col = i, j
                # store 4 elements in tmp
                for k in range(4):
                    tmp[k] = matrix[row][col]
                    row, col = col, n - 1 - row
                # rotate 4 elements
                for k in range(4):
                    matrix[row][col] = tmp[(k - 1) % 4]
                    row, col = col, n - 1 - row
        return matrix

    def rotate__(self, matrix):

        n = len(matrix[0])
        for i in range(n // 2 + n % 2):
            for j in range(n // 2):
                tmp = matrix[n - 1 - j][i]
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - j - 1]
                matrix[n - 1 - i][n - j - 1] = matrix[j][n - 1 - i]
                matrix[j][n - 1 - i] = matrix[i][j]
                matrix[i][j] = tmp
        return matrix

class Solution_: #详解
    def rotate(self,matrix):
        pos1,pos2=0,len(matrix)-1
        while pos1<pos2:
            add=0
            while add<pos2-pos1:
                temp=matrix[pos2-add][pos1]
                matrix[pos2][pos2-add]=matrix[pos1+add][pos2]
                matrix[pos1+add][pos2]=matrix[pos1][pos1+add]
                matrix[pos1][pos1+add]=temp
                add+=1
            pos1+=1
            pos2-=1
        return matrix



matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
sol=Solution_()
print(np.array(sol.rotate(matrix)))

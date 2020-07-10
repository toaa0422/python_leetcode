import numpy as np

#method 1 :需要用到辅助数组（auxiliary space）
class Solution1:
    def rotate(self, matrix):
        n = len(matrix)
        # Python 这里不能 matrix_new = matrix 或 matrix_new = matrix[:] 因为是引用拷贝
        matrix_new = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                matrix_new[j][n - i - 1] = matrix[i][j]
        # 不能写成 matrix = matrix_new
        matrix[:] = matrix_new
        return matrix


#method 2
"""
temp                        = matrix[row][col]                
matrix[row][col]            =      matrix[n−col−1][row]            
matrix[n−col−1][row]        =         matrix[n−row−1][n−col−1]       
matrix[n−row−1][n−col−1]    =          matrix[col][n−row−1]       
matrix[col][n−row−1]        =                temp         
"""
class Solution2:
    def rotate(self, matrix) -> None:
        """
        : List[List[int]]
        :param matrix:
        :return:
        """
        n = len(matrix)
        for i in range(n // 2):
            for j in range((n + 1) // 2):
                matrix[i][j], matrix[n - j - 1][i], matrix[n - i - 1][n - j - 1], matrix[j][n - i - 1] \
                    = matrix[n - j - 1][i], matrix[n - i - 1][n - j - 1], matrix[j][n - i - 1], matrix[i][j]
        return matrix

# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/rotate-matrix-lcci/solution/xuan-zhuan-ju-zhen-by-leetcode-solution/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

#method 3:用翻转代替旋转
class Solution3:
    def rotate(self, matrix):
        n=len(matrix)
        for i in range(n//2):
            for j in range(n):
                # matrix[i][j], matrix[n - i - 1][j]= matrix[n - i - 1], matrix[i][j]  #attention to a minor detail:
                matrix[i][j], matrix[n - i - 1][j] = matrix[n - i - 1][j], matrix[i][j]
        for i in range(n):
            for j in range(i):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]

        return matrix



# arr=np.arange(1,13)
# arr.shape=(3,4)
# print(arr)




x=[
  [1,2,3],
  [4,5,6],
  [7,8,9],
]

x_=np.array(x)
print(x_)
s=Solution3()
print(s.rotate(x_))

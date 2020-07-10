import numpy as np
class Solution:
    # 考察python内置函数技巧

    def spiralOrder(self, matrix):
        res = []

        print(np.array(matrix))
        while matrix:
            res += matrix.pop(0)
            matrix = list(map(list, zip(*matrix)))[::-1]
            print(np.array(matrix))
        return res








x=[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
xx=[[1,2],[3,4]]
sol=Solution()
print(sol.spiralOrder(x))
# print(np.array(list(map(list, zip(*xx)))[::-1]))
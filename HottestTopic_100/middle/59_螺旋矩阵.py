class Solution:
    # python内置技巧  待续
    def generateMatrix(self, n: int) :
        r, n = [[n**2]], n**2
        while n > 1: n, r = n - len(r), [[*range(n - len(r), n)]] + [*zip(*r[::-1])]
        return r


class Solution1:
    def generateMatrix(self, n: int):
        def rotation(matrix):
            return list(zip(*matrix[::-1]))

        r, n = [[n ** 2]], n ** 2
        while n > 1:
            new = [list(range(n - len(r), n))]
            rot = rotation(r)
            n -= len(r)
            r = new + rot
        return r

    def generateMatrix1(self, n: int) :

        def rotation(matrix):
            return list(zip(*matrix[::-1]))

        def iterate(r, n):
            if n == 1:
                return r
            else:
                new = list(range(n - len(r), n))
                rot = rotation(r)
                return iterate([new] + rot, n - len(r))

        return iterate([[n ** 2]], n ** 2)
sol=Solution1()
import numpy as np
print(np.array(sol.generateMatrix(10)))
print(np.array(sol.generateMatrix1(10)))
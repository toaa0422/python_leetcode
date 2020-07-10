"""surface area 表面积"""
class Solution_(object):
    def surfaceArea(self, grid):
        N = len(grid)
        ans = 0
        for r in range(N):
            for c in range(N):
                if grid[r][c]:
                    ans += 2
                    for dx, dy in ((r-1, c), (r+1, c), (r, c-1), (r,c+1)):  #技巧,依次读取
                        #print(f"nr:{dx},nc:{dy}")
                        if 0 <= dx < N and 0 <= dy < N:
                            nval = grid[dx][dy]
                        else:
                            nval = 0

                        ans += max(grid[r][c] - nval, 0)
        return ans

class Solution:
    def surfaceArea(self, grid) -> int:
        import numpy
        N=len(grid)
        def S(L):
            Sum=0
            for i in L:
                Last=0
                for j in i:
                    Sum+=abs(j-Last)
                    Last=j
                Sum+=Last
            return Sum
        return S(numpy.array(grid).T)+S(grid)+numpy.sign(grid).sum()*2
s=Solution()
print(s.surfaceArea([[2]]))
s=Solution_()
print(s.surfaceArea([[1,2],[3,4]]))
#for x,y in (1,2),(3,4),(5,6):
#    print(f"x:{x},y:{y}")


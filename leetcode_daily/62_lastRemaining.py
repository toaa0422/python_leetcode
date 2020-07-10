# Python 默认的递归深度不够，需要手动设置
import sys
sys.setrecursionlimit(100000)

def f(n, m):
    if n == 0:
        return 0
    x = f(n - 1, m)
    return (m + x) % n     #不考虑溢出   考虑的话  (n%m + x) % n

class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        return f(n, m)
s=Solution()
print(s.lastRemaining(5,3))

class Solution_:
    def lastRemaining(self, n: int, m: int) -> int:
        x = 0
        for i in range(2, n + 1):
            x = (m + x) % i
        return x

s=Solution_()
print(s.lastRemaining(5,3))
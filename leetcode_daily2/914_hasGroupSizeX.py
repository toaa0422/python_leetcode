"""
has Group size x
deck:   ***一副（为 52 张）
n. 甲板；行李仓；露天平台
vt. 装饰；装甲板；打扮
"""
class Solution__:
    def hasGroupsSizeX(self, deck) -> bool:
        """
        #: List[int]
        :param deck:
        :return:
        """
        D = {}
        for x in deck:
            D[x] = D.setdefault(x, 0) + 1
        a = []
        for v in D.values():
            a.append(v)
        gcd = a[0]
        for i in range(1, len(a)):
            gcd = math.gcd(gcd, a[i])
        if gcd == 1:
            return False
        return True










from functools import reduce
import collections
import fractions
import math
class Solution_(object):
    def hasGroupsSizeX(self, deck):
        vals=collections.Counter(deck).values()
        return reduce(math.gcd,vals)>=2

class Solution(object):
    def hasGroupsSizeX(self, deck):
        count = collections.Counter(deck)
        N = len(deck)
        for X in range(2, N+1):
            if N % X == 0:
                if all(v % X == 0 for v in count.values()):
                    return True
        return False

s=Solution()
print(s.hasGroupsSizeX([1,1,1,1]))
S=Solution_()
print(S.hasGroupsSizeX([0,0,0,1,1,1,2,2,2]))












"""
import collections


s=[1,1,2,2,3,3]
count=collections.Counter(s)
print(count)
x=len(s)
for i in range(2,7):
    print(f'{x} % {i}={x%i}')

if all(v % 6 == 0 for v in [2,2,2]):
   print(1)


"""
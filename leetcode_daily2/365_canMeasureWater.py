import math
#裴蜀定理
def canMeasureWater(x,y,z):
    if x+y<z:
        return False
    if x==0 or y==0 :
        return x==z or x+y==z
    return z%(math.gcd(x,y))==0

class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        if x+y<z:
            return False
        if x==0 or y==0:
            return x==z or y==z or  x+y==z   #>>>>1 0 0
        g=math.gcd(x,y)
        if not g:   #0 0 1   1 0 0 也拿来测试..
            return False
        return z%g==0
def canMeasureWater_(x,y,z):
    return x + y >= z and (z == 0 or y and z % math.gcd(x, y) == 0)
print(canMeasureWater(2,3,5))
print(canMeasureWater_(2,3,5))
'''gcd  greatest common divisor   最大公倍数'''
'''hcf  highest common factor'''
'''最大公因数，也称最大公约数、最大公因子，指两个或多个整数共有约数中最大的一个'''
'''  3、5 >>>1'''


def gcd(x,y):
    small=x if x<y else y
    for i in range(1,small+1):
        if x%small==0 and y%small==0:
            return small
"""
#lcm lowest common multiple
def lcm(x,y):
    greater=x if x>y else y
    while 1:
        if ((greater % x == 0) and (greater % y == 0)):
            lcm=greater
            break
        greater+=1
    return lcm

print(lcm(3,6))
print(lcm(54,24))
"""

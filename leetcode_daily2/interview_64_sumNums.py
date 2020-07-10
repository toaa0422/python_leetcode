class Solution:
    def sumNums(self,n):
        return n if n==0 else n+self.sumNums(n-1)


# 因为and这个逻辑运算的本质是——如果A&&B，A为false，B是不计算的；只有当A为true，才会继续计算B
class Solution_s:
    def sumNums(self, n: int) -> int:
        return n != 0 and n + self.sumNums(n -1)


class Solution_:
    def sumNums(self,n):
        return sum(range(n+1))
class Solution__:
    def __init__(self):
        self.res=0
    def sumNums(self,n):
        n>1 and self.sumNums(n-1)
        self.res+=n
        return  self.res

class Solution_1:
    # / **
    # *负数在参与位运算时使用的是补码
    # *-1
    # 的原码是
    # 10000000
    # 00000000
    # 00000000
    # 00000001
    # *-1
    # 的反码是
    # 11111111
    # 11111111
    # 11111111
    # 11111110
    # *-1
    # 的补码是
    # 11111111
    # 11111111
    # 11111111
    # 11111111
    # *因此任何数与 - 1
    # 做与运算的结果任然为原数
    # * /

    def sumNums(self,n):
        n1 = (n & -(n + 1 >> 0 & 1)) << 0
        n2 = (n & -(n + 1 >> 1 & 1)) << 1
        n3 = (n & -(n + 1 >> 2 & 1)) << 2
        n4 = (n & -(n + 1 >> 3 & 1)) << 3
        n5 = (n & -(n + 1 >> 4 & 1)) << 4
        n6 = (n & -(n + 1 >> 5 & 1)) << 5
        n7 = (n & -(n + 1 >> 6 & 1)) << 6
        n8 = (n & -(n + 1 >> 7 & 1)) << 7
        n9 = (n & -(n + 1 >> 8 & 1)) << 8
        n10 = (n & -(n + 1 >> 9 & 1)) << 9
        n11 = (n & -(n + 1 >> 10 & 1)) << 10
        n12 = (n & -(n + 1 >> 11 & 1)) << 11
        n13 = (n & -(n + 1 >> 12 & 1)) << 12
        n14 = (n & -(n + 1 >> 13 & 1)) << 13
        return (n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9 + n10 + n11 + n12 + n13 + n14) >> 1

sol=Solution_1()
print(sol.sumNums(10))
from functools import reduce


#位运算   异或运算
# 1、交换律   a^a^b=a    本程序 用其特点(性质)
#
# 2、结合律（即(a^b)^c == a^(b^c)）
#
# 3、对于任何数x，都有x^x=0，x^0=x
#
# 4、自反性 A XOR B XOR B = A xor  0 = A


class Solution:
    def singleNumber(self,nums):
        return reduce(lambda x,y:x^y,nums)


class Solution_:
    def singleNumber(self,nums):
        single_number=0     #初始状态  利用3,4  x^0=0,A xor 0=A
        for num in nums:
            single_number^=num
        return single_number
sol=Solution_()
print(sol.singleNumber([2,1,2,1,3]))
print(sol.singleNumber([5,5,2,1,2,1,3]))
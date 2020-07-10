class Solution:
    def isPalindrome(self,x):
        if x<0 or (x!=0 and x%10==0):
            return False
        revertedNumber=0
        while x>revertedNumber:
            revertedNumber=revertedNumber*10+x%10
            x/=10
            print(f'{revertedNumber},        x={x}')
        print(revertedNumber/10)
        return x==revertedNumber or x==revertedNumber/10
class Solution_:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: # 如果为负数，直接返回 false
            return False
        num = x
        cur = 0
        while num !=0:
            cur = cur*10 + num%10
            num //=10
        return cur == x # 最后比较 数值反转前后是否相等

sol=Solution()
sol_=Solution_()
print(sol.isPalindrome(525))
print(sol_.isPalindrome(525))

import random
# y=0
# while y<10:
#     x = random.randint(1, 1000000)
#     # print(x)
#     if sol.isPalinorome(x):
#         print(f'{x},{sol.isPalinorome(x)}')
#         y += 1
    # else:
    #     print(sol.isPalinorome(x))



# for x in range(1,100):
#     if (x % 10 == 0 ):
#         print(x)
# >>>  10 20 30  40 50 构成不了回文
# 方法一：袖珍计算器算法
# 时间复杂度：0（1），由于内置的exp函数与1og函数一般都很快，
# 我们在这里将其复杂度视为0（1）
class Solution:
    def mySqrt(self,x):
        import math
        if x==0:return 0
        ans=int(math.exp(0.5*math.log(x)))
        return ans+1 if (ans+1)**2<x else ans
# 方法二：二分查找
class Solution_:
    def mySqrt(self,x):
        l,r,ans=0,x,-1
        while l<=r:
            mid=(l+r)//2
            if mid*mid<=x:
                ans=mid
                l=mid+1
            else:r=mid-1
        return ans

# 方法三：牛顿迭代
class Solution__:
    def mySqrt(self,x):
        if x==0:return 0
        C,x0=float(x),float(x)
        while True:
            xi = 0.5 * (x0 + C / x0)
            if abs(x0 - xi) < 1e-7:
                break
            x0=xi
        return int(x0)




sol=Solution()
sol_=Solution_()
sol__=Solution__()
for x in range(1,10):
    print(f'f1_{x}={sol.mySqrt(x)}')
    print(f'f2_{x}={sol_.mySqrt(x)}')
    print(f'f3_{x}={sol__.mySqrt(x)}')

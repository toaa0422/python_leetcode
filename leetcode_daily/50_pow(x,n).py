# 快速幂算法的本质是分治算法
class Solution:
    def myPow(self,x,n):
        def quickMul(N):
            if N==0:return 1.0
            y=quickMul(N//2)
            return y*y if N%2==0 else y*y*x
            # return y**2 if N%2==0 else y**2*x    #OverflowError 溢出错误
        return quickMul(n) if n>=0 else 1.0/quickMul(-n)
# 方法二：快速幂 + 迭代
class Solution_:
    def myPow(self,x,n):
        def quickMul(N):
            ans=1.0
            x_contribute=x
            while N>0:
                if N%2==1:
                    ans*=x_contribute
                x_contribute*=x_contribute
                N//=2
            return ans
        return quickMul(n) if n>=0 else 1.0/quickMul(-n)
sol=Solution_()
print(sol.myPow(2,3))
# a & b 的结果，是未 << 1 的 carry
# a ^ b 是做不带进位的加法，结果更新给 a
# carry >> 1 得到进位数，更新给 b
# 位运算(超时)
class Solution:
    def addBinary(self,a,b):
        # x=int(a,2)
        x,y=int(a,2),int(b,2)
        while y:
            ans=x^y
            carry=(x&y)<<1
            x,y=ans,carry
        return bin(x)[2:]
# 内置函数   二进制转十进制,十进制数相加再转二进制
# 非内置函数  模拟加法过程
class Solution_:
    def addBinary(self, a, b) -> str:
        return bin(int(a,2) + int(b,2))[2:]
    def addBinary_(self,a,b):
        r,p='',0
        d=len(b)-len(a)
        a='0'*d+a
        b='0'*-d+b
        for i, j in zip(a[::-1],b[::-1]):
            s=int(i)+int(j)+p
            r=str(s%2)+r
            p=s//2
        return '1'+r if p else r

#模拟   ****
class Solution__:
    def addBinary(self,a,b):
        res=''
        carry=0
        i=len(a)-1
        j=len(b)-1
        while i>=0 or j>=0 or carry:
            tmp1=int(a[i]) if i>=0 else 0
            tmp2=int(b[j]) if j>=0 else 0
            carry,t=divmod(tmp1+tmp2+carry,2)
            res=str(t)+res
            i-=1
            j-=1
        return res


sol=Solution__()
print(sol.addBinary('1','11'))
print(str(0))



class Solution:
    # 模拟
    def multiply(self, num1: str, num2: str) -> str:
        a=num1[::-1]
        b=num2[::-1]
        print(a)
        print(b)
        res=0
        for i,x in enumerate(a):
            tmp_res=0
            for j,y in enumerate(b):
                tmp_res+=int(x)*int(y)*10**j
            res+=tmp_res*10**i
        return str(res)
sol=Solution()
print(sol.multiply('12','11'))
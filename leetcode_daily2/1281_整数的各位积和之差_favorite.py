# simulate simulation   模拟
class Solution:
    def subtractProductAndSum(self,n):
        add,mul=0,1
        while n>0:
            digit=n%10
            n//=10
            add+=digit
            mul*=digit
        return mul-add
    def subtractProductAndSum_(self, n):
        # return map(int,str(n))
        from functools import reduce
        # return reduce(lambda x,y:x*y,[int(x) for x in str(n)])-reduce(lambda x,y:x+y,[int(x) for x in str(n)])
        return reduce(lambda x, y: x * y, map(int, str(n))) - reduce(lambda x, y: x + y, map(int, str(n)))
        # return reduce(lambda x, y: x * y, [int(x) for x in str(n)]) - reduce(lambda x, y: x + y,[int(x) for x in str(n)])


class Solution1:
    def subtractProductAndSum(self, n: int) -> int:
        tem=1
        sum=0
        for i in str (n):
            tem*=int (i)
            sum+=int(i)
        return tem-sum




sol=Solution()
print(sol.subtractProductAndSum_(233))
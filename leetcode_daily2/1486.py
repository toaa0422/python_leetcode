from functools import reduce
class Solution:
    def xorOperation(self,n,start):
        res=0
        for i in range(n):
            tmp=start+2*i
            print(bin(tmp))
            res^=tmp
        return res
class Solution_:
    def xorOperation(self,n,start):
        return reduce(lambda x,y:x^y,[start+2*i for i in range(n)])
sol=Solution_()
print(sol.xorOperation(5,0))
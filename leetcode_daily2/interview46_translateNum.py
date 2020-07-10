class Solution:
    def translateNum(self,num):
        s=str(num)
        a=b=1
        for i in range(2,len(s)+1):
            tmp=s[i-2:i]
            c=a+b if '10'<=tmp<='25'else a
            b=a
            a=c
        return a

class Solution1:
    def translateNum(self, num: int) -> int:
        s = str(num)
        a = b = 1
        for i in range(2, len(s) + 1):
            tmp = s[i - 2:i]
            c = a + b if "10" <= tmp <= "25" else a
            b = a
            a = c
        return a



class Solution_:
    def translateNum(self,num):

        a=b=1
        y=num%10
        while num!=0:
            num//=10
            x=num%10
            tmp=10*x+y
            c= a+b if 10<=tmp<=25 else a
            a,b=c,a
            y=x
        return a
sol=Solution1()
sol_=Solution_()
print(sol.translateNum(12258))
print(sol_.translateNum(12258))



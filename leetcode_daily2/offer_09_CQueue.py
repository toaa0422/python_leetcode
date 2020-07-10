#双栈  一进一出
class CQueue:
    def __init__(self):
        self.A,self.B=[],[]
    def __str__(self):
        return self.A,self.B
    def appendTail(self,val):
        self.A.append(val)
    def deleteHead(self):
        if self.B:return self.B.pop()
        if not self.A:return -1
        while self.A:
            self.B.append(self.A.pop())
        return self.B.pop()
x=[[]]
sol=CQueue()

x.append(sol.appendTail(3))
print(x)

print(sol.deleteHead())
print(sol.deleteHead())

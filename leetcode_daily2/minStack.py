class MinStack:
    def __str__(self):
        print(f'stack={self.stack}')
        print(f'min_stack={self.min_stack}')
        return

    def __init__(self):
        import math
        self.stack=[]
        self.min_stack=[math.inf]
    def push(self,x):
        self.stack.append(x)
        self.min_stack.append(min(x,self.min_stack[-1]))
    def pop(self):
        self.stack.pop()
        self.min_stack.pop()
    def top(self):
        return self.stack[-1]
    def getMin(self):
        return self.min_stack[-1]
minStack=MinStack()

minStack.push(-2)
print(f'do;minStack.push(-2)')
print(minStack.__str__())

minStack.push(0)
print(f'do;minStack.push(0)')
print(minStack.__str__())

minStack.push(-3)
print(f'do;minStack.push(-3)')
print(minStack.__str__())


print(f'do;minStack.getMin()')
print(minStack.getMin())
print(minStack.__str__())


print(f'do:minStack.pop()')
print(minStack.pop())
print(minStack.__str__())


print(f'do:minStack.top()')
print(minStack.top())
print(minStack.__str__())


print(f'do:minStack.getMin()')
print(minStack.getMin())
print(minStack.__str__())

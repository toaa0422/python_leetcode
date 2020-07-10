#基操
def isHappy(n):
    def get_next(n):
        total_sum=0
        while n>0:
            n,dight=divmod(n,10)
            total_sum+=dight**2
        return total_sum
    seen=set()
    while n!=1 and n not in seen:
        seen.add(n)
        # print(seen)
        n=get_next(n)
    return n==1
#快慢指针
def ishappy_(n):
    def get_next(number):
        total_sum=0
        while number>0:    #细节  n>0  error
            number,dight=divmod(number,10)
            total_sum+=dight**2
        return total_sum
    slow_runner=n
    fast_runner=get_next(n)
    while fast_runner!=1 and slow_runner!=fast_runner:
        slow_runner=get_next(slow_runner)
        fast_runner=get_next(get_next(fast_runner))
    return fast_runner==1


#数学方法
#如果这样做，您会发现只有一个循环：
#   4>16>37>58>89>145>42>20    规律
def isHappy___(n):
    cycle_members={4,16,37,58,89,145,42,20}
    def get_next(number):
        total_sum=0
        while number>0:
            number,dight=divmod(number,10)
            total_sum+=dight**2
        return total_sum
    while n!=1 and n not in cycle_members:
        n=get_next(n)
    return n==1
# print(isHappy(7))
print(ishappy_(7))
print(isHappy___(7))
# xx=[]
# for x in range(1,100):
#     if isHappy(x):
#         xx.append(x)
#
# print(xx)
# >>>[1, 7, 10, 13, 19, 23, 28, 31, 32, 44, 49, 68, 70, 79, 82, 86, 91, 94, 97]



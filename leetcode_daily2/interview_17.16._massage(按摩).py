def message(nums):
    if not nums:
        return 0
    dp0=0
    dp1=nums[0]
    for i in range(len(nums)):
        tdp0=max(dp0,dp1)
        tdp1=dp0+nums[i]
        dp0,dp1=tdp0,tdp1
    return max(dp0,dp1)
def massage_(nums) :
    # massage  推拿

    not_choose = 0  # 没选的时候最大的情况
    choose = 0  # 选了之后最大的情况

    for item in nums:
        not_choose, choose = max(not_choose, choose), max(not_choose + item, choose)
    return max(not_choose, choose)

def massage(nums):
    a=b=0
    for i in range(len(nums)):
        a,b=b,max(a+nums[i],b)
    return b
"""
我们仔细观察的话，其实我们只需要保证前一个 dp[i - 1] 和 dp[i - 2] 两个变量就好了，
比如我们计算到 i = 6 的时候，即需要计算 dp[6]的时候， 我们需要 dp[5], dp[4]，但是我们
不需要 dp[3], dp[2] ...
"""

print(message([1,2,3,1]))
print(massage_([1,2,3,1]))
print(massage([1,2,3,1]))

"""
斐波拉契数列
"""

def fib(n):
    a=0
    b=1
    for i in range(n):
        a,b=b,a+b
    return b
def fib_(n):
    if n==0 or n==1:
        return n
    return fib_(n-1)+fib(n-2)
print(fib(5))
print(fib_(5))
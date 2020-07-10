# hashset  哈希集合 散列表
# 将输入数组存储到 HashSet，然后使用 HashSet 中数字和的三倍与数组之和比较。
#  3*(a+b+c)-(a+a+a+b+b+b+c)=2c
class Solution:
    def singleNumber(self,nums):
        return (3*sum(set(nums))-sum(nums))//2

#hashMap
from collections import Counter
class Solution_:
    def singleNumber(self,nums):
        hashMap=Counter(nums)
        for k in hashMap.keys():
            if hashMap[k]==1:
                return k

#位运算 not and xor
"""
not a 
a&b
a^b
"""
# https://leetcode-cn.com/problems/single-number-ii/solution/137-zhi-chu-xian-yi-ci-de-shu-zi-ii-by-meishaoming/
class Solution__:
    def singerNmuber(self,nums):
        seen_once=seen_twice=0
        for num in nums:
            seen_once=~seen_twice&(seen_once^num)
            seen_twice=~seen_once&(seen_twice^num)
        return seen_once
"""
假设
b = (b^1) & ~a
a = (a^1) & ~b
有以下
这不就是三进制嘛，列出真值表：
初始值：a = 0, b = 0
进来第一轮： a = 0, b = 1
进来第二轮： a = 1, b = 0
进来第三轮： a = 0, b = 0
"""
sol=Solution__()
print(sol.singerNmuber([2,2,2,1,1,1,5]))


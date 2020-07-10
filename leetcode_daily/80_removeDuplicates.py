"""


       ####快慢指针...*****
"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return len(nums)
        slow, fast = 1, 2
        n = len(nums)
        while fast < n:
            if nums[fast] != nums[slow - 1]:
                slow += 1
                # slow 始终指向更改后的位置
                nums[slow] = nums[fast]
            fast += 1
        # 返回的是元素个数, 数组索引 + 1 即可
        return slow + 1
def s1(nums):
    i=2
    while i<len(nums):
        if nums[i-2]==nums[i]:
            nums.pop(i)
        else:
            i+=1
    return len(nums)

x=[1,1,1,2,2,3]
x1=[0,0,1,1,1,1,2,3,3]
print(s1(x))
print(s1(x1))
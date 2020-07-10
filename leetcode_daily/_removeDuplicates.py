#双指针思想：相当于从原地，得到了一个与原数据结构有关联新数据结构。
class Solution:
    def removeDuplicates(self, nums) -> int:
        if not nums:
            return 0
        i, j = 0, 1
        while j < len(nums):
            if nums[j] == nums[i]:
                j += 1
            else:
                nums[i + 1] = nums[j]
                i += 1
                j += 1
        return i + 1
class Solution_():
    def removeDuplicates(self,nums):
        for num_index in range(len(nums) - 1, 0, -1):
            if nums[num_index] == nums[num_index - 1]:
                nums.pop(num_index)
        return len(nums)

s=Solution()
x=[1,2,3,3,1,2]
x=sorted(x)
print(s.removeDuplicates(x))
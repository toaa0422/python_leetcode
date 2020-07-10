class Solution:
    # 一次遍历   脑袋乱  待后续  2020/7/7
    # 本问题被称为 荷兰国旗问题
    def sortColors(self, nums):
        # print(nums)
        """
        Do not return anything, modify nums in-place instead.
        """
        p0 = curr = 0
        p2 = len(nums) - 1
        while curr <= p2:
            print(f'curr={curr},p0={p0},p2={p2}')
            if nums[curr] == 0:
                nums[p0], nums[curr] = nums[curr], nums[p0]
                p0 += 1
                curr += 1
            elif nums[curr] == 2:
                nums[curr], nums[p2] = nums[p2], nums[curr]
                p2-=1
            else:
                curr += 1
            print(f'curr={curr},p0={p0},p2={p2}')
            print(nums)
            print('___________________________________________')

        return nums
import random
sol = Solution()
x=[]
# for i in range(10):
#     x.append(random.randint(0,2))
# print(x)
# print(sol.sortColors(x))
print(sol.sortColors([2, 0, 2, 1, 1, 0]))



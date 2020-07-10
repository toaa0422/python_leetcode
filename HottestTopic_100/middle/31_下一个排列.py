class Solution:
    # to be continued
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                subNums = sorted(nums[i:len(nums)])
                for j in subNums:
                    if j > nums[i - 1]:
                        newSub = j
                        break
                k = nums.index(newSub, i)
                nums[i - 1], nums[k] = nums[k], nums[i - 1]
                nums[i:] = sorted(nums[i:])
                return nums
        return nums.sort()


sol=Solution()
print(sol.nextPermutation([1,2,3]))
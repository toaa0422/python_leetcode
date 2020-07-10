class Solution:
    # 方法1：线性扫描
    # 方法2：二分查找
    def searchRange(self, nums, target: int) :
        for i in range(len(nums)):
            if nums[i] == target:
                left_idx = i
                break
        else:
            return [-1, -1]

            # find the index of the rightmost appearance of `target` (by reverse
            # iteration). it is guaranteed to appear.
        for j in range(len(nums) - 1, -1, -1):
            if nums[j] == target:
                right_idx = j
                break

        return [left_idx, right_idx]

    def extreme_insertion_index(self, nums, target, left):
        lo = 0
        hi = len(nums)

        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > target or (left and target == nums[mid]):
                hi = mid
            else:
                lo = mid + 1

        return lo

    def searchRange1(self, nums, target: int) :
        left_idx = self.extreme_insertion_index(nums, target, True)

        # assert that `left_idx` is within the array bounds and that `target`
        # is actually in `nums`.
        if left_idx == len(nums) or nums[left_idx] != target:
            return [-1, -1]

        return [left_idx, self.extreme_insertion_index(nums, target, False) - 1]

sol=Solution()
print(sol.searchRange([1,2,3,2,4],target=2))
print(sol.searchRange(nums = [5,7,7,8,8,10], target = 8))
print(sol.searchRange1(nums = [5,7,7,8,8,10], target = 8))
# print(sol.searchRange1([1,2,3,2,4],target=2))   #有误 待续

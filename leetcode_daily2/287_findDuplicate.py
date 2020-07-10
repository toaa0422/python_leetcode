class Solution:
    def findDuplicate(self, nums):
        n = len(nums)
        l, r, ans = 1, n - 1, -1
        while l <= r:
            mid = (l + r) >> 1
            cnt = 0
            for i in range(n):
                cnt += nums[i] <= mid
            if cnt <= mid:
                l = mid + 1
            else:
                r = mid - 1
                ans = mid
        return ans


class Solution_:
    def findDuplicate(self, nums):
        slow, fast = 0, 0
        pass


class Solution__:
    def findDuplicate(self, nums):
        import collections
        numdic = collections.Counter(nums)
        for i, j in numdic.items():
            if j != 1: return i


sol = Solution__()
print(sol.findDuplicate([1, 2, 3, 3]))
print(sol.findDuplicate([1, 2, 3, 3]))
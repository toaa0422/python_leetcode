#枚举
class Solution:
    def subarraySum(self,nums,k):
        cnt=0
        for start in range(len(nums)):
            sum=0
            end=start
            while end>=0:
                sum+=nums[end]
                if sum==k:
                    cnt+=1
                end-=1
        return cnt
class Solution_:
    def subarraySum(self, nums, k: int) -> int:
        prefix = []
        for idx, val in enumerate(nums):
            if idx == 0:
                prefix.append(val)
            else:
                prefix.append(val + prefix[-1])
        ans = 0
        import collections
        cnt = collections.defaultdict(int)
        cnt[0] += 1
        for idx, val in enumerate(prefix):
            if val - k in cnt:
                ans += cnt[val - k]
            cnt[val] += 1
        return ans
sol=Solution_()
print(sol.subarraySum([1,1,1],2))

# burte     brute force
class Solution:   #yes
    def minSubArrayLen(self,s,nums):
        if not nums:return 0
        n=len(nums)
        ans=n+1
        for i in range(n):
            total=0
            for j in range(i,n):
                total+=nums[j]
                if total>=s:
                    ans=min(ans,j-i+1)
                    break

        return 0 if ans==n+1 else ans
# 前缀和 + 二分查找
import bisect
class Solution_:
    def minSubArrayLen(self,s,nums):
        if not nums:return 0
        n=len(nums)
        ans=n+1
        sums=[0]
        for i in range(n):
            sums.append(sums[i]+nums[i])
        # print(sums)
        for i in range(1,n+1):
            target=s+sums[i-1]
            bound=bisect.bisect_left(sums,target)
            if bound != len(sums):
                ans=min(ans,bound-(i-1))
        return 0 if ans ==n+1 else ans
# 双指针   yes
class Solution__:
    def minSubArrayLen(self,s,nums):
        if not nums:return 0
        n=len(nums)
        ans=n+1
        start,end=0,0
        total=0
        while end<n:
            total+=nums[end]
            while total>=s:
                ans=min(ans,end-start+1)
                total-=nums[start]
                start+=1
            end+=1
        return 0 if ans==n+1 else ans



sol=Solution__()
print(sol.minSubArrayLen(6,[1]*7))
print(sol.minSubArrayLen(s = 7, nums = [2,3,1,2,4,3]))


def maxSubArray(nums):
    ans=nums[0]
    cur=0
    for i in range(len(nums)):
        if cur>0:
            cur+=nums[i]
        else:
            cur=nums[i]
        ans=max(ans,cur)
    return ans

class Solution:
    def maxSubArray(self, nums) -> int:
        cur_sum=0
        res=nums[0]
        n=len(nums)
        for i in range(n):
            if(cur_sum>0):
                cur_sum+=nums[i]
            else:
                cur_sum=nums[i]
            res=max(res,cur_sum)
        return res



s=Solution()
x=[-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(x))
print(s.maxSubArray(x))

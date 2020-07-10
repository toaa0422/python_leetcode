class Solution:
    # brute force
    def smallerNumbersThanCurrent(self,nums):
        n=len(nums)
        vec=[0]*n
        for i in range(n):
            vec[i]=sum(1 for j in range(n) if nums[i]>nums[j])
        return vec
    #频次数组 + 前缀和
    def smallerNumbersThanCurrent_(self,nums):
        n=len(nums)
        cnt,vec=[0]*101,[0]*n
        for num in nums:
            cnt[num]+=1
        for i in range(1,101):
            cnt[i]+=cnt[i-1]
        for i in range(n):
            if nums[i]:
                vec[i]=cnt[nums[i]-1]
        return vec
    #sort
    def smallerNumbersThanCurrent__(self, nums):
        n=len(nums)
        vec=[0]*n
        tmp=sorted([nums[i],i] for i in range(n))
        # print(tmp) # >>>[[4, 2], [5, 1], [6, 0], [8, 3]]
        pre=-1
        for i in range(n):
            if i!=0 and tmp[i][0]!=tmp[i-1][0]:
                pre=i-1
            vec[tmp[i][1]]=pre+1
        return vec



sol=Solution()
print(sol.smallerNumbersThanCurrent(nums = [6,5,4,8]))
print(sol.smallerNumbersThanCurrent_(nums = [6,5,4,8]))
print(sol.smallerNumbersThanCurrent__(nums = [6,5,4,8]))
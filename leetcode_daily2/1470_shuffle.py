class Solution:
    def shuffle(self,nums,n):
        res=[]
        for i in range(n):
            res.append(nums[i])
            res.append(nums[i+n])
        return res
sol=Solution()
print(sol.shuffle(list(range(1,7)),3))
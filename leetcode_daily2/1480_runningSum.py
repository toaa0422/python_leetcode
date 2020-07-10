class Solution:
    def runningSum(self,nums):
        res=[]
        s=0
        for num in nums:
            s+=num
            res.append(s)
        return res
sol=Solution()
print(sol.runningSum([1,2,3,4]))
print(sol.runningSum([1]*5))
class Solution:
    def findNumbers(self, nums):
        ans=0
        for x in nums:
            if len(str(x))&1==0:
                ans+=1
        return ans
sol=Solution()
print(sol.findNumbers([12,345,2,6,7896]))
print(sol.findNumbers([555,901,482,1771]))
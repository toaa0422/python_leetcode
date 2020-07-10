class Solution:
    def firstMissingPostive(self,nums):
        n=len(nums)
        for i in range(n):
            if nums[i]<=0:
                nums[i]=n+1
        print(nums)
        for i in range(n):
            num=abs(nums[i])
            if num<=n:
                nums[num-1]=-abs(nums[num-1])
        print(nums)
        for i in range(n):
            if nums[i]>0:
                return i+1
        print(nums)
        return n+1
class Solution_:
    def firstMissingPostive(self,nums):
        n=len(nums)
        for i in range(n):
            while 1<=nums[i]<=n and nums[nums[i]-1]!=nums[i]:
                nums[nums[i]-1],nums[i]=nums[i],nums[nums[i]-1]
                print(nums)
        print('haha',nums)
        for i in range(n):
            if nums[i]!=i+1:
                return i+1
        return n+1

sol=Solution_()
print(sol.firstMissingPostive([-1,1,4,2]))
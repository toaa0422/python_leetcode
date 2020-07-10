
#贪心算法    下述两种方法是贪心算法不同两个策略
#时间限制
class Solution:
    def jump(self,nums):
        n=len(nums)-1
        steps=0
        while n>0:
            for i in range(n):
                if i+nums[i]>=n:
                    n=i
                    steps+=1
                    break
        return steps
class Solution_:
    def jump(self,nums):
        maxPos,end,step=0,0,0
        for i in range(len(nums)-1):
            # 细节 len(nums)
            if maxPos>=i:
                print(f'maxPos={maxPos}')
                maxPos=max(maxPos,i+nums[i])
                if i==end:
                    end=maxPos
                    step+=1
        return step

#刷这么多题，第一次遇到了贪心算法，每次找局部最优，最后达到全局最优，完美！

sol=Solution_()
print(sol.jump([2,3,1,1,4]))




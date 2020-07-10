#method:dynamic planning
class Solution:
    def maxSubArray(self,nums):
        pre=0
        max_ans=nums[0]
        pre_=[]
        max_=[]
        for x in nums:
            pre=max(pre+x,x)
            pre_.append(pre)
            max_ans=max(max_ans,pre)
            max_.append(max_ans)
        print(pre_)
        print(max_)
        return max_ans

#method:分治法 divide and conquer
# 这个分治方法类似于「线段树求解 LCIS 问题」的 pushUp 操作   待回归加强  比较复杂时候此作用凸显出来


#Brute force solution
class Solution_:
    def maxSubArray(self, nums) -> int:
        tmp = nums[0]
        max_ = tmp
        n = len(nums)
        for i in range(1, n):
            # 当当前序列加上此时的元素的值大于tmp的值，说明最大序列和可能出现在后续序列中，记录此时的最大值
            if tmp + nums[i] > nums[i]:
                max_ = max(max_, tmp + nums[i])
                tmp = tmp + nums[i]
            else:
                # 当tmp(当前和)小于下一个元素时，当前最长序列到此为止。以该元素为起点继续找最大子序列,
                # 并记录此时的最大值
                max_ = max(max_, tmp, tmp + nums[i], nums[i])
                tmp = nums[i]
        return max_
    #简化 simplify
    def maxSubArray1(self,nums):
        temp = nums[0]
        max_ = temp
        for i in range(1, len(nums)):
            if temp > 0:
                temp += nums[i]
                max_ = max(max_, temp)

            else:
                temp = nums[i]
                max_ = max(max_, temp)
        return max_

#recursion
class Solution__:
    def maxSubArray(self,nums):
        # n = len(nums)
        # # 递归终止条件
        # if n == 1:
        #     return nums[0]
        # else:
        #     # 递归计算左半边最大子序和
        #     max_left = self.maxSubArray(nums[0:len(nums) // 2])
        #     # 递归计算右半边最大子序和
        #     max_right = self.maxSubArray(nums[len(nums) // 2:len(nums)])

        n=len(nums)
        if n==1:return nums[0]
        else:
            max_left=self.maxSubArray(nums[0:len(nums)//2])
            max_right=self.maxSubArray(nums[len(nums)//2:len(nums)])
        max_l=nums[len(nums)//2-1]
        tmp=0
        for i in range(len(nums) // 2 - 1, -1, -1):
        #  for i in range(len(nums//2-1),-1,-1):  #细节
            tmp+=nums[i]
            max_l=max(tmp,max_l)
        max_r=nums[len(nums)//2]
        tmp=0
        for i in range(len(nums) // 2, len(nums)):
        # for i in range(len(nums//2),len(nums)):  #细节
            tmp+=nums[i]
            max_r=max(tmp,max_r)
        return max(max_left,max_right,max_l+max_r)
sol=Solution()
print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
# print(sol.maxSubArray([-1,1,-3,-1,2]))





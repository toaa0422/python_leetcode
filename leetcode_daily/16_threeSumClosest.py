# method: sort+double pointer
class Solution:
    def threeSumClosest(self,nums,target):
        nums.sort()
        # print(nums)
        n=len(nums)
        best=10**7
        def update(cur):
            nonlocal best
            if abs(cur-target)<abs(best-target):
                best=cur
                # print(best)
        for i in range(n):
            if i>0 and nums[i]==nums[i-1]:
                continue
            j,k=i+1,n-1
            while j<k:
                s=nums[i]+nums[j]+nums[k]
                if s==target:
                    return target
                update(s)
                if s>target:
                    k0=k-1
                    while j<k0 and nums[k0]==nums[k]:
                        k0-=1
                    k=k0
                else:
                    j0=j+1
                    while j0<k and nums[j0]==nums[j]:
                        j0+=1
                    j=j0
        return best
class Solution_:
    def threeSumClosest(self,nums,target):
        nums_len=len(nums)
        nums.sort()
        ans_sum=sum(nums[i] for i in range(3))
        for i in range(nums_len):
            left,right=i+1,nums_len-1
            while left<right:
                curr_sum=nums[i]+nums[left]+nums[right]
                if abs(curr_sum - target) < abs(ans_sum - target):
                    ans_sum = curr_sum
                if curr_sum > target:
                    right -= 1
                elif curr_sum < target:
                    left += 1
                else:
                    return target
        return ans_sum




sol=Solution()
print(sol.threeSumClosest([-1,2,1,-4], target =1 ))
sol_=Solution_()
print(sol_.threeSumClosest([-1,2,1,-4], target =1 ))

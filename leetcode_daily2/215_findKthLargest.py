#貌似 大根堆
class Solution:
    def findKthLargest(self, nums, k):
        def adjust_heap(idx, max_len):
            left = 2 * idx + 1
            right = 2 * idx + 2
            max_loc = idx
            if left < max_len and nums[max_loc] < nums[left]:
                max_loc = left
            if right<max_len and nums[max_loc]<nums[right]:
                max_loc=right
            if max_loc!=idx:
                nums[idx],nums[max_loc]=nums[max_loc],nums[idx]
                adjust_heap(max_loc,max_len)
        n=len(nums)
        for i in range(n//2-1,-1,-1):
            adjust_heap(i,n)
        res=None
        for i in range(1,k+1):
            res=nums[0]
            nums[0],nums[-i]=nums[-i],nums[0]
            adjust_heap(0,n-1)
        return res
# 快排+二分   pass
class Solution_:
    def findKthLargest(self, nums, k: int) -> int:
        def partition(left,right):
            pivot=nums[left]
            l=left+1
            r=right
            while l<=r:
                if nums[l]<pivot and nums[r]>pivot:
                    nums[l],nums[r]=nums[r],nums[l]
                if nums[l]>=pivot:
                    l+=1
                if nums[r]<=pivot:
                    r-=1
            nums[r],nums[left]=nums[left],nums[r]
            return r
        left=0
        right=len(nums)-1
        while 1:
            idx=partition(left,right)
            if idx==k-1:
                return  nums[idx]
            if idx<k-1:
                left=idx+1
            if idx>k-1:
                right=idx-1

#小根堆  #超过输出限制
class Solution__:
    def findKthLargest(self,nums,k):
        def shift(i,k):
            flag=0
            while (i*2+1)<k and flag==0:
                t=i
                if nums[i]>nums[2*i+1]:
                    t=2*i+1
                if (i*2+2)<k and nums[t]>nums[2*i+2]:
                    t=2*i+2
                if t==i:
                    flag=1
                else:
                    nums[i],nums[t]=nums[t],nums[i]
                    i=t
            # print(nums)
        for i in range(k//2,-1,-1):
            # print(i)
            shift(i,k)
        # print(nums)
        # 排序，只需要循环K次，排序TOPK个节点
        for i in range(k,len(nums)):
            if nums[0]<nums[i]:
                nums[0]=nums[i]
                shift(0,k)
                print(nums)
        # print(nums)
        return nums[0]

sol=Solution__()
print(sol.findKthLargest([3, 2, 1, 5, 6, 4], k = 2))

# print(sorted([3, 2, 1, 5, 6, 4]))
# print(sorted([3, 2, 3, 1, 2, 4, 5, 5, 6]))









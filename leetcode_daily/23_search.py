#搜索旋转排序数组
# ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
class Solution():
    def search(self,nums,target):
        if not nums:return -1
        l, r = 0, len(nums)-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:
                return mid
            if nums[0]<=nums[mid]:
                if nums[0]<=target<nums[mid]:
                    r=mid-1
                else:
                    l=mid+1
            else:
                if nums[mid]<target<=nums[len(nums)-1]:
                    l=mid+1
                else:
                    r=mid-1
        return -1
s=Solution()
print(s.search([4,5,6,7,0,1,2],0))
print(s.search([4,5,6,7,0,1,2],3))
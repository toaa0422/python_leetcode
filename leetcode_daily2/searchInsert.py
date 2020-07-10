def searchInsert(nums,target) -> int:
    low=0
    high=len(nums)-1
    if target< nums[0]:
        return 0
    if target>nums[-1]:
        return target+1
    while low<=high:
        mid=(low+high)//2
        if nums[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return low
print(searchInsert([1,3,5,6], 5))
print(searchInsert([1,3,5,6], 2))
# 枚举 + 二分查找
class Solution:
    def findBestValue(self,arr,target=None):
        import bisect
        arr.sort()
        n=len(arr)
        prefix=[0]
        for num in arr:
            prefix.append(prefix[-1]+num)
        # print(prefix)
        r,ans,diff=max(arr),0,target
        for i in range(1,r+1):
            it=bisect.bisect_left(arr,i)
            # print(i,end=' ')
            cur=prefix[it]+(n-it)*i
            # print(cur,end=' ')
            if abs(cur-target)<diff:
                # print(abs(cur - target))
                ans,diff=i,abs(cur-target)

        # print('\n')
        return ans
class Solution_:
    def findBestValue(self,arr,target):
        import bisect
        arr.sort()
        n=len(arr)
        prefix=[0]
        for num in arr:
            prefix.append(prefix[-1]+num)
        l,r,ans=0,max(arr),-1
        while l<=r:
            mid=(l+r)//2
            it=bisect.bisect_left(arr,mid)
            cur=prefix[it]+(n-it)*mid
            if cur<=target:
                ans=mid
                l=mid+1
            else:r=mid-1
        def check(x):
            return sum( x if num>=x else num for num in arr)
        choose_small=check(ans)
        choose_big=check(ans+1)
        return ans if abs(choose_small-target)<=abs(choose_big-target) else ans+1




sol=Solution()
print(sol.findBestValue([5,2,3,4],4))



#complexity analysis
#时间复杂度：O(N)O(N)，双指针总计最多遍历整个数组一次。
#空间复杂度：O(1)O(1)，只需要额外的常数级别的空间。
#method：双指针
class Solution():
    def maxArea(self,height):
        l,r=0,len(height)-1
        ans=0
        while l<r:
            area=min(height[l],height[r])*(r-l)
            ans=max(ans,area)
            if height[l]<=height[r]:
                l+=1
            else:
                r-=1
        return ans
class Solution_:
    def maxArea(self, height) -> int:
        i, j, res = 0, len(height) - 1, 0
        while i < j:
            if height[i] < height[j]:
                res = max(res, height[i] * (j - i))
                i += 1
            else:
                res = max(res, height[j] * (j - i))
                j -= 1
        return res








s=Solution()
print(s.maxArea([1,2]))

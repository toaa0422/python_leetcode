# 单调栈特别适合解决那些，两头大小决定中间值的大小的题。
class Solution_haha:
    def largestRectangleArea(self,heights):
        stack=[-1]
        max_res=0
        test=[]
        for i in range(len(heights)):
            while  len(stack) > 1 and heights[i]<=heights[stack[-1]]:

                max_res=max(max_res,heights[stack.pop()]*(i-stack[-1]-1))

            stack.append(i)
            # print(stack)
        for i in range(len(stack)-1):
            max_res = max(max_res, heights[stack.pop()] * (len(heights) - 1 - stack[-1]))
            # 细节  max_res=max(max_res,heights[stack.pop()]*    (  len(heights)-1-stack[-1])  )
        # for i in range(len(stack)-1):
        #     max_res = max(max_res, heights[stack.pop()]*(len(heights)-1-stack[-1]))
        return max_res
class Solution_test:
    def largestRectangleArea(self, heights) -> int:
        stack = [-1]
        max_res = 0
        for i in range(len(heights)):
            while len(stack) > 1 and heights[i] <= heights[stack[-1]]:
                max_res = max(max_res, heights[stack.pop()] * (i - stack[-1] - 1))
            stack.append(i)
        for i in range(len(stack)-1):
            max_res = max(max_res, heights[stack.pop()]*(len(heights)-1-stack[-1]))
        return max_res

sol=Solution_haha()
print(sol.largestRectangleArea([2,1,5,6,2,3]))

















class Solution:
    def largestRectangleArea(self,heights):
        n=len(heights)
        left,right=[0]*n,[0]*n
        mono_stack=list()
        # print(mono_stack)
        for i in range(n):
            while mono_stack and heights[mono_stack[-1]]>=heights[i]:
                mono_stack.pop()
            left[i]=mono_stack[-1] if mono_stack else -1
            # print(left)
            mono_stack.append(i)
            # print(mono_stack)
        mono_stack=list()
        for i in range(n-1,-1,-1):
            while mono_stack and heights[mono_stack[-1]]>=heights[i]:
                mono_stack.pop()
            right[i]=mono_stack[-1] if mono_stack else n
            mono_stack.append(i)
        ans=max((right[i]-left[i]-1)*heights[i] for i in range(n)) if n >0 else 0
        return  ans
class Solution_:
    def largestRectangleArea(self,heights):
        ans = 0
        n=len(heights)
        for mid in range(len(heights)):
            height = heights[mid]
            left = mid, right = mid
            while (left - 1 >= 0 and heights[left - 1] >= height) :
                left-=1
            while (right + 1 < n and heights[right + 1] >= height):
                right+=1
            ans = max(ans, (right - left + 1) * height)
        return ans


# sol=Solution_()
# print(sol.largestRectangleArea([2,1,5,6,2,3]))

# 4/4  2020
# 按列求
def trap(height):
    sum=0
    for i in range(1,len(height)-1):
        max_left=0
        for j in range(i-1,0,-1):
            if height[j]>max_left:
                max_left=height[j]
        max_right=0
        for j in range(i+1,len(height)):
            if height[j]>max_right:
                max_right=height[j]
        min_ = min(max_left, max_right)
        if min_>height[i]:
            sum=sum+(min_-height[i])
    return sum

#动态规划
def trap_(height):
    sum=0
    max_left,max_right=[0]*(len(height)+1),[0]*(len(height)+1)
    for i in range(1,len(height)):
        # print(f'max={max_left[i-1]},{height[i-1]}')
        max_left[i]=(max(max_left[i-1],height[i-1]))
    print(f'{max_left}')
    for i in range(1,len(height)-1)[::-1]:
        max_right[i]=max(max_right[i+1],height[i+1])
    for i in range(1,len(height)-2):
        min_=min(max_left[i],max_right[i])
        if min_ >   height[i]:
            sum=sum+(min_-height[i])
    return sum
#双指针

def trap__(heights) -> int:
    n = len(heights)
    l, r = [0] * (n + 1), [0] * (n + 1)
    ans = 0
    for i in range(1, len(heights) + 1):
        l[i] = max(l[i - 1], heights[i - 1])
    for i in range(len(heights) - 1, 0, -1):
        r[i] = max(r[i + 1], heights[i])
    print(f'{l},{r}')
    for i in range(len(heights)):
        ans += max(0, min(l[i + 1], r[i]) - heights[i])
        # print("{0}:{1}-{2}".format(ans,max(0, min(l[i + 1], r[i])),heights[i]))
    return ans

print(trap__([ 0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1 ]))






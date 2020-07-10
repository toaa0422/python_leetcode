#rightmost  最后边的
class Solution:
    def canJump(self, nums) -> bool:
        n, rightmost = len(nums), 0
        for i in range(n):
            if i <= rightmost:
                print(f'max({rightmost},{i + nums[i]})')
                rightmost = max(rightmost, i + nums[i])
                print(f'max={rightmost}')

                if rightmost >= n - 1:
                    return True
        return False
class Solution_:
    def canJump(self, nums) -> bool:
        current=0
        for i in range(len(nums)-1):#最后一格不用检测
            current=max(current-1,nums[i])
            if current==0:return False
        return True




s=Solution_()
print(s.canJump([2,3,1,1,4]))
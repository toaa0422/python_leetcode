# Consecutive
class Solution:
    def longestConsecutive(self,nums):
        longest_streak=0
        num_set=set(nums)
        for nums in num_set:
            if nums-1 not in num_set:
                cur_num=nums
                cur_streak=1
                while cur_num+1 in num_set:
                    cur_num+=1
                    cur_streak+=1
                longest_streak=max(cur_streak,longest_streak)
        return longest_streak
sol=Solution()
print(sol.longestConsecutive([14,88,8,9,10,11,12,13,1,2,3,4]))
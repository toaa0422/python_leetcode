class Solution:

    def climbStairs(self,n):

        q = 0
        r = 1
        for i in range(6):
            p = q
            q = r
            r = p + q


        return r
sol=Solution()
print(sol.climbStairs(5))
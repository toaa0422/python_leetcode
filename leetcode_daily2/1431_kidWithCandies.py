class Solution:
    def kidsWithCandies(self,candies,extraCandies):
        maxCandy=max(candies)
        ret=[candy+extraCandies>=maxCandy for candy in candies ]
        return ret
sol=Solution()
candies = [2,3,5,1,3]
extraCandies = 3
print(sol.kidsWithCandies(candies,extraCandies))
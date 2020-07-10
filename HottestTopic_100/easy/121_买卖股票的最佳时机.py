class Solution:
    #brute force       time over
    def maxProfit(self, prices) -> int:
        ans=0
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                ans=max(ans,prices[j]-prices[i])
        return ans
    #一次遍历
    def maxProfit_(self, prices) -> int:
        inf=float('inf')
        minprice=inf
        maxprofit=0
        for price in prices:
            maxprofit=max(price-minprice,maxprofit)
            minprice=min(price,minprice)
        return maxprofit
sol=Solution()
print(sol.maxProfit([7,1,5,3,6,4]))
print(sol.maxProfit([7,6,4,3,1]))
print(sol.maxProfit_([7,1,5,3,6,4]))
print(sol.maxProfit_([7,6,4,3,1]))



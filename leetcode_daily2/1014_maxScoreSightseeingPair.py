class Solution:
    def maxScoreSightseeingPair(self, A):
        x,y=[],[]
        res = 0
        pre_max = A[0] + 0  # 初始值
        for j in range(1, len(A)):
            res = max(res, pre_max + A[j] - j)  # 判断能否刷新res
            x.append(res)

            pre_max = max(pre_max, A[j] + j)  # 判断能否刷新pre_max， 得到更大的A[i] + i
            y.append(pre_max)
        print(x)
        print(y)

        return res
class Solution_:
    def maxScoreSightseeingPair(self,a):
        dp=a[0]+a[1]+1
        mx=dp
        for i in range(2,len(a)):
            dp=(max(dp-1-a[i-1]+a[i],a[i]+a[i-1]-1))
            mx=max(mx,dp)
        return mx


sol=Solution_()
print(sol.maxScoreSightseeingPair([8,1,5,2,6]))
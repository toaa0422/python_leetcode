class Solution:
    def divingBoard(self, shorter: int, longer: int, k: int) :
        if k<=0:return []
        if shorter==longer:return [shorter*k]
        ans=[0]*(k+1)
        for i in range(k+1):
            ans[i]=shorter*(k-i)+longer*i
        return ans
sol=Solution()
print(sol.divingBoard(1,2,3))

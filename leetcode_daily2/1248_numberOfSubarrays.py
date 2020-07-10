class Solution():
    def numberOfSubarrays(self,nums,k):
        n=len(nums)
        odd=[-1]
        ans=0
        for i in range(n):
            if nums[i]%2==1:
                odd.append(i)
        odd.append(n)
        print(odd)
        for i in range(1,len(odd)-k):
            ans+=(odd[i] - odd[i - 1]) * (odd[i + k] - odd[i + k - 1])
        return ans
class Solution_():
    def numberOfSubarrays(self,nums,k):
        cnt=[0]*(len(nums)+1)
        print(f'{cnt}')
        cnt[0]=1
        odd,ans=0,0
        for num in nums:
            if num%2==1:
                odd+=1
            if odd>=k:
                ans+=cnt[odd-k]
            cnt[odd]+=1
        return ans
s=Solution_()
print(s.numberOfSubarrays([1,1,2,1,1],3))
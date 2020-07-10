class Solution:
    # 待续
    def canPartition(self, nums) -> bool:
        n=len(nums)
        target=sum(nums)
        print(target)
        if target%2:
            return False
        target//=2
        dic=set()
        dic.add(0)
        for i in range(n):
            dic_tmp=set()
            for j in dic:
                tmp=j+nums[i]
                if tmp==target:
                    return True
                if tmp<target:
                    dic_tmp.add(tmp)
            for j in dic_tmp:
                dic.add(j)
                print(dic)
        return False
sol=Solution()
print(sol.canPartition([1, 5, 11, 5]))
print(sol.canPartition([1, 2, 3, 5]))

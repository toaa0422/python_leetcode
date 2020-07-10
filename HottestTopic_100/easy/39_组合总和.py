class Solution:
    #dynamic planning
    def combinationSum(self,candidates,target):
        dp={i:[] for i in range(target+1)}
        print(dp)
        # print(sorted(candiates,reverse=True))
        for i in sorted(candidates,reverse=True):
            print(i)
            for j in range(i,target+1):
                # print(j)
                if j==i:
                    dp[j]=[[i]]
                else:
                    print([x+[i] for x in dp[j-i]])
                    dp[j].extend([x+[i] for x in dp[j-i]])
                print(dp)
        return dp[target]
    # dynamic planning
    def combinationSum_(self, candidates, target: int):
        dict = {}
        for i in range(1, target + 1):
            dict[i] = []
        for i in range(1, target + 1):
            for j in candidates:
                if i == j:
                    dict[i].append([i])
                elif i > j:
                    for k in dict[i - j]:
                        x = k[:]
                        x.append(j)
                        x.sort()  # 升序，便于后续去重
                        if x not in dict[i]:
                            dict[i].append(x)
        return dict[target]

    #backtrack+剪枝  ***

sol=Solution()
print(sol.combinationSum([7,2,3,6], target = 7))
# print(sol.combinationSum_([2,3,6,7], target = 7))
# print(sol.combinationSum([2,3,5], target = 8))
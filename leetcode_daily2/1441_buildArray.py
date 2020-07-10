class Solution:
    def buildArray(self, target,n=None):
        res = []
        n=len(target) or n
        for i in range(1,n+1):
            if i in target:
                if i != target[-1]:
                    res.append("Push")
                else:
                    res.append("Push")
                    return res
            else:
                res.append("Push")
                res.append("Pop")
        return res
sol=Solution()
print(sol.buildArray([1,3],3))  #['Push', 'Push', 'Pop', 'Push']
print(sol.buildArray([1,3]))  #['Push', 'Push', 'Pop', 'Push']


import collections
import numpy as np
class Solution:
    # 排序数组分类  yes
    def groupAnagrams(self, strs):
        ans=collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return list(ans.values())
    # 按计数分类   yes
    def groupAnagrams_(self, strs):
        ans=collections.defaultdict(list)
        for s in strs:
            count=[0]*26
            for c in s:
                count[ord(c)-ord('a')]+=1
            # print(s)
            # print(count)
            ans[tuple(count)].append(s)
        print(np.array(list(ans)))
        # print(np.array(dict(ans)))
        return list(ans.values())

sol=Solution()
# print(sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(sol.groupAnagrams_(["eat", "tea", "tan", "ate", "nat", "bat"]))


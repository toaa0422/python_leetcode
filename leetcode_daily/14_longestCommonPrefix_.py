# 横向扫描   yes
class Solution1:
    def longestCommonPrefix(self,strs):
        if not strs:return ''
        prefix,count=strs[0],len(strs)
        for i in range(1,count):
            prefix=self.lcp(prefix,strs[i])
            # print(prefix)
            if not prefix:break  #
        return prefix
    def lcp(self,str1,str2):
        length,index=min(len(str1),len(str2)),0
        while index<length and str1[index]==str2[index]:
            index+=1
        # print(index)
        return str1[:index]
# 纵向扫描
class Solution2:
    def longestCommonPrefix(self,strs):
        if not strs:return ''
        length,count=len(strs[0]),len(strs)
        for i in range(length):
            c=strs[0][i]
            if any(len(strs[j])==i  or strs[j][i]!=c for j in range(1,count)):  ###
                return strs[0][:i]
        return strs[0]
# 分治   yes
class Solution3:
    def longestCommonPrefix(self,strs):
        def lcp(start,end):
            if start==end:return strs[start]
            mid =(start+end)//2
            lcpleft,lcpright=lcp(start,mid),lcp(mid+1,end)
            minlength=min(len(lcpleft),len(lcpright))
            for i in range(minlength):
                if lcpleft[i]!=lcpright[i]:
                    return lcpleft[:i]
            return lcpleft[:minlength]
        return '' if not strs else lcp(0,len(strs)-1)
# 二分查找   yes
class Solution4:
    def longestCommonPrefix(self,strs):
        def isCommonPrefix(length):
            str0,count=strs[0][:length],len(strs)
            return all(strs[i][:length]==str0 for i in range(1,count))
        if not strs:return ''

        minlength=min(len(s) for s in strs)
        # print(minlength)
        low,high=0,minlength
        while low<high:
            mid=(high-low+1)//2+low
            print(mid)
            if isCommonPrefix(mid):
                low=mid
            else:high=mid-1
        return strs[0][:low]

sol=Solution1()

print(sol.longestCommonPrefix(["flow","flower","flight"]))



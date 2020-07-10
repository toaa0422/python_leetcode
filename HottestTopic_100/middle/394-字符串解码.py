class Solution:
    # stack operation  yes
    def decodeString(self, s: str) -> str:
        stack,res,multi=[],'',0
        for c in s:
            if c=='[':
                stack.append([multi,res])
                res,multi='',0
            elif c==']':
                cur_multi,last_res=stack.pop()
                res=last_res+cur_multi*res
            elif '0'<=c<='9':
                multi=multi*10+int(c)
            else:res+=c
        return res
    # recursion
    def decodeString1(self, s: str) -> str:
        def dfs(s, i):
            res, multi = "", 0
            while i < len(s):
                if '0' <= s[i] <= '9':
                    multi = multi * 10 + int(s[i])
                elif s[i] == '[':
                    i, tmp = dfs(s, i + 1)
                    res += multi * tmp
                    multi = 0
                elif s[i] == ']':
                    return i, res
                else:
                    res += s[i]
                i += 1
            return res

        return dfs(s, 0)




sol=Solution()
print(sol.decodeString1('2[cc]'))
print(sol.decodeString1('2[a3[cc]]'))
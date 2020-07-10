class Solution:
    # dynamic planning
    def longestValidParentheses(self,s):
        pass

    # stack
    def longestValidParentheses1(self,s):
        if not s:return 0
        stack=[]
        ans=0
        for i in range(len(s)):
            if not stack or s[i]=='(' or s[stack[-1]]==')':
                stack.append(i)
            else:
                stack.pop()
                ans=max(ans,i-(stack[-1] if stack else -1))
        return ans
class Solution1:
    def longestValidParentheses(self, s: str) -> int:
        if not s: return 0

        stack = []
        ans = 0
        for i in range(len(s)):
            # 入栈条件
            if not stack or s[i] == '(' or s[stack[-1]] == ')':
                stack.append(i)     # 下标入栈
            else:
                # 计算结果
                stack.pop()
                ans = max(ans, i - (stack[-1] if stack else -1))
        return ans


sol=Solution()
# sol=Solution1()
print(sol.longestValidParentheses1("(()"))
print(sol.longestValidParentheses1(")()())"))


class Solution:
    def isValid(self, s: str) -> bool:
        dic = {')': '(', ']': '[', '}': '{'}
        stack = []
        for i in s:
            if stack and i in dic:
                if stack[-1] == dic[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return not stack
class Solution_:
    def isValid(self, s: str) -> bool:
        while '[]' in s or '{}' in s or '()' in s:
            s.replace('[]','')
            s.replace('()','')
            s.replace('{}','')
        return s ==''


s=Solution()
print(s.isValid("[}{}()()()"))
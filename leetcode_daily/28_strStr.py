class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)

class Solution_:
    def strStr(self, haystack: 'str', needle: 'str') -> 'int':
        if not haystack:
            return 0
        for i in range(0, len(haystack)):
            if haystack[i:i + len(needle)] == needle:
                return i
        return -1





s=Solution_()
x="ssabcd"
y="abcd"
print(s.strStr(x,y))
class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        return s[n:]+s[:n]
    """
    time complexity:O(N)
    space complexity:O(n)
    """
'''巧用模运算'''
class Solution_():
    def reverseLeftWords(self, s: str, k: int) -> str:
        n = len(s)
        res = ''
        for i in range(k, k + n):
            res += s[i % n]
        return res
    '''
    时间复杂度:O(N)  time complexity
    空间复杂度:O(1)  space complexity
    '''

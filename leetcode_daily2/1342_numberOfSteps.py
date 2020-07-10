#二进制+计数
class Solution:
    def numberOfSteps (self, num: int) -> int:
        binary=bin(num)
        # print(binary)
        # print(len(binary))
        # print(binary.count('1'))
        return len(binary)+binary.count('1')-3
    def numberOfSteps_(self, num: int) -> int:
        s = bin(num)[2:]
        res = len(s) + sum([int(i) for i in s]) - 1
        return res

sol=Solution()
print(sol.numberOfSteps(6))
print(sol.numberOfSteps(8))
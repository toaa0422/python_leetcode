class Solution:
    def maximum69Number (self, num: int) -> int:
        return int(str(num).replace("6", "9", 1))
sol=Solution()
print(sol.maximum69Number(6669))    #一行代码：第一次替换的，一定是最大的结果。  ****

#str.replace()
# old -- 将被替换的子字符串。
# new -- 新字符串，用于替换old子字符串。
# max -- 可选字符串, 替换不超过 max 次


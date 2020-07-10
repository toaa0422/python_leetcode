# 筛选 + 判断
class Solution:
    def isPalindrome(self,s):
        sgood=''.join(ch.lower() for ch in s if ch.isalnum())  #如果 c 是一个数字或一个字母，则该函数返回非零值，否则返回 0。
        print(sgood)
        return sgood==sgood[::-1]
#双指针
class Solution_:
    def isPalindrome(self,s):
        sgood=''.join(ch.lower() for ch in s if ch.isalnum())
        n=len(sgood)
        left,right=0,n-1
        while left<right:
            if sgood[left]!=sgood[right]:
                return False
            left+=1
            right-=1
        return True
# 在原字符串上直接判断
class Solution__:
    def isPalindrome(self,s):
        n=len(s)
        left,right=0,n-1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if left<right:
                if s[left].lower() !=s[right].lower():
                    return False
                left += 1
                right -= 1
        return True

sol=Solution()
# print(sol.isPalindrome("A man, a plan, a canal: Panama"))
print(sol.isPalindrome("race aecar"))

#***** 正则表达式
class Soulution:
    def vaildPalindrome(self,s):
        isPalindrome=lambda x:x==x[::-1]
        left,right=0,len(s)-1
        while left<=right:
            if s[left]==s[right]:
                left+=1
                right-=1
            else:
                # print(s[left+1:right+1])
                # print(isPalindrome(s[left+1:right+1]))
                # print(s[left:right])
                # print(isPalindrome(s[left:right]))
                return isPalindrome(s[left+1:right+1]) or isPalindrome(s[left:right])
        return True


x='abas'
sol=Soulution()
print(sol.vaildPalindrome(x))
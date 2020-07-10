import collections
def x_(s):
    print(set(s))
    for i in set(s):
        print(s.count(i),s.count(i)%2, end=" ")
        print(" ")
    a=[s.count(i)%2 for i in set(s)]
    print(a)
    print(sum(a)-1)
    return len(s) - max(0, sum([s.count(i) % 2 for i in set(s)]) - 1)

class Solution:
    def longestPalindrome(self, s):
        ans = 0
        count = collections.Counter(s)
        print(count)
        for v in count.values():
            #print(v)     #>>>1 1 4 2
            ans += v // 2 * 2  #0 0   5  7
            print(ans)
            if ans % 2 == 0 and v % 2 == 1:  # 0 1
                ans += 1                     # +1
        return ans

s=Solution()
print(s.longestPalindrome("abccccdd"))


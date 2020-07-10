class Solution:
    def minIncrementForUnique(self, A) -> int:
        count = [0] * 80000
        for x in A:
            count[x] += 1

        ans = taken = 0
        for x in range(80000):
            if count[x] >= 2:
                taken += count[x] - 1
                ans -= x * (count[x] - 1)
            elif taken > 0 and count[x] == 0:
                taken -= 1
                ans += x

        return ans
class Solution_:
    def minIncrementForUnique_(self, A) -> int:
        A.sort()
        A.append(100000)
        ans = taken = 0

        for i in range(1, len(A)):
            if A[i-1] == A[i]:
                taken += 1
                ans -= A[i]
            else:
                give = min(taken, A[i] - A[i-1] - 1)
                ans += give * (give + 1) // 2 + give * A[i-1]
                taken -= give
def f(arr):
    res=0
    list.sort(arr)
    for i in range(1,len(arr)):
        if arr[i-1]>=arr[i]:
            res+=arr[i-1]-arr[i]+1
            arr[i]=arr[i-1]+1
    return res
s=Solution()
ss=Solution_()
#print(s.minIncrementForUnique([1,200,200,330]))
#print(ss.minIncrementForUnique_([1,2,2]))
print(f([3,2,1,2,1,7]))
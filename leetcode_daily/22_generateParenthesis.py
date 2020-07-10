class Solution:
    def generateParenthesis(self, n: int):
        def generate(A):
            if len(A) == 2*n:
                # print(f"{len(A)}=={2*n}")
                if valid(A):
                    ans.append("".join(A))
            else:
                A.append('(')
                generate(A)
                print(A)
                print("---------------")
                A.pop()
                print(A)

                A.append(')')
                generate(A)
                A.pop()

        def valid(A):
            bal = 0
            for c in A:
                if c == '(': bal += 1
                else: bal -= 1
                if bal < 0: return False
            return bal == 0

        ans = []
        generate([])
        # print(generate([]))
        # print(ans)
        return set(ans)
class Solution_:
    def generateParenthesis(self, n: int):
        ans = []
        def backtrack(S, left, right):
            if len(S) == 2 * n:
                ans.append(''.join(S))
                return
            if left < n:
                S.append('(')
                backtrack(S, left+1, right)
                print("-------------------------")
                print(S)
                S.pop()
                print(S)
                print("-------------------------")
            if right < left:
                S.append(')')
                backtrack(S, left, right+1)
                S.pop()

        backtrack([], 0, 0)
        return ans
#method3
class Solution__():
    def generateParenthesis(self,n):
        if n==0:
            return ['']
        ans=[]
        for c in range(n):
            for left in self.generateParenthesis(c):
                print(f'left={left}')
                for right in self.generateParenthesis(n-1-c):
                    print(f'right={right}')
                    print("final="+str('({}){}'.format(left,right)))
                    ans.append('({}){}'.format(left,right))
                    print(f'{ans}')
        return ans
s=Solution__()
print(s.generateParenthesis(3))

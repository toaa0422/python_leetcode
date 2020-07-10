class Solution:
    # recursion
    def subsets(self, nums):
        # n=len(nums)
        output = [[]]
        for num in nums:
            output += [curr + [num] for curr in output]
        return output

    # backtrack
    def subsets_(self, nums):
        def backtrack(first=0, curr=[]):
            if len(curr) == k:
                output.append(curr[:])
            for i in range(first, n):
                curr.append(nums[i])
                backtrack(i + 1, curr)
                curr.pop()

        output = []
        n = len(nums)
        for k in range(n + 1):
            backtrack()
        return output


class Solution_:
    def subsets(self, nums):
        n = len(nums)
        output = []
        x=[]
        for i in range(2 ** n, 2 ** (n + 1)):
            bitmask = bin(i)[3:]
            print(bitmask)
            x.append(bitmask)
            output.append([nums[j] for j in range(n) if bitmask[j] == '1'])
        print(x)
        return output


sol = Solution_()
print(sol.subsets([1, 2, 3]))

# RLE  行程编码(Run length encoding)；行程编码(run length encoded)；游程编码
class Solution:
    def decompressRLElist(self, nums):
        ans = list()
        for i in range(0, len(nums), 2):
            # ans.extend([nums[i + 1]] * nums[i])   主义错误部分
            ans.extend([nums[i + 1]] * nums[i])
        return ans

class Solution_God():
    # 分开两列表法  yes
    def decompressRLElist(self, nums):
        x=list(zip(nums[1::2], nums[::2]))
        print(x)
        for i,j in x:
            for _ in range(j):
                print(i,end=" ")
        return [i for i, j in zip(nums[1::2], nums[::2]) for _ in range(j)]
    # 使用两个for循环法  yes
    def decompressRLElist_(self,nums):
        for i in range(len(nums)) :
            for j in range(nums[i - 1]) :
                if i % 2 == 1:
                    print(nums[i],end=' ')
        print()
        return [nums[i] for i in range(len(nums)) for j in range(nums[i - 1]) if i % 2 == 1]
    # 花样sum法
    def decompressRLElist__(self, nums):
        # print(sum([[1,2,3]],[])    #  tip：维度下降   3->2   2->1  1维不行
        print(list(([b] * a for a, b in zip(nums[::2], nums[1::2]))))   #[[2], [4, 4, 4]]
        return sum(([b] * a for a, b in zip(nums[::2], nums[1::2])), [])



sol = Solution_God()
# print(sol.decompressRLElist([1, 2, 3, 4]))
# print(sol.decompressRLElist_([1, 2, 3, 4]))
print(sol.decompressRLElist__([1, 2, 3, 4]))

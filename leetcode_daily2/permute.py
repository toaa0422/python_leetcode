#回溯su算法框架
# result = []
# def backtrack(路径, 选择列表):
#     if 满足结束条件:
#         result.add(路径)
#         return
#     #core point
#     for 选择 in 选择列表:
#         做选择
#         backtrack(路径, 选择列表)
#         撤销选择
# permute   v. 改变……的次序，重新排列
class Solution1:
    def permute(self, nums) :
        def trackback(nums,track):
            if len(track) == len(nums):
                res.append(track[:]) # 需要传递下track的拷贝，否则对track的修改会影响到结果
                return

            # if len(nums)==len(track):
            #     res.append(nums[:])  #注意细节  track
            #     return
            for i in nums:
                if i in track:
                    continue
                track.append(i)
                trackback(nums,track)
                track.pop()
        res=[]
        track=[]
        trackback(nums,track)
        return res
#最爱的解
class Solution__:

    def permute(self, nums):
        def trackBack(nums,track):
            if len(track) == len(nums):
                res.append(track[:]) # 需要传递下track的拷贝，否则对track的修改会影响到结果
                return
            for i in nums:
                if i in track:
                    continue
                track.append(i)
                # print(track)
                trackBack(nums,track)
                track.pop()
        res = []
        track = []
        trackBack(nums,track)
        return res
class Solution():
    def permute(self,nums):
        res=[]
        def backtrack(nums,tmp):
            if not nums:
                res.append(tmp)
                return
            for i in range(len(nums)):
                backtrack(nums[:i]+nums[i+1:],tmp+[nums[i]])
        backtrack(nums,[])
        return res

#官方解
class Solution_:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def backtrack(first=0):
            # 所有数都填完了
            if first == n:
                res.append(nums[:])
            # for i in range(first, n):
            for i in range(first, n):
                # 动态维护数组
                nums[first], nums[i] = nums[i], nums[first]
                # 继续递归填下一个数
                backtrack(first + 1)
                # 撤销操作
                nums[first], nums[i] = nums[i], nums[first]

        n = len(nums)
        res = []
        backtrack()
        return res


s=Solution__()
print(s.permute([1,2,3]))

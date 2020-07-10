# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#个人喜欢的解,易懂!!
class MountainArray:
    def __init__(self, arr):
        self.arr = arr
        self.size = len(arr)

    def get(self, index: int) -> int:
        return self.arr[index]

    def length(self) -> int:
        return self.size


class Solution:

    # 特别注意：3 个辅助方法的分支出奇地一样，因此选中位数均选左中位数，才不会发生死循环

    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        size = mountain_arr.length()
        # 步骤 1：先找到山顶元素所在的索引
        mountaintop = self.__find_mountaintop(mountain_arr, 0, size - 1)
        # 步骤 2：在前有序且升序数组中找 target 所在的索引
        res = self.__find_from_sorted_arr(mountain_arr, 0, mountaintop, target)
        if res != -1:
            return res
        # 步骤 3：如果步骤 2 找不到，就在后有序且降序数组中找 target 所在的索引
        return self.__find_from_inversed_arr(mountain_arr, mountaintop + 1, size - 1, target)

    def __find_mountaintop(self, mountain_arr: 'MountainArray', l: int, r: int):
        # 返回山顶元素
        while l < r:
            mid = l + (r - l) // 2
            # 取左中位数，因为进入循环，数组一定至少有 2 个元素
            # 因此，左中位数一定有右边元素，数组下标不会发生越界
            if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
                # 如果当前的数比右边的数小，它一定不是山顶
                l = mid + 1
            else:
                r = mid
        # 根据题意，山顶元素一定存在，因此退出 while 循环的时候，不用再单独作判断
        return l

    def __find_from_sorted_arr(self, mountain_arr: 'MountainArray', l: int, r: int, target: int):
        # 在前有序且升序数组中找 target 所在的索引
        while l < r:
            mid = l + (r - l) // 2
            if mountain_arr.get(mid) < target:
                l = mid + 1
            else:
                r = mid
        # 因为不确定区间收缩成 1 个数以后，这个数是不是要找的数，因此单独做一次判断
        if mountain_arr.get(l) == target:
            return l
        return -1

    def __find_from_inversed_arr(self, mountain_arr: 'MountainArray', l: int, r: int, target: int):
        # 在后有序且降序数组中找 target 所在的索引
        while l < r:
            mid = l + (r - l) // 2
            # 与 __find_from_sorted_arr 方法不同的地方仅仅在于由原来的小于号改成大于号
            if mountain_arr.get(mid) > target:
                l = mid + 1
            else:
                r = mid
        if mountain_arr.get(l) == target:
            return l
        return -1


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 3, 1]
    mountain_array = MountainArray(arr)
    target = 3
    solution = Solution()
    res = solution.findInMountainArray(target, mountain_array)
    print('res', res)




# 官方解
"""________________________________________________________________________________________________________________"""
class Solution:
    # 查找峰值索引
    # 峰值两端分别二分查找
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        def binary_search(start, end, left=True):
            while start <= end:
                mid = (start + end) // 2
                val = mountain_arr.get(mid)
                if val == target:
                    return mid
                elif val > target:
                    if left:
                        end = mid - 1
                    else:
                        start = mid + 1
                else:
                    if left:
                        start = mid + 1
                    else:
                        end = mid - 1
            return -1
        n = mountain_arr.length()
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            val = mountain_arr.get(mid)
            if mid > 0 and val < mountain_arr.get(mid - 1):
                right = mid - 1
            elif mid < n - 1 and val < mountain_arr.get(mid + 1):
                left = mid + 1
            else:
                break
        index = binary_search(0, mid)
        if index != -1:
            return index
        return binary_search(mid + 1, n - 1, False)

class MountainArray:
    def __init__(self, arr):
        self.arr = arr

    def get(self, index: int) -> int:
        return self.arr[index]

    def length(self) -> int:
        return len(self.arr)

# if __name__ == '__main__':
#     # sol = Solution()
#     #
#     # array = [1, 2, 3, 9, 5, 3, 1]
#     # target = 3
#     # print(sol.findInMountainArray(target, MountainArray(array)))  # 2
#     #
#     # array = [0, 1, 2, 4, 2, 1]
#     # target = 3
#     # print(sol.findInMountainArray(target, MountainArray(array)))  # -1

"""________________________________________________________________________________________________________________"""


class Solution:
    # 简单粗暴
    def searchMatrix(self, matrix, target):
        for row in matrix:
            if target in row:
                return True

        return False


    # methods
    """
    1.二分法搜索
    2.搜索空间的缩减
    3.
    """

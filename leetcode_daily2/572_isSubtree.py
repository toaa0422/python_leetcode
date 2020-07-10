# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    #判断是否为子树, 这三个条件是或的关系。
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not s and not t:
            return True
        if not s or not t:
            return False
        return self.isSameTree(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)#注意 套用下面的函数

    # 是否是相同的树
    def isSameTree(self, s, t):
        if not s and not t:
            return True
        if not s or not t:
            return False
        return s.val == t.val and self.isSameTree(s.left, t.left) and self.isSameTree(s.right, t.right)
class Solution__:
    def identical(self, node_a, node_b):  # 判定两棵树是否相同
        if not node_a and not node_b:  # 两个 node 都为空为 True
            return True
        if node_a is None or node_b is None:  # 一方空，一方不空，为False
            return False
        # 否则说明两个 node 都非空，那么如果两个树相等必须满足3个条件，即当前 node 的值相等，且各自左右子树也对应相等
        return node_a.val == node_b.val and \
               self.identical(node_a.left, node_b.left) and \
               self.identical(node_a.right, node_b.right)

    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s:
            return False  # 边界，如果s为空直接返回False

        if self.identical(s, t):  # 若 s 和 t 对应的两棵树相同则返回True
            return True
        # 不然的话就继续探索 s 的左右子树是否和 t 相等
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)


s_root=TreeNode(3)
s_root.left=TreeNode(4)
s_root.right=TreeNode(5)
s_root.left.left=TreeNode(1)
s_root.left.right=TreeNode(2)
t_root=TreeNode(4)
t_root.left=TreeNode(1)
t_root.right=TreeNode(2)
sol=Solution()
print(sol.isSubtree(s_root,t_root))

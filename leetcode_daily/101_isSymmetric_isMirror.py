# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def isSymmetric(self, root) -> bool:
        def dfs(root1,root2):
            if root1==root2:return True
            if not root1 or not root2:return False
            if root1.val!=root2.val:return False
            return dfs(root1.left,root2.right) and dfs(root1.right,root2.left)
        if not root:return True
        return dfs(root.left,root.right)
# 左右指针遍历子树
class Solution_():
    def isSymmetric(self,root):
        return self.isMirror(root,root)
    def isMirror(self,p1,p2):
        if not p1 and not p2:
            return True
        if not p1 or not p2:
            return False
        return p1.val==p2.val and self.isMirror(p1.left,p2.right) and self.isMirror(p1.right,p2.left)
        # return (p1.val == p2.val) and isMirror(p1.left, p2.right) and isMirror(p1.right, p2.left)   注意细节
root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(2)
root.left.left=TreeNode(3)
root.left.right=TreeNode(4)
root.right.left=TreeNode(4)
root.right.right=TreeNode(3)
sol=Solution_()
print(sol.isSymmetric(root))
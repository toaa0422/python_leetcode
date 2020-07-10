# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def flatten(self, root):
        while root:
            if root.left:
                sub_left=root.left
                while sub_left.right:
                    sub_left=sub_left.right
                sub_left.right=root.right
                root.right=root.left
                root.left=None
            root=root.right
        return root
root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(5)
root.left.left=TreeNode(3)
root.left.right=TreeNode(4)
root.right.right=TreeNode(6)
sol=Solution()
print(sol.flatten(root))










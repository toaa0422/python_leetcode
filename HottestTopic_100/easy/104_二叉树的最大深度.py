# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # recursion
    def maxDepth(self, root: TreeNode) -> int:
        if not root:return 0
        else:
            left_height=self.maxDepth(root.left)
            right_height=self.maxDepth(root.right)
            return max(left_height,right_height)+1
    # iteration
    def maxDepth_(self, root: TreeNode) -> int:
        stack=[]
        if root:
            stack.append((1,root))
        depth=0
        while stack:
            cur_len,root=stack.pop()
            if root:
                depth=max(depth,cur_len)
                stack.append((cur_len+1,root.left))
                stack.append((cur_len+1,root.right))
        return depth
root=TreeNode(3)
root.left=TreeNode(9)
root.right=TreeNode(20)
root.right.left=TreeNode(15)
root.right.right=TreeNode(7)
sol=Solution()
print(sol.maxDepth(root))
print(sol.maxDepth_(root))

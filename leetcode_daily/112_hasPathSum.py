# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:  #根节点到叶子节点  ***
    # bfs   yes
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        import collections
        if not root:return False
        que_node=collections.deque([root])
        que_val=collections.deque([root.val])
        while que_node:
            cur=que_node.popleft()
            tmp=que_val.popleft()
            if not cur.left and not cur.right:
                if tmp==sum:return True
                continue
            if cur.left:
                que_node.append(cur.left)
                que_val.append(cur.left.val+tmp)
            if cur.right:
                que_node.append(cur.right)
                que_val.append(cur.right.val+tmp)
        return False
    # recursion   yes
    def hasPathSum_(self, root: TreeNode, sum: int) -> bool:
        if not root:return False
        if not root.left and not root.right:
            return sum==root.val
        return self.hasPathSum_(root.left,sum-root.val) or self.hasPathSum_(root.right,sum-root.val)





root=TreeNode(5)
root.left=TreeNode(4)
root.right=TreeNode(8)
root.left.left=TreeNode(11)
root.right.left=TreeNode(13)
root.right.right=TreeNode(4)
root.left.left.left=TreeNode(7)
root.left.left.right=TreeNode(2)
root.right.right.right=TreeNode(1)
sol=Solution()
# print(sol.hasPathSum(root,22))
print(sol.hasPathSum_(root,26))
# print(sol.hasPathSum(root,50))



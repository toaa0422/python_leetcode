# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # recursion
    def inorderTraversal(self,root):
        res=[]
        stack=[]
        p=root
        s=[]
        while p or stack:
            while p:
                stack.append(p)
                p=p.left
            p=stack.pop()
            res.append(p.val)
            p=p.right
            # if p:s.append(1)
            # else:s.append(0)
        # print(s)
        return res

root=TreeNode(1)
root.right=TreeNode(2)
root.right.left=TreeNode(3)


sol=Solution()
print(sol.inorderTraversal(root))


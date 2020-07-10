# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans=TreeNode(None)
        def dfs(root,p,q):
            if not root:return False
            lson=dfs(root.left,p,q)
            rson=dfs(root.right,p,q)
            if (lson and rson) or ((root.val==p.val or root.val==q.val)and(lson and rson)):
                ans=root
            return lson or rson or (root.val==p.val or root.val==q.val)
        dfs(root,p,q)
        return ans
class Solution_:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q: return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left: return right
        if not right: return left
        return root

class Solution__:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root: return root
        if root is p or root is q: return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right: return root
        if not left: return right
        if not right: return left

def preorder(root):
    if root:
        return root.val

    else:return None
#root = [3,5,1,6,2,0,8,null,null,7,4]
r1=TreeNode(3)
r2,r3=TreeNode(5),TreeNode(1)
r1.left=r2
r1.right=r3
r4,r5=TreeNode(6),TreeNode(2)
r2.left=r4
r2.right=r5
r6,r7=TreeNode(0),TreeNode(8)
r3.left,r3.right=r6,r7
r8,r9=TreeNode(7),TreeNode(4)
r5.left=r8
r5.right=r9
sol=Solution__()
x1,x2=TreeNode(5),TreeNode(1)
print(preorder(sol.lowestCommonAncestor(r1,x1,x2)))


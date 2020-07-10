class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.maxSum=float('-inf')
    def maxPathSum(self,root):
        def maxGain(node):
            if not node:return 0
            leftGain=max(maxGain(node.left),0)
            rightGain=max(maxGain(node.right),0)
            priceNewpath=node.val+leftGain+rightGain
            self.maxSum=max(self.maxSum,priceNewpath)
            return node.val+max(leftGain,rightGain)
        maxGain(root)
        return self.maxSum
"""
def dfs(root):
    if not root: return
    dfs(root.left)
    dfs(root.right)
"""
class Solution_:
    def maxPathSum(self,root):
        self.maxsum=float('-inf')
        def dfs(root):
            if not root:return 0
            left=dfs(root.left)
            right=dfs(root.right)
            self.maxsum=max(self.maxsum,left+right+root.val)
            return max(0,max(left,right)+root.val)
        print(dfs(root))
        dfs(root)
        return self.maxsum
class Solution11:
    def maxPathSum(self, root) -> int:
        self.maxsum = float('-inf')
        def dfs(root):
            if not root: return 0
            left = dfs(root.left)
            right = dfs(root.right)
            self.maxsum = max(self.maxsum, left + right + root.val)
            return max(0, max(left, right) + root.val)
        dfs(root)
        return self.maxsum


sol=Solution_()
root=TreeNode(-1)
root.left=TreeNode(-2)
root.right=TreeNode(-3)

s=TreeNode(-10)
x1=TreeNode(9)
x2=TreeNode(20)
x2.left=TreeNode(15)
x2.right=TreeNode(7)
s.left=x1
s.right=x2
print(sol.maxPathSum(s))
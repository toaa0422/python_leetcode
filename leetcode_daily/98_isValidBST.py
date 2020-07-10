class TreeNode():
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None

# 递归
class Solution:
    def isValidBST(self,root):
        def helper(node,lower=float('-inf'),upper=float('inf')):
            if not node:return True
            val =node.val
            if val<=lower or val>=upper:
                return False
            if not helper(node.right,val,upper):
                return False
            if not helper(node.left,lower,val):
                return False
            return True
        return helper(root)
class Solution_:
    def isValidBST(self,root):
        stack,inorder=[],float('-inf')
        while stack or root:
            while root:
                stack.append(root)
                root=root.left
            root=stack.pop()
            print(f'{root.val},{inorder}')
            if root.val <= inorder:
                return False
            inorder = root.val
            root = root.right

        return True


class Solution__:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        stack, inorder = [], float('-inf')

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            # 如果中序遍历得到的节点的值小于等于前一个 inorder，说明不是二叉搜索树
            if root.val <= inorder:
                return False
            inorder = root.val
            root = root.right

        return True


root=TreeNode(2)
root.left=TreeNode(1)
root.right=TreeNode(3)
sol=Solution_()
print(sol.isValidBST(root))

# s=float('-inf')
# print(1<=float('-inf'))
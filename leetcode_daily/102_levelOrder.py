# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def levelOrder(self,root):
        if not root:return []
        res=[]
        def add_to_result(level,node):
            if level>len(res)-1:
                res.append([])
            res[level].append(node.val)
            if node.left:
                add_to_result(level+1,node.left)
            if node.right:
                add_to_result(level+1,node.right)
        add_to_result(0,root)
        return res
#优化
class Solution_:
    def levelOrder(self,root):
        nodes=[(root,)]
        values=[]
        while nodes:
            values.append([r.val for n in nodes for r in n if r])
            nodes = [(r.left, r.right) for n in nodes for r in n if r]
        return values[:-1]


# iteration
class Solution__:
    def levelOrder(self,root):
        if not root:return []
        res=[]
        cur_level=[root]
        while cur_level:
            tmp=[]
            next_level=[]
            for node in cur_level:
                tmp.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            res.append(tmp)
            cur_level=next_level
        return res
#recursion
class Solution___:
    def levelOrder(self,root):
        res=[]
        def helper(root,depth):
            if not root:return
            if len(res)==depth:
                res.append([])
            res[depth].append(root.val)
            helper(root.left,depth+1)
            helper(root.right,depth+1)
        helper(root,0)
        return res



root=TreeNode(3)
root.left=TreeNode(9)
root.right=TreeNode(20)
root.right.left=TreeNode(15)
root.right.right=TreeNode(7)


sol=Solution___()
print(sol.levelOrder(root))
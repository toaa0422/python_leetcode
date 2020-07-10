#Diameter  直径
#2020/05/01
class BinaryTree():
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
#官方解
class Solution():
    def diameterOfBinaryTree(self,root):
        self.ans=1
        def depth(node):
            if not node:return 0    #细节   error>>>if not root
            l=depth(node.left)
            # print(f'l={l}')
            r=depth(node.right)
            # print(f'r={r}')
            self.ans=max(self.ans,l+r+1)
            return max(l,r)+1
        depth(root)
        return self.ans-1

#感觉不用+1和-1这些操作，这样写也能通过而且容易理解点
class Solution_():
    def diameterOfBinaryTree(self,root):
        self.max_d = 0
        def depth(node):
            if not node: return 0
            l = depth(node.left)
            r=depth(node.right)
            self.max_d=max(l+r,self.max_d)
            return max(l,r)+1
        depth(root)
        return self.max_d

class Solution__():
    def diameterOfBinaryTree(self,root):
        if not root:return 0
        res=0
        def maxDepth(root):
            nonlocal res
            if not root:
                return -1
            left=maxDepth(root.left)+1
            right=maxDepth(root.right)+1
            res=max(res,right+left)
            return max(left,right)
        maxDepth(root)
        return res
r1=BinaryTree(1)
r2=BinaryTree(2)
r3=BinaryTree(3)
r4=BinaryTree(4)
r5=BinaryTree(5)
r1.left=r2
r1.right=r3
r2.left=r4
r2.right=r5
sol=Solution__()
print(sol.diameterOfBinaryTree(r1))




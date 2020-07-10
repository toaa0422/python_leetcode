# 先序遍历法
# 层次遍历法
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Codec:
    def serialize(self,root):
        def dfs(node):
            if node:
                vals.append(str(node.val))
                dfs(node.left)
                dfs(node.right)
            else:vals.append('#')
        vals=[]
        dfs(root)
        return ','.join(vals)
    def deserialize(self,data):
        def dfs():
            v=next(vals)   #next() 函数要和生成迭代器的iter() 函数一起使用。
            # print(v)
            if v=='#':
                return None
            node=TreeNode(int(v))
            node.left=dfs()
            node.right=dfs()
            # print('111')
            return node
        vals=iter(data.split(','))
        print(next(vals))
        return dfs()
def PreOrder(root):
    '''打印二叉树(先序)'''
    if root == None:return
    print(root.val, end=' ')
    PreOrder(root.left)
    PreOrder(root.right)
class CodeC:
    def serialize(self,root):
        s=''
        queue=[]
        queue.append(root)
        while queue:
            root=queue.pop(0)
            if root:
                s+=str(root.val)
                queue.append(root.left)
                queue.append(root.right)
            else:s+='n'
            s+=' '
        return s
    def deserialize(self,data):
        tree=data.split()
        if tree[0]=='n':
            return None
        queue=[]
        root=TreeNode(int(tree[0]))
        queue.append(root)
        i=1
        while queue:
            cur=queue.pop()
            if cur==None:continue
            cur.left=TreeNode(int(tree[i])) if tree[i]!='n' else None
            cur.right=TreeNode(int(tree[i+1])) if tree[i+1]!='n' else None
            i+=2
            queue.append(cur.left)
            queue.append(cur.right)
        return root
def BFS(root):
    if root == None:
        return
    # queue队列，保存节点
    queue = []
    # res保存节点值，作为结果
    # vals = []
    queue.append(root)

    while queue:
        # 拿出队首节点
        currentNode = queue.pop(0)
        # vals.append(currentNode.val)
        print(currentNode.val, end=' ')
        if currentNode.left:
            queue.append(currentNode.left)
        if currentNode.right:
            queue.append(currentNode.right)
    # return vals





bt=TreeNode(1)
bt.left=TreeNode(2)
bt.right=TreeNode(3)
# bt.left.left=None
# bt.left.right=None
bt.right.left=TreeNode(4)
bt.right.right=TreeNode(5)

codec=Codec()
print(type(codec.serialize(bt)))
PreOrder(codec.deserialize(codec.serialize(bt)))
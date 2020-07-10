class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution_:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        ans = {-1: TreeNode(0)}     #字典初始化
        def addTree(v, p):          #添加树函数
            ans[p] = TreeNode(int(v))
            if not ans[p - 1].left: #左子树不存在就加在左边
                ans[p - 1].left = ans[p]
            else:                   #反之加在右边
                ans[p - 1].right = ans[p]
        val, dep = '', 0            #值和对应深度初始化
        for c in S:
            if c != '-':
                val += c            #累加字符来获得数字
            elif val:               #如果是‘-’且存在val
                addTree(val, dep)   #就把累加好的数字和对应深度添加进树
                val, dep = '', 1    #值和对应深度重新初始化
            else:
                dep += 1            #连续的‘-’只加深度不加值
        addTree(val, dep)           #末尾剩余的数字也要加进树
        return ans[0]

class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        path, pos = list(), 0
        # print(len(S))
        while pos < len(S):
            level = 0
            while S[pos] == '-':
                level += 1
                pos += 1
            # print(level)
            # print(pos)
            value = 0
            while pos < len(S) and S[pos].isdigit():
                value = value * 10 + (ord(S[pos]) - ord('0'))        #49    0>>48
                # print(value)
                pos += 1
            node = TreeNode(value)
            if level == len(path):
                if path:
                    path[-1].left = node
            else:
                path = path[:level]
                path[-1].right = node
            path.append(node)
        return path[0]

def preorder(root):
    if not root:return
    print(root.val,end=' ')
    preorder(root.left)
    preorder(root.right)
def BFS(root):
    '''广度优先'''
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


sol=Solution()
preorder(sol.recoverFromPreorder("1-2--3--4-5--6--7"))
print('\n')
BFS((sol.recoverFromPreorder("1-2--3--4-5--6--7")))
# print(preorder(sol.recoverFromPreorder("1-2--3---4-5--6---7")))
# print(preorder(sol.recoverFromPreorder("1-401--349---90--88")))

# print(ord('0'))
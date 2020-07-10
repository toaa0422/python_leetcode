# dict.setdefault(key, default=None)
# params:
# key -- 查找的键值。
# default -- 键不存在时，设置的默认键值。

class TreeNode():
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None


#dfs

class Solution():
    def rightSideView(self,root):
        rightmost_val_at_depth=dict()
        max_depth=-1
        stack=[(root,0)]
        while stack:
            node,depth=stack.pop()
            if node is not None:
                max_depth=max(max_depth,depth)
                rightmost_val_at_depth.setdefault(depth,node.val)
                stack.append((node.left,depth+1))
                stack.append((node.right,depth+1))
        return [rightmost_val_at_depth[depth] for depth in range(max_depth+1)]


#bfs
from collections import deque
class Solution_():
    def rightSideView(self,root):
        rightmost_value_at_depth = dict()  # 深度为索引，存放节点
        max_depth = -1
        queue = deque([(root, 0)])
        while queue:
            node,depth=queue.popleft()
            if node is not None:
                max_depth=max(max_depth,depth)
                rightmost_value_at_depth[depth]=node.val
                queue.append((node.left,depth+1))
                queue.append((node.right,depth+1))
        return [rightmost_value_at_depth[depth] for depth in range(max_depth+1)]




a=TreeNode(1)
a.left=TreeNode(2)
a.right=TreeNode(3)
a.left.left=None
a.left.right=TreeNode(5)
a.right.left=None
a.right.right=TreeNode(4)
s=Solution_()
print(s.rightSideView(a))





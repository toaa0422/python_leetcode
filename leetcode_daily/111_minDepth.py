class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class BinaryTree(object):
    def __init__(self, root=None):
        self.root = root
    def add(self, val):
        node = Node(val)
        if self.root == None:
            self.root = node
        else:
            queue = []
            queue.append(self.root)
            while queue:
                cur = queue.pop(0)
                if cur.left == None:
                    cur.left = node
                    return
                elif cur.right == None:
                    cur.right = node
                    return
                else:
                    queue.append(cur.left)
                    queue.append(cur.right)
    def BFS(self, root):
        """利用队列实现树的层次遍历"""
        if root == None:
            return
        queue = []
        queue.append(root)
        while queue:
            node = queue.pop(0)
            print(node.val, end=" ")
            if node.left != None:
                queue.append(node.left)
            if node.right != None:
                queue.append(node.right)
    def preorder(self,root):
        if not root:
            return
        print(root.val,end=' ')
        self.preorder(root.left)
        self.preorder(root.right)
    #递归求解
    def minDepth(self, root):
        if  root==None: return 0
        if  root.left==None: return self.minDepth(root.right) + 1
        if  root.right==None: return self.minDepth(root.left) + 1
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
    "method:Depth-first search iteration"
    def minDepth_(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        else:
            stack, min_depth = [(1, root), ], float('inf')

        while stack:
            depth, root = stack.pop()
            children = [root.left, root.right]
            if not any(children):
                min_depth = min(depth, min_depth)
            for c in children:
                if c:
                    stack.append((depth + 1, c))

        return min_depth

if __name__ == "__main__":

    t = BinaryTree()
    all=Node(1)
    all.left=Node(2)
    print(t.BFS(all))
    print(t.minDepth(all))
    print(t.minDepth_(all))









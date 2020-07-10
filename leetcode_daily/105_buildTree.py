class TreeNode():
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None
class Solution:
    def buildTree(self, preorder, inorder) -> TreeNode:
        def myBuildTree(preorder_left: int, preorder_right: int, inorder_left: int, inorder_right: int):
            if preorder_left > preorder_right:
                return None

            # 前序遍历中的第一个节点就是根节点
            preorder_root = preorder_left
            # 在中序遍历中定位根节点
            inorder_root = index[preorder[preorder_root]]

            # 先把根节点建立出来
            root = TreeNode(preorder[preorder_root])
            # 得到左子树中的节点数目
            size_left_subtree = inorder_root - inorder_left
            # 递归地构造左子树，并连接到根节点
            # 先序遍历中「从 左边界+1 开始的 size_left_subtree」个元素就对应了中序遍历中「从 左边界 开始到 根节点定位-1」的元素
            root.left = myBuildTree(preorder_left + 1, preorder_left + size_left_subtree, inorder_left,
                                    inorder_root - 1)
            # 递归地构造右子树，并连接到根节点
            # 先序遍历中「从 左边界+1+左子树节点数目 开始到 右边界」的元素就对应了中序遍历中「从 根节点定位+1 到 右边界」的元素
            root.right = myBuildTree(preorder_left + size_left_subtree + 1, preorder_right, inorder_root + 1,
                                     inorder_right)
            return root

        n = len(preorder)
        # 构造哈希映射，帮助我们快速定位根节点
        index = {element: i for i, element in enumerate(inorder)}
        print(index)
        return myBuildTree(0, n - 1, 0, n - 1)
def bfs(root):
    if not root:return
    queue=[]
    queue.append(root)
    while queue:
        cur_node=queue.pop(0)
        print(cur_node.val)
        if cur_node.left:
            queue.append(cur_node.left)
        if cur_node.right:
            queue.append(cur_node.right)

# 个人最爱,简洁易懂
# 解决本题需要牢牢掌握先序遍历和中序遍历的含义，以及递归。
#
# 先序遍历：根节点，左子树的先序遍历，右子树的先序遍历。
# 中序遍历：左子树的中序遍历，根节点，右子树的中序遍历。
#
# 作者：fuxuemingzhu
# 链接：https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/solution/yi-ben-ti-wei-li-bang-zhu-li-jie-di-gui-by-fuxuemi/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
class Solution_:
    def buildTree(self,preorder,inorder):
        if not preorder or not inorder:
            return None
        root=TreeNode(preorder[0])
        index=inorder.index(preorder[0])
        root.left=self.buildTree(preorder[1:index+1],inorder[:index])
        root.right=self.buildTree(preorder[index+1:],inorder[index+1:])
        return root

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
sol=Solution_()
bfs(sol.buildTree(preorder,inorder))

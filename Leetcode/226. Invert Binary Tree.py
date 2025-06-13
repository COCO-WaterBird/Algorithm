class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        root.left, root.right = root.right, root.left  # 交换左右儿子
        self.invertTree(root.left)  # 翻转左子树
        self.invertTree(root.right)  # 翻转右子树
        return root
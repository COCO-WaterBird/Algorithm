def inorderTraversal(self, root):
    res = []  # 1️⃣ 初始化一个空列表 res，用于存储遍历结果
    if root:  # 2️⃣ 检查当前节点是否为空（递归终止条件）
        res = self.inorderTraversal(root.left)  # 3️⃣ 递归遍历左子树
        res.append(root.data)  # 4️⃣ 访问当前节点（中序遍历：先左，再根，后右）
        res = res + self.inorderTraversal(root.right)  # 5️⃣ 递归遍历右子树
    return res  # 6️⃣ 返回遍历结果

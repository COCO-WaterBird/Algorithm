def PostorderTraversal(self, root):
    res = []  # 1️⃣ 初始化一个空列表 res，用于存储遍历结果
    if root:  # 2️⃣ 检查当前节点是否为空（递归终止条件）
        res = self.PostorderTraversal(root.left)  # 3️⃣ 递归遍历左子树
        res = res + self.PostorderTraversal(root.right)  # 4️⃣ 递归遍历右子树
        res.append(root.data)  # 5️⃣ 访问当前节点（后序遍历：左 → 右 → 根）
    return res  # 6️⃣ 返回遍历结果

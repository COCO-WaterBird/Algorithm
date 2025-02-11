def PreorderTraversal(self, root):
    res = []  # 1️⃣ 初始化一个空列表，用于存储遍历结果
    if root:  # 2️⃣ 检查当前节点是否为空（递归终止条件）
        res.append(root.data)  # 3️⃣ 访问当前节点（前序遍历：先访问根）
        res = res + self.PreorderTraversal(root.left)  # 4️⃣ 递归遍历左子树
        res = res + self.PreorderTraversal(root.right) # 5️⃣ 递归遍历右子树
    return res  # 6️⃣ 返回遍历结果

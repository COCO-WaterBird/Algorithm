class Node:
    def __init__(self, data):
        self.left = None  # 初始化左子节点为空
        self.right = None  # 初始化右子节点为空
        self.data = data  # 存储节点数据

    def insert(self, data):
        """插入新节点"""
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def PrintTree(self):
        """中序遍历打印二叉搜索树"""
        if self.left:
            self.left.PrintTree()
        print(self.data, end=" ")  # 防止换行
        if self.right:
            self.right.PrintTree()

# 创建根节点
root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)

# 按照中序遍历输出
root.PrintTree()

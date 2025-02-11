class Node:
    def __init__(self, data):
        self.left = None  # 初始化左子节点为空
        self.right = None  # 初始化右子节点为空
        self.data = data  # 存储节点数据

    def PrintTree(self):
        print(self.data)  # 打印当前节点数据


# https://www.bilibili.com/video/BV1Ks411579J?spm_id_from=333.788.recommend_more_video.0&vd_source=11dc9b49e98d5afbe2906d4ee7b6d0f7
class Node:
    def __init__(self, data):
        self.left = None  # 初始化左子节点为空
        self.right = None  # 初始化右子节点为空
        self.data = data  # 存储节点数据

    def PrintTree(self):
        print(self.data)  # 打印当前节点数据


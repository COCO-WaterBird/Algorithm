class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        path = []

        def dfs(i: int, t: int) -> None:
            d = k - len(path)  # 还要选 d 个数
            if t < 0 or t > (i * 2 - d + 1) * d // 2:  # 剪枝
                return
            if d == 0:  # 找到一个合法组合
                ans.append(path.copy())
                return

            # 不选 i
            if i > d:
                dfs(i - 1, t)

            # 选 i
            path.append(i)
            dfs(i - 1, t - i)
            path.pop()

        dfs(9, n)
        return ans


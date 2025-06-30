class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        path = []

        def dfs(i: int) -> None:
            d = k - len(path)
            if d == 0:
                ans.append(path.copy())
                return

            if i < d:
                return

            if i > d:
                dfs(i - 1)

            path.append(i)
            dfs(i - 1)
            path.pop()

        dfs(n)
        return ans

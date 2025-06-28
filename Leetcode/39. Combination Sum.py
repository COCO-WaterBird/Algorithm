class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        path = []

        def dfs(i: int, left: int) -> None:
            if left == 0:
                ans.append(path.copy())
                return

            if i == len(candidates) or left < candidates[i]:
                return

            dfs(i + 1, left)

            path.append(candidates[i])
            dfs(i, left - candidates[i])
            path.pop()

        dfs(0, target)
        return ans

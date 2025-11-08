class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        @cache  # 缓存装饰器，避免重复计算 dfs（一行代码实现记忆化）
        def dfs(i: int, j: int) -> int:
            if i < 0:
                return 0 if j == 0 else -inf
            if nums[i] > j:
                return dfs(i - 1, j)
            return max(dfs(i - 1, j), dfs(i - 1, j - nums[i]) + 1)

        ans = dfs(len(nums) - 1, target)
        dfs.cache_clear()  # 防止爆内存
        return ans if ans > 0 else -1
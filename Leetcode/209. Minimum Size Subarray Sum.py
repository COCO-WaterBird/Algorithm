class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        ans = n+1  # inf
        s = 0
        left = 0
        for right, x in enumerate(nums):  # x: nums[right]
            s += x
            # left <= right and
            while s - nums[left] >= target:
                s -= nums[left]
                left += 1
            if s >= target:
                ans = min(ans, right-left+1)
        return ans if ans <= n else 0  # ans <= n ? ans : 0;
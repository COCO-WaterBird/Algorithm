class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()  # 排序：O(n log n)
        n = len(nums)

        # 两种情况取max
        return max(
            nums[n - 1] * nums[n - 2] * nums[n - 3],  # 最大的三个
            nums[0] * nums[1] * nums[n - 1]  # 两负一正
        )
# 时间： O(n log n)
# 空间： O(1)
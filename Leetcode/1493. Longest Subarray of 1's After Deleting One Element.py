class Solution:
    def longestSubarray(self, nums: List[int]) -> int: #返回删除一个元素后，最长全1子数组的长度
        ans = cnt0 = left = 0
        for right, x in enumerate(nums):
            cnt0 += 1 - x
            while cnt0 > 1:
                cnt0 -= 1 - nums[left]
                left += 1
            ans = max(ans, right - left)
        return ans

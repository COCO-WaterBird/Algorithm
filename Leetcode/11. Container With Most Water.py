class Solution:
    def maxArea(self, height: list[int]) -> int:
        ans = 0
        left, right = 0, len(height) - 1
        while left < right:
            area =  (right - left) * min(height[left], height[right])
            ans = max(ans, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return ans

s = Solution()
result = s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
print(result)
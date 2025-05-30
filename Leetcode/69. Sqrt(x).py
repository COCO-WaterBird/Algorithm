class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        left, right = 1, x//2
        while left <= right:
            mid = left + (right - left)//2
            if mid > x//mid:
                right = mid -1
            else:
                left = mid + 1
        return left - 1

s = Solution()
result1 =s.mySqrt(x = 4)
result2 =s.mySqrt(x = 8)
print(result1, result2)
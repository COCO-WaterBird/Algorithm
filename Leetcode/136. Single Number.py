class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        ans = 0
        for num in nums:
            ans ^= num
        return ans

s = Solution()
result1 = s.singleNumber([4,1,2,1,2])
result2 = s.singleNumber([1])
print(result1, result2)
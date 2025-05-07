class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        lookup = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in lookup:
                return[lookup[complement], i]
            lookup[num] = i

s = Solution()
result = s.twoSum([2,7,11,15],9)
print(result)
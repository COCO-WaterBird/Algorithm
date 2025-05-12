class Solution:
    def findMissingRanges(self, nums: list[int], lower: int, upper: int) -> list[list[int]]:
        n = len(nums)
        missing_ranges = []

        if n == 0:
            return[[lower,upper]]

        if lower < nums[0]:
            missing_ranges.append([lower, nums[0]-1])

        for i in range(n - 1):
            if nums[i+1] - nums[i] > 1:
                missing_ranges.append([nums[i]+1, nums[i+1]-1])

        if upper > nums[n-1]:
            missing_ranges.append([nums[n-1]+1, upper])
        return missing_ranges

s = Solution()
result1 = s.findMissingRanges(nums=[0,1,3,50,75], lower=0, upper=99)
result2 = s.findMissingRanges(nums=[-1], lower=-1, upper=-1)
print(result1, result2)
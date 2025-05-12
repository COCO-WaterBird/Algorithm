class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        l = len(nums)
        if l == 0:
            return []
        nums.append(float('inf'))
        res, start = [], 0
        for i in range(l):
            if nums[i+1] != nums[i] + 1:
                res.append(str(nums[i]) if i == start else "%s->%s" % (nums[start], nums[i]))
                start = i + 1
        return res

s = Solution()
result1 = s.summaryRanges([0,1,2,4,5,7])
result2 = s.summaryRanges([0,2,3,4,6,8,9])
print(result1, result2)
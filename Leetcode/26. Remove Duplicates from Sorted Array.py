class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0
        j = 0

        for i in range(len(nums)):
            if nums[j] != nums[i]:
                j += 1
                nums[j] = nums[i]

        return j+1

s = Solution()
result = s.removeDuplicates([0,0,1,1,1,2,2,3,3,4])
print(result)
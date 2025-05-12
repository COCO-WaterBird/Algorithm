class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j, n = 0, 0, len(nums)
        while i < n:
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1
            i += 1
        while j < n:
            nums[j] = 0
            j += 1
        return nums

s = Solution()
result1 = s.moveZeroes([0,1,0,3,12])
result2 = s.moveZeroes([0])
print(result1, result2)
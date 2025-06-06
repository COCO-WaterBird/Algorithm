from multiprocessing.connection import answer_challenge
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                total =  nums[i] + nums[left] + nums[right]

                if total == 0:
                    ans.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else :
                    right -= 1
        return ans

s = Solution()
result1 = s.threeSum([-1,0,1,2,-1,-4])
result2 = s.threeSum([0,1,1])
print(result1, result2)
import collections

class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)

        lookup = collections.defaultdict(int)
        for i in nums1:
            lookup[i] += 1

        result = []
        for i in nums2:
            if lookup[i] > 0:
                result += [i]
                lookup[i] -= 1

        return result

s = Solution()
result1 = s.intersect(nums1 = [4,9,5], nums2 = [9,4,9,8,4])
print(result1)
class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        if len(nums1) > len(nums2):
            return self.intersection(nums2, nums1)

        lookup = set()
        for i in nums1:
            lookup.add(i)

        result = []
        for i in nums2:
            if i in lookup:
                result.append(i)
                lookup.discard(i)

        return result

s = Solution()
result1 = s.intersection(nums1 = [4, 9, 5], nums2 = [9, 4, 9, 8, 4])
result2 = s.intersection(nums1 = [1, 2, 2, 1], nums2 = [2, 2])
print(result1, result2)

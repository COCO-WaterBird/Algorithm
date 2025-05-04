class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # Initialize three pointers: i points to the last valid element of nums1,
        # j points to the last element of nums2
        i, j, k = m - 1, n - 1, m + n - 1

        # Merge from the end to the beginning
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        # return nums1

s = Solution()
nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
m = 3
n = 3
s.merge(nums1, m, nums2, n)
print(nums1)
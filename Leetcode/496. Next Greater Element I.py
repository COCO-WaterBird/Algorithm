class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = {}
        s = []
        for n in nums2[::-1]:
            while s and n >= s[-1]:
                s.pop()
            res[n] = s[-1] if s else -1
            s.append(n)
        return [res[n] for n in nums1]

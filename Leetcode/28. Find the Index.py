class Solution:
    def search(self, haystack, needle) -> int:
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1

s = Solution()
result1 = s.search(haystack = "sadbutsad", needle = "sad")
result2 = s.search(haystack = "leetcode", needle = "leeto")
print(result1, result2)

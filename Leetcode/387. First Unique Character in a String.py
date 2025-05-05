class Solution:
    def firstUniqChar(self, s: str) -> int:
        from collections import Counter
        lookup = Counter(s)
        for i, c in enumerate(s):
            if lookup[c] == 1:
                return i
            
        return -1

s = Solution()
print(s.firstUniqChar('loveleetcode'))
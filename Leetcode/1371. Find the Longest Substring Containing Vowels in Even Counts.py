class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        pos = {0: -1}  
        status = 0
        ans = 0
        for i, c in enumerate(s):
            if c in 'aeiou':
                bit = 'aeiou'.index(c)
                status ^= (1 << bit)
            if status in pos:
                ans = max(ans, i - pos[status])
            else:
                pos[status] = i
        return ans
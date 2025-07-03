from collections import Counter
from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        cnt_p = Counter(p)
        cnt_s = Counter()
        for right, c in enumerate(s):
            cnt_s[c] += 1
            left = right - len(p) + 1
            if left < 0:
                continue
            if cnt_s == cnt_p:
                ans.append(left)
            cnt_s[s[left]] -= 1
        return ans

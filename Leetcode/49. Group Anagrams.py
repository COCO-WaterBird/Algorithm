from collections import defaultdict
# from typing import List

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        dic = defaultdict(list)
        for s in strs:
            key = ''.join(sorted(s))
            dic[key].append(s)
        return list(dic.values())

s = Solution()
print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lookup = {}

        for i in s:
            if i not in lookup:
                lookup[i] = 1
            else:
                lookup[i] += 1

        for j in t:
            if j not in lookup:
                return False
            else:
                lookup[j] -= 1

        for k in lookup:
            if lookup[k] != 0:
                return False

        return True

s = Solution()
print(s.isAnagram("anagram","nagaram"))
print(s.isAnagram("anagram","nagara"))
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        str = str.split(" ")
        if len(pattern) != len(str):
            return False

        dic1, dic2 = {}, {}
        for p, w in zip(pattern, str):
            if p not in dic1:
                dic1[p] = w
            elif dic1[p] != w:
                return False

            if w not in dic2:
                dic2[w] = p
            elif dic2[w] != p:
                return False

        return True
s = Solution()
print(s.wordPattern(patt    ern = "abba", str = "dog cat cat dog"))
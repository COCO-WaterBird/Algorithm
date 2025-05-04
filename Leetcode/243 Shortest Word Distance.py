class Solution:
    def shortestDistance(self, wordsDict: list[str], word1: str, word2: str) -> int:
        dist = float("inf")
        i, index1, index2 = 0, None, None
        while i < len(wordsDict):
            if wordsDict[i] == word1:
                index1 = i
            elif wordsDict[i] == word2:
                index2 = i

            if index1 is not None and index2 is not None:
                dist = min(dist, abs(index1 - index2))
            i += 1
        return dist

s = Solution()
wordsDict = ["practice", "makes", "perfect", "coding", "makes"]
word1 = "makes"
word2 = "coding"
print(s.shortestDistance(wordsDict, word1, word2))

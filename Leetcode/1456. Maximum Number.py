class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        ans = vowel = 0 #ans: 记录最大元音字母个数, vowel: 记录当前窗口中的元音字母个数
        for i, c in enumerate(s):
            # 1. 进入窗口
            if c in "aeiou":
                vowel += 1
            if i < k - 1:  # 窗口大小不足 k
                continue
            # 2. 更新答案
            ans = max(ans, vowel)
            # 3. 离开窗口
            if s[i - k + 1] in "aeiou":
                vowel -= 1
        return ans

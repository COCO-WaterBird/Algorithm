class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n, m = len(s1), len(s2)
        if n + m != len(s3):
            return False

        prev = [False] * (m + 1)
        for i in range(n, -1, -1):
            dp = [False] * (m + 1)
            for j in range(m, -1, -1):
                if i == n and j == m:
                    dp[j] = True
                elif i == n:
                    dp[j] = s2[j:] == s3[i + j:]
                elif j == m:
                    dp[j] = s1[i:] == s3[i + j:]
                else:
                    # 优化：消除重复逻辑，用单一表达式处理所有情况
                    c = s3[i + j]
                    dp[j] = ((s1[i] == c and prev[j]) or
                             (s2[j] == c and dp[j + 1]))
            prev = dp
        return prev[0]
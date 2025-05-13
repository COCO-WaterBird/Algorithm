class Solution:
    def isHappy(self, n: int) -> bool:
        d = {}
        while True:
            res = 0
            while n > 0:
                res += ( n%10 ) ** 2
                n = n // 10

            n = res
            if res == 1:
                return True
            elif res in d:
                return False
            else:
                d[n] = 1

sol = Solution()
sol.isHappy(19)
print(sol.isHappy(19))
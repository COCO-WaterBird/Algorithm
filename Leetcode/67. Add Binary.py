class Solution:
    def addBinary(self, a: str, b: str) -> str:
        def add(x, y, carry):
            s = x + y + carry
            return (s // 2, s % 2)

        ml = max(len(a), len(b))
        res = ''
        carry = 0
        a = a.rjust(ml, '0')
        b = b.rjust(ml, '0')

        for i in range(ml - 1, -1, -1):
            carry, s = add(int(a[i]), int(b[i]), carry)
            res = str(s) + res

        return '1' + res if carry else res

s = Solution()
result = s.addBinary(a = "111", b = "1")
print(result)
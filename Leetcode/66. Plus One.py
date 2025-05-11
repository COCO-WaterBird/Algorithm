class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        for i in reversed(range(len(digits))):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        digits[0] = 1
        digits.append(0)
        return digits

s = Solution()
result1 = s.plusOne([4,3,2,1])
result2 = s.plusOne([9,9,9,9])
print(result1, result2)
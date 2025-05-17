class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            while not s[i].isalnum():
                i += 1
            while not s[j].isalnum():
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True

s = Solution()
result1 = s.isPalindrome("A man, a plan, a canal: Panama")
result2 = s.isPalindrome("race a car")
print(result1, result2)
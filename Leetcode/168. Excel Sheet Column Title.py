from pyparsing import results


class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        result, num = "", n

        while num:
            result += chr((num - 1) % 26 + ord('A'))
            num = (num - 1) // 26

        return result[::-1]

s = Solution()
result = s.convertToTitle(705)
print(result)
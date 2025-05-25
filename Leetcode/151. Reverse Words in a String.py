class Solution:
    def reverseWords(self, s: str) -> str:
        if s == '':
            return self

        ls = s.split()

        # 两种写法都可
        # if ls == []:
        if ls == '':
            # return ls
            return ''

        result = ''
        for i in range(len(ls) - 1):
            result += ls[len(ls) - 1 - i] + " "

        result += ls[0]

        return result

s = Solution()
print(s.reverseWords("  hello world  "))
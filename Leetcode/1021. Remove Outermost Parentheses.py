class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res, level = "", 0
        for c in s:
            if c == ')':
                level -= 1
            if level:
                res += c
            if c == '(':
                level += 1
        return res


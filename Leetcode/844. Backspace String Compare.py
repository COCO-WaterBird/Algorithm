class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def dealBackspace(string):
            stack = []
            for ch in string:
                if ch == '#':
                    if stack:
                        stack.pop()
                else:
                    stack.append(ch)
            return stack

        return dealBackspace(s) == dealBackspace(t)

class Solution:
   def evalRPN(self, tokens: List[str]) -> int:
       s = []
       for token in tokens:
           if token[-1] not in '+-*/':
               s.append(int(token))
           else:
               n2 = s.pop()
               n1 = s.pop()
               s.append(int(eval(f'{n1}{token}{n2}')))
       return s[-1]
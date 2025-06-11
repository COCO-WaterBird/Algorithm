class Solution:
   def simplifyPath(self, path: str) -> str:
       result = []
       path_list = path.split('/')
       for p in path_list:
           if p:
               if p == '..':
                   if result:
                       result.pop()
               elif p == '.':
                   continue
               else:
                   result.append(p)
       res = '/' + '/'.join(result)
       return res
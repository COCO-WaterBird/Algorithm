# Case1
# def f(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return f(n-1) + f(n-2)
#
# for i in range(10):
#     print("f({}) = {}".format(i, f(i)))
#     print("f(" + str(i) + ") = " + str(f(i)))

# Case2
# def f(n,memo={}):
#     if n in memo:
#         return memo[n]
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         ans = f(n-1) + f(n-2)
#         memo[n] = ans
#         return ans
#
# print(f(100,{}))

# Case3

print(int("8") > 7)          # 把字符串 "8" 转换为整数后判断是否大于 7
print(str(111) == 111)       # 比较字符串 "111" 和整数 111 是否相等
print(bool(-1))              # 将 -1 转换为布尔值
print(bool(0))               # 将 0 转换为布尔值
print(bool(""))              # 将空字符串转换为布尔值
print(bool("你好"))          # 将非空字符串 "你好" 转换为布尔值
print(True == True)          # 比较 True 和 True 是否相等
print(True == False)         # 比较 True 和 False 是否相等
print(bool("") == bool(0))   # 比较空字符串转换的布尔值和 0 转换的布尔值是否相等

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
# 递归函数（自己调用自己）

# 对0~n 的数求和


def sum(n):
    if n == 0:
        return 0
    else:
        return n + sum(n - 1)

print(sum(6))

#阶乘
def mutiply(n):
    if n == 1:
        return 1
    elif n==0:
        return 0
    else:
        return n*mutiply(n-1)

print(mutiply(3))
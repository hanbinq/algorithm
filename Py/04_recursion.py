
"""
递归
利用函数编写斐波那契数列：
这样一个数列：0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55
"""


# 实现方法一：根据这一特性，可采用最简单的方法计算该项，循环计算每项的值
def fibo(num):
    a = 0
    b = 1
    i = 0

    while i < num:
        print(a)
        a, b = b, a+b
        i += 1

# fibo(10)


# 实现方式二：考虑到从第三项开始，每一项的值都为前面两项的和，可以使用递归的方法计算
def recur_fibo(n):
    '''递归函数
    输出斐波那契数列'''
    if n < 0:
        print("输入正整数")
    elif n <= 1:
        return n
    else:
        return (recur_fibo(n - 1) + recur_fibo(n - 2))


nterms = 10
for i in range(nterms):
    print(recur_fibo(i))



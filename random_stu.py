import random

# 1.random.random()
# 用户生成一个0到1的随机浮点数 0<=n<1.0
print(random.random())


# 2.random.uniform(a, b)
# 用户生成一个指定范围内的随机浮点数，两个参数其中一个是上限，一个是下限
print(random.uniform(1, 10))
print(random.uniform(10, 1))


# 3.random.randint(a, b)
# 用于生成一个指定范围的整数。其中参数a是下限，参数b是上限，生成随机数n: a<=n<=b
print(random.randint(1, 10))

# 4.random.randrange([start],stop[,step])
print(random.randrange(10, 30, 2))

# 5.random.choice(sequence)
# 从序列中获取一个随机元素
# 元组中有一个数据，随机取值时当作字符串处理
lst = ['python', 'C', 'javascript']
str = ('python is ok')
print(random.choice(lst))
print(random.choice(str))

# 6.random.shuffle(x[,random])
# 用于将列表中的元素打乱，即将列表内的元素随机排序。
lst = [1, 2, 3, 4, 5, 6]
random.shuffle(lst)
print(lst)
print(random.shuffle(lst))     # 打印出结果为None,证明shuffle改变原有列表顺序

# 7.random.sample(sequence,k)
# 从指定序列中随机获取指定长度的片段并随机排列。sample函数不会修改原有序列
lst = [1, 2, 3, 4, 5, 6]
print(random.sample(lst, 4))
print(lst)








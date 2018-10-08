
'''
冒泡排序
相邻的两个数相比，大的往右，最后一个元素就是最大值
以此类推循环排序
'''

List = [99, 11, 33, 88, 22, 44, 55, 77, 66]


def bubble_sort(L):
    length = len(L)
    for i in range(0, length):
        for j in range(i+1, length):
            if L[i] > L[j]:
                L[i], L[j] = L[j], L[i]
    return L


print(bubble_sort(List))

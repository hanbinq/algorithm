
"""
选择排序：
首先在未排序序列中找到最小(大)元素，存放到排序序列的起始位置，然后，再从剩余
未排序元素中继续寻找最小(大)元素，然后放到已排序序列的末尾。以此类推，直到所
有元素均排序完毕。

"""


def selection_sort(alist):
    n = len(alist)
    # 需要进行n-1次选择操作
    for i in range(n-1):
        # 记录最小的位置
        min_index = i
        # 从i+1位置到末尾选择出最小数据
        for j in range(i+1, n):
            if alist[j] < alist[min_index]:
                min_index = j
        # 如果选择出的数据不在正确位置，进行交换
        if min_index != i:
            alist[i], alist[min_index] = alist[min_index], alist[i]


alist = [54, 226, 93, 17, 77, 31, 44, 55, 20]
selection_sort(alist)
print(alist)


"""
最优时间复杂度：O(n^2)
最坏时间复杂度：O(n^2)
稳定性：不稳定(考虑升序每次选择最大的情况)
"""




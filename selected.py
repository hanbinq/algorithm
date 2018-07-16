
'''
选择排序：
在未排序序列中找到最小(大）元素，存放到排序序列
的起始位置，然后，再从剩余未排序元素中继续寻找最小(大)
元素，然后放到已排序序列的末尾。以此类推，直到所有元素
排序完毕。
'''


# 将小的数字提前
def select_sort1(alist):
    n = len(alist)
    for j in range(n - 1):
        min_index = j
        for i in range(j + 1, n):
            if alist[min_index] > alist[i]:
                min_index = i
        alist[j], alist[min_index] = alist[min_index], alist[j]


li = [99, 22, 64, 55, 11, 35, 89, 1, 2]
select_sort1(li)
print(li)


# 将大的数字坠后
def select_sort2(alist):
    n = len(alist)
    count = 1
    for j in range(n - 1):
        max_index = 0
        for i in range(1, n - j):
            if alist[max_index] < alist[i]:
                max_index = i
        alist[max_index], alist[n - count] = alist[n - count], alist[max_index]
        count += 1


li = [99, 22, 64, 55, 11, 35, 89, 1, 2]
select_sort2(li)
print(li)









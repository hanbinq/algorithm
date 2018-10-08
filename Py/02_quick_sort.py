
"""
快速排序
1、从列表中挑出一个元素，作为基准值key
2、所有小于key的元素放左边，所有大于key的元素放右边
3、分别递归左侧列表，右侧列表
"""


def quick_sort(lists, start, end):
    """快速排序"""

    # 递归过程中，发现start和end一致时，停止递归，直接返回列表(递归的退出条件)
    if start >= end:
        return lists

    # 设定起始元素为要寻找位置的基准元素
    mid = lists[start]

    # low为序列左边的由左向右移动的游标
    low = start
    # high为序列右边的由右向左移动的游标
    high = end

    while low < high:
        # 如果low与high未重合，high指向的元素不比基准元素小，则high向左移动
        while low < high and lists[high] >= mid:
            high -= 1
        # 将high指向的元素放到low的位置上
        lists[low] = lists[high]

        # 如果low与high未重合，low指向的元素比基准元素小，则low向右移动
        while low < high and lists[low] < mid:
            low += 1
        # 将low指向的元素放到high的位置上
        lists[high] = lists[low]

    # 退出循环后，low与high重合，此时所指位置为基准元素的正确位置
    # 将基准元素放到该位置
    lists[low] = mid

    # 对基准元素左边的子序列进行快速排序
    quick_sort(lists, start, low - 1)
    # 处理右侧元素
    quick_sort(lists, low + 1, end)
    return lists


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quick_sort(alist, 0, len(alist)-1)
print(alist)

"""
快速排序，又称划分交换排序(partition-exchange sort), 通过一趟排序将要排序的
数据分割成独立的两部分，其中一部分的所有数据都比另外一部分的所有数据都要小，然后再
按此方法对这两部分数据分别进行快速排序，整个排序过程可以递归进行，以此达到整个数据
变成有序序列。

步骤为：
   1. 从数列中挑出一个元素，称为"基准"，
   2. 重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在
      基准的后面(相同的数可以放在任一边)。在这个分区结束之后，该基准就处于数列的
      中间位置。这个称为分区(partition)操作。
   3. 递归的(recursive)把小于基准值元素的子数列和大于基准元素的子数列排序。
"""





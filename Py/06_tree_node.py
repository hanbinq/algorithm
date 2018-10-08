
"""
二分查找又称折半查找，优点是比较次数少，查找速度快，平均性能好；
其缺点就是要求待查表为有序表，且插入删除困难。因此，折半查找适用于不经常变动而查找频繁的
有序列表。首先，假设表中元素是按升序排列，将表中间位置的关键字与查找关键字比较，如果两者
相等，则查找成功；否则利用中间位置记录将表分成前、后两个子表，如果中间位置记录的关键字大
于查找关键字，则进一步查找前一子表，否则进一步查找后一子表。重复以上过程，直到找到满足条
件的记录，使查找成功，或直到子表不存在为止，此时查找不成功。
"""


def binary_search_1(alist, item):
    """非递归实现"""
    first = 0
    last = len(alist)-1
    while first <= last:
        midpoint = (first+last)/2
        if alist[midpoint] == item:
            return True
        elif item < alist[midpoint]:
            last = midpoint-1
        else:
            first = midpoint+1
    return False


testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(binary_search_1(testlist, 3))
print(binary_search_1(testlist, 13))

#############


def binary_search_2(alist, item):
    """递归实现"""
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist)//2
        if alist[midpoint] == item:
            return True
        else:
            if item < alist[midpoint]:
                return binary_search_2(alist[:midpoint], item)
            else:
                return binary_search_2(alist[midpoint+1:], item)


testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(binary_search_2(testlist, 3))
print(binary_search_2(testlist, 13))

"""
搜索：
搜索是在一个项目集合中找到一个特定项目的算法过程。搜索通常的答案是真的或假的，因为该项目
是否存在。搜索的几种常见方法：顺序查找、二分查找法、二叉树查找、哈希查找
"""




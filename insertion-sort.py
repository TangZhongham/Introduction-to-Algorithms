"""
插入排序
20190704
"""


def insert_sort(a):
    for j in range(1, len(a)):
        key = a[j]
        i = j - 1
        while i >= 0 and a[i] > key:
            a[i + 1] = a[i]
            i = i - 1
        a[i + 1] = key
    return a


# 看到高手写的如下
def insert_sort2(a):
    n = len(a)
    for j in range(1, n):
        for i in range(j, 0, -1):
            if a[i] < a[i - 1]:
                # 交换位置
                a[i], a[i - 1] = a[i - 1], a[i]
            else:
                break
    return a


if __name__ == '__main__':
    test = [2, 3, 1, 6, 5]
    # x = insert_sort(test)
    # print(x)
    y = insert_sort2(test)
    print(y)

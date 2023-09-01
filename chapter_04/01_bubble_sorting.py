"""
O(N^2) - говорит об полиномиальном росте.
"""


def bubble_sorting(array):
    index = len(array) - 1
    flg_sort = False

    while not flg_sort:
        flg_sort = True
        for i in range(index):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                flg_sort = False
        index -= 1
    return array


if __name__ == '__main__':
    print(bubble_sorting([7, 2, 5, 9, 8, 1]))

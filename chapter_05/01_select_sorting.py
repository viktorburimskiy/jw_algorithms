"""
O(N^2)
"""


def select_sorting(array):
    index = 0

    while index < len(array):
        min = array[index]
        idx_min = index
        for i in range(index, len(array)):
            if array[i] < min:
                min = array[i]
                idx_min = i
        array[index], array[idx_min] = array[idx_min], array[index]
        index += 1
    return array


if __name__ == '__main__':
    print(select_sorting([7, 2, 5, 9, 8, 1]))

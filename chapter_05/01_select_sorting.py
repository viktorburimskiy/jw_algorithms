"""
O(N^2)
Поскольку при сортировке
выбором количество шагов примерно в два раза меньше, чем N 2, было бы логич-
но выразить эффективность этого алгоритма как O(N^2/2). То есть при наличии
N элементов данных этот алгоритм выполняет N^2/2 шагов

N элементов     bubble_sort     select_sort
5               20              14 (10 сравнений + 4 перестановки)
10              90              54 (45 сравнений + 9 перестановок)
20              380             199 (180 сравнений + 19 перестановок)
40              1560            819 (780 сравнений + 39 перестановок)
80              6320            3239 (3160 сравнений + 79 перестановок)

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

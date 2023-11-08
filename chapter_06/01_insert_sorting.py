"""
O(N^2) - говорит об полиномиальном росте.
"""

def insertSorting(array):
    for i in range(1, len(array)):
        value = array[i]
        j = i - 1

        while j >= 0:
            if array[i-1] > value:
                array[i] = array[i-1]
                index = i-1
                j -= 1
            else:
                break
        array[index] = value





if __name__ == '__main__':
    print(insertSorting([7, 2, 5, 9, 8, 1]))

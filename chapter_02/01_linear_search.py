"""
O(N)
"""


def linear_search(array, search_value):
    for index, element in enumerate(array):
        if element == search_value:
            return index
        elif element > search_value:
            break
    return None


if __name__ == '__main__':
    print(linear_search([5, 2, 10, 4, 6], 3))

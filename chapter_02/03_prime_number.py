"""

"""


def prime_number(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


if __name__ == '__main__':
    print(prime_number(121))
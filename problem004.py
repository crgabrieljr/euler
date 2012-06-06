from math import ceil
from sys import argv


def is_palindrome(word):
    word = list(str(word))
    return word ==  word[::-1]


def largest_palindrome(num_digits):
    min_n = int('1' * num_digits)
    max_n = int('9' * num_digits)
    largest = 0
    for x in xrange(max_n, min_n - 1, -1):
        y = max_n
        while y >= x:
            product = x * y
            if product < largest:
                break
            if is_palindrome(product):
                largest = max(largest, product)
            y -= 1

    return largest


if __name__ == '__main__':
    print largest_palindrome(int(argv[1]))

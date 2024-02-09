"""
Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence,
which is the number of times you must multiply the digits in num until you reach a single digit.

Example:
999 --> 4 (because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, and finally 1*2 = 2)
4 --> 0 (because 4 is already a one-digit number)

"""

from functools import reduce


def persistence(n, count=0):
    if n < 10:
        return count
    digits = list(map(int, str(n)))  # Create list of digits in number
    multi = reduce(lambda x, y: x * y, digits)  # Multiply list
    return persistence(multi, count + 1)  # Repeat until multi < 10


print(persistence(999))


def persistence_v2(num):
    i = 0
    while num >= 10:
        num_arr = list(map(lambda x: int(x), str(num)))
        num = reduce(lambda x, y: x * y, num_arr)
        i += 1
    return i


print(persistence_v2(999))

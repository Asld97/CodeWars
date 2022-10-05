"""
Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that
occur more than once in the input string. The input string can be assumed to contain only alphabets
(both uppercase and lowercase) and numeric digits.

Example:
"abcde" -> 0 # no characters repeats more than once
"aabbcde" -> 2 # 'a' and 'b'

"""

from functools import reduce


# Reduction function
def count_duplicates(acc, value):
    if value > 1:
        acc = acc + 1
    return acc


# Finding duplicates function
def duplicate_count(text):
    text = text.lower()
    duplicates = {}
    for item in text:
        n = duplicates.get(item, 0)
        duplicates[item] = n + 1
    num_duplicates = reduce(count_duplicates, duplicates.values(), 0)
    return num_duplicates


print(duplicate_count("aaBbcde"))




# Exercise 8 Delete occurrences of an element if it occurs more than n times
"""
Given a list lst and a number N, create a new list that contains each number of lst at most N times without reordering.
For example if N = 2, and the input is [1,2,3,1,2,1,2,3], you take [1,2,3,1,2],
drop the next [1,2] since this would lead to 1 and 2 being in the result 3 times, and then take 3,
which leads to [1,2,3,1,2,3].
"""


def delete_nth(order, max_e):
    result = []
    for item in order:
        if result.count(item) <= max_e - 1:
            result.append(item)
    return result


check_table = [1, 1, 1, 1, 3, 3, 7, 2, 2, 2, 2]
print(delete_nth(check_table, 3))

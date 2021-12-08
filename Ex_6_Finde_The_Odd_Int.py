# Exercise 6: Find the odd int
# Return the number which appears an odd number of times -> only one number is correct

def find_it(seq):
    searched_value = 0
    for x in seq:
        if seq.count(x) % 2 != 0:
            searched_value = x
    return searched_value


example_list = [20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]
print(find_it(example_list))

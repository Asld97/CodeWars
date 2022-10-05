"""
Rules:
Implement the function unique_in_order which takes as argument a sequence and returns a list of items without
any elements with the same value next to each other and preserving the original order of elements.

"""

def unique_in_order(iterable):
    count_dict = {}
    collect = []
    for item in iterable:
        n = count_dict.get(item, 0)
        count_dict[item] = n + 1
        if len(count_dict) > 1:
            first_key = list(count_dict.keys())[0]
            collect.append(first_key)
            count_dict.pop(first_key)
    if iterable:
        collect.append(item)
    return collect


it_list = 'AAABBBCCCAAACCCBBB'
print(unique_in_order(it_list))

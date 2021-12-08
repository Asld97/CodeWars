# Exercise 3: Array.diff
# Delete all occurrences in list a, if the list b contain them, and retain their order

def array_diff(a, b):
    b = set(b)
    remain_a = []
    for i in b:
        for j in a:
            if i == j:
                remain_a.append(j)
    for numb in remain_a:
        a.remove(numb)
    return a


a = [1, 2, 3, 4, 4, 4, 6, 7, 7]
b = [1, 2, 3, 4, 5, 6, 745, 62, 34, 423, -1, -2, 3, 0]
print(array_diff(a, b))


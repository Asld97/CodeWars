def likes(names):
    num_of_names = len(names)

    if num_of_names == 0:
        string_to_print = "no one likes this"
    elif num_of_names == 1:
        string_to_print = f"{names[0]} likes this"
    elif num_of_names == 2:
        string_to_print = f"{names[0]} and {names[1]} like this"
    elif num_of_names == 3:
        string_to_print = f"{names[0]}, {names[1]} and {names[2]} like this"
    else:
        string_to_print = (
            f"{names[0]}, {names[1]} and {num_of_names-2} others like this"
        )

    return string_to_print


print(likes([]))
print(likes(["Peter"]))
print(likes(["Jacob", "Alex"]))
print(likes(["Max", "John", "Mark"]))
print(likes(["Alex", "Jacob", "Mark", "Max"]))


# Best solution:def likes(names):
def likes(names):
    n = len(names)
    return {
        0: "no one likes this",
        1: "{} likes this",
        2: "{} and {} like this",
        3: "{}, {} and {} like this",
        4: "{}, {} and {others} others like this",
    }[min(4, n)].format(*names[:3], others=n - 2)

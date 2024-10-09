def square_digits(num):

    return int("".join([str(int(x) ** 2) for x in str(num)]))


print(square_digits(0))


#
def square_digits(num):
    sum_string = ""
    for x in str(num):
        sum_string += str(int(x) ** 2)

    return int(sum_string)


print(square_digits(765))

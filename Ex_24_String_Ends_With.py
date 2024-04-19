def solution(text, ending):

    split_values = text.split(ending)
    print(split_values)
    if split_values[-1] == "":
        return True

    return False


print(solution("hej", "ej"))

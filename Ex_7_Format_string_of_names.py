# Exercise 7 Format a string of names like 'Bart, Lisa & Maggie'.
"""
Given: an array containing hashes of names

Return: a string formatted as a list of names separated by commas except for the last two names,
which should be separated by an ampersand.
"""


def namelist(names):
    string = ''
    if len(names) == 1:
        return f'{names[0]["name"]}'

    for i in range(len(names)):
        if i == len(names) - 2:
            string = string + f'{names[i]["name"]} & {names[i + 1]["name"]}'
            break
        else:
            string = string + f'{names[i]["name"]}, '

    return f'{string}'


names = [{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Rob'}]
print(namelist(names))

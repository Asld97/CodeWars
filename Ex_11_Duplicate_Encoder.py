# Exercise 11 Duplicate Encoder
"""
Rules:
    1. Create new string, where each character is changed for '(' or ')'
    2. If the character appears only once in the original string -> '('
    3. If the character appears more than once -> ')'
"""


# Solution 1 - My
def duplicate_encode(word):
    word = word.lower()
    trans_word = ''
    for char in word:
        if word.count(char) == 1:
            trans_word += '('
        else:
            trans_word += ')'
    return trans_word


test_word = "Success"
print(duplicate_encode(test_word))
print('-------------------------')

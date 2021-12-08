# Exercise_12 Rot13
"""
ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet.
ROT13 is an example of the Caesar cipher.

Create a function that takes a string and returns the string ciphered with Rot13.
If there are numbers or special characters included in the string, they should be returned as they are.
Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".
"""


def rot13(message):
    ciphered_word = ''
    for c in message:
        if 65 <= ord(c) <= 90 or 97 <= ord(c) <= 122:
            if c.isupper() and ord(c) + 13 > 90:
                diff_to_add = (ord(c) + 13) - 91
                ciphered_word += chr(65 + diff_to_add)

            elif c.islower() and ord(c) + 13 > 122:
                diff_to_add = (ord(c) + 13) - 123
                ciphered_word += chr(97 + diff_to_add)

            else:
                ciphered_word += chr(ord(c) + 13)
        else:
            ciphered_word += c

    return ciphered_word


test_message = 'Test'
print(rot13(test_message))

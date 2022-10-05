"""
Rules:

Given an array (arr) as an argument complete the function countSmileys that should return the total number of smiling faces.

Rules for a smiling face:

Each smiley face must contain a valid pair of eyes. Eyes can be marked as : or ;
A smiley face can have a nose but it does not have to. Valid characters for a nose are - or ~
Every smiling face must have a smiling mouth that should be marked with either ) or D
No additional characters are allowed except for those mentioned.

Valid smiley face examples: :) :D ;-D :~)
Invalid smiley faces: ;( :> :} :]

"""
def count_smileys(arr, count=0):
    for item in arr:
        if len(item) == 2 and item[0] in {':', ';'} and item[1] in {')', 'D'}:
            count += 1
        if len(item) == 3 and item[0] in {':', ';'} and item[1] in {'-', '~'} and item[2] in {')', 'D'}:
            count += 1
    return count


faces_v1 = [':)', ';(', ';}', ':-D']
faces_v2 = [';]', ':[', ';*', ':$', ';-D']
faces_v3 = [':D', ':~)', ';~D', ':)']
faces_v4 = [':)', ':(', ':D', ':O', ':;']
print(count_smileys(faces_v4))

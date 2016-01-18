# EDX
# MITx: 6.00.1x Introduction to Computer Science and Programming Using Python
# Problem Set 1
# Problem 1: Counting Bobs
'''
Assume s is a string of lower case characters.
Write a program that prints the number of times
the string 'bob' occurs in s.
For example, if s = 'azcbobobegghakl',
then your program should print

Number of times bob occurs is: 2
'''

s = 'azcbobobegghakl'  # note: remove this line on submission


def countSubstring(string, substring):

    index = string.find(substring)
    if index < 0:
        return 0
    return 1 + countSubstring(string[index+len(substring)-1:], substring)

print(countSubstring(s, 'bob'))

# EDX
# MITx: 6.00.1x Introduction to Computer Science and Programming Using Python
# Problem Set 1
# Problem 1: Counting Vowels
'''
Assume s is a string of lower case characters.
Write a program that counts up the number of vowels contained in the string s.
Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.
For example, if s = 'azcbobobegghakl', your program should print:
Number of vowels: 5
'''

s = ''  # note: comment this line on submission

def count_vowels(s):
    count = 0
    for vowel in s:
        if vowel in "aoeiu":
            count += 1
    return count

print (count_vowels(s))
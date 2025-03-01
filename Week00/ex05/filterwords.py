import sys
import string as string_lib

av = sys.argv[1::]
ac = len(av)

if (ac != 2): print("bad arguments"), exit()

text, number = av

if (number.isdecimal() == 0): print('u must pass a number'), exit()

number = int(number)
# print("punct = ", string_lib.punctuation)
# List Comprehension

args = ''.join([c for c in text if string_lib.punctuation.find(c) == -1]).split(" ")
result = ([arg for arg in args if len(arg) > number])
print(result)

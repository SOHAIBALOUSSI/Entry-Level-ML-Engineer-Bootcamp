import sys

ac = len(sys.argv)
av = sys.argv
if (ac == 1):
    print('AssertionError: no argument is provided')
elif (ac > 2) :
    print('AssertionError: more than one argument is provided')
elif not (av[1].isnumeric()):
    print('AssertionError: argument is not an integer')
else:
    num = int(av[1])
    if num == 0:
        print("I'm Zero.")
    elif num % 2:
        print("I'm Odd.")
    else:
        print("I'm Even.")
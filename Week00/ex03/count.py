import sys
import string


av = sys.argv 
ac = len(sys.argv[1::])
def text_analyzer(arg=None): 
    '''
      This function counts the number of upper characters, lower characters,
      punctuation and spaces in a given text.
    '''
    upperCase = 0
    lowerCase = 0
    spaces = 0
    punctuation = 0
    
    if (arg is None):
        arg = input("What is the text to analyze?\n")

    if type(arg) is not str:
        print("AssertionError: argument is not a string")
        return
    for c in arg:
        if (c.isupper()): upperCase += 1
        elif (c.islower()): lowerCase += 1
        elif (c.isspace()): spaces += 1
        elif (string.punctuation.find(c)!=-1): punctuation += 1
    
    print("The text contains", sum(1 for c in arg if c.isprintable())," printable character(s):")
    print("-",upperCase,"upper letter(s)")
    print("-",lowerCase,"lower letter(s)")
    print("-", punctuation, "punctuation mark(s)")
    print("-", spaces, "space(s)")

if __name__ == "__main__":
    if (ac == 1):
        text_analyzer(av[1])
    else:
        text_analyzer()
    
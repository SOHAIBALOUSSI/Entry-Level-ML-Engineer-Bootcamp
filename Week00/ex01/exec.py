import sys

result = " ".join(sys.argv[1::])
print(result.swapcase()[::-1])
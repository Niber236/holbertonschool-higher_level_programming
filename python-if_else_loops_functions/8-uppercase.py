#!/usr/bin/python3
def uppercase(str):
    for c in str:
        value = ord(c)
        if value >= 97 and value <= 122:
            value = value - 32
        print("{:c}".format(value), end="")
    print("")

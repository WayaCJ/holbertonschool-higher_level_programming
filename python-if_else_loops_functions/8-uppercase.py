#!/usr/bin/python3
def uppercase(str):
    result = ""
    for a in str:
        if ord(a) >= 97 and ord(a) <= 122:
            result += chr(ord(a) - 32)
        else:
            result += a
    print("{}".format(result))

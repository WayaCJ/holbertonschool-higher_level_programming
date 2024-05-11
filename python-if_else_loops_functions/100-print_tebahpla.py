#!/usr/bin/python3
aa = ""
for letters in range(ord('z'), ord('a')-1, -1):
    if letters % 2 == 0:
        aa += chr(letters)
    else:
        aa += chr(letters).upper()
print("{}".format(aa), end="")

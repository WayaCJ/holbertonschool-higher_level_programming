#!/usr/bin/python3
for letters in range(ord('z'), ord('a')-1, -1):
        if letters % 2 == 0:
            print(chr(letters), end="")
        else:
            print(chr(letters).upper(), end="")

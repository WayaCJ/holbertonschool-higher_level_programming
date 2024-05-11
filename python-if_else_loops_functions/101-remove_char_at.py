#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0 or n >= len(str):
        return str
    coppy = ""
    for i in range(len(str)):
        if i != n:
            coppy += str[i]
        return coppy

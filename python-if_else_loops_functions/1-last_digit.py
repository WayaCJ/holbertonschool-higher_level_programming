#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str = "Last digit of"
str2 = "is"
last = number % 10

if last > 5:
    print(f"{str} {number} {str2} {last} and is greater than 5")
elif last == 0:
    print(f"{str} {number} {str2} {last} and is 0")
elif last < 6:
    print(f"{str} {number} {str2} {last} and is less than 6 and not 0")

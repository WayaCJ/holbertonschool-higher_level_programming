#!/usr/bin/python3
import sys

numofa = len(sys.argv) - 1

if numofa == 0:
    print("NUmber of argument(s): {}".format(numofa))
else:
    print("Number of arguments(s): {}".format(numofa))

    print("Arguments:")
    for i in range(1, len(sys.argv)):
        print("{}: {}".format(i, sys.argv[i]))

#!/usr/bin/python3
import sys

if __name__ == "__main__":
    numofa = len(sys.argv) - 1

    if numofa == 0:
        print("{} arguments.".format(numofa))
    elif numofa == 1:
        print("{} argument:".format(numofa))
        for i in range(1, len(sys.argv)):
            print("{}: {}".format(i, sys.argv[i]))
    else:
        print("{} arguments:".format(numofa))
        for i in range(1, len(sys.argv)):
            print("{}: {}".format(i, sys.argv[i]))

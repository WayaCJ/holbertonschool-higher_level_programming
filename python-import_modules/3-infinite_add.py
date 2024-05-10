#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argg = sys.argv[1:]

    result = sum(int(arg) for arg in argg)

    print(result)

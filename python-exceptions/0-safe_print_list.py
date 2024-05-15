#!/usr/bin/python3
if __name__ == "__main__":
    def safe_print_list(my_list=[], x=0):
        c = 0
        try:
            for i in range(x):
                count += 1
                print("{:d}".format(c), end="")
        except IndexError:
            pass
        print()
        return c

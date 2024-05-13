#!/usr/bin/python3
if __name__ == "__main__":
    def print_list_integer(my_list=[]):
        for num in my_list:
            if isinstance(num, int):
                print("{:d}".format(num))

#!/usr/bin/python3
def max_intenger(my_list=[]):
    if my_list:
        max_num = my_list[0]
        for num in my_list[1:]:
            if num > max_num:
                max_num = num
        return max_num

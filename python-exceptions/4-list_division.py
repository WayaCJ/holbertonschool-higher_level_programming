#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            div_r = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            div_r = 0
        except ZeroDivisionError:
            print("division by 0")
            div_r = 0
        except IndexError:
            print("out of range")
            div_r = 0
        finally:
            result.append(div_r)
    return result

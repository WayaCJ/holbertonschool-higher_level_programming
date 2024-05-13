#!/usr/bin/python3
if __name__ == "__main__":
    def no_c(my_string):
        result = ""
        for char in my_string:
            if char != 'c' and char != 'C':
                result += char
        return result

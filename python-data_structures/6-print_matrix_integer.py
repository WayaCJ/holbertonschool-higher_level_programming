#!/usr/bin/python3
if __name__ == "__main__":
    def print_matrix_integer(matrix=[[]]):
        for row in matrix:
            for num in row:
                print("{:d}".format(num), end=" ")
            print()
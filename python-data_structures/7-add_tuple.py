#!/usr/bin/python3
if __name__ == "__main__":
    def add_tuple(tuple_a=(), tuple_b=()):

        tuple_a = tuple_a + (0, 0)[:2 - len(tuple_a)]
        tuple_b = tuple_b + (0, 0)[:2 - len(tuple_b)]

        sum_first = tuple_a[0] + tuple_b[0]
        sum_second = tuple_a[1] + tuple_b[1]
    
        return (sum_first, sum_second)

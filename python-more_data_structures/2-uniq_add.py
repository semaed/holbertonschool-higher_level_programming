#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_int = 0
    unique_elements = set(my_list)
    for num in unique_elements:
        unique_int += num
    return unique_int

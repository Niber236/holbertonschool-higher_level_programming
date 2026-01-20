#!/usr/bin/python3
element_at = __import__('1-element_at').element_at

my_list = [10, 20, 30, 40, 50]
idx = 3
print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))
## The code above is for testing the 'element_at' function from '1-element_at.py'.
#!/usr/bin/python3
"""
Module 1-my_list
Defines a class MyList that inherits from list.
"""


class MyList(list):
    """
    A subclass of list that includes a method to print the sorted list.
    """

    def print_sorted(self):
        """
        Prints the list, but sorted (ascending integers).
        """
        print(sorted(self))

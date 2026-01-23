#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    rom_n = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = 0
    n = len(roman_string)
    for i in range(n):
        val = rom_n.get(roman_string[i], 0)
        if i < n - 1 and rom_n.get(roman_string[i+1], 0) > val:
            num -= val
        else:
            num += val
    return num

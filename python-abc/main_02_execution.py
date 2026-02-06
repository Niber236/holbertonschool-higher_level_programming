#!/usr/bin/env python3
from task_02_execution import NoPylist

my_list = NoPylist()

# 1. Test valide (Doit marcher)
my_list.append(1)
my_list.append(4)
my_list.append(5)
print(my_list)

# 2. Test invalide (Doit planter)
try:
    my_list.append("Hello")
except TypeError as e:
    print(e)
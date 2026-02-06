#!/usr/bin/env python3
from task_03_countediterator import CountedIterator

data = [1, 2, 3, 4]
item_iterator = CountedIterator(data)

try:
    while True:
        item = next(item_iterator)
        print("Got item: {}".format(item))
except StopIteration:
    print("No more items.")

print("Total items: {}".format(item_iterator.get_count()))
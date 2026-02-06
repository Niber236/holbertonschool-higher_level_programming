#!/usr/bin/env python3
from task_01_duck_typing import Circle, Rectangle, shape_info

# Test du Cercle
circle = Circle(radius=5)
print("--- Circle ---")
shape_info(circle)

# Test du Rectangle
rectangle = Rectangle(width=4, height=7)
print("--- Rectangle ---")
shape_info(rectangle)
# Lesson 9 Pages Debugging and Unit Testing in Python
import pdb
pdb.set_trace()

def add_numbers(a, b):
    """This function adds a to b."""
    c = a + b
    print(c)

add_numbers(3, 4)
# Lesson 9 Pages Debugging and Unit Testing in Python
# import unittest
# import pdb
# pdb.set_trace()

# Page 2
# def add_numbers(a, b):
#     """This function adds a to b."""
#     c = a + b
#     print(c)
#
#
# add_numbers(3, 4)

# Page 3
# dog = "Zorro"
# cat = "Tesla"
#
# play = "My dog " + dog + " plays with my cat " + cat + " all the time."
#
# print(play)


# Page 5
# def format_name(first_name, last_name):
#     """Will neatly format a full name."""
#     full_name = first_name + ' ' + last_name
#     return full_name.title()
# def format_name(first_name, middle_name, last_name):
#     """Will neatly format a full name."""
#     full_name = first_name + ' ' + middle_name + ' ' + last_name
#     return full_name.title()
# def format_name(first_name, last_name, middle_name=''):
#     """Will neatly format a full name."""
#     if middle_name:
#         full_name = first_name + ' ' + middle_name + ' ' + last_name
#     else:
#         full_name = first_name + ' ' + last_name
#     return full_name.title()
#
#
# class FormatNamesTest(unittest.TestCase):
#     """Tests format_name() function."""
#
#     def test_format_name(self):
#         """Will the name 'James Jones' work?"""
#         name_formatted = format_name('james', 'jones')
#         self.assertEqual(name_formatted, 'James Jones')
#
#     def test_full_name(self):
#         """Will the name 'John Paul Jones' work?"""
#         name_formatted = format_name('john', 'jones', 'paul')
#         self.assertEqual(name_formatted, 'John Paul Jones')
#
#
# unittest.main()

# print('To quit at anytime enter "q".')
# while True:
#     first_name = input("\nPlease enter your first name: ")
#     if first_name == 'q':
#         break
#     last_name = input("Please enter your last name: ")
#     if last_name == 'q':
#         break
#
#     formatted_name = format_name(first_name, last_name)
#     print("\tHere is your name neatly formatted: " + formatted_name + '.')

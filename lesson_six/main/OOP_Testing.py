# OOP Pages Testing
class Person:
    """This is a person"""

    def __init__(self, firstName, lastName):
        """Initializer"""
        self.firstName = firstName
        self.lastName = lastName

class Greeter:
    """Creates a greeting"""
    @staticmethod
    def __init__(self, people):
        """Initializing class"""
        info = []


class Greeter:
    """ This is a greeter"""

    @staticmethod
    def greet(people):
        """Static method to greet a list of people"""
        greetings = []
        for person in people:
            greeting = "Hello " + person.firstName + " " + person.lastName + "!"
            greetings.append(greeting)
        return greetings


class Rectangle:
    """Makes a rectangle"""
    def __init__(self, width, height):
        width = 5
        height = 5


    def area(self):
        space = 'width' * 'height'
        return space


class Rectangle:
    """This is a shape"""

    def __init__(self, width, height):
        """Initializer"""
        self.width = width
        self.height = height

    def area(self):
        """Returns the area"""
        return self.width * self.height

# Object Oriented Programming AKA (OOP)
class Stadium:
    """Makes a stadium"""

    def __init__(self, name, city_state, capacity):
        """Initializer"""
        self.name = name
        self.city_state = city_state
        self.capacity = capacity

    def describe_stadium(self):
        print('The', self.name, 'is located in ', self.city_state, 'and holds', self.capacity, 'fans.')


stadium1 = Stadium('Mile High Stadium', 'Denver, CO', 79125)

stadium1.describe_stadium()

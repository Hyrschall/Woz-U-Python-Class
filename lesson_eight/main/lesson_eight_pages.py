# Lesson 8 pages
# Page 2


# class Car:
#     """Modeling a car."""
#
#     def __init__(self, make, model, year):
#         """Initialize attributes to describe a car."""
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer = 0
#
#     def get_car(self):
#         """Return formatted car."""
#         car_name = str(self.year) + ' ' + self.make + ' ' + self.model
#         return car_name.title()
#
#     def read_odometer(self):
#         """Show car's mileage."""
#         print("This car has", str(self.odometer), "miles on it.")
#
#     def update_odometer(self, miles):
#         """
#         Update the odometer with new mileages.
#         Reject changes if roll back is attempted.
#         """
#         if miles >= self.odometer:
#             self.odometer = miles
#         else:
#             print("Error: Rolling back odometer not allowed")
#
#     def increment_odometer(self, mileage):
#         """Add certain number of miles to odometer."""
#         self.odometer += mileage
#
# # Page 4
#     def mpg(self):
#         """Show car's miles-per-gallon."""
#         print("This car gets 25 MPG")
#
# # Page 5
# class Battery:
#     """Modeling a battery for an electric car."""
#
#     def __init__(self, battery_size=75):
#         """Initialize battery attributes."""
#         self.battery_size = battery_size
#
# # Page 3 & 4
#     def get_battery(self):
#         """Print a description of the battery size."""
#         print('This battery is a ' + str(self.battery_size) + '-kWh battery.')
#
# # Page 2 & 3
# class ElectricCar(Car):
#     """Represents a car that is specific to electric vehicles."""
#
# # Page 5
#     def __init__(self, make, model, year, battery_size=75):
#         """Initialize attributes."""
#         super().__init__(make, model, year)
#         self.battery = Battery(battery_size)
#
# # Page 4
#     def mpg(self):
#         """Electric cars do not use gasoline, so inform."""
#         print("This car does not use gasoline")
#
#
# my_electric_car = ElectricCar('Nissan', 'Leaf', '2016', 50)
# print(my_electric_car.get_car())
# my_electric_car.battery.get_battery()
# my_electric_car.mpg()

# Page 6
# class Dog:
#     def talk(self):
#         print('\nA dog barks.')
#
#     def coat(self):
#         print('\nDogs have fur.')
#
#
# class Duck:
#     def talk(self):
#         print('\nA duck quacks.')
#
#     def coat(self):
#         print('\nDucks have feathers.')
#
#
# def describe(our_object):
#     our_object.talk()
#     our_object.coat()
#
#
# zorro = Dog()
# donald = Duck()
#
# # describe(zorro)
# # describe(donald)
#
# for animal in (zorro, donald):
#     animal.talk()
#     animal.coat()

# Page 7 #1
# class Animal:
#     """This is an animal"""
#     def giveBirth(self):
#         """Return the birthing method"""
#         return "I don't know how"


# class Mammal(Animal):
#     """This is a Mammal"""
#     def giveBirth(self):
#         """Return mammal birthing"""
#         return "I give live birth"
#
#
# class Bird(Animal):
#     """This is a Bird"""
#     def giveBirth(self):
#         """Return bird birthing"""
#         return "I lay eggs"

# Page 7 #2
# class Animal:
#     """This is an animal"""
#
#     def __init__(self, name, birthMethod):
#         """Initializer"""
#         self.name = name
#         self.birthMethod = birthMethod
#
#     def giveBirth(self):
#         return self.birthMethod
#
#
#
# class Bird(Animal):
#     """This is a bird"""
#
#     def __init__(self, name, flies):
#         """Initializer"""
#         super().__init__(name, "eggs")
#         self.flies = flies

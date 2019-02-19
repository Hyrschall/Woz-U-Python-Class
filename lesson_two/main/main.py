

#day = 4
day = int(input("What day were you born? "))
#month = "July"
month = input("What month were you born? ")
#year = 1776
year = int(input("What year were you born? "))

my_birthday = str.format("{} {}, {}", month, day, year)

print(my_birthday)

first = "happy"
second = "birthday"
third = "to"
fourth = "you"

final = str.upper(first + " " + second + " " + third + " " + fourth)

print(final)

#age = 15
age = int(input("How old are you? "))

if age <= 10:
    print("Not Permitted")
elif age >= 15:
    print("Permitted with parent")
elif age >= 18:
    print("Permitted with anyone over 18")
elif age > 18:
    print("Permitted to attend alone")
else:
    print("You're up past your bed time")

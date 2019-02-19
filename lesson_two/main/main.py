# day = 4
while True:
    try:
        day = int(input("What day were you born? "))
        break
    except ValueError:
        print("Oops! That was not a valid number. Try again...")

# month = "July"

while True:
    try:
        month = input("What month were you born? ")
        if month.isalpha():
            break
    except:
        print("Please use text only")

# year = 1776
while True:
    try:
        year = int(input("What year were you born? "))
        break
    except ValueError:
        print("Oops! That was not a valid number. Try again...")

my_birthday = str.format("{} {}, {}", month, day, year)

print(my_birthday)

first = "happy"
second = "birthday"
third = "to"
fourth = "you"

final = str.upper(first + " " + second + " " + third + " " + fourth)

print(final)

# age = 15
while True:
    try:
        age = int(input("How old are you? "))
        break
    except ValueError:
        print("Oops! That was not a valid number. Try again...")

if age <= 10:
    print("Not Permitted")
elif 11 <= age <= 15:
    print("Permitted with parent")
elif 16 <= age <= 18:
    print("Permitted with anyone over 18")
elif age > 18:
    print("Permitted to attend alone")

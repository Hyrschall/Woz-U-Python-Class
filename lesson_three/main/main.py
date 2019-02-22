# Lists and Loops Part 1

list_of_names = ["Kurt", "David", "Katherine"]

for name in list_of_names:
    print("Where is " + name + " today?")

# Lists and Loops Part 2

my_favorite_cars = ["Tesla", "Audi", "Cadillac"]
my_favorite_flowers = ["Tulips", "Orchids", "Lilies", "Daffodils"]
my_favorite_animals = ["Cats", "Dogs", "Fish", "Snakes", "Dragons"]

my_favorite_things = my_favorite_animals + my_favorite_cars + my_favorite_flowers

for favorite in my_favorite_things:
    if len(favorite) % 2 == 0:
        print(favorite)

# Lists and Loops Part 3

number_range = list(range(1, 21))

for number in number_range:
    if number % 3 == 0 and number % 5 == 0:
        print("ZipZap")
    elif number % 3 == 0:
        print("Zip")
    elif number % 5 == 0:
        print("Zap")
    else:
        print(number)

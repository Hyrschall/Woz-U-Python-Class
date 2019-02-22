# Lesson 4 Hands-On with Dictionaries
fido = {'Name': 'Fido', 'Type': 'Dog', 'Color': 'Black', 'Nickname': 'DoeDoe', 'Owner': 'Joe'}

charlie = {'Name': 'Charlie', 'Type': 'Turtle', 'Color': 'Green', 'Nickname': 'Slow Poke', 'Owner': 'John'}

pets = [fido, charlie]
# pets['Pet1'] = fido
# pets['Pet2'] = charlie

# for key in pets:
#    print(key['Name'] + ':' + key['Type'])

print(list(pets, '\n'))

# print(pets)

# people = {
#    'person1': {
#        'name': 'Sally Sue',
#        'city': 'Phoenix'
#    },
#    'person2': {
#        'name': 'Billy Bob',
#        'city': 'Scottsdale'
#    },
#    'person3': {
#        'name': 'Rover',
#        'city': 'Zappa'
#    }
# }

# greetings = []

# for info in people.values():
#    greetings.append("Hello " + info['name'] + " from " + info['city'])

# print(greetings)

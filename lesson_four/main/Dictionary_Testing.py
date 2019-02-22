user = {'name': 'Andrew', 'email': 'andrew@email.com', 'username': 'andrewUser'}

for key in user:  # type: str
    print(key, user[key])

# Activities with Dictionaries
people = {
    'person1': {
        'name': 'Sally Sue',
        'city': 'Phoenix'
    },
    'person2': {
        'name': 'Billy Bob',
        'city': 'Scottsdale'
    },
    'person3': {
        'name': 'Rover',
        'city': 'Zappa'
    }
}

greetings = []

for key, info in people.items():
    greetings.append("Hello " + info['name'] + " from " + info['city'])

#for key, value in people.items():
 #   print(key)
 #   print(value)

    #for key1, value1 in value.items():
     #   print(key1)
     #   print(value1)
for info in people.values():
    greetings.append("Hello " + info['name'] + " from " + info['city'])

print(greetings)
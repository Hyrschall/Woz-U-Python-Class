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

for person in people.items:
    greetings.append("Hello " + person('name') + "from " + person('city'))





print(greetings)
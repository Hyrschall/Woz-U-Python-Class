# Lesson 4 Hands-On with Dictionaries
fido = {
    'Name': 'Fido',
    'Type': 'Dog',
    'Color': 'Black',
    'Nickname': 'DoeDoe',
    'Owner': 'Joe'
}

charlie = {
    'Name': 'Charlie',
    'Type': 'Turtle',
    'Color': 'Green',
    'Nickname': 'Slow Poke',
    'Owner': 'John'
}

pets = [fido, charlie]

for pet in pets:
    for key in pet:
        print('{} : {}'.format(key, pet[key]))

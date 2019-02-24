# Lesson 4 Hands-On with Dictionaries
# Part 1
fido = dict(Name='Fido', Type='Dog', Color='Black', Nickname='DoeDoe', Owner='Joe')

charlie = dict(Name='Charlie', Type='Turtle', Color='Green', Nickname='Slow Poke', Owner='John')

pets = [fido, charlie]

for pet in pets:
    for key in pet:
        print('{} : {}'.format(key, pet[key]))

# Part 2

england = dict(Capital='London', Population='53.01 million', Fact='Still has a Queen', Language='English')

france = dict(Capital='Paris', Population='66.9 million', Fact='Has the Eiffel Tower', Language='French')

belgium = dict(Capital='Brussels', Population='11.35 million', Fact='Hosted the 1920 Summer Olympics', Language='Dutch')

countries = [england, france, belgium]

for county in countries:
    for info in county:
        print('{} : {}'.format(info, county[info]))

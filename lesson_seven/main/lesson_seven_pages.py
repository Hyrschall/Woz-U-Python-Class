# L7 Standard Library Testing
# Page 6
# import math, random
#
# my_random = random.random()*100
#
# square_root = math.sqrt(my_random)

# Page 8
# file = open('example.txt', 'w')
#
# print('File Name:', file.name)
# print('File Open Mode:', file.mode)
#
#
# def status(x):
#     if x.closed:
#         return 'Closed'
#     else:
#         return 'Open'
#
#
# print('File Status:', status(file))
#
# file.close()
#
# print('File Status:', status(file))

# Page 9
# story = "Once upon a time there was\n"
# story += "a dog who loved to play ball.\n"
# story += "This dog could run as fast as the wind.\n"
#
# file = open('story.txt', 'w')
# file.write(story)
# file.close()
#
# file = open('story.txt', 'r')
#
# contents = file.read()
# print(contents)
# file.close()

# Page 10
# new_text = 'Python was conceived in the late 1990s by Guido van Rossum.'
# with open('updating.txt', 'w') as file:
#     file.write(new_text)
#     print('\nFile Now Closed?:', file.closed)
# print('File Now Closed?:', file.closed)
#
# with open('updating.txt', 'r+') as file:
#     new_text = file.read()
#     print('\nString:', new_text)
#     print('\nPosition In File Now:', file.tell())
#     position = file.seek(33)
#     print('Position In File Now:', file.tell())
#     file.write('1980s')
#     file.seek(0)
#     new_text = file.read()
#     print('\nString:', new_text)

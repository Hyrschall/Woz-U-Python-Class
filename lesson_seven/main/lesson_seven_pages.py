# L7 Standard Library Testing
# Page 6
#import math, random

#my_random = random.random()*100

#square_root = math.sqrt(my_random)

# Page 8
file = open('example.txt', 'w')

print('File Name:', file.name)
print('File Open Mode:', file.mode)

def status(x):
    if (x.closed != False):
        return 'Closed'
    else:
        return 'Open'


print('File Status:', status(file))
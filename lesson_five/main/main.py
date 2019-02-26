# Working with functions
import numpy

num = []
while True:
    number = input('Please enter a number(When done leave blank and press Enter): ')
    if number.isdigit():
        num.append(number)
        continue
    elif number.isalpha():
        print('No letters please')
    else:
        break

num = list(map(int, num))


def sum_function(n):
    return sum(n)


def product_function(n):
    return numpy.prod(n)


def average_function(n):
    return numpy.average(n)


print(sum_function(num))
print(product_function(num))
print(average_function(num))

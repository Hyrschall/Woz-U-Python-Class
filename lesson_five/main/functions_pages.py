def get_average(x, y, z):
    return (x + y + z) / 3


average = get_average(34, 54, 78)
print(average)

count = 0


def get_count(data_list, update_count=False):
    global count
    if update_count:
        count = len(data_list)
        return count


num = ['the', 'cat', 'is', 'black', 1, 2, 3]

print(get_count(num, True))


def get_count(data_list, update_count=False):
    if update_count:
        global count
        count = len(data_list)
    return len(data_list)


numbers = [[1, 2, 3], [4, 5, 6]]

fn_average = lambda x: sum(x) / len(x)

averages = map(fn_average, numbers)

print(list(averages))


list_a = [4, 6, 8]
list_b = [3, 3, 1]

products = map(lambda v1, v2: v1 * v2, list_a, list_b)

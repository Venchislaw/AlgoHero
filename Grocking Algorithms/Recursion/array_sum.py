def sum_(array):
    if len(array) == 1:
        return array[0]
    else:
        return array[0] + sum_(array[1:])


print(sum_([1, 2, 5]))

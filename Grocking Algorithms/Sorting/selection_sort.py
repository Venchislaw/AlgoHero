def min_idx(array):
    min_val = array[0]
    min_index = 0

    for i in range(1, len(array)):
        if array[i] < min_val:
            min_val = array[i]
            min_index = i
    return min_index


def sel_sort(array):
    new_array = []
    while len(array) > 0:
        min_index = min_idx(array)
        new_array.append(array.pop(min_index))

    return new_array


print(sel_sort([5, 2, 1, 4, 3]))

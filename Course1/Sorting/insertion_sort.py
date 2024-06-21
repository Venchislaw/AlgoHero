def insertion_sort(array):
    for i in range(1, len(array)):
        j = i - 1

        while (array[j + 1] < array[j]) and (j >= 0):
            array[j + 1], array[j] = array[j], array[j + 1]
            j -= 1

    return array


print(insertion_sort([4, 3, 0, 5]))

# Time complexity:
# Worst case: O(n^2)
# Best case: O(n)

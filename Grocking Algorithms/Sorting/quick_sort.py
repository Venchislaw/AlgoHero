def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
        bigger = [i for i in array[1:] if i >= pivot]
        smaller = [i for i in array if i < pivot]

        return quick_sort(smaller) + [pivot] + quick_sort(bigger)


print(quick_sort([4, 1, 2, 0]))


# quicksort is a great example of divide and conquer technique
# where we divide problem to smaller sub problems

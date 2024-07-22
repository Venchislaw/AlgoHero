# oke. Let's start with search
# it's only one algo

def binary_search(arr, target):
    l = 0
    r = len(arr) - 1

    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return None


print("binary search: ", binary_search([1, 3, 5, 7, 9], 5))

# sorting. Hehe boi...


def get_min_idx(arr):
    min_val = arr[0]
    min_idx = 0

    for i in range(1, len(arr)):
        if arr[i] < min_val:
            min_val = arr[i]
            min_idx = i
    return min_idx

def selection_sort(arr):
    new_arr = []

    while len(arr) > 0:
        min_idx = get_min_idx(arr)
        new_arr.append(arr.pop(min_idx))

    return new_arr


print("selection sort: ", selection_sort([2, 5, 7, 1, 4]))


def insertion_sort(arr):
    for i in range(len(arr)-1):
        j = i

        while arr[j] > arr[j + 1] and j >= 0:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            j -= 1
    return arr

print("insertion sort: ", insertion_sort([2, 5, 7, 1, 4]))


def qsort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    less = [i for i in arr[1:] if i <= pivot]
    more = [i for i in arr if i > pivot]

    return qsort(less) + [pivot] + qsort(more)

print("quick sort: ", qsort([2, 5, 7, 1, 4]))

# alright... It's gonna be a litle challenge

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        # merge starts here

        min_l = 0
        min_r = 0
        i = 0

        while min_l < len(left_half) and min_r < len(right_half):
            if left_half[min_l] < right_half[min_r]:
                arr[i] = left_half[min_l]
                min_l += 1
            else:
                arr[i] = right_half[min_r]
                min_r += 1
            i += 1

        # residuals while loops

        while min_l < len(left_half):
            arr[i] = left_half[min_l]
            min_l += 1
            i += 1
        
        while min_r < len(right_half):
            arr[i] = right_half[min_r]
            min_r += 1
            i += 1

    return arr


print("merge sort: ", merge_sort([2, 1, 4, 5, 7]))


def bucket_sort(arr):
    buckets = [0] * (max(arr) + 1)

    for number in arr:
        buckets[number] += 1

    j = 0
    for i in range(len(buckets)):
        for _ in range(buckets[i]):
            arr[j] = i
            j += 1
    return arr

print("bucket sort: ", bucket_sort([2, 1, 4, 5, 7]))
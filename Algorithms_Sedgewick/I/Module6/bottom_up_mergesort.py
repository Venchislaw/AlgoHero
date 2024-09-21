def bottom_up_merge_sort(arr):
    n = len(arr)
    size = 1
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(left + size, n)
            right = min(left + 2 * size, n)
            merge(arr, left, mid, right)
        size *= 2

def merge(arr, left, mid, right):
    # NOTE: These arrays are temporary and do not mind later changes in arr.
    left_part = arr[left:mid]
    right_part = arr[mid:right]
    i = j = 0
    k = left

    while i < len(left_part) and j < len(right_part):
        if left_part[i] <= right_part[j]:
            arr[k] = left_part[i]
            i += 1
        else:
            arr[k] = right_part[j]
            j += 1
        k += 1

    while i < len(left_part):
        arr[k] = left_part[i]
        i += 1
        k += 1

    while j < len(right_part):
        arr[k] = right_part[j]
        j += 1
        k += 1

arr = [5, 3, 5, 4, 2, 8, 1]
bottom_up_merge_sort(arr)
print(arr)  # [1, 2, 3, 4, 5, 5, 8]

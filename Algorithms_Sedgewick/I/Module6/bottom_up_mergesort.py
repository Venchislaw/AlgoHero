def bottom_up_merge_sort(arr):
    n = len(arr)
    size = 1

    while size < n:
        for left in range(0, n, size*2):
            l_end = min(left + size, n)
            r_end = min(l_end + size, n)

            merge(arr, left, l_end, r_end)
        size *= 2


def merge(arr, left, l_end, r_end):
    l_part = arr[left:l_end]
    r_part = arr[l_end:r_end]

    i = j = 0
    k = left

    while i < len(l_part) and j < len(r_part):
        if l_part[i] < r_part[j]:
            arr[k] = l_part[i]
            i += 1

        else:
            arr[k] = r_part[j]
            j += 1

        k += 1

    # residuals
    while i < len(l_part):
        arr[k] = l_part[i]
        i += 1
        k += 1

    while j < len(r_part):
        arr[k] = r_part[j]
        j += 1
        k += 1


arr = [3, 2, 4, 1]
bottom_up_merge_sort(arr)
print(arr)

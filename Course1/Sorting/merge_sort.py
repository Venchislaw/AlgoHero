def merge_sort(array, start, end):
    if end - start + 1 <= 1:
        return array

    mid = (start + end) // 2

    merge_sort(array, start, mid)
    merge_sort(array, mid + 1, end)

    merge(array, start, mid, end)

    return array


def merge(array, start, mid, end):
    L = array[start: mid + 1]
    R = array[mid + 1: end + 1]

    l_idx = 0
    r_idx = 0
    # array index
    i = start

    while l_idx < len(L) and r_idx < len(R):
        # changing original array in-place
        # thankfully we saved Left and Right
        if L[l_idx] <= R[r_idx]:
            array[i] = L[l_idx]
            l_idx += 1
        else:
            array[i] = R[r_idx]
            r_idx += 1
        i += 1

    # add remaining elements
    # one half will have
    while l_idx < len(L):
        array[i] = L[l_idx]
        l_idx += 1
        i += 1

    while r_idx < len(R):
        array[i] = R[r_idx]
        r_idx += 1
        i += 1


# [4, 2, 1, 8] --> [1, 2, 4, 8]
print(merge_sort([4, 2, 1, 8], 0, 3))

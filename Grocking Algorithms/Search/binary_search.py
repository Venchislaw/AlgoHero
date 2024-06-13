def binary_search(seq, elem):
    low = 0
    high = len(seq) - 1

    while high >= low:
        mid_index = (low + high) // 2
        if seq[mid_index] == elem:
            return mid_index
        elif seq[mid_index] > elem:
            high = mid_index - 1
        else:
            low = mid_index + 1


    return


print(binary_search([1, 2, 3, 4], 4))

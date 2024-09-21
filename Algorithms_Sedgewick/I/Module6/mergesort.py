# Bomj Merge Sort Implementation

def merge_sort(arr):
    mid = len(arr) // 2

    if len(arr) == 1:
        return arr

    if len(arr) >=2:
        left_half = merge_sort(arr[:mid])
        right_half = merge_sort(arr[mid:])

    output = [None] * len(arr)

    i = 0
    j = 0
    k = 0

    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            output[k] = left_half[i]
            i += 1

        else:
            output[k] = right_half[j]
            j += 1
        
        k += 1
    
    while i < len(left_half):
        output[k] = left_half[i]
        i += 1
        k += 1
    
    while j < len(right_half):
        output[k] = right_half[j]
        j += 1
        k += 1

    return output

    


print(merge_sort([1, 2, 3, 4]))
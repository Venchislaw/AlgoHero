def merge_sort(arr):
    if len(arr) == 1:
        return arr
    
    mid = len(arr) // 2
    left_subarray = merge_sort(arr[:mid])
    right_subarray = merge_sort(arr[mid:])

    return merge(left_subarray, right_subarray)

def merge(left_arr, right_arr):
    l = 0
    r = 0
    k = 0

    new_arr = [None] * (len(left_arr) + len(right_arr))
    while l < len(left_arr) and r < len(right_arr):
        if left_arr[l] < right_arr[r]:
            new_arr[k] = left_arr[l]
            l += 1
        
        else:
            new_arr[k] = right_arr[r]
            r += 1
        
        k += 1
    
    while l < len(left_arr):
        new_arr[k] = left_arr[l]
        l += 1
        k += 1
    
    while r < len(right_arr):
        new_arr[k] = right_arr[r]
        r += 1
        k += 1
    
    return new_arr


print(merge_sort([3, 2, 5, 1]))

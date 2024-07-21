def merge_sort(arr):
    if len(arr) > 1:
        left_half = arr[:len(arr) // 2]
        right_half = arr[len(arr) // 2:]
        
        merge_sort(left_half)
        merge_sort(right_half)
        
        # here we start merging
        
        leftmost_l = 0  # index for left half
        leftmost_r = 0  # index for right half
        i = 0  # curr arr elem index
        
        while leftmost_l < len(left_half) and leftmost_r < len(right_half):
            if left_half[leftmost_l] < right_half[leftmost_r]:
                arr[i] = left_half[leftmost_l]
                leftmost_l += 1
            else:
                arr[i] = right_half[leftmost_r]
                leftmost_r += 1
            
            i += 1
            
        # we will always have some residuals
        while leftmost_l < len(left_half):
            arr[i] = left_half[leftmost_l]
            leftmost_l += 1
            i += 1
            
        while leftmost_r < len(right_half):
            arr[i] = right_half[leftmost_r]
            leftmost_r += 1
            i += 1
            
    return arr
    
    
print(merge_sort([3, 2, 0, 1, 3, 4, 6]))

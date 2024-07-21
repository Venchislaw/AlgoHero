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
    

print(selection_sort([2, 1, 4, 3, 3, 5, 1, 9, 8, 8, 7, 0]))      

def bucket_sort(arr):
    counts = [0] * (max(arr) + 1)
    
    for val in arr:
        counts[val] += 1
    
    k = 0
    for i in range(len(counts)):
        for _ in range(counts[i]):
            arr[k] = i
            k += 1
            
    return arr
    
print(bucket_sort([3, 2, 0, 1, 3, 4, 6]))

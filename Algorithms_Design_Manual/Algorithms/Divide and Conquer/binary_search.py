def binary_search(arr, key, low, high):
    mid = (low + high) // 2

    if low > high:
        return -1

    if key < arr[mid]:
        return binary_search(arr, key, low, mid-1)
    elif key > arr[mid]:
        return binary_search(arr, key, mid+1, high)
    else:
        return mid
    
for i in range(1, 6):
    print(binary_search([1, 2, 3, 4, 5], i, 0, 4))


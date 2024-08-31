def occurencies(arr, item):
    if arr == []:
        return 0
    elif arr[0] == item:
        return 1 + occurencies(arr[1:], item)
    else:
        return 0 + occurencies(arr[1:], item)
    

print(occurencies([1, 2, 2, 3, 4, 5], 2))

def sqrt(n, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2

    if mid ** 2 == n:
        return mid
    elif mid ** 2 < n:
        return sqrt(n, mid+1, high)
    else:
        return sqrt(n, low, mid-1)
    
print(sqrt(9, 1, 9))  # 3
print(sqrt(4, 1, 4))  # 2
print(sqrt(25, 1, 25))  # 5
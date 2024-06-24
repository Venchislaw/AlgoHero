def bucket_sort(array):
    buckets = [0 for _ in range(max(array) + 1)]
    print(buckets)

    for n in array:
        buckets[n] += 1

    i = 0
    for n in range(len(buckets)):
        for _ in range(buckets[n]):
            array[i] = n
            i += 1
    return array


print(bucket_sort([2, 5, 0, 1, 0, 1, 1]))

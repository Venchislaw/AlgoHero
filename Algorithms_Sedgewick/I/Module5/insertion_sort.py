def insertion_sort(seq):
    for l in range(len(seq)-1):
        r = l + 1

        while r > 0 and seq[r-1] > seq[r]:
            seq[r-1], seq[r] = seq[r], seq[r-1]
            r -= 1
        
    return seq


print(insertion_sort([3, 2, 4, 1]))  # 1234

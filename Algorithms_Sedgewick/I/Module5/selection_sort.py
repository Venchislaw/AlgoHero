def min_idx(seq):
    min_ = seq[0]
    idx = 0

    for i in range(1, len(seq)):
        if seq[i] < min_:
            min_ = seq[i]
            idx = i
        
    return idx


def selection_sort(seq):
    new_seq = []
    while len(seq) > 0:
        i = min_idx(seq)
        new_seq.append(seq.pop(i))
    
    return new_seq


print(selection_sort([2, 1, 4, 3]))  # 1234
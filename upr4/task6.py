def conv(list1, list2):
    if not list1 or not list2:
        return []

    return [sum([list1[j] * list2[i - j] for j in range(max(0, i - len(list1) + 1),min(i + 1, len(list2)))]) 
            for i in range(len(list2) + len(list2) - 1)]

# Test cases
assert conv([1, 2, 3], [4, 5, 6]) == [4, 13, 28, 27, 18]
assert conv([1, 2, 3], [3, 2, 1]) == [3, 8, 14, 8, 3]
assert conv([2, 4, 6, 7], [-1, -2, -3, -4]) == [-2, -8, -20, -39, -48, -45, -28]
assert conv([1], [2]) == [2]
assert conv([], []) == []

#    X[0..n] Y[0..n]
# Z[0..2n]
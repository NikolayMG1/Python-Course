from functools import reduce

# def power_of_matrix(matrix):
#     if not matrix:
#         return 0

#     diagonal1 = list(map(lambda i: matrix[i][i], range(len(matrix))))
#     diagonal2 = list(map(lambda i: matrix[i][len(matrix) - i - 1], range(len(matrix))))

#     return reduce(lambda x, y: x + y, diagonal1) - reduce(lambda x, y: x + y, diagonal2)

def power_of_matrix(matrix):
    if not matrix:
        return 0

    diagonal1 = [matrix[i][i] for i in range(len(matrix))]
    diagonal2 = [matrix[i][len(matrix) - i - 1] for i in range(len(matrix))]

    return sum(diagonal1) - sum(diagonal2)


matrix_1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix_2 = [
    [2, 3, 4, 5],
    [5, 6, 7, 8],
    [9, 1, 6, 3],
    [-2, 3, 7, 7]
]

matrix_3 = []

# Write your code here


assert power_of_matrix(matrix_1) == 0
assert power_of_matrix(matrix_2) == 10
assert power_of_matrix(matrix_3) == 0
matrix = [
    [1, 4, 7, 12, 15, 1000],
    [2, 5, 19, 31, 32, 1001],
    [3, 8, 24, 33, 35, 1002],
    [40, 41, 42, 44, 45, 1003],
    [99, 100, 103, 106, 128, 1004]
]

target = 4


def search_in_matrix(matrix, target):
    result = []
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            if matrix[row][column] == target:
                result = [row, column]
            else:
                result = [-1, -1]
    return result


print(search_in_matrix(matrix, target))

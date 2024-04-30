def rotate_matrix(mtx):
    n = len(mtx)
    for row in range(n // 2):
        for col in range((n + 1) // 2):
            temp = mtx[row][col]
            mtx[row][col] = mtx[n - 1 - col][row]
            mtx[n - 1 - col][row] = mtx[n - 1 - row][n - 1 - col]
            mtx[n - 1 - row][n - 1 - col] = mtx[col][n - 1 - row]
            mtx[col][n - 1 - row] = temp


def print_matrix(mtx):
    for row in mtx:
        print(' '.join(map(str, row)))


rows = int(input())
matrix = []
for _ in range(rows):
    matrix.append(list(map(int, input().split())))

rotate_matrix(matrix)
print_matrix(matrix)

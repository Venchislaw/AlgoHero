def dfs(matrix, r, c, visit):
    ROWS, COLS = len(matrix), len(matrix[0])
    if (min(r, c) < 0 or
        r == ROWS or c == COLS or
        (r, c) in visit or matrix[r][c] == 1):
        return 0
    elif r == ROWS - 1 and c == COLS - 1:
        return 1

    visit.add((r, c))
    count = 0

    count += dfs(matrix, r + 1, c, visit)
    count += dfs(matrix, r - 1, c, visit)
    count += dfs(matrix, r, c + 1, visit)
    count += dfs(matrix, r, c - 1, visit)

    visit.remove((r, c))

    return count


grid = [[0, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 0, 1],
        [0, 1, 0, 0]]

print(dfs(grid, 0, 0, set()))


def dfs_graph(matrix, r, c, visited):
    ROWS, COLS = len(matrix), len(matrix[0])

    if r >= ROWS or c >= COLS or r < 0 or c < 0 or (r, c) in visited or matrix[r][c] == 1:
        return 0

    if r == ROWS - 1 and c == COLS - 1:
        return 1

    visited.add((r, c))

    count = 0
    count += dfs_graph(matrix, r + 1, c, visited)
    count += dfs_graph(matrix, r - 1, c, visited)
    count += dfs_graph(matrix, r, c + 1, visited)
    count += dfs_graph(matrix, r, c - 1, visited)

    visited.remove((r, c))

    return count


grid = [[0, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 0, 1],
        [0, 1, 0, 0]]

print(dfs_graph(grid, 0, 0, set()))


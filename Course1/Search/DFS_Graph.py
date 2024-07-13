def dfs_graph(matrix, visited, r=0, c=0):
    ROWS, COLS = len(matrix), len(matrix[0])

    if (min(r, c) < 0 or r == ROWS
        or c == COLS or (r, c) in visited
        or matrix[r][c] == 1):
        return 0
    elif r == ROWS - 1 and c == COLS - 1:
        return 1

    count = 0

    visited.add((r, c))

    count += dfs_graph(matrix, visited, r + 1, c)
    count += dfs_graph(matrix, visited, r - 1, c)
    count += dfs_graph(matrix, visited, r, c + 1)
    count += dfs_graph(matrix, visited, r, c - 1)

    visited.remove((r, c))

    return count


grid = [[0, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 0, 1],
        [0, 1, 0, 0]]

print(dfs_graph(grid, set()))

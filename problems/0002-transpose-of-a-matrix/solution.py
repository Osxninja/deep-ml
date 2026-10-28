def transpose_matrix(a):
    # Handle empty / degenerate input
    if not a or not a[0]:
        return []

    rows, cols = len(a), len(a[0])

    # New matrix: cols × rows; entry (i, j) -> (j, i)
    return [[a[i][j] for i in range(rows)] for j in range(cols)]
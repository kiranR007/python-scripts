def diagonal_sum(matrix):
    n = len(matrix)
    total = 0
    for i in range(n):
        total += matrix[i][i]  # Primary diagonal
        total += matrix[i][n-i-1]  # Secondary diagonal
    if n % 2 == 1:
        total -= matrix[n//2][n//2]  # Remove center if counted twice
    return total

# Test
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(diagonal_sum(matrix))  # Output: 25

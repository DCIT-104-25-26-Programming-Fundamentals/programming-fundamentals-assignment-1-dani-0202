# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================
def read_matrix(rows, columns):
    matrix = []

    for i in range(rows):
        row = list(map(float, input(f"Enter row {i + 1}: ").split()))
        matrix.append(row)

    return matrix


def display_matrix(matrix):
    for row in matrix:
        for value in row:
            print(f"{value:8.2f}", end="")
        print()


def transpose_matrix(matrix):
    transpose = []

    for j in range(len(matrix[0])):
        row = []

        for i in range(len(matrix)):
            row.append(matrix[i][j])

        transpose.append(row)

    return transpose


def add_matrices(matrix1, matrix2):
    result = []

    for i in range(len(matrix1)):
        row = []

        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])

        result.append(row)

    return result


def multiply_matrices(matrix1, matrix2):
    result = []

    for i in range(len(matrix1)):
        row = []

        for j in range(len(matrix2[0])):
            total = 0

            for k in range(len(matrix2)):
                total += matrix1[i][k] * matrix2[k][j]

            row.append(total)

        result.append(row)

    return result


rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))

matrix = read_matrix(rows, columns)
display_matrix(transpose_matrix(matrix))


rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))

matrix1 = read_matrix(rows, columns)
matrix2 = read_matrix(rows, columns)

display_matrix(add_matrices(matrix1, matrix2))


rows_a = int(input("Enter number of rows: "))
columns_a = int(input("Enter number of columns: "))

matrix1 = read_matrix(rows_a, columns_a)

rows_b = int(input("Enter number of rows: "))
columns_b = int(input("Enter number of columns: "))

matrix2 = read_matrix(rows_b, columns_b)

if columns_a == rows_b:
    display_matrix(multiply_matrices(matrix1, matrix2))
else:
    print("Matrix multiplication is not possible.")
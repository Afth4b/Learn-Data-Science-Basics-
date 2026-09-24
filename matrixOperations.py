# Read the number of rows and columns for Matrix 1 and create the matrix by reading its elements.
# Read the number of rows and columns for Matrix 2 and create the matrix by reading its elements.
# Find the product of Matrix 1 and Matrix 2.
# Find the transpose of both matrices.
# Find the trace of both matrices.
# Find the rank of both matrices.
# Find the determinant of Matrix 1.
# Find the inverse of Matrix 2.

import numpy as np

r1 = int(input("Enter number of rows for matrix 1 : "))
c1 = int(input("Enter number of columns matrix 1 : "))

print("Enter elements of matrix 1 : \n")

matrix1 = []

for i in range(r1):
    row = []
    for j in range(c1):
        value = float(input(f"Enter element[{i}][{j}] : "))
        row.append(value)
    matrix1.append(row)

r2 = int(input("Enter number of rows for matrix 2 : "))
c2 = int(input("Enter number of columns matrix 2 : "))

print("Enter elements of matrix 2 : \n")

matrix2 = []

for i in range(r2):
    row = []
    for j in range(c2):
        value = float(input(f"Enter element[{i}][{j}] : "))
        row.append(value)
    matrix2.append(row)

# convert to numpy arrays for numeric operations
matrix1 = np.array(matrix1, dtype=float)
matrix2 = np.array(matrix2, dtype=float)

print("Matrix 1 :")
print(matrix1)
print("Matrix 2 :")
print(matrix2)

# matrix multiplication (check dimensions)
if c1 != r2:
    print(f"\nCannot multiply: columns of matrix 1 ({c1}) != rows of matrix 2 ({r2})")
else:
    multi = np.dot(matrix1, matrix2)
    print("\nMatrix multiplication :")
    print(multi)

# Transpose of the matrix
print("\nTranspose of matrix 1 :")
print(matrix1.T)
print("Transpose of matrix 2 :")
print(matrix2.T)

# Trace of matrix
if r1 == c1:
    print("\nTrace of matrix 1 :", np.trace(matrix1))
else:
    print("\nTrace of matrix 1 cannot be computed: not a square matrix")

if r2 == c2:
    print("Trace of matrix 2 :", np.trace(matrix2))
else:
    print("Trace of matrix 2 cannot be computed: not a square matrix")

# Rank
print("\nRank of matrix 1 :", np.linalg.matrix_rank(matrix1))
print("Rank of matrix 2 :", np.linalg.matrix_rank(matrix2))

# Determinant of matrix1 (if square)
if r1 == c1:
    try:
        det1 = float(np.linalg.det(matrix1))
        if np.isclose(det1, round(det1)):
            det1 = int(round(det1))
        print("\nDeterminant of matrix 1 :", det1)
    except Exception as e:
        print("\nCould not compute determinant of matrix 1:", e)
else:
    print("\nDeterminant of matrix 1 cannot be computed: not a square matrix")

# Inverse of matrix2 (if square and non-singular)
if r2 == c2:
    try:
        det2 = float(np.linalg.det(matrix2))
        if np.isclose(det2, 0.0):
            print("\nMatrix 2 is singular (determinant is zero); inverse does not exist")
        else:
            inv2 = np.linalg.inv(matrix2)
            print("\nInverse of matrix 2 :")
            print(inv2)
    except Exception as e:
        print("\nCould not compute inverse of matrix 2:", e)
else:
    print("\nInverse of matrix 2 cannot be computed: not a square matrix")


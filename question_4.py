import numpy as np


middle_matrix = matrix[1:4, 1:4]
print("\nMiddle 3x3 Matrix:")
print(middle_matrix)


first_row = middle_matrix[0, :]
last_col = middle_matrix[:, -1]

print("\nFirst row of 3x3 matrix:", first_row)
print("Last column of 3x3 matrix:", last_col)


dot_product = np.dot(first_row, last_col)
print("\nDot Product of first row and last column:", dot_product)

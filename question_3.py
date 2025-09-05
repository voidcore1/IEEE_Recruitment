import numpy as np


matrix = np.random.randint(1, 101, size=(5, 5))
print("Original 5x5 Matrix:")
print(matrix)


max_val = np.max(matrix)
min_val = np.min(matrix)
mean_val = np.mean(matrix)

print("\nMaximum value:", max_val)
print("Minimum value:", min_val)
print("Mean value:", mean_val)


normalized_matrix = (matrix - min_val) / (max_val - min_val)
print("\nNormalized Matrix (values between 0 and 1):")
print(normalized_matrix)

# Flatten and sort
flattened_sorted = np.sort(matrix.flatten())
print("\nFlattened and Sorted Array:")
print(flattened_sorted)

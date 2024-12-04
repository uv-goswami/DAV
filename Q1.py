import numpy as np

# a. Create a two-dimensional array, ARR1 having random values from 0 to 1.
ARR1 = np.random.rand(5, 5)  # Example size 5x5
mean_arr1 = np.mean(ARR1, axis=1)
std_arr1 = np.std(ARR1, axis=1)
var_arr1 = np.var(ARR1, axis=1)

print("ARR1:\n", ARR1)
print("Mean along second axis:", mean_arr1)
print("Standard Deviation along second axis:", std_arr1)
print("Variance along second axis:", var_arr1)

# b. Create a 2-dimensional array of size m x n integer elements.
m = int(input("Enter number of rows (m): "))
n = int(input("Enter number of columns (n): "))
array_2d = np.random.randint(0, 100, size=(m, n))
print("Array shape:", array_2d.shape)
print("Array type:", type(array_2d))
print("Data type of array elements:", array_2d.dtype)

# Reshape it into an n x m array
reshaped_array = array_2d.reshape(n, m)
print("Reshaped Array:\n", reshaped_array)

# c. Test whether the elements of a given 1D array are zero, non-zero and NaN.
array_1d = np.array([0, 1, 2, np.nan, 3, 0, np.nan])
zero_indices = np.where(array_1d == 0)[0]
non_zero_indices = np.where(array_1d != 0)[0]
nan_indices = np.where(np.isnan(array_1d))[0]

print("Indices of zeros:", zero_indices)
print("Indices of non-zeros:", non_zero_indices)
print("Indices of NaNs:", nan_indices)

# d. Create three random arrays of the same size.
Array1 = np.random.rand(5)
Array2 = np.random.rand(5)
Array3 = np.random.rand(5)

Array4 = Array3 - Array2
Array5 = 2 * Array1

covariance = np.cov(Array1, Array4)[0][1]
correlation = np.corrcoef(Array1, Array5)[0][1]

print("Array1:", Array1)
print("Array2:", Array2)
print("Array3:", Array3)
print("Array4 (Array3 - Array2):", Array4)
print("Array5 (2 * Array1):", Array5)
print("Covariance of Array1 and Array4:", covariance)
print("Correlation of Array1 and Array5:", correlation)

# e. Create two random arrays of the same size 10.
Array1 = np.random.rand(10)
Array2 = np.random.rand(10)

sum_first_half = np.sum(Array1[:5]) + np.sum(Array2[:5])
product_second_half = np.prod(Array1[5:]) * np.prod(Array2[5:])

print("Sum of first half of both arrays:", sum_first_half)
print("Product of second half of both arrays:", product_second_half)

# f. Create an array with random values and determine the size of the memory occupied by the array.
random_array = np.random.rand(1000)  # Example size
memory_size = random_array.nbytes  # Size in bytes
print("Memory size occupied by the array:", memory_size, "bytes")

# g. Create a 2-dimensional array of size m x n having integer elements in the range (10,100).
m = 5
n = 5
int_array = np.random.randint(10, 100, size=(m, n))
print("Original Array:\n", int_array)

# Swap any two rows (e.g., row 0 and row 1)
int_array[[0, 1]] = int_array[[1, 0]]
print("Array after swapping rows 0 and 1:\n", int_array)

# Reverse a specified column (e.g., column 2)
int_array[:, 2] = int_array[::-1, 2]
print("Array after reversing column 2:\n", int_array)
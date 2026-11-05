# 1. Write a Python program using NumPy to create a one-dimensional array containing 10 integers and display the array, its size, data type, and number of dimensions.

import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

print("Array:", arr)

print("Size:", arr.size)

print("Data Type:", arr.dtype)

print("Number of Dimensions:", arr.ndim)

# =========================================================================

# 2.	Create two NumPy arrays of 5 integers each. Perform and display:
# •	Addition 
# •	Subtraction 
# •	Multiplication 
# •	Division 
# •	Modulus

a = np.array([10,20,30,40,50])
b = np.array([2,4,5,8,10])
print("Addition:", a+b)
print("Subtraction:", a-b)
print("Multiplication:", a*b)
print("Division:", a/b)
print("Modulus:", a%b)

# ===========================================================================

# 3. Create a NumPy array containing 10 numbers. Find and display the maximum, minimum, sum, and average of the elements.

a = np.array([12,25,8,45,32,19,50,7,28,15])
print("Maximum:", np.max(a))
print("Minimum:", np.min(a))
print("Sum:", np.sum(a))
print("Average:", np.mean(a))

# =============================================================================

# 4. Create a NumPy array of integers from 1 to 20. Use Boolean indexing to separate and display the even and odd numbers.

a = np.arange(1,21)
print("Even numbers:", a[a%2==0])
print("Odd numbers:", a[a%2!=0])

# =============================================================================

# 5.	Create a one-dimensional array containing numbers from 1 to 12. Reshape it into:
# •	2 × 6 matrix 
# •	3 × 4 matrix 
# •	4 × 3 matrix

a = np.arange(1,13)
print("2 x 6:")
print(a.reshape(2,6))
print("3 x 4:")
print(a.reshape(3,4))
print("4 x 3:")
print(a.reshape(4,3))

# ==============================================================================

# 6. Create two 3 × 3 NumPy matrices and perform matrix addition.

a = np.array([[1,2,3],[4,5,6],[7,8,9]])
b = np.array([[9,8,7],[6,5,4],[3,2,1]])
print(a+b)

# =============================================================================

# 7. Create two compatible matrices using NumPy and perform matrix multiplication using an appropriate NumPy function.

a = np.array([[1,2,3],[4,5,6]])
b = np.array([[7,8],[9,10],[11,12]])
print(np.dot(a,b))

# ==============================================================================

# 8. Create a 3 × 4 matrix and display its transpose.

a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print("Original:")
print(a)
print("Transpose:")
print(a.T)

# ==============================================================================

# 9. Create a 4 × 4 NumPy array and write a program to:
# •	Display the first row 
# •	Display the last column 
# •	Display the diagonal elements 
# •	Display the elements from the second and third rows

a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
print("First row:", a[0])
print("Last column:", a[:,-1])
print("Diagonal:", np.diag(a))
print("Second row:", a[1])
print("Third row:", a[2])

# ================================================================================

# # 10: Sum of rows and columns
a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
print("Row sums:", np.sum(a,axis=1))
print("Column sums:", np.sum(a,axis=0))

# =================================================================================

# 11: Array slicing
a = np.arange(1,21)
print("First 5:", a[:5])
print("Last 5:", a[-5:])
print("Alternate:", a[::2])
print("Reverse:", a[::-1])

# ===================================================================================

# 12: Replace values greater than 50 with 0
a = np.array([25,60,45,80,30,75,10,90,55,40])
a[a>50] = 0
print(a)

#====================================================================================

# 13: Ascending and descending order
a = np.array([45,12,78,23,9,56,34])
print("Ascending:", np.sort(a))
print("Descending:", np.sort(a)[::-1])

# ===================================================================================

# 14: Unique elements
a = np.array([10,20,10,30,20,40,30,50,40])
print(np.unique(a))

# ===================================================================================

# 15: Horizontal and vertical concatenation
a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])
print("Horizontal:")
print(np.hstack((a,b)))
print("Vertical:")
print(np.vstack((a,b)))

# ===================================================================================

# 16: Marks of 10 students
marks = np.array([75,82,68,90,55,78,88,72,95,60])
print("Highest:", np.max(marks))
print("Lowest:", np.min(marks))
print("Average:", np.mean(marks))
print("Median:", np.median(marks))
print("Standard deviation:", np.std(marks))

#======================================================================================

# 17: Class average and marks above average
marks = np.array([65,72,81,55,90,76,84,69,95,61,73,88,79,52,67,91,70,85,63,77])
average = np.mean(marks)
print("Class average:", average)
print("Above average:", marks[marks>average])

# =====================================================================================

# 18: 3D array
a = np.arange(1,25).reshape(2,3,4)
print(a)
print("Dimensions:", a.ndim)
print("Shape:", a.shape)
print("Size:", a.size)

# ======================================================================================

# 19: Access elements from 3D array
a = np.arange(1,25).reshape(2,3,4)
print("First element:", a[0,0,0])
print("Last element:", a[1,2,3])
print("Element [0,1,2]:", a[0,1,2])
print("Element [1,2,3]:", a[1,2,3])

# =========================================================================================

# 20: Sums in 3D array
a = np.arange(1,25).reshape(2,3,4)
print("Total sum:", np.sum(a))
print("Layer sums:", np.sum(a,axis=(1,2)))
print("Row sums:", np.sum(a,axis=1))
print("Column sums:", np.sum(a,axis=2))

# ==========================================================================================

# 21: Replace values greater than 50 in random 3D array
a = np.random.randint(1,101,(2,3,4))
print("Original:")
print(a)
a[a>50] = 0
print("Updated:")
print(a)

# ========================================================================================

# 22: Statistics of random 3D array
a = np.random.randint(1,101,(3,4,5))
print("Mean:", np.mean(a))
print("Median:", np.median(a))
print("Standard deviation:", np.std(a))
print("Variance:", np.var(a))
print("Minimum:", np.min(a))
print("Maximum:", np.max(a))

# ==========================================================================================

# 23: Flatten a 3D array
a = np.arange(1,25).reshape(2,3,4)
print("Original:")
print(a)
print("Flattened:")
print(a.flatten())

# =========================================================================================

# 24: Flatten and calculate statistics
a = np.arange(1,28).reshape(3,3,3)
b = a.flatten()
print("Flattened array:", b)
print("Sum:", np.sum(b))
print("Average:", np.mean(b))
print("Maximum:", np.max(b))
print("Minimum:", np.min(b))

# =========================================================================================

# 25: Elements greater than 50, even and less than average
a = np.random.randint(1,101,(3,4,5))
b = a.flatten()
average = np.mean(b)
print("Original:")
print(a)
print("Greater than 50:", b[b>50])
print("Even elements:", b[b%2==0])
print("Less than average:", b[b<average])

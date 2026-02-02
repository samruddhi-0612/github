import numpy as np

A = np.random.randint(1, 10, (3, 3))
B = np.random.randint(1, 10, (3, 3))

print("Matrix A:")
print(A)

print("\nMatrix B:")
print(B)

# Matrix Addition
add = A + B
print("\nMatrix Addition:")
print(add)

# Matrix Multiplication
mul = np.dot(A, B)
print("\nMatrix Multiplication:")
print(mul)

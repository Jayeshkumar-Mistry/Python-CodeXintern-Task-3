import numpy as np

def matrix_operations_tool():
    print("Welcome to the Matrix Operations Tool!")
    print("=======================================")
    
    # Get matrix dimensions
    print("\nEnter the dimensions of the matrices:")
    rows = int(input("Number of rows: "))
    cols = int(input("Number of columns: "))
    
    if rows <= 0 or cols <= 0:
        print("Error: Dimensions must be positive numbers.")
        return
    
    # Function to input a matrix
    def get_matrix(name):
        print(f"\nEnter the elements of {name} (row by row, space-separated):")
        matrix = []
        for i in range(rows):
            row = input(f"Row {i + 1}: ").split()
            if len(row) != cols:
                print(f"Error: Row {i + 1} must have exactly {cols} elements.")
                return None
            matrix.append(list(map(float, row)))
        return np.array(matrix)
    
    # Input matrices
    matrix1 = get_matrix("Matrix 1")
    if matrix1 is None:
        return
    
    matrix2 = get_matrix("Matrix 2")
    if matrix2 is None:
        return
    
    # Display matrices
    print("\nMatrix 1:")
    print(matrix1)
    print("\nMatrix 2:")
    print(matrix2)
    
    # Perform operations
    print("\nMatrix Addition:")
    print(matrix1 + matrix2)
    
    print("\nMatrix Subtraction:")
    print(matrix1 - matrix2)
    
    if matrix1.shape[1] == matrix2.shape[0]:
        print("\nMatrix Multiplication:")
        print(np.dot(matrix1, matrix2))
    else:
        print("\nMatrix Multiplication not possible due to incompatible dimensions.")
    
    print("\nTranspose of Matrix 1:")
    print(matrix1.T)
    
    if rows == cols:
        print("\nDeterminant of Matrix 1:")
        print(round(np.linalg.det(matrix1), 2))
    else:
        print("\nDeterminant not possible for non-square matrices.")

# Running the tool
matrix_operations_tool()

import numpy as np
import matplotlib.pyplot as plt

# Function to create a rectangle
def create_rectangle():
    # Get user input for dimensions
    rows = int(input("Enter number of rows: "))
    columns = int(input("Enter number of columns: "))

    # Create empty matrix with given dimensions
    rectangle = np.zeros((rows, columns))

    # Fill in matrix with 1s to represent the shape
    for rows in range(rows):
        for col in range(columns):
            rectangle[row][col] = 1

    # Plot the matrix using matplotlib
    plt.imshow(rectangle, cmap='binary')
    plt.show()

# Function to create a circle
def create_circle():
    # Get user input for radius
    radius = int(input("Enter radius: "))

    # Create empty matrix with given dimensions
    circle = np.zeros((2*radius+1, 2*radius+1))

    # Fill in matrix with 1s to represent the shape

    for i in range(2*radius+1):
        for j in range(2*radius+1):
            if (i-radius)**2 + (j-radius)**2 <= radius**2:
                circle[i][j] = 1

    # Plot the matrix using matplotlib
    plt.imshow(circle, cmap='binary')
    plt.show()

# Function to create a triangle
def create_triangle():
    # Get user input for height
    height = int(input("Enter height: "))

    # Create empty matrix with given dimensions
    triangle = np.zeros((height, height))

    # Fill in matrix with 1s to represent the shape

    for row in range(height):
        for col in range(row+1):
            triangle[row][col] = 1

    # Plot the matrix using matplotlib
    plt.imshow(triangle, cmap='binary')
    plt.show()

# Main program
print("Welcome to the shape creator!")
print("Choose a shape to create:")
print("1. Rectangle")
print("2. Circle")
print("3. Triangle")
shape = int(input("Enter your choice (1-3): "))

if shape == 1:
    create_rectangle()
elif shape == 2:
    create_circle()

elif shape == 3:
    create_triangle()
else:
    print("Invalid choice. Please try again.")

import matplotlib.pyplot as plt
import numpy as np

def draw_line():
    x = np.linspace(0, 10, 100)
    y =  x + 1
    plt.plot(x, y, color='red')  # Red color
    plt.show()

def draw_parallel_lines():
    x = np.linspace(0, 10, 100)
    y1 = 2 * x + 1
    y2 = 2 * x + 3
    plt.plot(x, y1, label='y = 2x + 1', color='green')  # Green color
    plt.plot(x, y2, label='y = 2x + 3', color='blue')  # Blue color
    plt.legend()
    plt.show()

def draw_triangle():
    x = [1, 3, 2, 1]
    y = [1, 1, 3, 1]
    plt.fill(x, y, color='yellow')  # Yellow color
    plt.show()

def draw_rectangle():
    x = [1, 3, 3, 1, 1]
    y = [1, 1, 3, 3, 1]
    plt.fill(x, y, color='cyan')  # Cyan color
    plt.show()

def draw_polygon(num_sides):
    angles = np.linspace(0, 2*np.pi, num_sides+1)
    x = np.cos(angles)
    y = np.sin(angles)
    plt.fill(x, y, color='magenta')  # Magenta color
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

def draw_circle(radius):
    angles = np.linspace(0, 2*np.pi, 100)
    x = radius * np.cos(angles)
    y = radius * np.sin(angles)
    plt.fill(x, y, color='black')  # Black color
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

def main():
    num_lines = int(input("Enter the number of lines: "))
    
    if num_lines == 1:
        draw_line()
    elif num_lines == 2:
        draw_parallel_lines()
    elif num_lines == 3:
        draw_triangle()
    elif num_lines == 4:
        draw_rectangle()
    elif num_lines >= 5:
        draw_polygon(num_lines)
    elif num_lines >= 23:
        radius = float(input("Enter the radius of the circle: "))
        draw_circle(radius)
    else:
        print("Invalid number of lines.")

if __name__ == "__main__":
    main()


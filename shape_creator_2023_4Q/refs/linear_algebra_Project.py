import tkinter as tk

class ShapeCreator:
    def __init__(self, root):
        self.root = root
        self.root.title("Shape Creator")

        self.canvas = tk.Canvas(self.root, width=400, height=400, bg="white")
        self.canvas.pack()

        self.shape_type = tk.StringVar()
        self.shape_type.set("Rectangle")

        shape_options = ["Rectangle", "Circle", "Triangle"]
        shape_menu = tk.OptionMenu(self.root, self.shape_type, *shape_options)
        shape_menu.pack()

        draw_button = tk.Button(self.root, text="Draw", command=self.draw_shape)
        draw_button.pack()

    def draw_shape(self):
        if self.shape_type.get() == "Rectangle":
            self.canvas.create_rectangle(50, 50, 150, 150, outline="black")
        elif self.shape_type.get() == "Circle":
            self.canvas.create_oval(50, 50, 150, 150, outline="black")
        elif self.shape_type.get() == "Triangle":
            self.canvas.create_polygon(100, 50, 50, 150, 150, 150, outline="black")

if __name__ == "__main__":
    root = tk.Tk()
    app = ShapeCreator(root)
    root.mainloop()

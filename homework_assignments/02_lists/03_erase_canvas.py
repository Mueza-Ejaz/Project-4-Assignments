# Problem Statement:
# Implement an 'eraser' on a canvas.

# The canvas consists of a grid of blue 'cells' which are drawn as rectangles on the screen. We then create an eraser rectangle which, when dragged around the canvas, sets all of the rectangles it is in contact with to white.

# conclusion of problem statement:
# is me aik rectangle shape banani hy or us k andar blue color k cells or phir aik chotta sa eraser hoga wo jis jis cell par jaiga usy white kardy ga.


import tkinter as tk

# Canvas size
WIDTH, HEIGHT = 400, 400
CELL_SIZE = 30


root = tk.Tk() # create the main window(jis me hum apni canvas drawing rakhaingy)

root.title("Eraser on Canvas")# title(top par name show hoga canva ka ) 

# Create a area of canvas:
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="white") 

# ye canvas ko window k andar show karwai ga 
canvas.pack()

# Draw the grid with blue cells
cells = []
for h in range(0, WIDTH, CELL_SIZE):
    for v in range(0, HEIGHT, CELL_SIZE):
        rect = canvas.create_rectangle(h, v, h + CELL_SIZE, v + CELL_SIZE, fill="blue", outline="black")
        cells.append(rect)

# Create an eraser
eraser = canvas.create_rectangle(50, 50, 90, 90, fill="black") # to define a top-right eraser position and size

# Move the eraser with the mouse
def move_eraser(event):
    x, y = event.x, event.y
    canvas.coords(eraser, x-14, y-14, x+14, y+14)

    # Erase cells (make them white)
    for rect in cells:
        x1, y1, x2, y2 = canvas.coords(rect)
        ex1, ey1, ex2, ey2 = canvas.coords(eraser)
        if not (x2 < ex1 or x1 > ex2 or y2 < ey1 or y1 > ey2):  # Collision detection
            canvas.itemconfig(rect, fill="white")

# Bind mouse movement
canvas.bind("<Motion>", move_eraser)

# Run the app
root.mainloop()







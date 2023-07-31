import tkinter as tk

def draw_square(canvas):
    canvas.create_rectangle(50, 50, 150, 150, fill='green')

# Create the main application window
root = tk.Tk()
root.title("Canvas Models: Square and rectangle")

# Create two canvas widgets
canvas_square = tk.Canvas(root, width=200, height=200, bg='white')
canvas_square.pack(side=tk.LEFT, padx=10, pady=10)
# Draw the square and on respective canvases
draw_square(canvas_square)

# Run the main loop
root.mainloop()
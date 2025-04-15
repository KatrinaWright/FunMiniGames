import tkinter as tk
import math

def draw_spiral(canvas, center_x, center_y, num_turns, spacing):
    """
    Draws a spiral on a Tkinter canvas.

    Parameters:
        canvas: The Tkinter canvas to draw on.
        center_x: The x-coordinate of the spiral's center.
        center_y: The y-coordinate of the spiral's center.
        num_turns: The number of turns in the spiral.
        spacing: The distance between successive turns of the spiral.
    """
    angle = 0
    radius = 0
    step = 2 * math.pi / 100  # Smaller step for smoother spiral

    points = []

    while radius <= num_turns * spacing:
        x = center_x + radius * math.cos(angle)
        y = center_y + radius * math.sin(angle)
        points.append((x, y))

        angle += step
        radius += spacing * step / (2 * math.pi)

    # Draw the spiral as a series of connected lines
    for i in range(len(points) - 1):
        canvas.create_line(points[i][0], points[i][1], points[i + 1][0], points[i + 1][1], fill="blue")

# Create the Tkinter window
root = tk.Tk()
root.title("Spiral Drawer")

# Set up the canvas
canvas_width = 600
canvas_height = 600
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="white")
canvas.pack()

# Draw the spiral in the center of the canvas
draw_spiral(canvas, center_x=canvas_width // 2, center_y=canvas_height // 2, num_turns=10, spacing=10)

# Run the Tkinter main loop
root.mainloop()
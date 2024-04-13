import tkinter as tk
import random

# Initialize the game window
window = tk.Tk()
window.title("Minesweeper")

# Game settings
grid_size = 9
num_mines = 10

minefield = [[0 for _ in range(grid_size)] for _ in range(grid_size)]

# Place mines randomly
mines_placed = 0
while mines_placed < num_mines:
    x = random.randrange(grid_size)
    y = random.randrange(grid_size)
    if minefield[x][y] != 'X':
        minefield[x][y] = 'X'
        mines_placed += 1
print(minefield)
window.mainloop()


# import csv
# import itertools

# import random

# def create_nonogram_csv(filename, width=10, height=10):
#     board = []

#     # Generate clues with a mix of single and split clues
#     clues_row = [generate_clue(width) for _ in range(height)]
#     clues_col = [generate_clue(height) for _ in range(width)]

#     # Create the board with approximately half 'V' and half '8'
#     for _ in range(height):
#         row = ['V' if random.random() < 0.5 else '8' for _ in range(width)]
#         board.append(row)

#     # Write to CSV file
#     with open(filename, 'w', newline='') as file:
#         writer = csv.writer(file)
#         writer.writerow([''] + clues_row)
#         for i, row in enumerate(board):
#             writer.writerow([clues_col[i]] + row)

# def generate_clue(size):
#     """Generates a random nonogram clue, ensuring at least one split"""
#     segments = []
#     while sum(segments) < size:
#         segment_size = random.randint(1, size // 2)
#         segments.append(segment_size)

#     # Force at least one split if all segments were size 1
#     if len(segments) > 1 and all(s == 1 for s in segments):
#         segments[0] += 1
#         segments[1] -= 1

#     return '/'.join(str(s) for s in segments)

# # Example usage:
 

# def read_nonogram_csv(filename):
#     with open(filename, 'r') as file:
#         reader = csv.reader(file)
#         nonogram = list(reader)

#     # Separate the clues from the board
#     clues_row = nonogram[0][1:]
#     clues_col = [row[0] for row in nonogram[1:]]
#     board = [row[1:] for row in nonogram[1:]]
    
#     # Print the nonogram in a console-viewable way
#     print('   ', *clues_row)  # Print the column clues
#     for i, row in enumerate(board):
#         print(clues_col[i], *row)

#     # Determine if the board is filled
#     is_filled = all("" not in row for row in board)
#     # is_filled = all('V' not in row for row in board)
#     print("\nBoard is filled:" , is_filled) 

#     # Initialize a flag for correctness
#     is_correct = True

#     # Verify rows
#     for i, row in enumerate(board):
#         expected = [int(x) for x in clues_col[i].split('/')]  # Fix: Use clues_col
#         actual = [len(list(group)) for key, group in itertools.groupby(row) if key == '8']
#         if expected != actual:
#             print(f"Row {i+1} has incorrect markings: expected {expected}, found {actual}")
#             is_correct = False

#     # Verify columns 
#     for j, col in enumerate(zip(*board)):
#         expected = [int(x) for x in clues_row[j].split('/')]  # Fix: Use clues_row
#         actual = [len(list(group)) for key, group in itertools.groupby(col) if key == '8']
#         if expected != actual:
#             print(f"Column {j+1} has incorrect markings: expected {expected}, found {actual}")
#             is_correct = False

#     if is_correct:
#         print("Correct!")

#     return clues_row, clues_col, board
    

# #Example usage: 
# create_nonogram_csv('my_nonogram.csv', width=10, height=10)
# clues_row, clues_col, board = read_nonogram_csv('nonogram_puzzle.csv')



# import csv
# import itertools
# import random
# import tkinter as tk
# from tkinter import font

# class NonogramVisualizer:
#     def __init__(self, root, clues_row, clues_col, board):
#         self.root = root
#         self.root.title("Nonogram Puzzle")
        
#         self.clues_row = clues_row
#         self.clues_col = clues_col
#         self.board = board
        
#         # Calculate dimensions
#         self.cell_size = 40
#         self.clue_width = 60
#         self.clue_height = 60
        
#         # Create canvas
#         total_width = self.clue_width + len(board[0]) * self.cell_size
#         total_height = self.clue_height + len(board) * self.cell_size
#         self.canvas = tk.Canvas(root, width=total_width, height=total_height, bg='white')
#         self.canvas.pack(padx=20, pady=20)
        
#         self.draw_grid()
#         self.draw_clues()
#         self.draw_board()

#     def draw_grid(self):
#         # Draw vertical lines
#         for i in range(len(self.board[0]) + 1):
#             x = self.clue_width + i * self.cell_size
#             self.canvas.create_line(x, self.clue_height, 
#                                   x, self.clue_height + len(self.board) * self.cell_size,
#                                   fill='black')
        
#         # Draw horizontal lines
#         for i in range(len(self.board) + 1):
#             y = self.clue_height + i * self.cell_size
#             self.canvas.create_line(self.clue_width, y,
#                                   self.clue_width + len(self.board[0]) * self.cell_size, y,
#                                   fill='black')

#     def draw_clues(self):
#         # Draw column clues
#         for col in range(len(self.clues_row)):
#             clue = self.clues_row[col]
#             x = self.clue_width + col * self.cell_size + self.cell_size/2
#             y = self.clue_height/2
#             self.canvas.create_text(x, y, text=clue, font=('Arial', 10))

#         # Draw row clues
#         for row in range(len(self.clues_col)):
#             clue = self.clues_col[row]
#             x = self.clue_width/2
#             y = self.clue_height + row * self.cell_size + self.cell_size/2
#             self.canvas.create_text(x, y, text=clue, font=('Arial', 10))

#     def draw_board(self):
#         for row in range(len(self.board)):
#             for col in range(len(self.board[0])):
#                 x = self.clue_width + col * self.cell_size
#                 y = self.clue_height + row * self.cell_size
                
#                 # Fill cell based on value
#                 if self.board[row][col] == '8':
#                     self.canvas.create_rectangle(x, y, 
#                                               x + self.cell_size, y + self.cell_size,
#                                               fill='black')
#                 elif self.board[row][col] == 'V':
#                     # Draw an X for empty cells
#                     padding = 5
#                     self.canvas.create_line(x + padding, y + padding,
#                                           x + self.cell_size - padding,
#                                           y + self.cell_size - padding,
#                                           fill='red')
#                     self.canvas.create_line(x + self.cell_size - padding, y + padding,
#                                           x + padding, y + self.cell_size - padding,
#                                           fill='red')

# def generate_nonogram_csv(filename, width=10, height=10):
#     board = [['V' if random.random() < 0.5 else '8' for _ in range(width)] for _ in range(height)]

#     # Generate clues
#     clues_col = []
#     for row in board:
#         clue = '/'.join([str(len(list(group))) for key, group in itertools.groupby(row) if key == '8'])
#         clues_col.append(clue if clue else '0')
        
#     clues_row = []
#     for col in zip(*board):
#         clue = '/'.join([str(len(list(group))) for key, group in itertools.groupby(col) if key == '8'])
#         clues_row.append(clue if clue else '0')

#     with open(filename, 'w', newline='') as file: 
#         writer = csv.writer(file)
#         writer.writerow([''] + clues_row) 
#         for i, row in enumerate(board):
#             writer.writerow([clues_col[i]] + row)

# def read_nonogram_csv(filename):
#     with open(filename, 'r') as file:
#         reader = csv.reader(file)
#         nonogram = list(reader)

#     clues_row = nonogram[0][1:]
#     clues_col = [row[0] for row in nonogram[1:]]
#     board = [row[1:] for row in nonogram[1:]]
    
#     # Verify the puzzle
#     is_filled = all("" not in row for row in board)
#     print("\nBoard is filled:", is_filled)

#     is_correct = True

#     # Verify rows
#     for i, row in enumerate(board):
#         expected = [int(x) for x in clues_col[i].split('/')]
#         actual = [len(list(group)) for key, group in itertools.groupby(row) if key == '8']
#         if expected != actual:
#             print(f"Row {i+1} has incorrect markings: expected {expected}, found {actual}")
#             is_correct = False

#     # Verify columns 
#     for j, col in enumerate(zip(*board)):
#         expected = [int(x) for x in clues_row[j].split('/')]
#         actual = [len(list(group)) for key, group in itertools.groupby(col) if key == '8']
#         if expected != actual:
#             print(f"Column {j+1} has incorrect markings: expected {expected}, found {actual}")
#             is_correct = False

#     if is_correct:
#         print("Correct!")

#     return clues_row, clues_col, board

# # Example usage
# if __name__ == "__main__":
#     # Generate and read the puzzle
#     generate_nonogram_csv('random_nonogramMM1.csv', 10, 10)
#     clues_row, clues_col, board = read_nonogram_csv('random_nonogramMM1.csv')
    
#     # Create the visualization
#     root = tk.Tk()
#     app = NonogramVisualizer(root, clues_row, clues_col, board)
#     root.mainloop()

import csv
import itertools
import random
import os

def generate_nonogram_csv(filename, width=10, height=10):
    board = [['V' if random.random() < 0.5 else '8' for _ in range(width)] for _ in range(height)]

    # Generate clues - could be replaced with a more sophisticated logic for clue generation
    clues_col = []
    for row in board:
        clue = '/'.join([str(len(list(group))) for key, group in itertools.groupby(row) if key == '8'])
        clues_col.append(clue if clue else '0')
        
    clues_row = []
    for col in zip(*board):
        clue = '/'.join([str(len(list(group))) for key, group in itertools.groupby(col) if key == '8'])
        clues_row.append(clue if clue else '0')

    # Write the CSV file, adding in a blank spot at 0,0 to allow for the clues to be read in our solving program. 
    with open(filename, 'w', newline='') as file: 
        writer = csv.writer(file)
        writer.writerow([''] + clues_row) 
        for i, row in enumerate(board):
            writer.writerow([clues_col[i]] + row)

def read_nonogram_csv(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        nonogram = list(reader)

    # Separate the clues from the board
    clues_row = nonogram[0][1:]
    clues_col = [row[0] for row in nonogram[1:]]
    board = [row[1:] for row in nonogram[1:]]
    
    # Print the nonogram in an improved, graph-like format
    print_improved_nonogram(clues_row, clues_col, board)

    # Determine if the board is filled
    is_filled = all("" not in row for row in board)
    print("\nBoard is filled:", is_filled)

    # Initialize a flag for correctness
    is_correct = True

    # Verify rows
    for i, row in enumerate(board):
        expected = [int(x) for x in clues_col[i].split('/') if x != '0']
        actual = [len(list(group)) for key, group in itertools.groupby(row) if key == '8']
        if expected != actual:
            print(f"Row {i+1} has incorrect markings: expected {expected}, found {actual}")
            is_correct = False

    # Verify columns 
    for j, col in enumerate(zip(*board)):
        expected = [int(x) for x in clues_row[j].split('/') if x != '0']
        actual = [len(list(group)) for key, group in itertools.groupby(col) if key == '8']
        if expected != actual:
            print(f"Column {j+1} has incorrect markings: expected {expected}, found {actual}")
            is_correct = False

    if is_correct:
        print("Correct!")

    return clues_row, clues_col, board

def print_improved_nonogram(clues_row, clues_col, board):
    # Calculate the maximum width of column clues
    max_col_clue_width = max(len(clue.split('/')) for clue in clues_row)
    
    # Calculate the maximum width of row clues
    max_row_clue_width = max(len(clue) for clue in clues_col)
    
    # Print column clues
    for i in range(max_col_clue_width - 1, -1, -1):  # Start from bottom, go up
        print(' ' * (max_row_clue_width + 2), end='')
        for clue in clues_row:
            parts = clue.split('/')
            if i < len(parts):
                print(f'{parts[-(i+1)]:>2}', end=' ')  # Print from bottom up
            else:
                print('  ', end=' ')
        print()
    
    # Print horizontal line
    print(' ' * (max_row_clue_width + 1) + '+' + '-' * (len(board[0]) * 3 - 1))
    
    # Print board with row clues
    for i, row in enumerate(board):
        # Print row clues
        clue_parts = clues_col[i].split('/')
        print(f'{"/".join(clue_parts):>{max_row_clue_width}}', end=' |')
        
        # Print board cells
        for cell in row:
            if cell == '8':
                print(' ■ ', end='')
            elif cell == 'V':
                print(' · ', end='')
            else:
                print('   ', end='')
        print()

# Example usage:
script_dir = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(script_dir, 'random_nonogramMM1.csv')

generate_nonogram_csv(filename, 10, 10)
clues_row, clues_col, board = read_nonogram_csv(filename)

print(f"Generated and read nonogram from: {filename}")
# import csv
# import itertools

# import random

# def generate_nonogram_csv(filename, width=10, height=10):
#     board = [['V' if random.random() < 0.5 else '8' for _ in range(width)] for _ in range(height)]

#     # Generate clues - could be replaced with a more sophisticated logic for clue generation
#     clues_col = []
#     for row in board:
#         clue = '/'.join([str(len(list(group))) for key, group in itertools.groupby(row) if key == '8'])
#         clues_col.append(clue if clue else '0')
        
#     clues_row = []
#     for col in zip(*board):
#         clue = '/'.join([str(len(list(group))) for key, group in itertools.groupby(col) if key == '8'])
#         clues_row.append(clue if clue else '0')

#     # Ensure at least one split clue exists; add one if necessary 
#     # clues_row[0] += '/1'
#     # clues_col[0] += '/1'
#     # board[0][0] = 'V' # Ensure validity of added clue

#     # Write the CSV file, adding in a blank spot at 0,0 to allow for the clues to be read in our solving program. 
#     with open(filename, 'w', newline='') as file: 
#         writer = csv.writer(file)
#         writer.writerow([''] + clues_row) 
#         for i, row in enumerate(board):
#             writer.writerow([clues_col[i]] + row)

# #example usage: 
# # generate_nonogram_csv('random_nonogram.csv', 10, 10)

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

# generate_nonogram_csv('random_nonogramMM1.csv', 10, 10)
# clues_row, clues_col, board = read_nonogram_csv('random_nonogramMM1.csv')


# import csv
# import itertools
# import random

# def generate_nonogram_csv(filename, width=10, height=10):
#     board = [['V' if random.random() < 0.5 else '8' for _ in range(width)] for _ in range(height)]

#     # Generate clues - could be replaced with a more sophisticated logic for clue generation
#     clues_col = []
#     for row in board:
#         clue = '/'.join([str(len(list(group))) for key, group in itertools.groupby(row) if key == '8'])
#         clues_col.append(clue if clue else '0')
        
#     clues_row = []
#     for col in zip(*board):
#         clue = '/'.join([str(len(list(group))) for key, group in itertools.groupby(col) if key == '8'])
#         clues_row.append(clue if clue else '0')

#     # Ensure at least one split clue exists; add one if necessary 
#     # clues_row[0] += '/1'
#     # clues_col[0] += '/1'
#     # board[0][0] = 'V' # Ensure validity of added clue

#     # Write the CSV file, adding in a blank spot at 0,0 to allow for the clues to be read in our solving program. 
#     with open(filename, 'w', newline='') as file: 
#         writer = csv.writer(file)
#         writer.writerow([''] + clues_row) 
#         for i, row in enumerate(board):
#             writer.writerow([clues_col[i]] + row)

# def read_nonogram_csv(filename):
#     with open(filename, 'r') as file:
#         reader = csv.reader(file)
#         nonogram = list(reader)

#     # Separate the clues from the board
#     clues_row = nonogram[0][1:]
#     clues_col = [row[0] for row in nonogram[1:]]
#     board = [row[1:] for row in nonogram[1:]]
    
#     # Print the nonogram in an improved, graph-like format
#     print_improved_nonogram(clues_row, clues_col, board)

#     # Determine if the board is filled
#     is_filled = all("" not in row for row in board)
#     print("\nBoard is filled:", is_filled)

#     # Initialize a flag for correctness
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

# def print_improved_nonogram(clues_row, clues_col, board):
#     # Calculate the maximum width of column clues
#     max_col_clue_width = max(len(clue) for clue in clues_row)
    
#     # Calculate the maximum width of row clues
#     max_row_clue_width = max(len(clue) for clue in clues_col)
    
#     # Print column clues in a more compact way
#     max_parts = max(len(clue.split('/')) for clue in clues_row)
#     col_clues = []
#     for clue in clues_row:
#         parts = clue.split('/')
#         # Pad with empty strings to make all columns have same number of parts
#         padded_parts = parts + [''] * (max_parts - len(parts))
#         col_clues.append(padded_parts)
    
#     # Print column clues from bottom to top (closest to the board)
#     for i in range(max_parts - 1, -1, -1):
#         print(' ' * (max_row_clue_width + 2), end='')
#         for col in col_clues:
#             if col[i]:
#                 print(f'{col[i]:>2}', end=' ')
#             else:
#                 print('  ', end=' ')
#         print()
    
#     # Print horizontal line
#     print(' ' * (max_row_clue_width + 1) + '+' + '-' * (len(board[0]) * 3 - 1))
    
#     # Print board with row clues
#     for i, row in enumerate(board):
#         # Print row clues
#         clue_parts = clues_col[i].split('/')
#         print(f'{"/".join(clue_parts):>{max_row_clue_width}}', end=' |')
        
#         # Print board cells
#         for cell in row:
#             if cell == '8':
#                 print(' ■ ', end='')
#             elif cell == 'V':
#                 print(' · ', end='')
#             else:
#                 print('   ', end='')
#         print()

# # Example usage:
# generate_nonogram_csv('random_nonogramMM1.csv', 10, 10)
# clues_row, clues_col, board = read_nonogram_csv('random_nonogramMM1.csv')


import csv
import itertools
import random

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
    try:
        with open(filename, 'w', newline='') as file: 
            writer = csv.writer(file)
            writer.writerow([''] + clues_row) 
            for i, row in enumerate(board):
                writer.writerow([clues_col[i]] + row)
        print(f"Successfully generated new nonogram puzzle and saved to {filename}")
        
        # Verify the file was written by trying to read it
        with open(filename, 'r') as file:
            content = file.read()
            print(f"File size: {len(content)} bytes")
            
    except Exception as e:
        print(f"Error writing to file {filename}: {str(e)}")
        print(f"Attempting to write to /tmp/outputs/{filename} instead...")
        
        # Try writing to the /tmp/outputs directory instead
        filename = f"/tmp/outputs/{filename}"
        with open(filename, 'w', newline='') as file: 
            writer = csv.writer(file)
            writer.writerow([''] + clues_row) 
            for i, row in enumerate(board):
                writer.writerow([clues_col[i]] + row)
        print(f"Successfully saved to {filename}")
    return filename  # Return the filename so we know where it was actually saved

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
        expected = [int(x) for x in clues_col[i].split('/')]
        actual = [len(list(group)) for key, group in itertools.groupby(row) if key == '8']
        if expected != actual:
            print(f"Row {i+1} has incorrect markings: expected {expected}, found {actual}")
            is_correct = False

    # Verify columns 
    for j, col in enumerate(zip(*board)):
        expected = [int(x) for x in clues_row[j].split('/')]
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
filename = generate_nonogram_csv('random_nonogramClaude1.csv', 10, 10)
clues_row, clues_col, board = read_nonogram_csv(filename)
import pygame
import sys
import numpy as np


def is_connected_to_rivet(grid, rivets, position):
    """Checks if a part is connected to a rivet (iteratively)"""
    visited = set()
    queue = [position]


    while queue:
        x, y = queue.pop(0)
        if (x, y) in rivets:
            return True


        if (x, y) not in visited:
            visited.add((x, y))
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < grid.shape[0] and 0 <= ny < grid.shape[1] and \
                   grid[nx, ny] == 0:
                    queue.append((nx, ny))
    return False


def break_section(grid, position):
    """Marks a section as broken and propagates to connected parts"""
    grid[position] = 1
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        nx, ny = position[0] + dx, position[1] + dy
        if 0 <= nx < grid.shape[0] and 0 <= ny < grid.shape[1] and \
           grid[nx, ny] == 0:
            break_section(grid, (nx, ny))




# Initialize Pygame
pygame.init()


# Set up some constants
WIDTH, HEIGHT = 800, 800
SQUARE_SIZE = 40


# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))


# Set up the font
font = pygame.font.SysFont('Arial', 20)


# Set up the board
board = np.zeros((20, 20), dtype=int)


# Set up the rivets
rivets = [(4, 4), (4, 15), (15, 4), (15, 15)]


# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Get the mouse position
            x, y = event.pos


            # Convert the mouse position to grid coordinates
            grid_x = x // SQUARE_SIZE
            grid_y = y // SQUARE_SIZE


            # Check if the grid position is valid
            if 0 <= grid_x < 20 and 0 <= grid_y < 20:
                # Change the color of the square
                if (grid_x, grid_y) in rivets:
                    board[grid_y][grid_x] = 1  # 1 represents a clicked rivet
                else:
                    board[grid_y][grid_x] = 1


                # Check for and "drop" disconnected sections
                for x, y in np.ndindex(board.shape):
                    if board[x, y] == 0 and not is_connected_to_rivet(board, rivets, (x, y)):
                        break_section(board, (x, y))


    # Draw the board
    screen.fill((255, 255, 255))
    for i in range(20):
        for j in range(20):
            if board[i][j] == 1:
                color = (128, 128, 128)
            elif (i, j) in rivets:
                color = (255, 0, 0)  # Red for rivets
            else:
                color = (255, 255, 255)
            pygame.draw.rect(screen, color, (j * SQUARE_SIZE, i * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))


    # Update the display
    pygame.display.flip()




# Quit Pygame
pygame.quit()
sys.exit()
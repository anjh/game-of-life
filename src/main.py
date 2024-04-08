import pygame
import numpy as np
import random

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
CELL_SIZE = 10
ROWS, COLS = HEIGHT // CELL_SIZE, WIDTH // CELL_SIZE

# Constants for the center region
CENTER_REGION_SIZE = 20  # Adjust this to change the size of the center region


# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Game of Life')

# Grid
grid = np.zeros((ROWS, COLS), dtype=int)

# Function to draw the grid
def draw_grid():
    for row in range(ROWS):
        for col in range(COLS):
            color = WHITE if grid[row][col] == 1 else BLACK
            pygame.draw.rect(screen, color, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))

# Function to update the grid
def update_grid():
    global grid
    new_grid = grid.copy()
    for row in range(ROWS):
        for col in range(COLS):
            alive_neighbors = np.sum(grid[row-1:row+2, col-1:col+2]) - grid[row][col]
            if grid[row][col] == 1 and (alive_neighbors < 2 or alive_neighbors > 3):
                new_grid[row][col] = 0
            elif grid[row][col] == 0 and alive_neighbors == 3:
                new_grid[row][col] = 1
    grid = new_grid

# Function to randomly populate the grid
def random_populate_center():
    center_row = ROWS // 2
    center_col = COLS // 2
    start_row = max(0, center_row - CENTER_REGION_SIZE // 2)
    end_row = min(ROWS, center_row + CENTER_REGION_SIZE // 2)
    start_col = max(0, center_col - CENTER_REGION_SIZE // 2)
    end_col = min(COLS, center_col + CENTER_REGION_SIZE // 2)

    for row in range(start_row, end_row):
        for col in range(start_col, end_col):
            grid[row][col] = random.randint(0, 1)

# Main loop
running = True
random_populate_center()  # Populate the grid randomly
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)
    draw_grid()
    update_grid()
    pygame.display.update()
    pygame.time.delay(100)

pygame.quit()
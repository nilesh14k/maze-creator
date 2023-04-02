import pygame
import random

# Initialize Pygame
pygame.init()

# Set the dimensions of the screen
WIDTH = 600
HEIGHT = 600

# Set the dimensions of the maze
ROWS = 30
COLUMNS = 30

# Set the size of each cell
CELL_SIZE = 20

# Set the margin between cells
MARGIN = 1

# Set the colors of the maze
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set the title of the screen
pygame.display.set_caption("Maze")

# Create the grid of cells
grid = [[1] * COLUMNS for _ in range(ROWS)]

# Create a stack to keep track of the cells visited during the generation process
stack = []

# Create the starting cell
start_row = random.randint(0, ROWS - 1)
start_column = random.randint(0, COLUMNS - 1)
grid[start_row][start_column] = 0
stack.append((start_row, start_column))

# Generate the maze using the depth-first search algorithm
while stack:
    current_row, current_column = stack.pop()
    neighbors = [(current_row - 1, current_column), (current_row, current_column + 1), (current_row + 1, current_column), (current_row, current_column - 1)]
    random.shuffle(neighbors)
    for neighbor_row, neighbor_column in neighbors:
        if 0 <= neighbor_row < ROWS and 0 <= neighbor_column < COLUMNS and grid[neighbor_row][neighbor_column] == 1:
            grid[neighbor_row][neighbor_column] = 0
            stack.append((neighbor_row, neighbor_column))
            pygame.draw.rect(screen, WHITE, [(MARGIN + CELL_SIZE) * neighbor_column + MARGIN, (MARGIN + CELL_SIZE) * neighbor_row + MARGIN, CELL_SIZE, CELL_SIZE])

# Draw the maze
def draw_maze():
    for row in range(ROWS):
        for column in range(COLUMNS):
            if grid[row][column] == 1:
                pygame.draw.rect(screen, BLACK, [(MARGIN + CELL_SIZE) * column + MARGIN, (MARGIN + CELL_SIZE) * row + MARGIN, CELL_SIZE, CELL_SIZE])

# Solve the maze using the depth-first search algorithm
def solve_maze(row, column):
    if row < 0 or column < 0 or row >= ROWS or column >= COLUMNS or grid[row][column] == 0:
        return False
    if row == ROWS - 1 and column == COLUMNS - 1:
        return True
    pygame.draw.rect(screen, GREEN, [(MARGIN + CELL_SIZE) * column + MARGIN, (MARGIN + CELL_SIZE) * row + MARGIN, CELL_SIZE, CELL_SIZE])
    grid[row][column] = 0
    if solve_maze(row-1, column) or solve_maze(row, column+1) or solve_maze(row+1, column) or solve_maze(row, column-1):
        return True
    pygame.draw.rect(screen, WHITE, [(MARGIN + CELL_SIZE) * column + MARGIN, (MARGIN + CELL_SIZE) * row + MARGIN, CELL_SIZE, CELL_SIZE])
    return False

# Solve the maze
solve_maze(0, 0)

# Loop until the user clicks the
# Loop until the user clicks the close button
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the maze
    draw_maze()

    # Update the screen
    pygame.display.update()

# Quit Pygame
pygame.quit()

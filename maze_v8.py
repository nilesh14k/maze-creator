import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set the dimensions of the grid
WIDTH = 800
HEIGHT = 600
MARGIN = 5
CELL_SIZE = 20
ROWS = int((HEIGHT - MARGIN * 2) / CELL_SIZE)
COLUMNS = int((WIDTH - MARGIN * 2) / CELL_SIZE)

# Initialize Pygame
pygame.init()

# Set the size of the screen
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)

# Set the caption of the window
pygame.display.set_caption("Maze")

# Create the grid
grid = []
for row in range(ROWS):
    grid.append([])
    for column in range(COLUMNS):
        grid[row].append(0)


# Define a function to generate the maze using a recursive backtracking algorithm
def generate_maze(row, column):
    grid[row][column] = 1
    neighbors = [(row - 1, column), (row, column + 1), (row + 1, column), (row, column - 1)]
    random.shuffle(neighbors)
    for neighbor in neighbors:
        r, c = neighbor
        if r < 0 or c < 0 or r >= ROWS or c >= COLUMNS or grid[r][c] == 1:
            continue
        if r == row:
            grid[r][max(column, c)] = 1
        if c == column:
            grid[max(row, r)][c] = 1
        generate_maze(r, c)


# Generate the maze
generate_maze(0, 0)


# Define a function to draw the maze
def draw_maze():
    for row in range(ROWS):
        for column in range(COLUMNS):
            if grid[row][column] == 1:
                color = WHITE
            else:
                color = BLACK
            pygame.draw.rect(screen, color,
                             [(MARGIN + CELL_SIZE) * column + MARGIN, (MARGIN + CELL_SIZE) * row + MARGIN, CELL_SIZE,
                              CELL_SIZE])


# Main loop
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Fill the screen with black color
    screen.fill(BLACK)

    # Draw the maze
    draw_maze()

    # Update the screen
    pygame.display.flip()

# Quit Pygame
pygame.quit()

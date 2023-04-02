import random
import turtle

# set up the turtle window
wn = turtle.Screen()
wn.setup(400, 400)
wn.title("Maze")

# create the turtle
t = turtle.Turtle()
t.speed(0)
t.penup()


# set up the UI
def set_difficulty(difficulty):
    # clear the screen
    t.clear()

    # set the maze size and density based on the difficulty level
    if difficulty == 1:
        size = 10
        density = 0.1
    elif difficulty == 2:
        size = 20
        density = 0.2
    else:
        size = 30
        density = 0.3

    # generate and draw the maze
    cell_size = 20
    maze = generate_maze(size, density)
    draw_maze(maze, cell_size)


def draw_form():
    # draw the form
    t.goto(-100, 50)
    t.write("Select difficulty level:", font=("Arial", 14, "bold"))
    t.goto(-100, 0)
    easy_btn = turtle.Turtle()
    easy_btn.speed(0)
    easy_btn.penup()
    easy_btn.goto(-50, -20)
    easy_btn.write("Easy", font=("Arial", 12, "bold"))
    easy_btn.onclick(lambda x, y: set_difficulty(1))
    medium_btn = turtle.Turtle()
    medium_btn.speed(0)
    medium_btn.penup()
    medium_btn.goto(0, -20)
    medium_btn.write("Medium", font=("Arial", 12, "bold"))
    medium_btn.onclick(lambda x, y: set_difficulty(2))
    hard_btn = turtle.Turtle()
    hard_btn.speed(0)
    hard_btn.penup()
    hard_btn.goto(50, -20)
    hard_btn.write("Hard", font=("Arial", 12, "bold"))
    hard_btn.onclick(lambda x, y: set_difficulty(3))


# set up the maze generator
def generate_maze(size, density):
    maze = []
    for i in range(size):
        maze.append([1] * size)

    def carve(x, y):
        maze[y][x] = 0

        directions = [(x, y - 2), (x, y + 2), (x + 2, y), (x - 2, y)]
        random.shuffle(directions)

        for new_x, new_y in directions:
            if new_x < 0 or new_x >= size or new_y < 0 or new_y >= size:
                continue
            if maze[new_y][new_x] == 1:
                maze[(y + new_y) // 2][(x + new_x) // 2] = 0
                carve(new_x, new_y)

    carve(0, 0)

    # Add additional walls to increase density
    for y in range(size):
        for x in range(size):
            if maze[y][x] == 0:
                if random.random() < density:
                    maze[y][x] = 1

    return maze


def draw_maze(maze, cell_size):
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            if maze[y][x] == 1:
                screen_x = -200 + (x * cell_size)
                screen_y = 200 - (y * cell_size)
                t.goto(screen_x, screen_y)
                t.setheading(0)
                t.pendown()
                t.goto(screen_x + cell_size, screen_y)
                t.penup()
            else:
                screen_x = -200 + (x * cell_size)
                screen_y = 200 - (y * cell_size)
                t.goto(screen_x, screen_y)
                t.pendown()
                t.goto(screen_x + cell_size, screen_y)
                t.goto(screen_x + cell_size, screen_y - cell_size)
                t.goto(screen_x, screen_y - cell_size)
                t.goto(screen_x, screen_y)
                t.penup()

# draw the form
draw_form()

# start the turtle event loop
turtle.done()

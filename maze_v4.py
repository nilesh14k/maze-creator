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
                t.pendown()
                t.setheading(0)
                for i in range(4):
                    t.forward(cell_size)
                    t.left(90)
                t.penup()


# set the maze difficulty
difficulty = 2  # 1=easy, 2=medium, 3=hard

# set the maze size based on difficulty
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

# hide the turtle
t.hideturtle()

# start the main event loop
turtle.done()

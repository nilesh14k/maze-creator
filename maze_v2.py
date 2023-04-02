import random

# set up the maze
maze = []
size = 20
for i in range(size):
    maze.append([0] * size)

# recursive backtracking algorithm
def generate_maze(x, y):
    directions = ["N", "S", "E", "W"]
    random.shuffle(directions)
    for direction in directions:
        if direction == "N" and y > 1 and maze[y-2][x] == 0:
            maze[y-1][x] = 1
            maze[y-2][x] = 1
            generate_maze(x, y-2)
        elif direction == "S" and y < size-2 and maze[y+2][x] == 0:
            maze[y+1][x] = 1
            maze[y+2][x] = 1
            generate_maze(x, y+2)
        elif direction == "E" and x < size-2 and maze[y][x+2] == 0:
            maze[y][x+1] = 1
            maze[y][x+2] = 1
            generate_maze(x+2, y)
        elif direction == "W" and x > 1 and maze[y][x-2] == 0:
            maze[y][x-1] = 1
            maze[y][x-2] = 1
            generate_maze(x-2, y)

# generate the maze starting from the top-left corner
generate_maze(1, 1)

# draw the maze using turtle
import turtle

# set up the turtle window
wn = turtle.Screen()
wn.setup(400, 400)
wn.title("Maze")

# create the turtle
t = turtle.Turtle()
t.speed(0)
t.penup()

# draw the maze
for y in range(size):
    for x in range(size):
        if maze[y][x] == 1:
            screen_x = -200 + (x * 20)
            screen_y = 200 - (y * 20)
            t.goto(screen_x, screen_y)
            t.stamp()

# hide the turtle
t.hideturtle()

# start the main event loop
turtle.done()

import random
import turtle
import tkinter as tk
from queue import Queue

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


def solve_maze(maze):
    # initialize variables
    start = (0, 0)
    end = (len(maze) - 1, len(maze) - 1)
    visited = set()
    q = Queue()
    q.put((start, []))

    # perform BFS search
    while not q.empty():
        curr, path = q.get()

        if curr == end:
            return path + [curr]

        if curr in visited:
            continue

        visited.add(curr)

        x, y = curr

        if x > 0 and maze[y][x - 1] == 0:
            q.put(((x - 1, y), path + [curr]))

        if x < len(maze[y]) - 1 and maze[y][x + 1] == 0:
            q.put(((x + 1, y), path + [curr]))

        if y > 0 and maze[y - 1][x] == 0:
            q.put(((x, y - 1), path + [curr]))

        if y < len(maze) - 1 and maze[y + 1][x] == 0:
            q.put(((x, y + 1), path + [curr]))

    return None


# def generate_button_click():
#     # get the selected difficulty level
#     difficulty = difficulty_var.get()
#
#     # set the maze size and density based on the difficulty level
#     if difficulty == "Easy":
#         size = 10
#         density = 0.2
#     elif difficulty == "Medium":
#         size = 20
#         density = 0.4
#     elif difficulty == "Hard":
#         size = 30
#         density = 0.6
#
#     # generate the maze
#     maze = generate_maze(size, density)
#
#     # draw the maze
#     cell_size = 400 // size
#     t.penup()
#     t.goto(-200, 200)
#     draw_maze(maze, cell_size)
#
#     # solve the maze
#     path = solve_maze(maze)
#     if path is not None:
#         t.pencolor("red")
#         t.goto(-200 + (path[0][0] * cell_size) + (cell_size // 2),
#                200 - (path[0][1] * cell_size) - (cell_size // 2))
#         t.pendown()
#         for i in range(1, len(path)):
#             x, y = path[i]
#             t.goto(-200 + (x * cell_size) + (cell_size // 2),
#                    200 - (y * cell_size) - (cell_size // 2))
#         t.penup()
#
#     # hide the turtle
#     t.hideturtle()
#
#
# # create the tkinter window for the difficulty selection
# root = tk.Tk()
# root.title("Maze Difficulty")
#
# # create the difficulty selection variable and set the default value
# difficulty_var = tk.StringVar()
# difficulty_var.set("Easy")
#
# # create the difficulty selection options
# difficulty_options = ["Easy", "Medium", "Hard"]
#
# # create the difficulty selection menu
# difficulty_menu = tk.OptionMenu(root, difficulty_var, *difficulty_options)
# difficulty_menu.pack()
#
# # create the generate button
# generate_button = tk.Button(root, text="Generate Maze", command=generate_button_click)
# generate_button.pack()
#
# # start the tkinter mainloop
# root.mainloop()

def generate_button_click():
    # get the selected difficulty level
    difficulty = difficulty_var.get()

    # set the maze size and density based on the difficulty level
    if difficulty == "Easy":
        size = 10
        density = 0.2
    elif difficulty == "Medium":
        size = 20
        density = 0.4
    elif difficulty == "Hard":
        size = 30
        density = 0.6

    # generate the maze
    maze = generate_maze(size, density)

    # draw the maze
    cell_size = 400 // size
    t.penup()
    t.goto(-200, 200)
    t.pendown()
    t.forward(size * cell_size)
    t.right(90)
    t.forward(size * cell_size)
    t.right(90)
    t.forward(size * cell_size)
    t.right(90)
    t.forward(size * cell_size)
    t.right(90)
    draw_maze(maze, cell_size)

    # solve the maze
    path = solve_maze(maze)
    if path is not None:
        t.pencolor("red")
        t.goto(-200 + (path[0][0] * cell_size) + (cell_size // 2),
               200 - (path[0][1] * cell_size) - (cell_size // 2))
        t.pendown()
        for i in range(1, len(path)):
            x, y = path[i]
            t.goto(-200 + (x * cell_size) + (cell_size // 2),
                   200 - (y * cell_size) - (cell_size // 2))
        t.penup()

    # hide the turtle
    t.hideturtle()


# create the tkinter window for the difficulty selection
root = tk.Tk()
root.title("Maze Difficulty")

# create the difficulty selection variable and set the default value
difficulty_var = tk.StringVar()
difficulty_var.set("Easy")

# create the difficulty selection options
difficulty_options = ["Easy", "Medium", "Hard"]

# create the difficulty selection menu
difficulty_menu = tk.OptionMenu(root, difficulty_var, *difficulty_options)
difficulty_menu.pack()

# create the generate button
generate_button = tk.Button(root, text="Generate Maze", command=generate_button_click)
generate_button.pack()

# start the tkinter mainloop
root.mainloop()

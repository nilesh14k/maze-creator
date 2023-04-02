import random
import turtle
import tkinter as tk

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


def generate_button_click():
    # get the selected difficulty level
    difficulty = difficulty_var.get()

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

    # hide the turtle
    t.hideturtle()


# create the GUI window
root = tk.Tk()
root.title("Maze Difficulty")

# create the difficulty selection options
difficulty_var = tk.IntVar()
easy_rb = tk.Radiobutton(root, text="Easy", variable=difficulty_var, value=1)
medium_rb = tk.Radiobutton(root, text="Medium", variable=difficulty_var, value=2)
hard_rb = tk.Radiobutton(root, text="Hard", variable=difficulty_var, value=3)

# create the submit button
generate_button = tk.Button(root, text="Generate Maze", command=generate_button_click)

# layout the widgets in the window
easy_rb.pack()
medium_rb.pack()
hard_rb.pack()
generate_button.pack()

# start the main event loop
root.mainloop()

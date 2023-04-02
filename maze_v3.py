import turtle

# set up the turtle window
wn = turtle.Screen()
wn.setup(400, 400)
wn.title("Maze")

# create the turtle
t = turtle.Turtle()
t.speed(0)
t.penup()

# define the maze layout
maze = [
    "XXXXXXXXXXXXXXXXXXXX",
    "X                   X",
    "X XXXXXXX   XXXXXXX X",
    "X X         X       X",
    "X X   XXXXXXX   XXX X",
    "X X   X           X X",
    "X XXXXXXX   XXXXXXX X",
    "X         X         X",
    "XXXXXXX   XXXXXXXXX X",
    "X         X         X",
    "X   XXXXXXX   XXX   X",
    "X   X               X",
    "XXXXX   XXXXXXXXX   X",
    "X                   X",
    "XXXXXXXXXXXXXXXXXXXX",
]

# draw the maze
cell_size = 20
for y in range(len(maze)):
    for x in range(len(maze[y])):
        char = maze[y][x]
        screen_x = -200 + (x * cell_size)
        screen_y = 200 - (y * cell_size)

        if char == "X":
            t.goto(screen_x, screen_y)
            t.pendown()
            t.setheading(0)
            for i in range(4):
                t.forward(cell_size)
                t.left(90)
            t.penup()
        else:
            pass

# hide the turtle
t.hideturtle()

# start the main event loop
turtle.done()

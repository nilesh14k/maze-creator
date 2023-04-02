import turtle

# Define the maze as a 2D list of 0's and 1's, where 0 is a wall and 1 is a path
maze = [
    [1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1],
    [1, 1, 1, 0, 1],
    [0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1],
    [1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1],
    [1, 1, 1, 0, 1],
    [0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1]
]

# Set up the Turtle window and pen
wn = turtle.Screen()
wn.bgcolor("white")
wn.title("Maze Solver")
pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.goto(-200, 200)
pen.pendown()

# Define a function to draw the maze
def draw_maze():
    for row in maze:
        for cell in row:
            if cell == 0:
                pen.begin_fill()
                for i in range(4):
                    pen.forward(40)
                    pen.right(90)
                pen.end_fill()
            pen.forward(40)
        pen.backward(40 * len(row))
        pen.right(90)
        pen.forward(40)
        pen.left(90)

# Define a function to solve the maze
def solve_maze(x, y):
    if maze[x][y] == 0:
        return False
    if x == len(maze) - 1 and y == len(maze[0]) - 1:
        return True
    maze[x][y] = 0
    pen.fillcolor("green")
    pen.begin_fill()
    pen.circle(15)
    pen.end_fill()
    if x > 0 and solve_maze(x - 1, y):
        pen.fillcolor("red")
        pen.begin_fill()
        pen.circle(15)
        pen.end_fill()
        return True
    if x < len(maze) - 1 and solve_maze(x + 1, y):
        pen.fillcolor("red")
        pen.begin_fill()
        pen.circle(15)
        pen.end_fill()
        return True
    if y > 0 and solve_maze(x, y - 1):
        pen.fillcolor("red")
        pen.begin_fill()
        pen.circle(15)
        pen.end_fill()
        return True
    if y < len(maze[0]) - 1 and solve_maze(x, y + 1):
        pen.fillcolor("red")
        pen.begin_fill()
        pen.circle(15)
        pen.end_fill()
        return True
    return False

# Draw the maze
draw_maze()

# Solve the maze starting at the top-left corner
solve_maze(0, 0)

# Wait for the user to close the window
wn.mainloop()
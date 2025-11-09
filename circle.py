import math
import turtle

def drawCircle(t, x, y, radius):
    """Draws a circle centered at (x, y) with the given radius using turtle t."""

    t.penup()
    t.setposition(x + radius, y)
    t.setheading(90)   
    t.pendown()


    step_length = 2.0 * math.pi * radius / 120.0

    for _ in range(120):
        t.left(3)
        t.forward(step_length)

def main():
    """Creates a Turtle object and calls drawCircle for testing."""
    screen = turtle.Screen()
    screen.title("Draw Circle Example")

    t = turtle.Turtle()
    t.width(2)
    t.color("blue")

    drawCircle(t, 0, 0, 100)

    print("Drawing complete. Close the turtle window to exit.")
    screen.mainloop()

if __name__ == "__main__":
    main()

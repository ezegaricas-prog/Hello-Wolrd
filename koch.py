import turtle

def drawFractalLine(t, distance, angle, level):
    if level == 0:
        t.setheading(angle)
        t.forward(distance)
    else:
        third = distance / 3.0
        drawFractalLine(t, third, angle, level - 1)
        drawFractalLine(t, third, angle + 60, level - 1)
        drawFractalLine(t, third, angle - 60, level - 1)
        drawFractalLine(t, third, angle, level - 1)

def main():
    screen = turtle.Screen()
    t = turtle.Turtle()
    t.speed(0)
    size = 200
    level = 2
    t.penup()
    t.setposition(-size/2, size/3)
    t.pendown()
    for ang in (0, -120, 120):
        drawFractalLine(t, size, ang, level)
    turtle.done()

if __name__ == "__main__":
    main()

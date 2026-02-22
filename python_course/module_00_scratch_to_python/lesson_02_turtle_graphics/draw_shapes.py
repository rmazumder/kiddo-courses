"""
===================================================
  Lesson 2: Draw Shapes with Turtle!
  Module 0 - From Scratch to Python!
===================================================

This program draws 5 different shapes:
  - Square
  - Triangle
  - Circle
  - Star
  - Pentagon

Each shape is drawn in a different colour using
its own function. The maths behind each shape is
explained in the comments.

Run it and watch the shapes appear!
"""

import turtle


# --------------------------------------------------
# SETUP
# --------------------------------------------------
screen = turtle.Screen()
screen.title("Shape Gallery!")
screen.bgcolor("black")          # Dark background makes colours pop!
screen.setup(width=700, height=600)

t = turtle.Turtle()
t.speed(6)
t.pensize(2)


# ==================================================
# SHAPE FUNCTIONS
# Each function draws one shape at the given position
# ==================================================


def draw_square(size: int, x: int, y: int, colour: str) -> None:
    """
    Draws a filled square.

    How it works:
    A square has 4 equal sides and 4 corners of 90 degrees.
    We repeat: move forward, turn right 90 degrees - four times!

    Args:
        size: The length of each side in pixels.
        x: Horizontal position on screen.
        y: Vertical position on screen.
        colour: Fill colour name.
    """
    t.penup()
    t.goto(x, y)          # Jump to position without drawing
    t.pendown()
    t.color(colour)
    t.begin_fill()

    # In Scratch: "repeat 4 { move [size] steps, turn right 90 }"
    for _ in range(4):    # Repeat 4 times (once per side)
        t.forward(size)   # Move forward by 'size' pixels
        t.right(90)       # Turn right 90 degrees (square corner!)

    t.end_fill()

    # Label the shape
    t.penup()
    t.goto(x + size / 4, y - 20)
    t.color("white")
    t.write("Square", font=("Arial", 10, "normal"))


def draw_triangle(size: int, x: int, y: int, colour: str) -> None:
    """
    Draws a filled equilateral triangle.

    How it works:
    An equilateral triangle has 3 equal sides and 3 corners of 60 degrees.
    But when TURNING, we turn the EXTERIOR angle = 180 - 60 = 120 degrees.

    Args:
        size: The length of each side in pixels.
        x: Horizontal position on screen.
        y: Vertical position on screen.
        colour: Fill colour name.
    """
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.setheading(0)       # Face right before drawing
    t.color(colour)
    t.begin_fill()

    # In Scratch: "repeat 3 { move [size] steps, turn right 120 }"
    for _ in range(3):    # 3 sides = 3 repeats
        t.forward(size)
        t.right(120)      # Exterior angle of equilateral triangle = 120

    t.end_fill()

    t.penup()
    t.goto(x + size / 4, y - 20)
    t.color("white")
    t.write("Triangle", font=("Arial", 10, "normal"))


def draw_circle(radius: int, x: int, y: int, colour: str) -> None:
    """
    Draws a filled circle.

    How it works:
    turtle.circle(radius) does all the work!
    The radius is the distance from the centre to the edge.

    Args:
        radius: The radius of the circle in pixels.
        x: Horizontal position on screen (left edge of circle).
        y: Vertical position on screen (bottom of circle).
        colour: Fill colour name.
    """
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(colour)
    t.begin_fill()

    t.circle(radius)      # Draw a full circle with this radius

    t.end_fill()

    t.penup()
    t.goto(x - radius / 2, y - 20)
    t.color("white")
    t.write("Circle", font=("Arial", 10, "normal"))


def draw_star(size: int, x: int, y: int, colour: str) -> None:
    """
    Draws a 5-pointed star.

    How it works:
    A star is drawn by moving forward and turning 144 degrees, 5 times.
    Why 144? Because 360 / 5 * 2 = 144. We skip one point each turn!

    Args:
        size: The length of each point in pixels.
        x: Horizontal position on screen.
        y: Vertical position on screen.
        colour: Fill colour name.
    """
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.setheading(90)      # Face up so the star points upward
    t.color(colour)
    t.begin_fill()

    # In Scratch: "repeat 5 { move [size] steps, turn right 144 }"
    for _ in range(5):    # 5 points = 5 repeats
        t.forward(size)
        t.right(144)      # The magic star angle!

    t.end_fill()

    t.penup()
    t.goto(x - size / 4, y - 20)
    t.color("white")
    t.write("Star", font=("Arial", 10, "normal"))


def draw_pentagon(size: int, x: int, y: int, colour: str) -> None:
    """
    Draws a filled pentagon (5 sides).

    How it works:
    A pentagon has 5 sides. The exterior angle = 360 / 5 = 72 degrees.

    Args:
        size: The length of each side in pixels.
        x: Horizontal position on screen.
        y: Vertical position on screen.
        colour: Fill colour name.
    """
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.setheading(0)
    t.color(colour)
    t.begin_fill()

    # In Scratch: "repeat 5 { move [size] steps, turn right 72 }"
    for _ in range(5):    # 5 sides = 5 repeats
        t.forward(size)
        t.right(72)       # Exterior angle: 360 / 5 = 72 degrees

    t.end_fill()

    t.penup()
    t.goto(x, y - 20)
    t.color("white")
    t.write("Pentagon", font=("Arial", 10, "normal"))


# ==================================================
# DRAW A TITLE ON SCREEN
# ==================================================
def draw_title() -> None:
    """Writes the gallery title at the top of the screen."""
    t.penup()
    t.goto(-160, 230)
    t.pendown()
    t.color("white")
    t.write("Shape Gallery!", font=("Arial", 22, "bold"))
    t.penup()


# ==================================================
# MAIN: Draw all 5 shapes in their positions
# ==================================================
def main() -> None:
    """Draws all shapes in an organised layout."""
    print("Drawing the Shape Gallery...")

    draw_title()

    # Top row: square (left), triangle (middle), circle (right)
    # Each shape is positioned so they don't overlap
    draw_square(size=120, x=-280, y=60, colour="dodgerblue")
    draw_triangle(size=130, x=-70, y=60, colour="limegreen")
    draw_circle(radius=65, x=160, y=60, colour="orange")

    # Bottom row: star (left), pentagon (right) - centred
    draw_star(size=80, x=-150, y=-160, colour="gold")
    draw_pentagon(size=90, x=60, y=-160, colour="hotpink")

    print("Shape Gallery complete!")
    print("Can you figure out the maths behind each shape?")

    turtle.done()


if __name__ == "__main__":
    main()

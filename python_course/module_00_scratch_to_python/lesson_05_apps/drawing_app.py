"""
===================================================
  Lesson 5: Drawing App!
  Module 0 - From Scratch to Python!
===================================================

A mini paint application using turtle!

CONTROLS:
  Mouse click     - Draw a dot
  Mouse drag      - Draw a line
  R key           - Switch to Red
  G key           - Switch to Green
  B key           - Switch to Blue
  P key           - Switch to Purple
  O key           - Switch to Orange
  C key           - Clear the canvas
  + key           - Bigger brush
  - key           - Smaller brush

This is like Scratch's pen blocks, but YOU control it!
"""

import turtle


# ==================================================
# SETUP
# ==================================================
screen = turtle.Screen()
screen.title("Drawing App - Click and Drag to Draw!")
screen.bgcolor("white")
screen.setup(width=800, height=650)
screen.tracer(1)          # Normal mode (drawing happens in real-time with drag)


# ==================================================
# DRAWING TURTLE
# This turtle does the actual drawing
# ==================================================
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pensize(5)
pen.color("black")
pen.penup()


# ==================================================
# HUD TURTLE
# This turtle draws the toolbar at the top
# ==================================================
hud = turtle.Turtle()
hud.hideturtle()
hud.speed(0)
hud.penup()


# ==================================================
# APP STATE
# In Scratch: your project's variables
# ==================================================
current_colour: str = "black"
brush_size: int = 5
MIN_BRUSH: int = 1
MAX_BRUSH: int = 30


# ==================================================
# DRAW THE TOOLBAR
# ==================================================

def draw_toolbar() -> None:
    """Draws the colour palette and info bar at the top."""
    hud.clear()

    # Toolbar background
    hud.goto(-400, 280)
    hud.color("#f0f0f0")
    hud.begin_fill()
    hud.fillcolor("#f0f0f0")
    hud.pendown()
    for _ in range(2):
        hud.forward(800)
        hud.left(90)
        hud.forward(50)
        hud.left(90)
    hud.end_fill()
    hud.penup()

    # Colour swatches
    swatch_colours = [
        ("black",  -350),
        ("red",    -290),
        ("green",  -230),
        ("blue",   -170),
        ("purple", -110),
        ("orange",  -50),
    ]

    for colour, x in swatch_colours:
        hud.goto(x, 290)
        hud.color(colour)
        hud.dot(28)

        # Highlight the active colour
        if colour == current_colour:
            hud.goto(x, 290)
            hud.color("gold")
            # Draw a ring around the active colour
            hud.pendown()
            hud.pensize(3)
            hud.circle(16)
            hud.penup()
            hud.pensize(1)

    # Brush size indicator
    hud.goto(50, 295)
    hud.color("black")
    hud.dot(brush_size)

    # Instructions text
    hud.goto(80, 285)
    hud.color("#333333")
    hud.write(
        f"Brush: {brush_size}px  |  Keys: R G B P O = colours  |  +/- = size  |  C = clear",
        font=("Arial", 11, "normal"),
    )

    # Current colour label
    hud.goto(-400, 265)
    hud.color(current_colour if current_colour != "white" else "black")
    hud.write(
        f"Drawing with: {current_colour.upper()}",
        font=("Arial", 12, "bold"),
    )


# ==================================================
# MOUSE EVENTS
# In Scratch: "when this sprite clicked"
# ==================================================

def on_click(x: float, y: float) -> None:
    """Called when user clicks on the canvas."""
    # Don't draw on the toolbar area
    if y > 260:
        return

    pen.color(current_colour)
    pen.pensize(brush_size)
    pen.goto(x, y)
    pen.dot(brush_size)       # Draw a dot at click position
    draw_toolbar()            # Refresh toolbar


def on_drag(x: float, y: float) -> None:
    """Called when user clicks and drags."""
    # Don't draw on the toolbar area
    if y > 260:
        return

    pen.color(current_colour)
    pen.pensize(brush_size)
    pen.pendown()
    pen.goto(x, y)            # Draw a line to where the mouse is
    draw_toolbar()


def on_release(x: float, y: float) -> None:
    """Called when user releases the mouse button."""
    pen.penup()               # Lift pen when mouse released


# ==================================================
# KEY PRESS EVENTS
# In Scratch: "when [key] pressed" blocks
# ==================================================

def set_red() -> None:
    """Switch to red colour."""
    global current_colour
    current_colour = "red"
    pen.color("red")
    draw_toolbar()


def set_green() -> None:
    """Switch to green colour."""
    global current_colour
    current_colour = "green"
    pen.color("green")
    draw_toolbar()


def set_blue() -> None:
    """Switch to blue colour."""
    global current_colour
    current_colour = "blue"
    pen.color("blue")
    draw_toolbar()


def set_purple() -> None:
    """Switch to purple colour."""
    global current_colour
    current_colour = "purple"
    pen.color("purple")
    draw_toolbar()


def set_orange() -> None:
    """Switch to orange colour."""
    global current_colour
    current_colour = "orange"
    pen.color("orange")
    draw_toolbar()


def set_black() -> None:
    """Switch to black (default) colour."""
    global current_colour
    current_colour = "black"
    pen.color("black")
    draw_toolbar()


def increase_brush() -> None:
    """Make the brush bigger."""
    global brush_size
    if brush_size < MAX_BRUSH:
        brush_size += 2
        pen.pensize(brush_size)
    draw_toolbar()


def decrease_brush() -> None:
    """Make the brush smaller."""
    global brush_size
    if brush_size > MIN_BRUSH:
        brush_size -= 2
        pen.pensize(brush_size)
    draw_toolbar()


def clear_canvas() -> None:
    """Erase all drawings."""
    pen.clear()
    draw_toolbar()


# ==================================================
# MAIN: Register all events and start the app
# ==================================================

def main() -> None:
    """Sets up the drawing app and starts it."""
    print("Drawing App started!")
    print()
    print("CONTROLS:")
    print("  Click/drag on screen  - Draw")
    print("  R = Red, G = Green, B = Blue, P = Purple, O = Orange")
    print("  + = Bigger brush, - = Smaller brush")
    print("  C = Clear everything")
    print()
    print("Draw something amazing!")

    # Draw the toolbar first
    draw_toolbar()

    # Register mouse events
    # In Scratch: "when sprite clicked" and "when sprite dragged"
    screen.onclick(on_click)
    pen.ondrag(on_drag)
    screen.onscreenclick(on_click)

    # Register key bindings
    # In Scratch: "when [key] pressed" for each key
    screen.listen()
    screen.onkey(set_red,     "r")
    screen.onkey(set_green,   "g")
    screen.onkey(set_blue,    "b")
    screen.onkey(set_purple,  "p")
    screen.onkey(set_orange,  "o")
    screen.onkey(set_black,   "k")
    screen.onkey(increase_brush, "plus")
    screen.onkey(decrease_brush, "minus")
    screen.onkey(clear_canvas, "c")

    # Start the app (mainloop keeps the window open)
    screen.mainloop()


if __name__ == "__main__":
    main()

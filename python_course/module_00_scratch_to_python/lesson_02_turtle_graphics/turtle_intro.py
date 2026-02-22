"""
===================================================
  Lesson 2: Turtle Intro - Draw a House!
  Module 0 - From Scratch to Python!
===================================================

This program draws a house using turtle graphics.
Every single line has a comment explaining what it
does AND what the Scratch equivalent would be.

Run it and watch the turtle build the house step by step!
"""

import turtle


# --------------------------------------------------
# SETUP: Create the window and the turtle
# In Scratch: this happens automatically when you open a project
# --------------------------------------------------

# Create a drawing window and give it a title
screen = turtle.Screen()
screen.title("My First Drawing!")          # Name the window
screen.bgcolor("lightblue")               # Set background colour
screen.setup(width=600, height=500)       # Set window size

# Create our turtle (we name it "t" to type less)
# In Scratch: this is your sprite
t = turtle.Turtle()
t.speed(3)         # Drawing speed: 1=slow, 6=medium, 10=fast
                   # In Scratch: this is how fast your sprite moves
t.pensize(3)       # Make lines 3 pixels thick
                   # In Scratch: "set pen size to 3"


# --------------------------------------------------
# FUNCTION: Draw the walls (a square)
# In Scratch: this would be a "define [draw walls]" block
# --------------------------------------------------
def draw_walls():
    """Draws the square walls of the house."""
    t.color("brown")      # In Scratch: "set pen color to brown"
    t.begin_fill()        # Start filling shape with colour
                          # In Scratch: no direct equivalent, but like fill tool

    # Draw 4 sides of a square (the walls)
    # In Scratch: "repeat 4 { move 150 steps, turn right 90 degrees }"
    for side in range(4):                # Repeat 4 times
        t.forward(150)                   # Move forward 150 pixels
        t.right(90)                      # Turn right 90 degrees

    t.end_fill()          # Finish filling the shape


# --------------------------------------------------
# FUNCTION: Draw the roof (a triangle)
# In Scratch: this would be a "define [draw roof]" block
# --------------------------------------------------
def draw_roof():
    """Draws the triangular roof on top of the house."""
    # Move to the top-left corner of the walls
    # In Scratch: "go to x: (current_x) y: (current_y + 150)"
    t.penup()             # Lift pen - stop drawing
                          # In Scratch: "pen up"
    t.goto(-75, 75)       # Jump to position (-75, 75) - top left of walls
                          # In Scratch: "go to x:-75 y:75"
    t.pendown()           # Put pen down - start drawing again
                          # In Scratch: "pen down"

    t.color("red")        # In Scratch: "set pen color to red"
    t.begin_fill()

    # Draw 3 sides of a triangle (the roof)
    # A triangle has 3 sides, each turned at 120 degrees
    for side in range(3):                # In Scratch: "repeat 3"
        t.forward(150)                   # Each side is 150 pixels
        t.left(120)                      # Triangle angle is 120 degrees

    t.end_fill()


# --------------------------------------------------
# FUNCTION: Draw the door
# --------------------------------------------------
def draw_door():
    """Draws a door in the centre of the house."""
    # Move to where the door starts
    t.penup()
    t.goto(-20, -75)      # Bottom-left of the door position
    t.pendown()

    t.color("darkblue")
    t.begin_fill()

    # Door is a small rectangle: 40 wide, 60 tall
    t.forward(40)         # Bottom of door
    t.left(90)
    t.forward(60)         # Right side of door
    t.left(90)
    t.forward(40)         # Top of door
    t.left(90)
    t.forward(60)         # Left side of door
    t.left(90)

    t.end_fill()


# --------------------------------------------------
# FUNCTION: Draw two windows
# --------------------------------------------------
def draw_windows():
    """Draws two square windows on the house."""
    # Window positions (left and right of the door)
    window_positions = [(-65, -20), (25, -20)]   # (x, y) for each window

    t.color("lightyellow")

    for position in window_positions:    # In Scratch: "repeat 2"
        t.penup()
        t.goto(position[0], position[1]) # Go to this window's position
        t.pendown()

        t.begin_fill()
        # Draw a square window: 30 x 30 pixels
        for side in range(4):            # In Scratch: "repeat 4"
            t.forward(30)
            t.right(90)
        t.end_fill()


# --------------------------------------------------
# FUNCTION: Add a label
# --------------------------------------------------
def draw_label():
    """Writes a label below the house."""
    t.penup()
    t.goto(-80, -120)     # Move below the house
    t.pendown()

    t.color("darkblue")
    # In Scratch: "say 'My House!'" but drawn on the canvas
    t.write("My House!", font=("Arial", 16, "bold"))


# --------------------------------------------------
# MAIN: Run everything in order
# In Scratch: this is the green flag script
# --------------------------------------------------
def main():
    """Main function - draws the complete house."""
    print("Drawing a house with turtle!")
    print("Watch the turtle work...")

    # Start turtle in the right position (bottom-left of house)
    t.penup()
    t.goto(-75, -75)      # Go to starting corner
    t.pendown()
    t.setheading(0)       # Face right (0 degrees = East)

    # Draw each part of the house
    draw_walls()
    draw_roof()
    draw_door()
    draw_windows()
    draw_label()

    # Move turtle out of the way
    t.penup()
    t.goto(0, -150)
    t.pendown()

    print("House complete! Nice work!")

    # Keep the window open until you close it
    # In Scratch: the project just stays open
    turtle.done()


# In Scratch: "when green flag clicked"
if __name__ == "__main__":
    main()

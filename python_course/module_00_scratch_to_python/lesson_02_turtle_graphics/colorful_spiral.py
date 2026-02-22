"""
===================================================
  Lesson 2: Colourful Spiral!
  Module 0 - From Scratch to Python!
===================================================

Watch this program create a SPECTACULAR rainbow spiral!

How it works:
  - We draw a line, turn slightly, draw a longer line, repeat!
  - Each line gets a tiny bit longer (size grows each loop)
  - The colour changes every step through the rainbow list
  - The result is a beautiful spiral pattern!

Try modifying:
  - TURN_ANGLE (try 91, 89, 121, 89.5)
  - NUMBER_OF_LINES (try 200, 400, 600)
  - Starting SPEED

In Scratch, this would be:
  "repeat 300 {
      set pen color to (rainbow colour)
      move (size) steps
      turn right 91 degrees
      change size by 1
  }"
"""

import turtle


# ==================================================
# SETTINGS - Try changing these!
# ==================================================
TURN_ANGLE = 91          # The secret to the spiral shape! Try 89, 121, 91.5
NUMBER_OF_LINES = 300    # How many lines to draw (more = bigger spiral)
STARTING_SIZE = 5        # How long the first line is
DRAWING_SPEED = 0        # 0 = instant (fastest!), 1 = slow, 10 = fast

# Rainbow colour cycle - each line gets the next colour
RAINBOW_COLOURS = [
    "red",
    "orange",
    "yellow",
    "limegreen",
    "cyan",
    "dodgerblue",
    "blue",
    "blueviolet",
    "violet",
    "hotpink",
]


# ==================================================
# SETUP
# ==================================================
screen = turtle.Screen()
screen.title("Colourful Spiral!")
screen.bgcolor("black")           # Black background makes colours glow!
screen.setup(width=700, height=700)

t = turtle.Turtle()
t.speed(DRAWING_SPEED)            # Set drawing speed
t.pensize(2)
t.hideturtle()                    # Hide the turtle arrow for a cleaner look


# ==================================================
# MAIN: Draw the spiral
# ==================================================
def main() -> None:
    """Draws the rainbow spiral."""
    print("Drawing the rainbow spiral...")
    print(f"  Turn angle: {TURN_ANGLE} degrees")
    print(f"  Lines: {NUMBER_OF_LINES}")
    print(f"  Colour count: {len(RAINBOW_COLOURS)}")

    current_size = STARTING_SIZE

    # In Scratch: "repeat NUMBER_OF_LINES { ... }"
    for line_number in range(NUMBER_OF_LINES):

        # Pick the colour for this line
        # % (modulo) cycles back to 0 when we reach the end of the list
        # In Scratch: "set pen color to (colour from list)"
        colour_index = line_number % len(RAINBOW_COLOURS)
        t.color(RAINBOW_COLOURS[colour_index])

        # Draw one line of the spiral
        # In Scratch: "move (current_size) steps"
        t.forward(current_size)

        # Turn to create the spiral
        # In Scratch: "turn right (TURN_ANGLE) degrees"
        t.right(TURN_ANGLE)

        # Make the next line slightly longer
        # This is what creates the SPIRAL (expanding lines)
        # In Scratch: "change size by 0.5"
        current_size += 0.5

    # Write a message when done
    t.penup()
    t.goto(-140, -310)
    t.pendown()
    t.color("white")
    t.write("Rainbow Spiral Complete!", font=("Arial", 16, "bold"))
    t.penup()

    print("Spiral complete! Looks amazing, right?")
    print()
    print("Now try changing TURN_ANGLE to 89 or 121 and run again!")
    print("Each angle creates a completely different pattern!")

    turtle.done()


if __name__ == "__main__":
    main()

"""
===================================================
  Lesson 5: Build Your Own App! (Exercise File)
  Module 0 - From Scratch to Python!
===================================================

TWO app templates for you to complete:

  OPTION A: Digital Greeting Card
    - Draws colourful decorations with turtle
    - Displays a personalised message
    - The user can type their name to customise it

  OPTION B: Pattern Maker
    - Asks the user to pick a number (3-10)
    - Draws a geometric pattern based on that number
    - Each number creates a completely different shape!

Pick ONE (or do both for extra XP!)
"""

import turtle
import math


# ==================================================
# OPTION A: Digital Greeting Card
# ==================================================
# Build a digital greeting card that:
#   1. Draws a decorative border (stars or flowers)
#   2. Displays a big greeting message in the centre
#   3. Asks the user for their name and includes it
#   4. Maybe draws some extra decorations!
#
# STEPS TO COMPLETE:
#   Step 1: Draw a border of small stars around the edge
#   Step 2: Write a big greeting in the centre
#   Step 3: Use turtle.textinput() to ask for the user's name
#   Step 4: Write the personalised message below the greeting
#   Step 5: Add your own decoration (hearts, flowers, anything!)
#
# HINTS:
#   - turtle.textinput("Title", "Prompt") opens a text input box!
#     name = turtle.textinput("What's your name?", "Type your name:")
#   - To draw stars around the border, use a loop and goto() to
#     position each star around the edges
#   - t.write("Hello!", font=("Arial", 30, "bold"), align="center")
#   - align="center" centres text on the turtle's position
#
# EXTRA IDEAS:
#   - Use multiple colours for the decorations
#   - Add animated blinking (clear and redraw)
#   - Let the user pick a colour for their name

def option_a_greeting_card() -> None:
    """OPTION A: Build a personalised digital greeting card."""
    screen = turtle.Screen()
    screen.title("Digital Greeting Card!")
    screen.bgcolor("white")
    screen.setup(650, 550)
    screen.tracer(0)

    # Decorations turtle
    deco = turtle.Turtle()
    deco.hideturtle()
    deco.penup()
    deco.speed(0)

    # Message turtle
    msg = turtle.Turtle()
    msg.hideturtle()
    msg.penup()
    msg.speed(0)

    # TODO Step 1: Draw a border of small stars or hearts
    # HINT: Use a for loop to place small stars at regular positions
    # around the edges. For example, draw 20 stars spaced evenly.
    # Star positions: x goes from -300 to 300, y stays at 240 (top edge)
    #
    # for i in range(20):
    #     x = -300 + i * 32
    #     deco.goto(x, 240)
    #     deco.color("gold")
    #     deco.dot(12)   # or draw a mini star shape

    # YOUR CODE HERE:

    # TODO Step 2: Write the main greeting in the centre
    # HINT: msg.goto(0, 80), msg.color("purple")
    # msg.write("Happy Birthday!", font=("Arial", 36, "bold"), align="center")

    # YOUR CODE HERE:

    # TODO Step 3: Ask for the user's name
    # HINT: name = turtle.textinput("Your Name", "What is your name?")
    # This opens a popup box where they type their name!

    # YOUR CODE HERE:
    name = "Friend"   # Replace with the textinput result!

    # TODO Step 4: Write a personalised message using the name
    # HINT: msg.goto(0, 20)
    # msg.write(f"For: {name}", font=("Arial", 20, "normal"), align="center")

    # YOUR CODE HERE:

    # TODO Step 5: Add more decorations! (Be creative!)
    # Ideas: draw hearts, flowers, confetti dots, a frame, balloons

    # YOUR CODE HERE:

    # Show the card
    screen.update()
    print(f"Greeting card created for {name}!")
    turtle.done()


# ==================================================
# OPTION B: Pattern Maker
# ==================================================
# Ask the user for a number between 3 and 10.
# Draw a beautiful geometric pattern based on that number.
#
# HOW IT WORKS:
#   - A polygon with N sides has exterior angle = 360 / N
#   - Drawing N overlapping rotated polygons creates a star burst!
#   - Each polygon in the burst is rotated by (360 / N) degrees
#
# STEPS TO COMPLETE:
#   Step 1: Use turtle.numinput() to ask for a number 3-10
#   Step 2: Calculate the exterior angle: angle = 360 / num_sides
#   Step 3: Use a loop to draw num_sides polygons
#   Step 4: After each polygon, rotate by angle degrees
#   Step 5: Use different colours for each polygon
#
# HINTS:
#   - turtle.numinput("Title", "Prompt", default, minval, maxval)
#     num = turtle.numinput("Pattern Maker", "Enter sides (3-10):", 5, 3, 10)
#   - To draw ONE polygon with N sides:
#     for side in range(n):
#         t.forward(size)
#         t.right(360 / n)
#   - To draw the burst:
#     for polygon in range(n):
#         draw_one_polygon(n)
#         t.right(360 / n)   <- rotate before the next polygon
#   - Use RAINBOW_COLOURS list and cycle through them per polygon
#
# EXAMPLE RESULTS:
#   3 sides = triangle burst (like a peace sign)
#   4 sides = square burst (like a pinwheel)
#   5 sides = pentagram burst
#   6 sides = Star of David style
#   8 sides = octagram (very beautiful!)

PATTERN_COLOURS = [
    "#FF6B6B", "#FFD93D", "#6BCB77", "#4D96FF",
    "#C77DFF", "#FF9A00", "#00D4FF", "#FF6B9D",
    "#A8DADC", "#F72585",
]

def option_b_pattern_maker() -> None:
    """OPTION B: Draw geometric patterns based on user's number."""
    screen = turtle.Screen()
    screen.title("Pattern Maker!")
    screen.bgcolor("black")
    screen.setup(650, 600)
    screen.tracer(0)

    # Instructions screen
    intro = turtle.Turtle()
    intro.hideturtle()
    intro.penup()
    intro.speed(0)
    intro.goto(0, 60)
    intro.color("white")
    intro.write("Pattern Maker!", font=("Arial", 28, "bold"), align="center")
    intro.goto(0, 0)
    intro.color("gold")
    intro.write("Choose a number 3-10 to create a pattern", font=("Arial", 14, "normal"), align="center")
    screen.update()

    # TODO Step 1: Ask for a number using numinput
    # HINT:
    # num_sides = turtle.numinput(
    #     "Pattern Maker",
    #     "Enter number of sides (3 to 10):",
    #     default=5,
    #     minval=3,
    #     maxval=10,
    # )
    # if num_sides is None:
    #     num_sides = 5    # Default if user cancels

    # YOUR CODE HERE:
    num_sides = 5   # Replace with numinput result!

    num_sides = int(num_sides)
    intro.clear()

    # Create drawing turtle
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.speed(0)
    t.pensize(2)

    # TODO Step 2: Calculate the rotation angle between polygons
    # HINT: rotation_angle = 360 / num_sides

    # YOUR CODE HERE:
    rotation_angle = 360 / num_sides   # Keep this - it's a freebie!

    # TODO Step 3: Loop num_sides times, drawing one polygon each time
    # After each polygon, rotate the turtle by rotation_angle
    #
    # for i in range(num_sides):
    #     # Set colour (cycle through PATTERN_COLOURS)
    #     colour = PATTERN_COLOURS[i % len(PATTERN_COLOURS)]
    #     t.color(colour)
    #
    #     # TODO: Draw one polygon with num_sides sides, size=150
    #     # for side in range(num_sides):
    #     #     t.forward(150)
    #     #     t.right(360 / num_sides)
    #
    #     # TODO: Rotate turtle for the next polygon
    #     # t.right(rotation_angle)
    #
    #     screen.update()

    # YOUR CODE HERE:

    # Add a title label
    label = turtle.Turtle()
    label.hideturtle()
    label.penup()
    label.goto(0, -280)
    label.color("white")
    label.write(
        f"{num_sides}-sided pattern!",
        font=("Arial", 16, "bold"),
        align="center",
    )

    screen.update()
    print(f"Pattern with {num_sides} sides complete!")
    turtle.done()


# ==================================================
# MAIN: Choose which app to build
# ==================================================

def main() -> None:
    """Run one app. Comment/uncomment to choose."""
    print("App Builder Exercise!")
    print("Complete one of the two options:")
    print()
    print("  option_a_greeting_card()  - Personalised card")
    print("  option_b_pattern_maker()  - Geometric patterns")
    print()

    # Uncomment ONE:
    option_a_greeting_card()
    # option_b_pattern_maker()


if __name__ == "__main__":
    main()

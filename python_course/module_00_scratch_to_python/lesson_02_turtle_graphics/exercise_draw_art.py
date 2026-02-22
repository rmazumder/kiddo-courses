"""
===================================================
  Lesson 2: Draw Your Own Art! (Exercise File)
  Module 0 - From Scratch to Python!
===================================================

YOUR MISSION: Complete all 5 drawing tasks below!

Each task has:
  - What to draw
  - HINTS to help you
  - Starter code to build on

Take your time, experiment, and have fun!
Every artist makes mistakes - just keep going!
"""

import turtle
import math


# --------------------------------------------------
# SETUP - Don't change this part
# --------------------------------------------------
screen = turtle.Screen()
screen.title("My Turtle Art Gallery!")
screen.bgcolor("white")
screen.setup(width=800, height=700)

t = turtle.Turtle()
t.speed(6)
t.pensize(2)


# ==================================================
# TASK 1: Draw the First Letter of Your Name
# ==================================================
# Draw the first letter of YOUR name using turtle lines.
# For example, if your name is "Alex", draw the letter A.
# Use forward(), backward(), left(), right() to make the strokes.
#
# HINTS:
#   - Plan the letter on paper first - where does each line go?
#   - Use penup() to move without drawing (to start a new stroke)
#   - Use pendown() when you want to draw
#   - Make the letter at least 100 pixels tall
#   - Choose a colour you like with t.color("colour_name")
#
# Example colours: "red", "blue", "green", "purple", "orange",
#                  "hotpink", "gold", "teal", "tomato"

def draw_my_letter():
    """Draw the first letter of your name here!"""
    t.penup()
    t.goto(-300, 200)     # Start position (top-left area)
    t.pendown()

    # TODO: Pick a colour!
    t.color("blue")       # Change "blue" to your favourite colour

    # TODO: Draw your letter here!
    # Example for letter "I":
    # t.forward(100)   # vertical line
    # Add more lines for your letter!

    # YOUR CODE HERE:


# ==================================================
# TASK 2: Draw a Smiley Face
# ==================================================
# Draw a smiley face using circles!
# A smiley face has:
#   - A big circle for the head
#   - Two small circles for the eyes
#   - A half circle (arc) for the smile
#
# HINTS:
#   - t.circle(radius) draws a circle
#   - t.circle(radius, 180) draws a half circle (semicircle)
#   - Use t.penup() and t.goto() to move between parts
#   - Fill the head with yellow: t.fillcolor("yellow")

def draw_smiley_face():
    """Draw a smiley face using turtle circles."""
    t.penup()
    t.goto(-50, -200)     # Start at bottom of head position
    t.pendown()

    # TODO: Draw the face outline (big yellow circle)
    # HINT: t.fillcolor("yellow"), t.begin_fill(), t.circle(80), t.end_fill()

    # YOUR CODE HERE:

    # TODO: Draw the left eye (move to the right position, draw small circle)
    # HINT: t.penup(), t.goto(-70, -90), t.pendown(), t.circle(10)

    # YOUR CODE HERE:

    # TODO: Draw the right eye

    # YOUR CODE HERE:

    # TODO: Draw the smile (move to position, draw a half-circle)
    # HINT: t.circle(30, 180) draws a semicircle with radius 30

    # YOUR CODE HERE:


# ==================================================
# TASK 3: Draw a Colourful Flower
# ==================================================
# Draw a flower with petals in a loop!
# Each petal is an oval shape made with two arcs.
#
# HINTS:
#   - Draw one petal: t.circle(40, 90), t.left(90), t.circle(40, 90)
#   - Then rotate the turtle and draw the next petal
#   - Use a for loop: for petal in range(8):
#   - After each petal, turn right: t.right(360 / 8)  = t.right(45)
#   - Use different colours for each petal!

PETAL_COLOURS = ["red", "orange", "yellow", "pink",
                 "purple", "hotpink", "tomato", "gold"]

def draw_flower():
    """Draw a colourful flower with 8 petals."""
    t.penup()
    t.goto(150, 50)       # Centre of the flower
    t.pendown()

    # TODO: Loop 8 times, drawing a petal and rotating each time
    # for petal in range(8):
    #     t.color(PETAL_COLOURS[petal])
    #     t.begin_fill()
    #     # draw one petal (two arcs):
    #     t.circle(40, 90)
    #     t.left(90)
    #     t.circle(40, 90)
    #     t.end_fill()
    #     t.right(45)  # rotate for next petal

    # YOUR CODE HERE:

    # TODO: Draw a yellow centre circle
    # YOUR CODE HERE:


# ==================================================
# TASK 4: Draw a Rainbow
# ==================================================
# Draw a rainbow with 7 coloured arcs!
# Each arc is a semicircle, slightly bigger than the last.
#
# HINTS:
#   - t.circle(radius, 180) draws a semicircle
#   - Draw the biggest arc first (red), then smaller ones
#   - Move the turtle slightly before each arc to nest them
#   - Rainbow order: red, orange, yellow, green, blue, indigo, violet

RAINBOW_COLOURS = ["red", "orange", "yellow", "green",
                   "blue", "indigo", "violet"]

def draw_rainbow():
    """Draw a 7-colour rainbow."""
    t.penup()
    t.goto(-200, -180)    # Start position
    t.pendown()
    t.setheading(0)       # Face right

    t.pensize(8)          # Thick lines look better for rainbows

    # TODO: Loop through the rainbow colours
    # HINT: Start with radius = 180, decrease by 20 each time
    # for i, colour in enumerate(RAINBOW_COLOURS):
    #     radius = 180 - (i * 20)
    #     t.color(colour)
    #     t.circle(radius, 180)  # Draw a semicircle
    #     # Move to next arc's starting position
    #     t.penup()
    #     t.goto(-200 + (i + 1) * 10, -180)
    #     t.pendown()
    #     t.setheading(0)

    # YOUR CODE HERE:

    t.pensize(2)          # Reset pen size


# ==================================================
# TASK 5: BONUS - Draw a Whole Scene!
# ==================================================
# Draw a complete scene with:
#   - A house (use what you learned in turtle_intro.py!)
#   - A tree next to it
#   - A sun in the sky
#   - Maybe some clouds or flowers?
#
# This is your creative challenge - there are no rules!
# Use the functions from the other lessons as inspiration.
#
# HINTS:
#   - A tree trunk: brown rectangle, then green circle on top
#   - A sun: yellow circle with lines (petals) coming out
#   - A cloud: several overlapping white/light grey circles

def draw_scene():
    """BONUS: Draw your own complete scene!"""
    # TODO: Draw a house
    # YOUR CODE HERE:

    # TODO: Draw a tree
    # YOUR CODE HERE:

    # TODO: Draw a sun
    # YOUR CODE HERE:

    # TODO: Add anything else you like!
    # YOUR CODE HERE:
    pass


# ==================================================
# MAIN: Run all tasks
# ==================================================
def main() -> None:
    """Run all drawing tasks."""
    print("Starting your art gallery!")
    print("Complete each function above, then run this file.")
    print()

    # Draw a title
    t.penup()
    t.goto(-120, 310)
    t.pendown()
    t.color("darkblue")
    t.write("My Turtle Art!", font=("Arial", 20, "bold"))

    # Call each task
    # Uncomment tasks as you complete them!
    draw_my_letter()
    draw_smiley_face()
    draw_flower()
    draw_rainbow()
    # draw_scene()  # Uncomment when ready for the bonus!

    print("Art gallery complete!")
    print("Great work - you are a turtle artist!")
    turtle.done()


if __name__ == "__main__":
    main()

"""
===================================================
  Lesson 3: Animation Exercises!
  Module 0 - From Scratch to Python!
===================================================

THREE animation challenges for you to complete!

  Exercise 1: Square Path Animation
  Exercise 2: Turtle Race!
  Exercise 3: BONUS - Sunrise Animation

Read each exercise carefully, look at the HINTS,
and fill in every section that says TODO.

You can run this file to test your work as you go!
"""

import turtle
import time
import random


# ==================================================
# EXERCISE 1: Square Path Animation
# ==================================================
# Make a turtle walk in a square path, over and over.
#
# What it should do:
#   - A turtle walks forward, turns right 90 degrees
#   - Does this 4 times to complete a square
#   - Then does the WHOLE square again (and again, in a loop)
#   - Keep going for at least 3 full laps
#
# HINTS:
#   - Use a for loop inside a for loop (nested loops)
#   - Outer loop: for lap in range(3):
#   - Inner loop: for side in range(4):
#   - Inside inner loop: forward(150), right(90)
#   - Add time.sleep(0.05) to slow it down so you can watch
#
# In Scratch this is:
#   "repeat 3 {
#       repeat 4 { move 150 steps, turn right 90 }
#   }"

def exercise_1_square_path() -> None:
    """Exercise 1: Walk in a square path, 3 laps."""
    screen = turtle.Screen()
    screen.title("Exercise 1: Square Path")
    screen.bgcolor("white")
    screen.setup(600, 500)

    t = turtle.Turtle()
    t.speed(6)
    t.color("blue")
    t.pensize(3)

    # Move turtle to starting position
    t.penup()
    t.goto(-75, 75)
    t.pendown()

    # TODO: Write nested loops to walk 3 laps of a square
    # OUTER loop: repeat 3 times (3 laps)
    #   INNER loop: repeat 4 times (4 sides)
    #     forward(150)
    #     right(90)
    #     time.sleep(0.05)

    # YOUR CODE HERE:

    t.color("red")
    t.penup()
    t.goto(-100, -200)
    t.pendown()
    t.write("Exercise 1 Done!", font=("Arial", 14, "bold"))

    turtle.done()


# ==================================================
# EXERCISE 2: Turtle Race!
# ==================================================
# Two turtles race across the screen.
# Each "turn", both turtles move a random number of steps.
# The first one to reach the right side wins!
#
# What it should do:
#   - Set up 2 turtles at the left side of screen
#   - In each turn, move each turtle a random amount (1-10 steps)
#   - Check if either turtle has reached x=280 (the finish line)
#   - Stop the race and announce the winner!
#
# HINTS:
#   - random.randint(1, 10) gives a random number 1 to 10
#   - t.xcor() gets the turtle's current x position
#   - use a while loop: while not race_finished:
#   - Check after each turtle moves: if t1.xcor() >= 280:
#
# In Scratch this is like the "turtle race" example project!

def exercise_2_turtle_race() -> None:
    """Exercise 2: Race two turtles across the screen."""
    screen = turtle.Screen()
    screen.title("Exercise 2: Turtle Race!")
    screen.bgcolor("lightgreen")
    screen.setup(700, 400)

    # Create turtle 1 (blue)
    t1 = turtle.Turtle()
    t1.shape("turtle")
    t1.color("blue")
    t1.penup()
    t1.goto(-280, 50)
    t1.pendown()
    t1.pensize(2)

    # Create turtle 2 (red)
    t2 = turtle.Turtle()
    t2.shape("turtle")
    t2.color("red")
    t2.penup()
    t2.goto(-280, -50)
    t2.pendown()
    t2.pensize(2)

    # Draw the finish line
    finish_line = turtle.Turtle()
    finish_line.hideturtle()
    finish_line.penup()
    finish_line.goto(280, 150)
    finish_line.pendown()
    finish_line.color("black")
    finish_line.pensize(3)
    finish_line.goto(280, -150)
    finish_line.penup()
    finish_line.goto(240, 180)
    finish_line.write("FINISH", font=("Arial", 12, "bold"))

    # Label the turtles
    label_t = turtle.Turtle()
    label_t.hideturtle()
    label_t.penup()
    label_t.goto(-320, 50)
    label_t.color("blue")
    label_t.write("Blue", font=("Arial", 12, "bold"))
    label_t.goto(-320, -50)
    label_t.color("red")
    label_t.write("Red", font=("Arial", 12, "bold"))

    race_finished = False
    winner = ""

    # TODO: Write the race loop!
    # while not race_finished:
    #     Move t1 by random steps (random.randint(1, 10))
    #     Move t2 by random steps (random.randint(1, 10))
    #     time.sleep(0.1)    <- small pause between turns
    #     Check if t1 reached x=280 -> winner = "Blue Turtle!"
    #     Check if t2 reached x=280 -> winner = "Red Turtle!"
    #     If either reached the finish: race_finished = True

    # YOUR CODE HERE:

    # Announce the winner
    result_t = turtle.Turtle()
    result_t.hideturtle()
    result_t.penup()
    result_t.goto(-150, -150)
    result_t.color("darkgreen")
    if winner:
        result_t.write(f"WINNER: {winner}", font=("Arial", 18, "bold"))
    else:
        result_t.write("Complete the TODO to race!", font=("Arial", 14, "bold"))

    turtle.done()


# ==================================================
# EXERCISE 3: BONUS - Sunrise Animation
# ==================================================
# Create a "sunrise" animation:
#   - A dark blue sky at the start
#   - A yellow circle (sun) starts below the bottom of the screen
#   - The sun slowly moves upward
#   - As the sun rises, the sky changes from dark to lighter blue
#   - The sun changes from orange/red at the bottom to yellow at the top
#
# HINTS:
#   - screen.bgcolor() can be called in a loop to change the sky
#   - Use a list of sky colours: ["#0d0d2b", "#1a1a4e", "#2e4057", "#4a7fa5", "#87ceeb"]
#   - Use sun_y variable, start it at -300, increase it each frame
#   - Change sun colour from "orangered" to "orange" to "gold" to "yellow"
#   - Run the loop until sun_y > 200 (the sun is high in the sky)
#   - Use screen.tracer(0) and screen.update() for smooth animation
#
# In Scratch this is like a scrolling backdrop effect!

def exercise_3_sunrise() -> None:
    """BONUS Exercise 3: Sunrise animation."""
    screen = turtle.Screen()
    screen.title("Exercise 3 BONUS: Sunrise!")
    screen.setup(700, 500)
    screen.tracer(0)

    sky_colours = ["#0d0d2b", "#1a1a4e", "#2e4057", "#4a7fa5", "#87ceeb"]
    sun_colours = ["orangered", "orange", "gold", "yellow", "lightyellow"]

    sun = turtle.Turtle()
    sun.hideturtle()
    sun.penup()
    sun.speed(0)

    # TODO: Set the initial sky colour to sky_colours[0]
    # YOUR CODE HERE:

    # TODO: Write the sunrise loop!
    # - sun_y starts at -300
    # - Each frame: sun_y += 2
    # - Clear and redraw the sun at new position
    # - Change sky colour based on how high the sun is
    # - Change sun colour based on how high the sun is
    # - Call screen.update() and time.sleep(0.02) each frame
    # - Stop when sun_y > 200

    # YOUR CODE HERE:

    # Add a message when sunrise is complete
    msg_t = turtle.Turtle()
    msg_t.hideturtle()
    msg_t.penup()
    msg_t.goto(-130, -220)
    msg_t.color("white")
    msg_t.write("Good morning!", font=("Arial", 20, "bold"))
    screen.update()

    turtle.done()


# ==================================================
# MAIN: Choose which exercise to run
# ==================================================
def main() -> None:
    """Run one exercise at a time. Comment/uncomment to choose!"""
    print("Animation Exercises!")
    print("Uncomment ONE exercise below to run it.")
    print()
    print("  exercise_1_square_path()  - Walk in squares")
    print("  exercise_2_turtle_race()  - Race turtles")
    print("  exercise_3_sunrise()      - BONUS sunrise")

    # Uncomment ONE line to run that exercise:
    exercise_1_square_path()
    # exercise_2_turtle_race()
    # exercise_3_sunrise()


if __name__ == "__main__":
    main()

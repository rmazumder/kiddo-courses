"""
===================================================
  Lesson 3: Turtle Animation - Moving Character!
  Module 0 - From Scratch to Python!
===================================================

Watch a little character bounce back and forth
across the screen!

How it works:
  - We draw the character at position (x, y)
  - Each frame, we move x by speed_x
  - When x goes past the edge, we flip the speed negative
    (that makes it go the other way - like bouncing!)
  - We clear and redraw everything each frame

In Scratch this is:
  "forever {
      move (speed) steps
      if on edge, bounce
      draw costume
  }"
"""

import turtle
import time
import math


# ==================================================
# SETUP
# ==================================================
screen = turtle.Screen()
screen.title("Bouncing Character!")
screen.bgcolor("skyblue")
screen.setup(width=700, height=500)

# tracer(0) = manual screen control = smooth animation
# In Scratch, this happens automatically
screen.tracer(0)

# We need several turtles for different drawing layers
character = turtle.Turtle()   # Draws our character
ground_t = turtle.Turtle()    # Draws the ground
hud_t = turtle.Turtle()       # Draws the score/info (HUD = Heads-Up Display)

for t_obj in [character, ground_t, hud_t]:
    t_obj.hideturtle()
    t_obj.penup()
    t_obj.speed(0)


# ==================================================
# GAME STATE - Variables that track what is happening
# In Scratch: these are your sprite's variables
# ==================================================
char_x: float = -200.0        # Character's x position (starts left)
char_y: float = -80.0         # Character's y position (stays same - ground)
speed_x: float = 4.0          # How fast to move each frame (positive = right)
bounce_count: int = 0         # How many times we have bounced
frame: int = 0                # Current animation frame (for animation cycles)
facing_right: bool = True     # Which way the character faces

SCREEN_LEFT: int = -340       # Left boundary
SCREEN_RIGHT: int = 340       # Right boundary


# ==================================================
# DRAWING FUNCTIONS
# ==================================================

def draw_ground() -> None:
    """Draws the ground once (static, doesn't move)."""
    ground_t.goto(-350, -100)
    ground_t.pendown()
    ground_t.color("saddlebrown")
    ground_t.pensize(4)

    ground_t.begin_fill()
    ground_t.fillcolor("green")
    for _ in range(2):
        ground_t.forward(700)
        ground_t.right(90)
        ground_t.forward(50)
        ground_t.right(90)
    ground_t.end_fill()
    ground_t.penup()


def draw_character(x: float, y: float, facing: bool, frame_num: int) -> None:
    """
    Draws a simple stick-figure character at position (x, y).

    Args:
        x: Horizontal position.
        y: Vertical position (feet position).
        facing: True = facing right, False = facing left.
        frame_num: Current frame for leg animation.
    """
    character.clear()             # Erase previous position
                                  # In Scratch: costume changes each frame

    # Direction multiplier: 1 = right, -1 = left (mirrors the character)
    direction = 1 if facing else -1

    # HEAD (circle)
    character.goto(x, y + 40)
    character.color("peachpuff")
    character.dot(28)             # A filled circle (head)

    # EYES
    character.color("black")
    eye_offset = 5 * direction
    character.goto(x + eye_offset, y + 46)
    character.dot(5)              # Eye

    # SMILE
    character.goto(x + 3 * direction, y + 40)
    character.color("darkred")
    # Draw a small arc for the smile
    character.setheading(-45 * direction)
    character.pendown()
    character.circle(5, 90)
    character.penup()

    # BODY (line from head down to waist)
    character.goto(x, y + 26)
    character.color("dodgerblue")
    character.pensize(4)
    character.pendown()
    character.goto(x, y + 5)
    character.penup()

    # LEGS (animate by alternating angle each frame)
    # In Scratch: "point in direction" and "move steps"
    leg_swing = math.sin(frame_num * 0.3) * 20   # Oscillates back and forth
    character.pensize(3)
    character.color("navy")

    # Left leg
    character.goto(x, y + 5)
    character.pendown()
    character.goto(x - 8, y - 20 + leg_swing * direction)
    character.penup()

    # Right leg
    character.goto(x, y + 5)
    character.pendown()
    character.goto(x + 8, y - 20 - leg_swing * direction)
    character.penup()

    # ARMS
    arm_swing = math.sin(frame_num * 0.3) * 15
    character.pensize(3)
    character.color("dodgerblue")

    # Left arm
    character.goto(x, y + 22)
    character.pendown()
    character.goto(x - 12 * direction, y + 15 + arm_swing * direction)
    character.penup()

    # Right arm
    character.goto(x, y + 22)
    character.pendown()
    character.goto(x + 12 * direction, y + 15 - arm_swing * direction)
    character.penup()


def draw_hud(bounces: int) -> None:
    """Draws the on-screen information (bounce count)."""
    hud_t.clear()
    hud_t.goto(-330, 200)
    hud_t.color("white")
    hud_t.write(
        f"Bounces: {bounces}",
        font=("Arial", 16, "bold"),
    )


# ==================================================
# MAIN ANIMATION LOOP
# ==================================================
def main() -> None:
    """Main animation loop."""
    global char_x, speed_x, bounce_count, frame, facing_right

    print("Animation running! Close the window to stop.")
    print("Watch the character bounce back and forth!")

    # Draw the ground once (it never changes)
    draw_ground()

    # THE ANIMATION LOOP
    # In Scratch: "forever { ... }"
    while True:
        # 1. UPDATE POSITION
        # In Scratch: "move (speed_x) steps"
        char_x += speed_x
        frame += 1

        # 2. CHECK BOUNDARIES (bounce off edges)
        # In Scratch: "if on edge, bounce"
        if char_x >= SCREEN_RIGHT:
            char_x = SCREEN_RIGHT
            speed_x = -abs(speed_x)     # Flip direction: go left
            facing_right = False
            bounce_count += 1
        elif char_x <= SCREEN_LEFT:
            char_x = SCREEN_LEFT
            speed_x = abs(speed_x)      # Flip direction: go right
            facing_right = True
            bounce_count += 1

        # 3. DRAW
        draw_character(char_x, char_y, facing_right, frame)
        draw_hud(bounce_count)

        # 4. UPDATE SCREEN (show this frame)
        # This is what actually makes the drawing appear
        screen.update()

        # 5. SMALL PAUSE to control speed (~60 frames per second)
        # In Scratch: wait 0.016 secs
        time.sleep(0.016)


if __name__ == "__main__":
    main()

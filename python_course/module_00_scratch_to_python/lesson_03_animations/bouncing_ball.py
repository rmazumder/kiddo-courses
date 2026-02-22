"""
===================================================
  Lesson 3: Bouncing Ball with Score!
  Module 0 - From Scratch to Python!
===================================================

A ball bounces around the screen.
Every time it hits a wall, the score goes up
and the ball changes colour!

This shows:
  - The animation loop (move, check walls, draw, repeat)
  - Velocity (speed in x and y directions)
  - Collision detection (checking boundaries)
  - Score display

In Scratch this would be:
  "forever {
      change x by speed_x
      change y by speed_y
      if touching edge {
          change colour effect
          change score by 1
          bounce (flip speed)
      }
      stamp sprite
  }"
"""

import turtle
import time
import random


# ==================================================
# SETUP
# ==================================================
screen = turtle.Screen()
screen.title("Bouncing Ball - Catch the Bounces!")
screen.bgcolor("#1a1a2e")         # Dark navy background
screen.setup(width=700, height=600)
screen.tracer(0)                  # Manual screen control for smooth animation

# Drawing turtles
ball_t = turtle.Turtle()          # Draws the ball
text_t = turtle.Turtle()          # Draws score and info
trail_t = turtle.Turtle()         # Draws a fading trail effect

for t_obj in [ball_t, text_t, trail_t]:
    t_obj.hideturtle()
    t_obj.penup()
    t_obj.speed(0)


# ==================================================
# GAME STATE
# In Scratch: these are the sprite's variables
# ==================================================
ball_x: float = 0.0              # Ball x position (starts at centre)
ball_y: float = 0.0              # Ball y position (starts at centre)
speed_x: float = 5.0             # Horizontal speed (pixels per frame)
speed_y: float = 4.0             # Vertical speed (pixels per frame)
ball_radius: int = 25            # Size of the ball
score: int = 0                   # How many wall bounces

# Boundaries (half of screen width/height, minus ball radius)
LEFT_WALL: int = -340
RIGHT_WALL: int = 340
TOP_WALL: int = 270
BOTTOM_WALL: int = -270

# Ball colours - cycles through these on each bounce
BALL_COLOURS = [
    "#FF6B6B",  # coral red
    "#FFD93D",  # sunny yellow
    "#6BCB77",  # grass green
    "#4D96FF",  # sky blue
    "#FF6B9D",  # pink
    "#C77DFF",  # purple
    "#FF9A00",  # orange
    "#00D4FF",  # cyan
]
current_colour_index: int = 0


# ==================================================
# HELPER FUNCTIONS
# ==================================================

def get_next_colour() -> str:
    """Returns the next colour in the cycle."""
    global current_colour_index
    colour = BALL_COLOURS[current_colour_index]
    current_colour_index = (current_colour_index + 1) % len(BALL_COLOURS)
    return colour


def draw_ball(x: float, y: float, colour: str, radius: int) -> None:
    """
    Draws the ball at position (x, y).

    Args:
        x: Horizontal position.
        y: Vertical position.
        colour: Fill colour.
        radius: Ball radius in pixels.
    """
    ball_t.clear()                # Erase old ball position
    ball_t.goto(x, y)
    ball_t.color(colour)
    ball_t.dot(radius * 2)        # dot() draws a filled circle

    # Draw a highlight (makes ball look 3D!)
    ball_t.goto(x - radius * 0.3, y + radius * 0.3)
    ball_t.color("white")
    ball_t.dot(radius * 0.5)


def draw_walls() -> None:
    """Draws the wall boundaries as a border."""
    wall_t = turtle.Turtle()
    wall_t.hideturtle()
    wall_t.penup()
    wall_t.speed(0)
    wall_t.goto(LEFT_WALL, BOTTOM_WALL)
    wall_t.pendown()
    wall_t.color("#4a4e69")
    wall_t.pensize(4)
    wall_t.begin_fill()
    wall_t.fillcolor("#16213e")
    for _ in range(2):
        wall_t.forward(RIGHT_WALL - LEFT_WALL)
        wall_t.left(90)
        wall_t.forward(TOP_WALL - BOTTOM_WALL)
        wall_t.left(90)
    wall_t.end_fill()
    wall_t.penup()


def draw_hud(bounces: int, current_col: str) -> None:
    """
    Draws the heads-up display (score and colour info).

    Args:
        bounces: Current bounce count.
        current_col: The ball's current colour hex code.
    """
    text_t.clear()

    # Score
    text_t.goto(-320, 280)
    text_t.color("white")
    text_t.write(f"Bounces: {bounces}", font=("Arial", 18, "bold"))

    # Current colour label
    text_t.goto(-320, 250)
    text_t.color(current_col)
    text_t.write(f"Colour: {current_col}", font=("Arial", 12, "normal"))

    # Instructions
    text_t.goto(120, 280)
    text_t.color("#888888")
    text_t.write("Close window to stop", font=("Arial", 10, "normal"))


# ==================================================
# MAIN ANIMATION LOOP
# ==================================================
def main() -> None:
    """Main function - runs the bouncing ball animation."""
    global ball_x, ball_y, speed_x, speed_y, score, current_colour_index

    current_colour = get_next_colour()

    print("Bouncing ball started!")
    print("Watch it bounce and change colour!")
    print("Close the window to stop.")

    # Draw the static background
    draw_walls()

    # THE ANIMATION LOOP
    # In Scratch: "forever { ... }"
    while True:

        # ------------------------------------------
        # 1. MOVE the ball
        # In Scratch: "change x by speed_x" and "change y by speed_y"
        # ------------------------------------------
        ball_x += speed_x
        ball_y += speed_y

        # ------------------------------------------
        # 2. CHECK WALLS (bounce detection)
        # In Scratch: "if <x position > 240> { ... }"
        # ------------------------------------------
        bounced = False

        # Left and right walls
        if ball_x + ball_radius >= RIGHT_WALL:
            ball_x = RIGHT_WALL - ball_radius
            speed_x = -abs(speed_x)        # Reverse horizontal direction
            bounced = True

        elif ball_x - ball_radius <= LEFT_WALL:
            ball_x = LEFT_WALL + ball_radius
            speed_x = abs(speed_x)          # Reverse horizontal direction
            bounced = True

        # Top and bottom walls
        if ball_y + ball_radius >= TOP_WALL:
            ball_y = TOP_WALL - ball_radius
            speed_y = -abs(speed_y)         # Reverse vertical direction
            bounced = True

        elif ball_y - ball_radius <= BOTTOM_WALL:
            ball_y = BOTTOM_WALL + ball_radius
            speed_y = abs(speed_y)           # Reverse vertical direction
            bounced = True

        # ------------------------------------------
        # 3. ON BOUNCE: update score and colour
        # In Scratch: "change score by 1" and "change colour effect by 25"
        # ------------------------------------------
        if bounced:
            score += 1
            current_colour = get_next_colour()

            # Every 10 bounces, speed up slightly!
            if score % 10 == 0:
                speed_x *= 1.05
                speed_y *= 1.05
                print(f"Score: {score} - Speeding up!")

        # ------------------------------------------
        # 4. DRAW everything
        # ------------------------------------------
        draw_ball(ball_x, ball_y, current_colour, ball_radius)
        draw_hud(score, current_colour)

        # ------------------------------------------
        # 5. SHOW the frame on screen
        # ------------------------------------------
        screen.update()

        # ------------------------------------------
        # 6. WAIT a tiny moment (~60 FPS)
        # ------------------------------------------
        time.sleep(0.016)


if __name__ == "__main__":
    main()

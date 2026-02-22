"""
===================================================
  Lesson 4: Catch the Star!
  Module 0 - From Scratch to Python!
===================================================

GAME: Stars fall from the top of the screen.
      Move your catcher left and right to catch them.
      Miss 3 stars and the game is over!

CONTROLS:
  Left Arrow  - Move catcher left
  Right Arrow - Move catcher right

SCORING:
  Catch a star  = +1 point
  Miss a star   = -1 life
  3 misses      = Game Over

This is EXACTLY like a Scratch game, just typed instead of clicked!
"""

import turtle
import random
import time


# ==================================================
# SETUP
# ==================================================
screen = turtle.Screen()
screen.title("Catch the Star!")
screen.bgcolor("#0f0e17")
screen.setup(width=600, height=650)
screen.tracer(0)              # Manual refresh for smooth animation


# ==================================================
# GAME STATE VARIABLES
# In Scratch: these are your project's variables
# ==================================================
score: int = 0
lives: int = 3
game_over: bool = False
catcher_x: float = 0.0
star_x: float = 0.0
star_y: float = 0.0
star_speed: float = 3.0
catcher_speed: float = 20.0
stars_caught: int = 0


# ==================================================
# CREATE TURTLES
# ==================================================
# Catcher paddle (player-controlled)
catcher = turtle.Turtle()
catcher.hideturtle()
catcher.penup()
catcher.speed(0)

# The falling star
star = turtle.Turtle()
star.hideturtle()
star.penup()
star.speed(0)

# HUD (score, lives, messages)
hud = turtle.Turtle()
hud.hideturtle()
hud.penup()
hud.speed(0)


# ==================================================
# FUNCTIONS TO RESET / SPAWN
# ==================================================

def reset_star() -> None:
    """Move the star to a random position at the top of the screen."""
    global star_x, star_y
    star_x = random.randint(-260, 260)   # In Scratch: "set x to (pick random -260 to 260)"
    star_y = 300                          # Start at top of screen


def draw_catcher(x: float) -> None:
    """
    Draws the catcher paddle at horizontal position x.

    Args:
        x: Centre x position of the paddle.
    """
    catcher.clear()
    y = -270                  # Paddle stays near the bottom

    # Draw paddle body
    catcher.goto(x - 50, y)
    catcher.color("#4d96ff")
    catcher.begin_fill()
    catcher.fillcolor("#4d96ff")

    # Rectangle: 100 wide, 15 tall
    catcher.pendown()
    catcher.forward(100)
    catcher.left(90)
    catcher.forward(15)
    catcher.left(90)
    catcher.forward(100)
    catcher.left(90)
    catcher.forward(15)
    catcher.left(90)
    catcher.penup()

    catcher.end_fill()

    # Glowing edge
    catcher.goto(x - 50, y + 14)
    catcher.color("#a8d8ff")
    catcher.pendown()
    catcher.forward(100)
    catcher.penup()


def draw_star_shape(x: float, y: float) -> None:
    """
    Draws a 5-pointed star at position (x, y).

    Args:
        x: Horizontal position.
        y: Vertical position.
    """
    star.clear()
    star.goto(x, y)
    star.setheading(90)
    star.color("gold")
    star.begin_fill()
    for _ in range(5):            # In Scratch: "repeat 5"
        star.forward(25)
        star.right(144)           # Star angle (360/5 * 2)
    star.end_fill()

    # Star sparkle
    star.goto(x, y + 28)
    star.color("lightyellow")
    star.dot(6)


def draw_hud_display() -> None:
    """Draws the score and lives on screen."""
    hud.clear()

    # Score (top left)
    hud.goto(-270, 280)
    hud.color("gold")
    hud.write(f"Score: {score}", font=("Arial", 18, "bold"))

    # Lives (top right)
    hud.goto(130, 280)
    hud.color("#FF6B6B")
    hearts = "* " * lives
    hud.write(f"Lives: {hearts}", font=("Arial", 18, "bold"))

    # Divider line
    hud.goto(-290, 265)
    hud.color("#333355")
    hud.pendown()
    hud.forward(580)
    hud.penup()


def draw_game_over() -> None:
    """Draws the game over screen."""
    hud.clear()

    # Dark overlay effect (text over everything)
    hud.goto(-200, 50)
    hud.color("#FF6B6B")
    hud.write("GAME OVER!", font=("Arial", 36, "bold"))

    hud.goto(-180, -20)
    hud.color("gold")
    hud.write(f"Final Score: {score}", font=("Arial", 24, "bold"))

    hud.goto(-220, -80)
    hud.color("white")
    hud.write(f"Stars Caught: {stars_caught}", font=("Arial", 18, "normal"))

    hud.goto(-160, -130)
    hud.color("#888888")
    hud.write("Close window to exit", font=("Arial", 14, "normal"))


# ==================================================
# KEYBOARD CONTROLS
# In Scratch: "when [arrow] pressed" blocks
# ==================================================

def move_left() -> None:
    """Move catcher paddle left. Called when Left Arrow pressed."""
    global catcher_x
    # In Scratch: "change x by -20"
    if catcher_x - 50 > -290:         # Don't go off left edge
        catcher_x -= catcher_speed


def move_right() -> None:
    """Move catcher paddle right. Called when Right Arrow pressed."""
    global catcher_x
    # In Scratch: "change x by 20"
    if catcher_x + 50 < 290:          # Don't go off right edge
        catcher_x += catcher_speed


# Register key bindings
screen.listen()                         # In Scratch: always listening
screen.onkey(move_left, "Left")         # In Scratch: "when [left arrow] pressed"
screen.onkey(move_right, "Right")       # In Scratch: "when [right arrow] pressed"


# ==================================================
# MAIN GAME LOOP
# ==================================================

def main() -> None:
    """Main game loop - runs until game over."""
    global star_x, star_y, star_speed
    global score, lives, game_over, stars_caught

    print("Catch the Star!")
    print("Use LEFT and RIGHT arrow keys to move the paddle.")
    print("Miss 3 stars and it's game over!")

    # Start the star at a random position
    reset_star()

    # THE GAME LOOP
    # In Scratch: "forever { ... }" connected to green flag
    while not game_over:

        # ------------------------------------------
        # 1. MOVE THE STAR DOWNWARD
        # In Scratch: "change y by -star_speed"
        # ------------------------------------------
        star_y -= star_speed

        # ------------------------------------------
        # 2. CHECK: Did the player CATCH the star?
        # In Scratch: "if <touching [catcher]?>"
        # We check if star is near the paddle height AND within paddle width
        # ------------------------------------------
        paddle_y = -270
        if (star_y <= paddle_y + 20 and
                abs(star_x - catcher_x) < 60):      # Within 60 pixels (paddle half-width + star)
            # CAUGHT IT!
            score += 1                               # In Scratch: "change score by 1"
            stars_caught += 1
            reset_star()                             # Spawn new star at top

            # Speed up slightly every 5 catches
            if stars_caught % 5 == 0:
                star_speed += 0.3
                print(f"Score: {score} - Speeding up!")

        # ------------------------------------------
        # 3. CHECK: Did the star hit the BOTTOM (miss)?
        # In Scratch: "if <y position < -310>"
        # ------------------------------------------
        elif star_y < -320:
            lives -= 1                               # In Scratch: "change lives by -1"
            reset_star()

            if lives <= 0:
                game_over = True                     # In Scratch: "stop all"

        # ------------------------------------------
        # 4. DRAW EVERYTHING
        # ------------------------------------------
        draw_star_shape(star_x, star_y)
        draw_catcher(catcher_x)
        draw_hud_display()

        # ------------------------------------------
        # 5. SHOW THE FRAME
        # ------------------------------------------
        screen.update()                              # In Scratch: screen refreshes automatically
        time.sleep(0.016)

    # Game over!
    draw_game_over()
    screen.update()
    print(f"\nGame Over! Final Score: {score}")
    screen.mainloop()


if __name__ == "__main__":
    main()

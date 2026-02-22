"""
===================================================
  Lesson 4: Build Your Own Game! (Exercise File)
  Module 0 - From Scratch to Python!
===================================================

TWO mini-game templates for you to complete:

  GAME A: "Click the Target"
    - A circle appears on screen
    - Click on it as fast as you can to score points
    - Target moves to a new random spot after each click
    - Score goes up every time you hit it

  GAME B: "Keyboard Navigator"
    - Control a turtle with W/A/S/D keys
    - Navigate around the screen
    - Optional: add walls to avoid!

Pick ONE to complete (or do both for extra XP!)
"""

import turtle
import random
import time


# ==================================================
# GAME A: Click the Target
# ==================================================
# A circle "target" appears on screen.
# The player clicks on it to score points.
# After each click, the target jumps to a new spot.
#
# HOW IT WORKS:
#   - Use screen.onclick(callback) to detect mouse clicks
#   - The callback receives (x, y) = where the player clicked
#   - Check if the click is close enough to the target centre
#   - If yes: score += 1, move target to new random position
#   - Display the score with a text turtle
#
# HINTS:
#   - Distance formula: ((x - tx)**2 + (y - ty)**2) ** 0.5
#     (this gives the distance between two points)
#   - If distance < TARGET_RADIUS: it was a hit!
#   - random.randint(-250, 250) for random x position
#   - random.randint(-200, 200) for random y position
#
# In Scratch this is like:
#   "when this sprite clicked: change score by 1"
#   "when this sprite clicked: go to (random position)"

def game_a_click_target() -> None:
    """GAME A: Click the Target to score points!"""
    screen = turtle.Screen()
    screen.title("Game A: Click the Target!")
    screen.bgcolor("#1a1a2e")
    screen.setup(600, 550)
    screen.tracer(0)

    # Target turtle (draws the circle to click on)
    target_t = turtle.Turtle()
    target_t.hideturtle()
    target_t.penup()
    target_t.speed(0)

    # Score display turtle
    score_t = turtle.Turtle()
    score_t.hideturtle()
    score_t.penup()
    score_t.speed(0)

    # Game state
    target_x: float = 0.0
    target_y: float = 0.0
    TARGET_RADIUS: int = 35
    score: int = 0
    time_limit: int = 30          # 30 seconds to play
    start_time: float = time.time()

    def spawn_target() -> None:
        """Move target to a random position."""
        nonlocal target_x, target_y
        # TODO: Set target_x to a random value between -240 and 240
        # TODO: Set target_y to a random value between -200 and 200
        # YOUR CODE HERE:
        target_x = 0      # Replace with random position!
        target_y = 0      # Replace with random position!

    def draw_target() -> None:
        """Draw the target circle at current position."""
        target_t.clear()
        target_t.goto(target_x, target_y)

        # Outer ring (red)
        target_t.color("red")
        target_t.dot(TARGET_RADIUS * 2)

        # Inner ring (white)
        target_t.dot(TARGET_RADIUS)

        # Bull's eye (red)
        target_t.color("red")
        target_t.dot(TARGET_RADIUS // 2)

    def draw_score() -> None:
        """Display score and time remaining."""
        score_t.clear()
        score_t.goto(-270, 240)
        score_t.color("white")
        score_t.write(f"Score: {score}", font=("Arial", 18, "bold"))

        elapsed = time.time() - start_time
        remaining = max(0, time_limit - int(elapsed))
        score_t.goto(130, 240)
        score_t.color("gold" if remaining > 10 else "red")
        score_t.write(f"Time: {remaining}s", font=("Arial", 18, "bold"))

    def on_click(x: float, y: float) -> None:
        """Called whenever the player clicks the screen."""
        nonlocal score, target_x, target_y

        # TODO: Calculate the distance from click (x,y) to target (target_x, target_y)
        # HINT: distance = ((x - target_x)**2 + (y - target_y)**2) ** 0.5
        # YOUR CODE HERE:
        distance = 999      # Replace with real distance calculation!

        # TODO: If distance < TARGET_RADIUS, the player hit it!
        # If hit:
        #   - Add 1 to score
        #   - Call spawn_target() to move target
        # YOUR CODE HERE:

    # Start
    spawn_target()
    screen.onclick(on_click)      # Register click handler

    # Game loop
    game_running = True
    while game_running:
        draw_target()
        draw_score()
        screen.update()
        time.sleep(0.016)

        # Check time limit
        if time.time() - start_time >= time_limit:
            game_running = False

    # Game over
    target_t.clear()
    score_t.clear()
    score_t.goto(-150, 30)
    score_t.color("gold")
    score_t.write(f"TIME'S UP!", font=("Arial", 36, "bold"))
    score_t.goto(-160, -40)
    score_t.color("white")
    score_t.write(f"Final Score: {score}", font=("Arial", 22, "bold"))
    screen.update()
    screen.mainloop()


# ==================================================
# GAME B: Keyboard Navigator
# ==================================================
# Control a turtle with W/A/S/D keys.
# Navigate around the screen however you like!
# Optional: add boundaries, collect items, or avoid obstacles.
#
# CONTROLS:
#   W = move up
#   S = move down
#   A = move left
#   D = move right
#
# HOW IT WORKS:
#   - screen.onkey(function, "key") binds a key to an action
#   - screen.listen() tells Python to watch for key presses
#   - Each key press calls a function that moves the player
#   - The game loop redraws the player each frame
#
# HINTS:
#   - player_x += SPEED  (move right)
#   - player_x -= SPEED  (move left)
#   - player_y += SPEED  (move up)
#   - player_y -= SPEED  (move down)
#   - Keep player inside screen: if player_x > 280: player_x = 280
#
# OPTIONAL CHALLENGES (once basic movement works):
#   - Add collectible dots that disappear when you touch them
#   - Add a boundary (stop when hitting the edge)
#   - Add obstacles to avoid
#
# In Scratch this is like:
#   "when [w] pressed: change y by SPEED"
#   "when [s] pressed: change y by -SPEED" etc.

def game_b_keyboard_navigator() -> None:
    """GAME B: Control a turtle with WASD keys."""
    screen = turtle.Screen()
    screen.title("Game B: Keyboard Navigator! (WASD to move)")
    screen.bgcolor("#0d1b2a")
    screen.setup(620, 580)
    screen.tracer(0)

    # Player turtle
    player = turtle.Turtle()
    player.hideturtle()
    player.penup()
    player.speed(0)

    # Trail turtle (draws the path)
    trail = turtle.Turtle()
    trail.hideturtle()
    trail.speed(0)
    trail.color("#4d96ff")
    trail.pensize(2)
    trail.penup()
    trail.goto(0, 0)
    trail.pendown()

    # Info display
    info_t = turtle.Turtle()
    info_t.hideturtle()
    info_t.penup()
    info_t.speed(0)

    # Player state
    player_x: float = 0.0
    player_y: float = 0.0
    SPEED: int = 8
    BOUNDARY: int = 275
    steps_taken: int = 0

    # TODO: Define the four movement functions
    # Each one should change player_x or player_y by SPEED
    # And keep the player inside the boundary (BOUNDARY = 275)

    def move_up() -> None:
        """Move player up. Called when W is pressed."""
        nonlocal player_y, steps_taken
        # TODO: Increase player_y by SPEED (but not above BOUNDARY)
        # YOUR CODE HERE:
        pass

    def move_down() -> None:
        """Move player down. Called when S is pressed."""
        nonlocal player_y, steps_taken
        # TODO: Decrease player_y by SPEED (but not below -BOUNDARY)
        # YOUR CODE HERE:
        pass

    def move_left() -> None:
        """Move player left. Called when A is pressed."""
        nonlocal player_x, steps_taken
        # TODO: Decrease player_x by SPEED (but not below -BOUNDARY)
        # YOUR CODE HERE:
        pass

    def move_right() -> None:
        """Move player right. Called when D is pressed."""
        nonlocal player_x, steps_taken
        # TODO: Increase player_x by SPEED (but not above BOUNDARY)
        # YOUR CODE HERE:
        pass

    # TODO: Register the key bindings
    # HINT: screen.listen()
    #       screen.onkey(move_up, "w")
    #       screen.onkey(move_down, "s")  etc.
    # YOUR CODE HERE:

    def draw_player() -> None:
        """Draw the player character at current position."""
        player.clear()
        player.goto(player_x, player_y)

        # Body
        player.color("#4d96ff")
        player.dot(30)

        # Face
        player.color("white")
        player.dot(20)

        player.color("#4d96ff")
        player.dot(10)

        # Eyes
        player.goto(player_x - 5, player_y + 4)
        player.color("black")
        player.dot(4)

        player.goto(player_x + 5, player_y + 4)
        player.dot(4)

        # Update trail
        trail.goto(player_x, player_y)

    def draw_info() -> None:
        """Show position and steps info."""
        info_t.clear()
        info_t.goto(-290, 255)
        info_t.color("white")
        info_t.write(
            f"X:{int(player_x):4d}  Y:{int(player_y):4d}  Steps: {steps_taken}",
            font=("Arial", 13, "normal"),
        )
        info_t.goto(-290, -280)
        info_t.color("#888888")
        info_t.write("W=Up  S=Down  A=Left  D=Right", font=("Arial", 12, "normal"))

    # Game loop
    while True:
        draw_player()
        draw_info()
        screen.update()
        time.sleep(0.016)


# ==================================================
# MAIN: Choose which game to run
# ==================================================
def main() -> None:
    """Run one game. Comment/uncomment to switch."""
    print("Game Exercise File!")
    print("Uncomment ONE game below to play it.")
    print()
    print("  game_a_click_target()       - Click the circles")
    print("  game_b_keyboard_navigator() - WASD movement")

    # Uncomment ONE line:
    game_a_click_target()
    # game_b_keyboard_navigator()


if __name__ == "__main__":
    main()

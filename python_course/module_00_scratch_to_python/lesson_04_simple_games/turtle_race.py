"""
===================================================
  Lesson 4: Turtle Race!
  Module 0 - From Scratch to Python!
===================================================

GAME: 5 turtles line up at the start.
      You bet which one will win.
      Each turn, every turtle moves a random distance.
      First to the finish line wins!

HOW TO PLAY:
  When asked, type the colour of the turtle you think will win:
  red, orange, yellow, green, or blue

This is just like the Scratch "Turtle Race" project, but in Python!

In Scratch this would use:
  - "pick random 1 to 10" for random moves
  - "if touching [finish line]" to detect the winner
  - "move (random) steps" each turn
"""

import turtle
import random
import time


# ==================================================
# SETUP
# ==================================================
screen = turtle.Screen()
screen.title("Turtle Race! Place Your Bet!")
screen.bgcolor("#228B22")         # Grass green racetrack
screen.setup(width=750, height=500)
screen.tracer(0)


# ==================================================
# RACE SETTINGS
# In Scratch: these are your project variables
# ==================================================
TURTLE_COLOURS = ["red", "orange", "yellow", "cyan", "hotpink"]
TURTLE_NAMES   = ["Red",  "Orange", "Yellow", "Cyan",  "Pink"]
NUM_TURTLES = len(TURTLE_COLOURS)

START_X = -320
FINISH_X = 310

# Y positions for each lane (spread out vertically)
LANE_Y = [160, 80, 0, -80, -160]


# ==================================================
# DRAWING HELPER FUNCTIONS
# ==================================================

def draw_track() -> None:
    """Draws the racetrack lanes and labels."""
    track_pen = turtle.Turtle()
    track_pen.hideturtle()
    track_pen.penup()
    track_pen.speed(0)

    # Draw lane dividers
    for i, y in enumerate(LANE_Y):
        # Lane background
        track_pen.goto(START_X, y - 30)
        lane_colour = "#1a7a1a" if i % 2 == 0 else "#1e8a1e"
        track_pen.color(lane_colour)
        track_pen.begin_fill()
        track_pen.fillcolor(lane_colour)
        track_pen.pendown()
        for _ in range(2):
            track_pen.forward(FINISH_X - START_X)
            track_pen.left(90)
            track_pen.forward(60)
            track_pen.left(90)
        track_pen.end_fill()
        track_pen.penup()

    # Start line
    track_pen.goto(START_X + 10, 200)
    track_pen.color("white")
    track_pen.pendown()
    track_pen.pensize(3)
    track_pen.goto(START_X + 10, -200)
    track_pen.penup()
    track_pen.goto(START_X - 15, 210)
    track_pen.color("white")
    track_pen.write("START", font=("Arial", 10, "bold"))

    # Finish line (checkered style)
    track_pen.pensize(4)
    track_pen.goto(FINISH_X, 200)
    track_pen.color("white")
    track_pen.pendown()
    track_pen.goto(FINISH_X, -200)
    track_pen.penup()
    track_pen.goto(FINISH_X - 30, 210)
    track_pen.color("white")
    track_pen.write("FINISH", font=("Arial", 10, "bold"))


def draw_turtle_label(colour: str, name: str, y: float) -> None:
    """Draws a colour label next to the start line for each turtle."""
    label = turtle.Turtle()
    label.hideturtle()
    label.penup()
    label.speed(0)
    label.goto(START_X - 10, y - 8)
    label.color(colour)
    label.write(name, font=("Arial", 10, "bold"), align="right")


# ==================================================
# MAIN GAME
# ==================================================

def main() -> None:
    """Runs the turtle race."""
    print("=" * 50)
    print("  TURTLE RACE!")
    print("=" * 50)
    print()
    print("The turtles are:")
    for i, name in enumerate(TURTLE_NAMES):
        print(f"  {i + 1}. {name}")
    print()

    # Ask the player for their bet
    # In Scratch: "ask 'Which turtle will win?' and wait"
    player_bet = ""
    while player_bet not in [c.lower() for c in TURTLE_COLOURS]:
        player_bet = input(
            "Which turtle will win? Type a colour (red/orange/yellow/cyan/pink): "
        ).strip().lower()
        if player_bet not in [c.lower() for c in TURTLE_COLOURS]:
            print("Hmm, that's not one of the turtles. Try again!")

    print(f"\nYou bet on {player_bet.upper()}! Let's race!")
    print("Closing this window shows the race is over.\n")

    # Draw the track
    draw_track()

    # Create the racing turtles
    racers: list[turtle.Turtle] = []
    for i, colour in enumerate(TURTLE_COLOURS):
        racer = turtle.Turtle()
        racer.shape("turtle")
        racer.color(colour)
        racer.penup()
        racer.goto(START_X + 15, LANE_Y[i])
        racer.setheading(0)             # Face right
        racer.pendown()
        racer.pensize(2)
        racers.append(racer)

        # Draw colour labels
        draw_turtle_label(colour, TURTLE_NAMES[i], LANE_Y[i])

    screen.update()
    time.sleep(1.5)               # Pause before race starts

    # Countdown
    countdown_t = turtle.Turtle()
    countdown_t.hideturtle()
    countdown_t.penup()
    countdown_t.speed(0)

    for count in ["3", "2", "1", "GO!"]:
        countdown_t.clear()
        countdown_t.goto(0, 10)
        countdown_t.color("white")
        countdown_t.write(count, font=("Arial", 60, "bold"), align="center")
        screen.update()
        time.sleep(0.8)

    countdown_t.clear()
    screen.update()

    # ==================================================
    # THE RACE LOOP
    # In Scratch: "repeat until <winner found>"
    # ==================================================
    winner_colour = ""
    turn = 0

    while winner_colour == "":
        turn += 1

        # Move each turtle a random amount
        # In Scratch: "repeat 5 { move (pick random 1 to 10) steps }"
        for i, racer in enumerate(racers):
            # In Scratch: "move (pick random 1 to 10) steps"
            steps = random.randint(1, 10)
            racer.forward(steps)

            # Check if this turtle crossed the finish line
            # In Scratch: "if <x position > FINISH_X>"
            if racer.xcor() >= FINISH_X and winner_colour == "":
                winner_colour = TURTLE_COLOURS[i]

        screen.update()
        time.sleep(0.05)        # Small pause between turns so we can watch

    # ==================================================
    # ANNOUNCE THE WINNER
    # ==================================================
    announce_t = turtle.Turtle()
    announce_t.hideturtle()
    announce_t.penup()
    announce_t.speed(0)

    # Background box for announcement
    announce_t.goto(-250, -30)
    announce_t.color("#000000")
    announce_t.begin_fill()
    announce_t.fillcolor("#000000")
    announce_t.pendown()
    for _ in range(2):
        announce_t.forward(500)
        announce_t.left(90)
        announce_t.forward(120)
        announce_t.left(90)
    announce_t.end_fill()
    announce_t.penup()

    # Winner name
    winner_name = TURTLE_NAMES[TURTLE_COLOURS.index(winner_colour)]
    announce_t.goto(0, 40)
    announce_t.color(winner_colour)
    announce_t.write(
        f"{winner_name} WINS!",
        font=("Arial", 28, "bold"),
        align="center",
    )

    # Did player win their bet?
    announce_t.goto(0, -10)
    if player_bet == winner_colour.lower():
        announce_t.color("gold")
        announce_t.write(
            "You guessed RIGHT! Amazing!",
            font=("Arial", 16, "normal"),
            align="center",
        )
        print(f"\n{winner_name} wins! You guessed RIGHT! Incredible!")
    else:
        announce_t.color("#FF6B6B")
        announce_t.write(
            f"You picked {player_bet} - better luck next time!",
            font=("Arial", 14, "normal"),
            align="center",
        )
        print(f"\n{winner_name} wins! You picked {player_bet} - better luck next time!")

    screen.update()
    print("Close the window to exit.")
    screen.mainloop()


if __name__ == "__main__":
    main()

"""
===================================================
  Module 0 Final Challenge: Build a Scratch Remake!
  Module 0 - From Scratch to Python!
===================================================

THE BIG CHALLENGE: Take one of your favourite Scratch
projects and rebuild it in Python using turtle!

This is YOUR project. Use everything you have learned:
  - turtle graphics for drawing
  - loops for repetition
  - functions for organisation
  - conditionals for decisions
  - variables for tracking things

Choose ONE option below and complete the template.
When you finish, you have earned 50 XP and the
Visual Coder badge!

===================================================
  OPTIONS:
    A. Animated Story
    B. Mini Game
    C. Interactive Art
===================================================
"""

import turtle
import random
import time
import math


# ==================================================
# READ BEFORE YOU START
# ==================================================
#
# CHECKLIST - Your project MUST include all of these:
#
#   [ ] At least ONE function you defined with def
#   [ ] At least ONE loop (for or while)
#   [ ] At least ONE if statement
#   [ ] turtle graphics (drawing something visual)
#   [ ] At least ONE variable that changes during the program
#   [ ] A title displayed on the screen
#
# Pick your option and fill in the template.
# You can use code from previous lessons as a starting point!
# ==================================================


# ==================================================
# YOUR CHOICE: Comment out the two options you are
# NOT doing, and fill in the one you picked!
# ==================================================

MY_OPTION = "B"   # Change to "A", "B", or "C"


# ==================================================
# OPTION A: ANIMATED STORY
# ==================================================
# Tell a short animated story with 3 scenes.
# Each scene uses turtle to draw characters/backgrounds.
# Text explains what is happening.
#
# EXAMPLE STORY IDEAS:
#   - A turtle goes on an adventure
#   - A rocket launches to space
#   - A seed grows into a flower
#
# REQUIREMENTS for Option A:
#   [ ] 3 distinct scenes (clear screen between each)
#   [ ] At least one character drawn with turtle shapes
#   [ ] Text narrating each scene (turtle.write)
#   [ ] At least one animation (something that moves)
#   [ ] A title screen at the start
#
# HOW TO USE THIS TEMPLATE:
#   1. Think of your story
#   2. Fill in scene_1, scene_2, scene_3
#   3. Add characters in draw_character
#   4. Fill in the title screen

def option_a_story() -> None:
    """
    OPTION A: Tell an animated story in 3 scenes.
    Fill in the functions below to tell YOUR story!
    """
    screen = turtle.Screen()
    screen.title("My Animated Story!")      # TODO: Change to your story title
    screen.setup(700, 550)
    screen.tracer(0)

    pen = turtle.Turtle()
    pen.hideturtle()
    pen.penup()
    pen.speed(0)

    narrator = turtle.Turtle()
    narrator.hideturtle()
    narrator.penup()
    narrator.speed(0)

    def clear_scene() -> None:
        """Clear screen between scenes."""
        pen.clear()
        narrator.clear()
        screen.update()
        time.sleep(0.3)

    def write_narration(text: str, y: float = -220) -> None:
        """
        Write narration text at the bottom of screen.

        Args:
            text: The narration text to display.
            y: Vertical position for the text.
        """
        narrator.clear()
        narrator.goto(-300, y)
        narrator.color("white")
        narrator.write(text, font=("Arial", 14, "italic"))
        screen.update()

    # --------------------------------------------------
    # TODO: TITLE SCREEN
    # --------------------------------------------------
    # Draw a title screen before the story begins.
    # HINTS:
    #   - Set the background colour with screen.bgcolor()
    #   - Write your title with pen.write() at position (0, 50)
    #   - Write "A story by [your name]" below it
    #   - Wait 2 seconds, then clear and start Scene 1

    def title_screen() -> None:
        """Display the story title."""
        screen.bgcolor("black")   # TODO: Change to your preferred colour

        # TODO: Write your story title
        pen.goto(0, 50)
        pen.color("gold")
        pen.write(
            "My Story Title",     # TODO: Change to your title!
            font=("Arial", 32, "bold"),
            align="center",
        )

        # TODO: Write your name
        pen.goto(0, -20)
        pen.color("white")
        pen.write(
            "A story by Me",      # TODO: Change to your name!
            font=("Arial", 16, "normal"),
            align="center",
        )

        screen.update()
        time.sleep(2.5)
        clear_scene()

    # --------------------------------------------------
    # TODO: SCENE 1
    # --------------------------------------------------
    # Draw your first scene here.
    # Ideas: Introduce the main character, show where they are.

    def scene_1() -> None:
        """Scene 1: The beginning of the story."""
        screen.bgcolor("#87ceeb")   # TODO: Change to match your scene

        # TODO: Draw your scene!
        # Examples:
        #   - Draw a background (ground, sky, buildings)
        #   - Draw your main character
        #   - Write the narration

        # EXAMPLE (replace with your own code):
        # Draw ground
        pen.goto(-350, -150)
        pen.color("#228B22")
        pen.begin_fill()
        pen.fillcolor("#228B22")
        pen.pendown()
        for _ in range(2):
            pen.forward(700)
            pen.left(90)
            pen.forward(100)
            pen.left(90)
        pen.end_fill()
        pen.penup()

        # TODO: Add more to this scene!

        write_narration("Scene 1: Your story begins here...")   # TODO: Your narration
        time.sleep(3)
        clear_scene()

    # --------------------------------------------------
    # TODO: SCENE 2
    # --------------------------------------------------

    def scene_2() -> None:
        """Scene 2: Something happens!"""
        screen.bgcolor("#001133")   # TODO: Change for your scene

        # TODO: Draw your second scene!
        # This is where the action or problem happens.

        write_narration("Scene 2: Something exciting happens!")   # TODO: Your narration
        time.sleep(3)
        clear_scene()

    # --------------------------------------------------
    # TODO: SCENE 3
    # --------------------------------------------------

    def scene_3() -> None:
        """Scene 3: The ending."""
        screen.bgcolor("#ffd700")   # TODO: Change for your scene

        # TODO: Draw your third scene!
        # This is the resolution - how does the story end?

        write_narration("Scene 3: And they all lived happily ever after!")   # TODO: Your ending
        time.sleep(3)
        clear_scene()

    # --------------------------------------------------
    # THE END SCREEN
    # --------------------------------------------------
    def end_screen() -> None:
        """Show the end credits."""
        screen.bgcolor("black")
        pen.goto(0, 30)
        pen.color("gold")
        pen.write("THE END", font=("Arial", 40, "bold"), align="center")
        pen.goto(0, -40)
        pen.color("white")
        pen.write("Thanks for watching!", font=("Arial", 18, "normal"), align="center")
        screen.update()

    # Run the story!
    title_screen()
    scene_1()
    scene_2()
    scene_3()
    end_screen()
    screen.update()
    turtle.done()


# ==================================================
# OPTION B: MINI GAME
# ==================================================
# Build a complete mini game with:
#   - A player the user controls
#   - Something to do (collect, avoid, reach a goal)
#   - A score that changes
#   - A win or game over condition
#
# EXAMPLE GAME IDEAS:
#   - Dodge the falling rocks
#   - Eat the apples (avoid the red ones!)
#   - Reach the treasure chest
#   - Pong (bounce a ball with a paddle)
#
# REQUIREMENTS for Option B:
#   [ ] Player that moves with keyboard input
#   [ ] Something that changes position automatically
#   [ ] Score tracking (show it on screen)
#   [ ] Win or game over condition
#   [ ] Game loop (while not game_over:)

def option_b_game() -> None:
    """
    OPTION B: Build your mini game here!
    Use this template as a starting point.
    """
    # --------------------------------------------------
    # SETUP
    # --------------------------------------------------
    screen = turtle.Screen()
    screen.title("My Mini Game!")           # TODO: Your game title
    screen.bgcolor("#0f0e17")               # TODO: Your background colour
    screen.setup(700, 600)
    screen.tracer(0)

    # --------------------------------------------------
    # GAME STATE VARIABLES
    # TODO: Add/change these to match your game!
    # --------------------------------------------------
    player_x: float = 0.0
    player_y: float = -240.0
    score: int = 0
    lives: int = 3
    game_over: bool = False

    # TODO: Add variables for your "thing to catch/avoid"
    # Example: enemy_x = 0.0, enemy_y = 200.0, enemy_speed = 3.0

    # --------------------------------------------------
    # DRAWING TURTLES
    # --------------------------------------------------
    player_t = turtle.Turtle()
    player_t.hideturtle()
    player_t.penup()
    player_t.speed(0)

    obj_t = turtle.Turtle()       # The object to catch/avoid
    obj_t.hideturtle()
    obj_t.penup()
    obj_t.speed(0)

    hud_t = turtle.Turtle()
    hud_t.hideturtle()
    hud_t.penup()
    hud_t.speed(0)

    # --------------------------------------------------
    # TODO: DRAWING FUNCTIONS
    # --------------------------------------------------

    def draw_player(x: float, y: float) -> None:
        """Draw the player at position (x, y)."""
        player_t.clear()
        player_t.goto(x, y)
        # TODO: Draw your player here!
        # Could be a coloured dot, a shape, a turtle shape, etc.
        player_t.color("dodgerblue")     # TODO: Change colour
        player_t.dot(30)                 # TODO: Change this to your design

    def draw_object(x: float, y: float) -> None:
        """Draw the game object (thing to catch or avoid)."""
        obj_t.clear()
        obj_t.goto(x, y)
        # TODO: Draw what the player catches or avoids
        obj_t.color("gold")              # TODO: Change colour
        obj_t.dot(20)                    # TODO: Change this

    def draw_hud_info() -> None:
        """Display score and lives."""
        hud_t.clear()
        hud_t.goto(-330, 260)
        hud_t.color("white")
        hud_t.write(f"Score: {score}", font=("Arial", 16, "bold"))
        hud_t.goto(150, 260)
        hud_t.color("#FF6B6B")
        hud_t.write(f"Lives: {'* ' * lives}", font=("Arial", 16, "bold"))

    def draw_game_over_screen() -> None:
        """Show the game over screen."""
        hud_t.clear()
        player_t.clear()
        obj_t.clear()
        hud_t.goto(0, 50)
        hud_t.color("#FF6B6B")
        hud_t.write("GAME OVER!", font=("Arial", 36, "bold"), align="center")
        hud_t.goto(0, -30)
        hud_t.color("gold")
        hud_t.write(f"Final Score: {score}", font=("Arial", 22, "bold"), align="center")
        screen.update()

    # --------------------------------------------------
    # TODO: KEYBOARD CONTROLS
    # --------------------------------------------------
    PLAYER_SPEED = 20

    def move_left() -> None:
        nonlocal player_x
        # TODO: Move player left, check boundary
        player_x -= PLAYER_SPEED
        if player_x < -330:
            player_x = -330

    def move_right() -> None:
        nonlocal player_x
        # TODO: Move player right, check boundary
        player_x += PLAYER_SPEED
        if player_x > 330:
            player_x = 330

    # TODO: Add more controls if your game needs them!
    # def move_up() -> None: ...
    # def move_down() -> None: ...

    screen.listen()
    screen.onkey(move_left,  "Left")
    screen.onkey(move_right, "Right")
    # screen.onkey(move_up, "Up")       # Uncomment if needed
    # screen.onkey(move_down, "Down")   # Uncomment if needed

    # --------------------------------------------------
    # TODO: GAME OBJECT VARIABLES
    # --------------------------------------------------
    # Add variables for whatever falls, moves, or needs to be collected.
    obj_x: float = random.randint(-300, 300)
    obj_y: float = 250.0
    obj_speed: float = 4.0

    def reset_object() -> None:
        """Reset the object to a new random position at the top."""
        nonlocal obj_x, obj_y
        obj_x = random.randint(-300, 300)
        obj_y = 250.0

    # --------------------------------------------------
    # THE GAME LOOP
    # TODO: Update this logic to match your game!
    # --------------------------------------------------
    print("Game starting!")
    print("Use LEFT and RIGHT arrow keys.")

    while not game_over:

        # TODO: Move your game object
        obj_y -= obj_speed    # Move down (or change direction for your game)

        # TODO: CHECK COLLISION (did player catch/hit the object?)
        # Example collision check:
        distance = math.sqrt((player_x - obj_x) ** 2 + (player_y - obj_y) ** 2)
        if distance < 30:
            # TODO: What happens when player touches the object?
            # Example: score += 1, reset object
            score += 1
            reset_object()
            # Speed up every 5 catches:
            if score % 5 == 0:
                obj_speed += 0.5

        # TODO: CHECK if object goes off screen (miss/hit boundary)
        elif obj_y < -300:
            # TODO: What happens when the object goes off screen?
            # Example: lose a life, reset object
            lives -= 1
            reset_object()
            if lives <= 0:
                game_over = True

        # TODO: DRAW everything
        draw_player(player_x, player_y)
        draw_object(obj_x, obj_y)
        draw_hud_info()

        screen.update()
        time.sleep(0.016)

    # Game over
    draw_game_over_screen()
    print(f"Game over! Final score: {score}")
    screen.mainloop()


# ==================================================
# OPTION C: INTERACTIVE ART
# ==================================================
# Create art that responds to the mouse and keyboard!
# The user's actions change what gets drawn.
#
# EXAMPLE IDEAS:
#   - Click to place flowers, stars, or fireworks
#   - Move mouse to control a drawing brush
#   - Press keys to change the pattern being drawn
#   - Create a "screensaver" that responds to clicks
#
# REQUIREMENTS for Option C:
#   [ ] At least ONE mouse interaction (click or drag)
#   [ ] At least ONE keyboard interaction (key press)
#   [ ] At least TWO different visual elements
#   [ ] Something changes over time (colours, size, etc.)
#   [ ] A variable that tracks the user's interactions

def option_c_interactive_art() -> None:
    """
    OPTION C: Create interactive art here!
    """
    screen = turtle.Screen()
    screen.title("My Interactive Art!")   # TODO: Your title
    screen.bgcolor("black")              # TODO: Your background
    screen.setup(750, 650)
    screen.tracer(0)

    art_pen = turtle.Turtle()
    art_pen.hideturtle()
    art_pen.penup()
    art_pen.speed(0)

    info_pen = turtle.Turtle()
    info_pen.hideturtle()
    info_pen.penup()
    info_pen.speed(0)

    # --------------------------------------------------
    # APP STATE
    # TODO: Add variables for your art app!
    # --------------------------------------------------
    click_count: int = 0
    current_style: str = "star"    # TODO: What gets drawn on click

    # A list of colours to cycle through
    art_colours = ["red", "orange", "gold", "limegreen",
                   "cyan", "dodgerblue", "violet", "hotpink"]
    colour_index: int = 0

    def get_next_colour() -> str:
        nonlocal colour_index
        colour = art_colours[colour_index % len(art_colours)]
        colour_index += 1
        return colour

    # --------------------------------------------------
    # TODO: DRAWING FUNCTIONS
    # --------------------------------------------------
    # Define functions that draw your art elements.
    # These get called when the user interacts.

    def draw_star_burst(x: float, y: float, size: int, colour: str) -> None:
        """
        Draw a small star at position (x, y).

        Args:
            x: Horizontal position.
            y: Vertical position.
            size: Size of the star.
            colour: Fill colour.
        """
        art_pen.goto(x, y)
        art_pen.setheading(90)
        art_pen.color(colour)
        art_pen.begin_fill()
        # TODO: Make this draw a real star shape, or your own design!
        for _ in range(5):
            art_pen.forward(size)
            art_pen.right(144)
        art_pen.end_fill()

    # TODO: Add more drawing functions here!
    # Ideas: draw_flower(), draw_firework(), draw_spiral(), etc.

    def draw_info_bar() -> None:
        """Show info about the current art mode."""
        info_pen.clear()
        info_pen.goto(-360, 290)
        info_pen.color("white")
        info_pen.write(
            f"Clicks: {click_count}  |  Style: {current_style.upper()}  |  Keys: 1=Star  C=Clear",
            font=("Arial", 12, "normal"),
        )
        screen.update()

    # --------------------------------------------------
    # TODO: INTERACTION HANDLERS
    # --------------------------------------------------

    def on_click(x: float, y: float) -> None:
        """Called when user clicks. Draw art at that position."""
        nonlocal click_count
        if y > 280:    # Ignore clicks on toolbar
            return

        click_count += 1
        colour = get_next_colour()
        size = random.randint(15, 45)

        # TODO: Call your drawing function based on current_style
        if current_style == "star":
            draw_star_burst(x, y, size, colour)
        # TODO: Add more styles here!
        # elif current_style == "flower":
        #     draw_flower(x, y, size, colour)

        draw_info_bar()

    def switch_to_star() -> None:
        """Switch drawing style to star."""
        nonlocal current_style
        current_style = "star"
        draw_info_bar()

    # TODO: Add more style switchers and key bindings!

    def clear_art() -> None:
        """Clear all drawings."""
        art_pen.clear()
        draw_info_bar()

    # Register events
    screen.onclick(on_click)
    screen.listen()
    screen.onkey(switch_to_star, "1")
    screen.onkey(clear_art, "c")
    # TODO: Add more key bindings for your styles!

    # Welcome message
    art_pen.goto(0, 10)
    art_pen.color("white")
    art_pen.write(
        "Click anywhere to create art!",
        font=("Arial", 18, "normal"),
        align="center",
    )
    art_pen.goto(0, -30)
    art_pen.color("#888888")
    art_pen.write(
        "Press 1 = Star  |  C = Clear",
        font=("Arial", 13, "normal"),
        align="center",
    )
    draw_info_bar()

    print("Interactive Art started! Click to create!")
    screen.mainloop()


# ==================================================
# MAIN: Run your chosen option
# ==================================================

def main() -> None:
    """Run the selected challenge option."""
    print("=" * 55)
    print("  MODULE 0 FINAL CHALLENGE!")
    print("=" * 55)
    print()
    print(f"  Running Option {MY_OPTION}")
    print()

    if MY_OPTION == "A":
        print("  Building: Animated Story")
        print("  Fill in the scene functions to tell your story!")
        print()
        option_a_story()

    elif MY_OPTION == "B":
        print("  Building: Mini Game")
        print("  Complete the game logic in option_b_game()!")
        print()
        option_b_game()

    elif MY_OPTION == "C":
        print("  Building: Interactive Art")
        print("  Add your drawing functions and styles!")
        print()
        option_c_interactive_art()

    else:
        print(f"  Unknown option '{MY_OPTION}'. Set MY_OPTION to 'A', 'B', or 'C'.")


# ==================================================
# COMPLETION CHECKLIST
# ==================================================
# Before you say you are done, check these off!
#
#   [ ] I defined at least ONE function with def
#   [ ] I used at least ONE loop (for or while)
#   [ ] I used at least ONE if statement
#   [ ] I used turtle graphics to draw something
#   [ ] I have at least ONE variable that changes
#   [ ] A title is shown somewhere on screen
#   [ ] I ran the file and it works without errors
#   [ ] I am proud of what I built!
#
# If all boxes are checked: YOU EARNED 50 XP!
# Congratulations, Visual Coder!
# ==================================================


if __name__ == "__main__":
    main()

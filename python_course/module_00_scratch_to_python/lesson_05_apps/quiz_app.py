"""
===================================================
  Lesson 5: Python Quiz App!
  Module 0 - From Scratch to Python!
===================================================

A graphical quiz about Python!

HOW IT WORKS:
  - A question appears on screen
  - 4 answer buttons are drawn as coloured rectangles
  - Click an answer to submit it
  - Green = correct! Red = wrong!
  - After 5 questions, see your final score!

This shows how to build a real interactive app with turtle.
"""

import turtle
import time


# ==================================================
# QUIZ DATA
# Each question has: text, 4 options, correct answer index (0-3)
# ==================================================
QUESTIONS: list[dict] = [
    {
        "question": "What does print('Hello') do in Python?",
        "options": [
            "A. Prints Hello on paper",
            "B. Shows Hello on screen",
            "C. Saves Hello to a file",
            "D. Nothing happens",
        ],
        "answer": 1,   # B is correct (index 1)
        "explanation": "print() shows text on the screen - just like Scratch's 'say' block!",
    },
    {
        "question": "Which Python module lets you draw graphics?",
        "options": [
            "A. math",
            "B. random",
            "C. turtle",
            "D. time",
        ],
        "answer": 2,   # C is correct (index 2)
        "explanation": "The turtle module lets you draw shapes and pictures - like Scratch's pen!",
    },
    {
        "question": "What does turtle.forward(100) do?",
        "options": [
            "A. Makes the turtle go 100 times faster",
            "B. Moves the turtle backward 100 pixels",
            "C. Draws a circle of size 100",
            "D. Moves the turtle forward 100 pixels",
        ],
        "answer": 3,   # D is correct (index 3)
        "explanation": "forward(100) moves the turtle forward 100 pixels, drawing a line!",
    },
    {
        "question": "How do you repeat something 10 times in Python?",
        "options": [
            "A. repeat 10:",
            "B. for i in range(10):",
            "C. loop(10):",
            "D. while 10:",
        ],
        "answer": 1,   # B is correct (index 1)
        "explanation": "for i in range(10): is exactly like Scratch's 'repeat 10' block!",
    },
    {
        "question": "What Scratch block is most like Python's 'while True:'?",
        "options": [
            "A. repeat 10",
            "B. if ... then",
            "C. forever",
            "D. wait 1 secs",
        ],
        "answer": 2,   # C is correct (index 2)
        "explanation": "'while True:' loops forever - just like Scratch's 'forever' block!",
    },
]

# ==================================================
# BUTTON LAYOUT
# 4 answer buttons arranged in a 2x2 grid
# ==================================================
BUTTON_POSITIONS = [
    (-290, 50),    # A: top left
    (10,   50),    # B: top right
    (-290, -60),   # C: bottom left
    (10,   -60),   # D: bottom right
]
BUTTON_WIDTH = 270
BUTTON_HEIGHT = 80

BUTTON_COLOURS = [
    "#3d5a80",   # A: dark blue
    "#5e60ce",   # B: purple-blue
    "#4ea8de",   # C: medium blue
    "#48cae4",   # D: light blue
]


# ==================================================
# SETUP
# ==================================================
screen = turtle.Screen()
screen.title("Python Quiz App!")
screen.bgcolor("#0f0e17")
screen.setup(width=620, height=500)
screen.tracer(0)


# Drawing turtles
bg_t = turtle.Turtle()         # Background and buttons
text_t = turtle.Turtle()       # Question and option text
feedback_t = turtle.Turtle()   # Correct/wrong feedback

for t_obj in [bg_t, text_t, feedback_t]:
    t_obj.hideturtle()
    t_obj.penup()
    t_obj.speed(0)


# ==================================================
# QUIZ STATE
# ==================================================
current_question: int = 0
score: int = 0
waiting_for_next: bool = False


# ==================================================
# DRAWING FUNCTIONS
# ==================================================

def draw_button(x: float, y: float, colour: str, label: str) -> None:
    """
    Draws one answer button as a filled rectangle.

    Args:
        x: Left edge x position.
        y: Bottom edge y position.
        colour: Fill colour.
        label: The text to show (e.g. "A. Paris").
    """
    # Draw filled rectangle
    bg_t.goto(x, y)
    bg_t.color(colour)
    bg_t.begin_fill()
    bg_t.fillcolor(colour)
    bg_t.pendown()
    for _ in range(2):
        bg_t.forward(BUTTON_WIDTH)
        bg_t.left(90)
        bg_t.forward(BUTTON_HEIGHT)
        bg_t.left(90)
    bg_t.end_fill()
    bg_t.penup()

    # Draw button text
    text_t.goto(x + 10, y + BUTTON_HEIGHT // 2 - 10)
    text_t.color("white")
    # Wrap long text
    display_text = label if len(label) < 32 else label[:30] + "..."
    text_t.write(display_text, font=("Arial", 12, "normal"))


def draw_question(q_text: str, q_num: int, total: int) -> None:
    """
    Draws the question text at the top of the screen.

    Args:
        q_text: The question string.
        q_num: Current question number (1-based).
        total: Total number of questions.
    """
    # Question number
    text_t.goto(-290, 210)
    text_t.color("#aaaaaa")
    text_t.write(
        f"Question {q_num} of {total}  |  Score: {score}",
        font=("Arial", 13, "normal"),
    )

    # Question text (word-wrap manually for long questions)
    text_t.goto(-290, 165)
    text_t.color("white")
    text_t.write(q_text, font=("Arial", 14, "bold"))


def draw_all_buttons(options: list[str], highlight: int = -1,
                     correct: int = -1) -> None:
    """
    Draws all 4 answer buttons.

    Args:
        options: List of 4 option strings.
        highlight: Index of button to highlight red (wrong answer).
        correct: Index of button to highlight green (correct answer).
    """
    bg_t.clear()

    for i, (option, pos) in enumerate(zip(options, BUTTON_POSITIONS)):
        colour = BUTTON_COLOURS[i]

        if i == correct:
            colour = "#2dc653"      # Green for correct
        elif i == highlight:
            colour = "#e63946"      # Red for wrong

        draw_button(pos[0], pos[1], colour, option)


def draw_score_screen() -> None:
    """Draws the final score screen."""
    bg_t.clear()
    text_t.clear()
    feedback_t.clear()

    # Background
    bg_t.goto(-300, -250)
    bg_t.color("#1a1a2e")
    bg_t.begin_fill()
    bg_t.fillcolor("#1a1a2e")
    bg_t.pendown()
    for _ in range(2):
        bg_t.forward(600)
        bg_t.left(90)
        bg_t.forward(500)
        bg_t.left(90)
    bg_t.end_fill()
    bg_t.penup()

    total = len(QUESTIONS)
    percentage = int((score / total) * 100)

    # Title
    text_t.goto(-170, 120)
    text_t.color("gold")
    text_t.write("Quiz Complete!", font=("Arial", 30, "bold"))

    # Score
    text_t.goto(-200, 40)
    text_t.color("white")
    text_t.write(f"You scored {score} out of {total}", font=("Arial", 22, "normal"))

    # Percentage and message
    text_t.goto(-160, -20)
    if percentage == 100:
        msg = "PERFECT SCORE! You are amazing!"
        colour = "gold"
    elif percentage >= 80:
        msg = "Excellent work! You really know Python!"
        colour = "#6BCB77"
    elif percentage >= 60:
        msg = "Good job! Keep practising!"
        colour = "#4D96FF"
    else:
        msg = "Keep learning - you are getting there!"
        colour = "#FFD93D"

    text_t.color(colour)
    text_t.write(msg, font=("Arial", 14, "bold"))

    # Stars based on score
    text_t.goto(-80, -80)
    text_t.color("gold")
    stars = "*" * score + " " * (total - score)
    text_t.write(f"Stars: {stars}", font=("Arial", 20, "bold"))

    text_t.goto(-170, -140)
    text_t.color("#888888")
    text_t.write("Close window to exit", font=("Arial", 12, "normal"))


# ==================================================
# QUIZ LOGIC
# ==================================================

def show_question(q_index: int) -> None:
    """Display a question and its options."""
    text_t.clear()
    feedback_t.clear()

    q = QUESTIONS[q_index]
    draw_question(q["question"], q_index + 1, len(QUESTIONS))
    draw_all_buttons(q["options"])
    screen.update()


def on_answer_click(x: float, y: float) -> None:
    """
    Called when player clicks anywhere on the screen.
    Determines which button was clicked.
    """
    global score, current_question, waiting_for_next

    if waiting_for_next:
        return                     # Ignore clicks during feedback pause

    # Figure out which button was clicked (if any)
    clicked_button = -1
    for i, (bx, by) in enumerate(BUTTON_POSITIONS):
        if bx <= x <= bx + BUTTON_WIDTH and by <= y <= by + BUTTON_HEIGHT:
            clicked_button = i
            break

    if clicked_button == -1:
        return                     # Didn't click any button

    waiting_for_next = True
    q = QUESTIONS[current_question]
    correct_index = q["answer"]
    is_correct = (clicked_button == correct_index)

    if is_correct:
        score += 1

    # Show feedback colours
    draw_all_buttons(
        q["options"],
        highlight=clicked_button if not is_correct else -1,
        correct=correct_index,
    )

    # Show feedback text
    feedback_t.clear()
    feedback_t.goto(-290, -165)
    if is_correct:
        feedback_t.color("#2dc653")
        feedback_t.write(
            "Correct! Well done!",
            font=("Arial", 14, "bold"),
        )
    else:
        feedback_t.color("#e63946")
        feedback_t.write(
            "Not quite - the green answer is correct.",
            font=("Arial", 13, "normal"),
        )

    feedback_t.goto(-290, -195)
    feedback_t.color("#aaaaaa")
    feedback_t.write(q["explanation"], font=("Arial", 11, "italic"))

    screen.update()

    # Pause, then move to next question
    screen.ontimer(advance_question, 2200)


def advance_question() -> None:
    """Move to the next question or show the final score."""
    global current_question, waiting_for_next

    waiting_for_next = False
    current_question += 1

    if current_question >= len(QUESTIONS):
        draw_score_screen()
        screen.update()
        screen.onclick(None)       # Disable further clicks
    else:
        show_question(current_question)


# ==================================================
# MAIN
# ==================================================

def main() -> None:
    """Starts the quiz app."""
    print("Python Quiz App!")
    print("Click on the correct answer.")
    print()

    # Draw title screen briefly
    text_t.goto(-150, 80)
    text_t.color("gold")
    text_t.write("Python Quiz!", font=("Arial", 32, "bold"))
    text_t.goto(-180, 10)
    text_t.color("white")
    text_t.write("5 questions about Python", font=("Arial", 16, "normal"))
    text_t.goto(-140, -40)
    text_t.color("#aaaaaa")
    text_t.write("Loading in 2 seconds...", font=("Arial", 13, "normal"))
    screen.update()

    # Brief pause, then start
    screen.ontimer(lambda: (text_t.clear(), show_question(0)), 2000)

    # Register click handler
    screen.onclick(on_answer_click)

    screen.mainloop()


if __name__ == "__main__":
    main()

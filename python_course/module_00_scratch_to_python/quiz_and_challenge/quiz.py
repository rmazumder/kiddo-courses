"""
===================================================
  Module 0 Quiz: From Scratch to Python!
  Module 0 - From Scratch to Python!
===================================================

5 questions to test what you have learned!

Answer each question by typing a letter (a, b, c, or d)
then pressing Enter.

Get 4 or more right to pass and earn 20 XP!
"""

import time


# ==================================================
# QUIZ QUESTIONS
# ==================================================
QUESTIONS: list[dict] = [
    {
        "number": 1,
        "question": (
            "What is the Python equivalent of Scratch's 'say Hello' block?"
        ),
        "options": {
            "a": "input('Hello')",
            "b": "print('Hello')",
            "c": "say('Hello')",
            "d": "show('Hello')",
        },
        "answer": "b",
        "explanation": (
            "print('Hello') shows text on the screen - "
            "just like Scratch's 'say' block shows a speech bubble!"
        ),
    },
    {
        "number": 2,
        "question": (
            "Which Python module lets you draw graphics like Scratch's pen?"
        ),
        "options": {
            "a": "graphics",
            "b": "draw",
            "c": "turtle",
            "d": "paint",
        },
        "answer": "c",
        "explanation": (
            "The turtle module is Python's built-in drawing tool. "
            "It works just like Scratch's pen blocks - "
            "put the pen down and move to draw lines!"
        ),
    },
    {
        "number": 3,
        "question": "What does turtle.forward(100) do?",
        "options": {
            "a": "Makes the turtle 100 times faster",
            "b": "Draws a circle with a radius of 100",
            "c": "Moves the turtle backward 100 pixels",
            "d": "Moves the turtle forward 100 pixels, drawing a line",
        },
        "answer": "d",
        "explanation": (
            "forward(100) moves the turtle forward by 100 pixels "
            "and draws a line along the way. "
            "Like Scratch's 'move 100 steps'!"
        ),
    },
    {
        "number": 4,
        "question": (
            "How do you make something happen repeatedly in Python?"
        ),
        "options": {
            "a": "repeat(10):",
            "b": "loop 10 times:",
            "c": "for i in range(10):",
            "d": "do 10:",
        },
        "answer": "c",
        "explanation": (
            "for i in range(10): is the Python repeat loop! "
            "It is exactly like Scratch's 'repeat 10' block. "
            "The code inside runs 10 times."
        ),
    },
    {
        "number": 5,
        "question": (
            "What Scratch block is most similar to Python's 'while True:'?"
        ),
        "options": {
            "a": "repeat 10",
            "b": "wait 1 secs",
            "c": "if ... then",
            "d": "forever",
        },
        "answer": "d",
        "explanation": (
            "'while True:' loops forever without stopping - "
            "exactly like Scratch's 'forever' block! "
            "Both are used for the main game loop."
        ),
    },
]

PASS_SCORE = 4   # Need at least 4 out of 5 to pass


# ==================================================
# QUIZ RUNNER
# ==================================================

def print_separator(char: str = "-", width: int = 55) -> None:
    """Prints a line of repeated characters."""
    print(char * width)


def ask_question(q: dict) -> bool:
    """
    Asks one quiz question and returns True if correct.

    Args:
        q: The question dictionary.

    Returns:
        True if the player answered correctly, False otherwise.
    """
    print()
    print_separator()
    print(f"  Question {q['number']} of {len(QUESTIONS)}")
    print_separator()
    print()
    print(f"  {q['question']}")
    print()

    for letter, text in q["options"].items():
        print(f"    {letter.upper()}.  {text}")

    print()

    # Get a valid answer
    while True:
        answer = input("  Your answer (a/b/c/d): ").strip().lower()
        if answer in ("a", "b", "c", "d"):
            break
        print("  Please type a, b, c, or d and press Enter.")

    # Check the answer
    if answer == q["answer"]:
        print()
        print("  CORRECT! Great job!")
        print(f"  {q['explanation']}")
        return True
    else:
        correct_letter = q["answer"].upper()
        correct_text = q["options"][q["answer"]]
        print()
        print(f"  Not quite. The correct answer was {correct_letter}: {correct_text}")
        print(f"  {q['explanation']}")
        return False


def show_results(score: int, total: int) -> None:
    """Displays the final quiz results."""
    print()
    print_separator("=")
    print()
    print(f"  QUIZ COMPLETE!")
    print()
    print(f"  Your score: {score} out of {total}")

    percentage = int((score / total) * 100)
    print(f"  That is {percentage}%!")
    print()

    if score == total:
        print("  PERFECT SCORE! You absolutely nailed it!")
        print("  You have totally mastered Scratch to Python!")
        xp = 20
    elif score >= PASS_SCORE:
        print("  PASSED! Excellent work!")
        print("  You understand the Scratch-to-Python bridge!")
        xp = 20
    elif score == total - 1:
        print("  So close! One more right and you would have passed.")
        print("  Review the lessons and try again!")
        xp = 10
    else:
        print("  Keep learning! Go back and review the lessons,")
        print("  then try the quiz again.")
        xp = 0

    print()
    if xp > 0:
        print(f"  XP EARNED: +{xp} XP!")
    print()

    # Show a star rating
    stars_earned = score
    stars_empty = total - score
    star_display = "* " * stars_earned + ". " * stars_empty
    print(f"  Rating: {star_display.strip()}")
    print()
    print_separator("=")
    print()

    if score >= PASS_SCORE:
        print("  Move on to the Final Challenge to earn 50 more XP!")
    else:
        print("  Tip: Re-read the lesson READMEs and run the example files.")
        print("  Then come back and try the quiz again!")


# ==================================================
# MAIN
# ==================================================

def main() -> None:
    """Runs the full quiz."""
    print()
    print_separator("=")
    print()
    print("  MODULE 0 QUIZ: From Scratch to Python!")
    print()
    print("  5 questions. You need 4/5 to pass.")
    print("  Type a letter and press Enter for each answer.")
    print()
    print_separator("=")

    input("\n  Press Enter when you are ready to start...")

    score = 0
    for question in QUESTIONS:
        correct = ask_question(question)
        if correct:
            score += 1
        time.sleep(0.5)   # Brief pause between questions

    show_results(score, len(QUESTIONS))


if __name__ == "__main__":
    main()

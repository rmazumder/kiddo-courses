"""
==============================================
  MODULE 1 QUIZ: Welcome to Python!
  Earn 20 XP by answering these questions!
==============================================

Run this file and answer the questions.
Type the letter of your answer (a, b, or c).
"""

import time


def ask_question(number, question, options, correct_answer):
    """Ask a quiz question and check the answer."""
    print(f"\nQuestion {number}: {question}")
    for option in options:
        print(f"  {option}")

    answer = input("Your answer (a/b/c): ").strip().lower()

    if answer == correct_answer:
        print("Correct! Great job!")
        return True
    else:
        print(f"Not quite! The correct answer was: {correct_answer}")
        return False


def main():
    print("=" * 50)
    print("  MODULE 1 QUIZ: Welcome to Python!")
    print("=" * 50)
    print()
    print("Answer 3 questions to earn 20 XP!")
    print("Let's see what you learned!")

    score = 0

    # Question 1
    if ask_question(
        1,
        "What is a program?",
        [
            "a) A TV show about computers",
            "b) A set of instructions that tells a computer what to do",
            "c) A type of video game",
        ],
        "b"
    ):
        score += 1

    # Question 2
    if ask_question(
        2,
        "Which function do we use to show text on the screen?",
        [
            "a) show()",
            "b) display()",
            "c) print()",
        ],
        "c"
    ):
        score += 1

    # Question 3
    if ask_question(
        3,
        "What must go around text when you use print()?",
        [
            "a) Parentheses and quotation marks",
            "b) Square brackets",
            "c) Curly braces",
        ],
        "a"
    ):
        score += 1

    # Results
    print()
    print("=" * 50)
    print(f"  QUIZ RESULTS: {score}/3 correct!")
    print("=" * 50)

    if score == 3:
        print("  PERFECT SCORE! You are a natural!")
        print("  +20 XP earned!")
    elif score == 2:
        print("  Great job! Almost perfect!")
        print("  +20 XP earned!")
    elif score == 1:
        print("  Good try! Review the lessons and try again.")
        print("  +10 XP earned for trying!")
    else:
        print("  No worries! Go back and review the lessons,")
        print("  then come back and try the quiz again.")
        print("  +5 XP earned for trying!")

    print()
    print("Next up: Complete the Module 1 Challenge!")
    print("Open challenge.py to earn your badge!")


if __name__ == "__main__":
    main()

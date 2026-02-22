"""
==============================================
  MODULE 2 QUIZ: Variables & Data Types
  Earn 20 XP!
==============================================
"""


def ask_question(number, question, options, correct):
    print(f"\nQuestion {number}: {question}")
    for opt in options:
        print(f"  {opt}")
    answer = input("Your answer (a/b/c): ").strip().lower()
    if answer == correct:
        print("Correct!")
        return True
    else:
        print(f"Not quite! The answer was: {correct}")
        return False


def main():
    print("=" * 50)
    print("  MODULE 2 QUIZ: Variables & Data Types")
    print("=" * 50)

    score = 0

    if ask_question(1,
        "What symbol do we use to put a value INTO a variable?",
        ["a) ==", "b) =", "c) ->"],
        "b"
    ):
        score += 1

    if ask_question(2,
        "What type of data is 3.14?",
        ["a) integer (int)", "b) string (str)", "c) float"],
        "c"
    ):
        score += 1

    if ask_question(3,
        'What does len("hello") return?',
        ["a) 5", "b) 4", "c) hello"],
        "a"
    ):
        score += 1

    if ask_question(4,
        "What are the two possible values of a boolean?",
        ["a) Yes and No", "b) True and False", "c) 0 and 1"],
        "b"
    ):
        score += 1

    if ask_question(5,
        "What does the == operator do?",
        ["a) Assigns a value", "b) Adds two numbers", "c) Checks if two things are equal"],
        "c"
    ):
        score += 1

    print()
    print("=" * 50)
    print(f"  RESULTS: {score}/5 correct!")
    if score >= 4:
        print("  Amazing! +20 XP!")
    elif score >= 3:
        print("  Good job! +20 XP!")
    else:
        print("  Review the lessons and try again! +10 XP for trying!")
    print("=" * 50)


if __name__ == "__main__":
    main()

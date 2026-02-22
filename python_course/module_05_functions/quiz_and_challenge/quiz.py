"""
==============================================
  MODULE 5 QUIZ: Functions
  Earn 20 XP!
==============================================
"""


def ask(num, q, opts, ans):
    print(f"\nQuestion {num}: {q}")
    for o in opts:
        print(f"  {o}")
    a = input("Your answer (a/b/c): ").strip().lower()
    if a == ans:
        print("Correct!")
        return True
    print(f"Not quite! Answer was: {ans}")
    return False


def main():
    print("=" * 50)
    print("  MODULE 5 QUIZ: Functions")
    print("=" * 50)

    s = 0

    if ask(1, "What keyword starts a function definition?",
           ["a) function", "b) func", "c) def"], "c"):
        s += 1

    if ask(2, "What is a 'parameter'?",
           ["a) A value you pass to a function",
            "b) A variable in the function definition",
            "c) A type of loop"], "b"):
        s += 1

    if ask(3, "What does 'return' do in a function?",
           ["a) Prints a value to the screen",
            "b) Sends a value back to the caller",
            "c) Stops the program"], "b"):
        s += 1

    if ask(4, "What happens if a function does not have a return statement?",
           ["a) It crashes", "b) It returns 0", "c) It returns None"], "c"):
        s += 1

    print()
    print("=" * 50)
    print(f"  RESULTS: {s}/4 correct!")
    if s >= 3:
        print("  Great work! +20 XP!")
    else:
        print("  Review and try again! +10 XP for effort!")
    print("=" * 50)


if __name__ == "__main__":
    main()

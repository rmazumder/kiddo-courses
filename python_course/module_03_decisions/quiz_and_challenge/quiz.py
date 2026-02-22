"""
==============================================
  MODULE 3 QUIZ: Making Decisions
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
    print("  MODULE 3 QUIZ: Making Decisions")
    print("=" * 50)

    s = 0

    if ask(1, "What keyword starts a decision in Python?",
           ["a) decide", "b) if", "c) check"], "b"):
        s += 1

    if ask(2, "What does 'elif' stand for?",
           ["a) else if", "b) elephant if", "c) eliminate if"], "a"):
        s += 1

    if ask(3, "What does the 'and' operator require?",
           ["a) At least one condition True",
            "b) Both conditions True",
            "c) Neither condition True"], "b"):
        s += 1

    if ask(4, "What does 'not True' equal?",
           ["a) True", "b) False", "c) Error"], "b"):
        s += 1

    print()
    print("=" * 50)
    print(f"  RESULTS: {s}/4 correct!")
    if s >= 3:
        print("  Excellent! +20 XP!")
    else:
        print("  Review lessons and try again! +10 XP for effort!")
    print("=" * 50)


if __name__ == "__main__":
    main()

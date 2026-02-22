"""
==============================================
  MODULE 4 QUIZ: Loops & Repetition
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
    print("  MODULE 4 QUIZ: Loops & Repetition")
    print("=" * 50)

    s = 0

    if ask(1, "How many times does range(5) loop?",
           ["a) 4", "b) 5", "c) 6"], "b"):
        s += 1

    if ask(2, "What does range(2, 8) produce?",
           ["a) 2,3,4,5,6,7", "b) 2,3,4,5,6,7,8", "c) 1,2,3,4,5,6,7,8"], "a"):
        s += 1

    if ask(3, "Which loop is best when you don't know how many times to repeat?",
           ["a) for loop", "b) while loop", "c) if statement"], "b"):
        s += 1

    if ask(4, "What does 'break' do inside a loop?",
           ["a) Crashes the program", "b) Pauses the loop", "c) Exits the loop immediately"], "c"):
        s += 1

    if ask(5, "What happens if a while loop condition is always True?",
           ["a) It runs forever (infinite loop)", "b) It runs once", "c) It gives an error"], "a"):
        s += 1

    print()
    print("=" * 50)
    print(f"  RESULTS: {s}/5 correct!")
    if s >= 4:
        print("  Excellent! +20 XP!")
    else:
        print("  Review and try again! +10 XP for effort!")
    print("=" * 50)


if __name__ == "__main__":
    main()

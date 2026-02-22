"""
==============================================
  MODULE 6 QUIZ: Lists & Collections
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
    print("  MODULE 6 QUIZ: Lists & Collections")
    print("=" * 50)

    s = 0

    if ask(1, "What brackets do lists use?",
           ["a) ( )", "b) { }", "c) [ ]"], "c"):
        s += 1

    if ask(2, "What index is the FIRST item in a list?",
           ["a) 0", "b) 1", "c) -1"], "a"):
        s += 1

    if ask(3, "What method adds an item to the END of a list?",
           ["a) .add()", "b) .append()", "c) .insert()"], "b"):
        s += 1

    if ask(4, "What does .pop() do?",
           ["a) Adds an item",
            "b) Sorts the list",
            "c) Removes and returns the last item"], "c"):
        s += 1

    if ask(5, "What does 'for item in my_list:' do?",
           ["a) Creates a new list",
            "b) Loops through every item in the list",
            "c) Sorts the list"], "b"):
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

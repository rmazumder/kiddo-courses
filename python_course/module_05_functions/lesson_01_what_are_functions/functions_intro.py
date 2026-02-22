"""
==============================================
  MODULE 5 - LESSON 1: What Are Functions?
==============================================

Create your own commands!
"""

print("=" * 50)
print("  FUNCTIONS: YOUR OWN COMMANDS!")
print("=" * 50)
print()

# --------------------------------------------------
# Defining and Calling a Function
# --------------------------------------------------
print("--- Define and Call ---")


# Step 1: DEFINE the function
def say_hello():
    """This function says hello."""
    print("Hello there!")
    print("Welcome to the Function Zone!")


# Step 2: CALL the function
say_hello()
print()

# You can call it as many times as you want!
print("Calling it 3 times:")
say_hello()
say_hello()
say_hello()
print()

# --------------------------------------------------
# Why Functions Are Useful
# --------------------------------------------------
print("--- Why Functions Rock ---")


# Without functions, you would have to repeat code:
# print("====================")
# print("   GAME OVER")
# print("====================")
# ... everywhere you need it!

# With a function, define it once, use it everywhere:
def show_game_over():
    print("=" * 20)
    print("    GAME OVER")
    print("=" * 20)


def show_you_win():
    print("*" * 20)
    print("   YOU WIN!")
    print("*" * 20)


# Now you can use them anywhere:
show_game_over()
print()
show_you_win()
print()

# --------------------------------------------------
# Functions Keep Code Organized
# --------------------------------------------------
print("--- Organized Code ---")


def draw_cat():
    print("  /\\_/\\")
    print(" ( o.o )")
    print("  > ^ <")


def draw_dog():
    print("  / \\__")
    print(" (    @\\___")
    print(" /         O")
    print("/   (_____/")


print("Here's a cat:")
draw_cat()
print()
print("Here's a dog:")
draw_dog()
print()

# --------------------------------------------------
# Functions Can Use Loops and If Statements
# --------------------------------------------------
print("--- Functions + Loops ---")


def countdown():
    for i in range(5, 0, -1):
        print(f"  {i}...")
    print("  BLAST OFF!")


def draw_triangle(size):
    for i in range(1, size + 1):
        print("  " + "*" * i)


print("Countdown:")
countdown()
print()
print("Triangle:")
draw_triangle(5)
print()

print("Function creator! +10 XP!")

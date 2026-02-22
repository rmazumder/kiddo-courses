"""
==============================================
  MODULE 5 - LESSON 3: Return Values
==============================================

Get information BACK from your functions!
"""

print("=" * 50)
print("  RETURN VALUES: GETTING ANSWERS BACK!")
print("=" * 50)
print()

# --------------------------------------------------
# Basic Return
# --------------------------------------------------
print("--- Basic Return ---")


def add(a, b):
    return a + b


result = add(3, 5)
print(f"3 + 5 = {result}")

# You can also use the function directly:
print(f"10 + 20 = {add(10, 20)}")
print()

# --------------------------------------------------
# Print vs. Return
# --------------------------------------------------
print("--- Print vs. Return ---")


def add_print(a, b):
    print(a + b)  # Shows the answer, but you can't save it


def add_return(a, b):
    return a + b  # Gives the answer back -- you CAN save it


# With print:
print("Using print:")
add_print(3, 5)  # Shows 8, but...
result1 = add_print(3, 5)  # result1 is None!
print(f"Saved result: {result1}")  # None -- the value is lost!
print()

# With return:
print("Using return:")
result2 = add_return(3, 5)
print(f"Saved result: {result2}")  # 8 -- the value is saved!
# Now you can USE the result:
doubled = result2 * 2
print(f"Doubled: {doubled}")
print()

# --------------------------------------------------
# Functions That Return Different Things
# --------------------------------------------------
print("--- Returning Different Types ---")


def get_greeting(name):
    """Return a greeting string."""
    return f"Hello, {name}!"


def is_even(number):
    """Return True if the number is even, False otherwise."""
    return number % 2 == 0


def get_letter_grade(score):
    """Return a letter grade based on the score."""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


message = get_greeting("Coder")
print(message)

print(f"Is 4 even? {is_even(4)}")
print(f"Is 7 even? {is_even(7)}")

grade = get_letter_grade(87)
print(f"Score 87 = Grade {grade}")
print()

# --------------------------------------------------
# Using Return Values in Calculations
# --------------------------------------------------
print("--- Chaining Return Values ---")


def square(n):
    return n * n


def cube(n):
    return n * n * n


# Use return values in bigger expressions:
total = square(3) + square(4)
print(f"3 squared + 4 squared = {total}")

# Functions can call other functions:
def distance(x1, y1, x2, y2):
    """Calculate distance between two points."""
    dx = x2 - x1
    dy = y2 - y1
    return (dx ** 2 + dy ** 2) ** 0.5  # Square root using ** 0.5


d = distance(0, 0, 3, 4)
print(f"Distance from (0,0) to (3,4) = {d}")
print()

# --------------------------------------------------
# Returning Multiple Values
# --------------------------------------------------
print("--- Returning Multiple Values ---")


def min_and_max(a, b, c):
    """Return both the smallest and largest of three numbers."""
    smallest = min(a, b, c)
    largest = max(a, b, c)
    return smallest, largest  # Return TWO values!


low, high = min_and_max(5, 2, 8)
print(f"Numbers: 5, 2, 8")
print(f"Smallest: {low}, Largest: {high}")
print()

# --------------------------------------------------
# Fun Example: Coin Flip Simulator
# --------------------------------------------------
print("--- Coin Flip Simulator ---")
import random


def flip_coin():
    """Simulate a coin flip. Return 'Heads' or 'Tails'."""
    if random.random() < 0.5:
        return "Heads"
    else:
        return "Tails"


print("Flipping 5 coins:")
for i in range(5):
    result = flip_coin()
    print(f"  Flip {i + 1}: {result}")

print()
print("Return value master! +10 XP!")

"""
==============================================
  MODULE 4 - LESSON 1: For Loops
==============================================

Repeat things without rewriting code!
"""

print("=" * 50)
print("  FOR LOOPS: REPEAT, REPEAT, REPEAT!")
print("=" * 50)
print()

# --------------------------------------------------
# Basic For Loop
# --------------------------------------------------
print("--- Basic For Loop ---")

for i in range(5):
    print(f"Loop number: {i}")

# range(5) gives us: 0, 1, 2, 3, 4
# (starts at 0 and stops BEFORE 5)
print()

# --------------------------------------------------
# Counting from 1
# --------------------------------------------------
print("--- Counting from 1 ---")

for i in range(1, 6):
    print(f"Step {i}")

# range(1, 6) gives us: 1, 2, 3, 4, 5
# (starts at 1 and stops BEFORE 6)
print()

# --------------------------------------------------
# Counting by 2s
# --------------------------------------------------
print("--- Counting by 2s ---")

for i in range(0, 11, 2):
    print(i, end=" ")  # end=" " prints on the same line

# range(0, 11, 2) gives: 0, 2, 4, 6, 8, 10
# The third number is the "step" (how much to count by)
print()  # New line after the loop
print()

# --------------------------------------------------
# Countdown!
# --------------------------------------------------
print("--- Countdown! ---")

for i in range(10, 0, -1):
    print(i, end="... ")

print("LIFTOFF!")
print()

# --------------------------------------------------
# Looping Through a String
# --------------------------------------------------
print("--- Looping Through a String ---")

word = "PYTHON"
for letter in word:
    print(f"Letter: {letter}")

print()

# --------------------------------------------------
# Fun: Multiplication Table
# --------------------------------------------------
print("--- Times Table for 7 ---")

for i in range(1, 11):
    result = 7 * i
    print(f"7 x {i:2d} = {result:3d}")

print()

# --------------------------------------------------
# Using Loops with If Statements
# --------------------------------------------------
print("--- FizzBuzz (1 to 20) ---")
print("Rules: If divisible by 3, say Fizz.")
print("       If divisible by 5, say Buzz.")
print("       If divisible by both, say FizzBuzz!")
print()

for number in range(1, 21):
    if number % 3 == 0 and number % 5 == 0:
        print(f"{number:2d}: FizzBuzz!")
    elif number % 3 == 0:
        print(f"{number:2d}: Fizz")
    elif number % 5 == 0:
        print(f"{number:2d}: Buzz")
    else:
        print(f"{number:2d}:")

print()

# --------------------------------------------------
# Drawing with Loops
# --------------------------------------------------
print("--- Drawing a Triangle ---")

for row in range(1, 6):
    print("*" * row)

print()
print("--- Drawing an Upside-Down Triangle ---")

for row in range(5, 0, -1):
    print("*" * row)

print()
print("Loop learner! +10 XP!")

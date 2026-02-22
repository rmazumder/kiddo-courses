"""
==============================================
  MODULE 4 - LESSON 3: Loop Patterns
==============================================

Common patterns that programmers use daily!
"""

print("=" * 50)
print("  LOOP PATTERNS")
print("=" * 50)
print()

# --------------------------------------------------
# Pattern 1: Counter
# Count how many times something happens
# --------------------------------------------------
print("--- Pattern 1: Counter ---")

sentence = "I love programming in Python every day"
space_count = 0

for char in sentence:
    if char == " ":
        space_count += 1

print(f"Sentence: '{sentence}'")
print(f"Number of spaces: {space_count}")
print()

# --------------------------------------------------
# Pattern 2: Accumulator
# Build up a total value
# --------------------------------------------------
print("--- Pattern 2: Accumulator ---")

# Sum all numbers from 1 to 10
total = 0
for num in range(1, 11):
    total += num
    print(f"  Added {num}, total is now {total}")

print(f"Final total: {total}")
print()

# --------------------------------------------------
# Pattern 3: Search
# Look for something specific
# --------------------------------------------------
print("--- Pattern 3: Search ---")

secret_word = "python"
words = ["java", "ruby", "python", "scratch", "swift"]

found = False
for word in words:
    if word == secret_word:
        found = True
        break

if found:
    print(f"Found '{secret_word}' in the list!")
else:
    print(f"'{secret_word}' was not found.")

print()

# --------------------------------------------------
# Pattern 4: Nested Loops (Loop inside a Loop)
# --------------------------------------------------
print("--- Pattern 4: Nested Loops ---")
print("Multiplication table (1-5):")
print()

# Header row
print("    ", end="")
for col in range(1, 6):
    print(f"{col:4d}", end="")
print()
print("   " + "-" * 20)

# Table body
for row in range(1, 6):
    print(f"{row:2d} |", end="")
    for col in range(1, 6):
        print(f"{row * col:4d}", end="")
    print()

print()

# --------------------------------------------------
# Pattern 5: Building a String
# --------------------------------------------------
print("--- Pattern 5: Building a String ---")

# Reverse a word by building a new string
original = "PYTHON"
reversed_word = ""

for char in original:
    reversed_word = char + reversed_word  # Add each letter to the FRONT

print(f"Original: {original}")
print(f"Reversed: {reversed_word}")
print()

# --------------------------------------------------
# Useful Trick: enumerate()
# --------------------------------------------------
print("--- enumerate(): Position + Value ---")

fruits = ["apple", "banana", "cherry", "date"]

for index, fruit in enumerate(fruits):
    print(f"  #{index}: {fruit}")

# enumerate() gives you both the position number AND the item!
print()

# --------------------------------------------------
# Fun: Drawing a Rectangle with Nested Loops
# --------------------------------------------------
print("--- Nested Loop Art ---")

width = 10
height = 5

for row in range(height):
    for col in range(width):
        if row == 0 or row == height - 1 or col == 0 or col == width - 1:
            print("#", end="")
        else:
            print(" ", end="")
    print()

print()
print("Pattern pro! +10 XP!")

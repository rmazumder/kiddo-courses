"""
==============================================
  MODULE 6 - LESSON 3: Loops and Lists
==============================================

Process every item in a list with loops!
"""

print("=" * 50)
print("  LOOPS + LISTS = POWER!")
print("=" * 50)
print()

# --------------------------------------------------
# Basic List Loop
# --------------------------------------------------
print("--- Basic List Loop ---")

animals = ["cat", "dog", "parrot", "rabbit"]
for animal in animals:
    print(f"  I have a {animal}!")

print()

# --------------------------------------------------
# Loop with Index (enumerate)
# --------------------------------------------------
print("--- Enumerate: Index + Value ---")

students = ["Alice", "Bob", "Charlie", "Diana"]
for index, name in enumerate(students):
    print(f"  Seat #{index + 1}: {name}")

print()

# --------------------------------------------------
# Building a New List from an Old One
# --------------------------------------------------
print("--- Building New Lists ---")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Find all even numbers
evens = []
for num in numbers:
    if num % 2 == 0:
        evens.append(num)

print(f"All numbers: {numbers}")
print(f"Even numbers: {evens}")
print()

# Double every number
doubled = []
for num in numbers:
    doubled.append(num * 2)

print(f"Doubled: {doubled}")
print()

# --------------------------------------------------
# List Comprehensions (Python Shortcut!)
# --------------------------------------------------
print("--- List Comprehensions ---")

# This is a shorter way to build lists:
# [expression for item in list]

squares = [n * n for n in range(1, 6)]
print(f"Squares: {squares}")

# With a condition:
# [expression for item in list if condition]

big_scores = [s for s in [72, 95, 88, 63, 91, 77] if s >= 80]
print(f"High scores (80+): {big_scores}")

upper_names = [name.upper() for name in ["alex", "pat", "sam"]]
print(f"Uppercase: {upper_names}")
print()

# --------------------------------------------------
# Fun Example: Grade Report
# --------------------------------------------------
print("--- Grade Report ---")

student_scores = {
    "Alice": 95,
    "Bob": 82,
    "Charlie": 67,
    "Diana": 91,
    "Eve": 78,
}

print(f"{'Name':10s} {'Score':6s} {'Grade':5s}")
print("-" * 25)

for name, score in student_scores.items():
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    else:
        grade = "D"
    print(f"{name:10s} {score:6d} {grade:5s}")

print()

# --------------------------------------------------
# Fun Example: Word Counter
# --------------------------------------------------
print("--- Word Counter ---")

sentence = "the cat sat on the mat and the cat ate the food"
words = sentence.split()  # Split string into a list of words!
print(f"Sentence: '{sentence}'")
print(f"Words: {words}")
print(f"Word count: {len(words)}")

# Count each unique word
unique_words = []
for word in words:
    if word not in unique_words:
        unique_words.append(word)

print(f"Unique words: {unique_words}")
print(f"Unique count: {len(unique_words)}")
print()

# --------------------------------------------------
# Fun Example: Random Team Maker
# --------------------------------------------------
print("--- Random Team Maker ---")
import random

players = ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank"]
random.shuffle(players)  # Shuffle the list randomly

team_size = len(players) // 2
team_1 = players[:team_size]
team_2 = players[team_size:]

print(f"Team 1: {team_1}")
print(f"Team 2: {team_2}")
print()

print("Loop + list master! +10 XP!")

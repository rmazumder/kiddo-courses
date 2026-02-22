"""
==============================================
  MODULE 6 - LESSON 3: Exercise
  Loops + Lists Challenges
==============================================
"""

print("=" * 50)
print("  LOOPS + LISTS EXERCISES")
print("=" * 50)
print()

# --------------------------------------------------
# EXERCISE 1: Print Each Item
# Loop through the list and print each fruit
# with a number:  "1. apple", "2. banana", etc.
# --------------------------------------------------
print("Exercise 1: Numbered List")
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
# for i, fruit in enumerate(fruits):
#     print(f"  {i + 1}. {fruit}")
print()

# --------------------------------------------------
# EXERCISE 2: Sum a List
# Calculate the sum of all numbers using a loop.
# (Don't use the sum() function -- do it manually!)
# --------------------------------------------------
print("Exercise 2: Sum")
numbers = [10, 20, 30, 40, 50]
# total = 0
# for num in numbers:
#     total += ___
# print(f"Sum: {total}")
print()

# --------------------------------------------------
# EXERCISE 3: Filter Names
# Create a new list containing only names that
# start with the letter "A".
# --------------------------------------------------
print("Exercise 3: Filter Names")
names = ["Alice", "Bob", "Anna", "Charlie", "Amy", "David"]
# a_names = []
# for name in names:
#     if name[0] == "___":
#         a_names.append(name)
# print(f"Names starting with A: {a_names}")
print()

# --------------------------------------------------
# EXERCISE 4: List Comprehension
# Use a list comprehension to create a list of
# the first 10 cube numbers (1, 8, 27, 64, ...)
# --------------------------------------------------
print("Exercise 4: Cubes")
# cubes = [n ** ___ for n in range(1, ___)]
# print(f"Cubes: {cubes}")
print()

# --------------------------------------------------
# EXERCISE 5: Find the Longest Word
# Find the longest word in the list.
# --------------------------------------------------
print("Exercise 5: Longest Word")
words = ["python", "programming", "is", "incredibly", "fun"]
# longest = words[0]
# for word in words:
#     if len(word) > len(longest):
#         longest = ___
# print(f"Longest word: '{longest}' ({len(longest)} letters)")
print()

# --------------------------------------------------
# BONUS STAR CHALLENGE:
# Write a function that takes a list of numbers
# and returns a NEW list with duplicates removed,
# keeping the original order.
# Example: [1, 2, 3, 2, 1, 4] -> [1, 2, 3, 4]
# --------------------------------------------------

print()
print("Run this file to check your answers!")

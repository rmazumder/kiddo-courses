"""
==============================================
  MODULE 6 - LESSON 1: What Are Lists?
==============================================

Store MANY items in one variable!
"""

print("=" * 50)
print("  LISTS: COLLECTIONS OF STUFF!")
print("=" * 50)
print()

# --------------------------------------------------
# Creating Lists
# --------------------------------------------------
print("--- Creating Lists ---")

# A list of favorite foods
favorite_foods = ["pizza", "ice cream", "tacos", "sushi", "pasta"]
print(f"Favorite foods: {favorite_foods}")

# A list of scores
scores = [95, 87, 92, 78, 100]
print(f"Game scores: {scores}")

# A list can hold different types!
player = ["Luna", 12, 500, True]
print(f"Player info: {player}")
print()

# --------------------------------------------------
# Accessing Items by Index
# --------------------------------------------------
print("--- Accessing Items ---")

animals = ["cat", "dog", "parrot", "hamster", "goldfish"]
print(f"Full list: {animals}")
print(f"First animal (index 0): {animals[0]}")
print(f"Third animal (index 2): {animals[2]}")
print(f"Last animal (index -1): {animals[-1]}")
print()

# --------------------------------------------------
# List Length
# --------------------------------------------------
print("--- List Length ---")

colors = ["red", "blue", "green", "yellow", "purple"]
print(f"Colors: {colors}")
print(f"Number of colors: {len(colors)}")
print()

# --------------------------------------------------
# Changing Items
# --------------------------------------------------
print("--- Changing Items ---")

menu = ["burger", "fries", "soda"]
print(f"Original menu: {menu}")

menu[2] = "lemonade"  # Change "soda" to "lemonade"
print(f"Updated menu: {menu}")
print()

# --------------------------------------------------
# Checking If Something Is in a List
# --------------------------------------------------
print("--- Checking for Items ---")

inventory = ["sword", "shield", "potion", "map"]
print(f"Inventory: {inventory}")

# Use the 'in' keyword to check
if "sword" in inventory:
    print("You have a sword! Ready for battle!")

if "bow" not in inventory:
    print("You don't have a bow. Visit the shop!")

print()

# --------------------------------------------------
# List Slicing
# --------------------------------------------------
print("--- List Slicing ---")

numbers = [10, 20, 30, 40, 50, 60, 70]
print(f"Full list: {numbers}")
print(f"First 3: {numbers[0:3]}")
print(f"Middle: {numbers[2:5]}")
print(f"Last 2: {numbers[-2:]}")
print()

print("List learner! +10 XP!")

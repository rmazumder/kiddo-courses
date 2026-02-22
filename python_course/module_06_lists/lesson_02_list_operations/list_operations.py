"""
==============================================
  MODULE 6 - LESSON 2: List Operations
==============================================

Add, remove, sort, and more!
"""

print("=" * 50)
print("  LIST OPERATIONS!")
print("=" * 50)
print()

# --------------------------------------------------
# Adding Items
# --------------------------------------------------
print("--- Adding Items ---")

backpack = ["water", "snacks"]
print(f"Start:  {backpack}")

backpack.append("map")          # Add to the END
print(f"Append: {backpack}")

backpack.insert(0, "compass")   # Insert at position 0 (beginning)
print(f"Insert: {backpack}")

backpack.append("flashlight")
print(f"Final:  {backpack}")
print()

# --------------------------------------------------
# Removing Items
# --------------------------------------------------
print("--- Removing Items ---")

snacks = ["chips", "cookies", "apple", "candy", "apple"]
print(f"Start:   {snacks}")

snacks.remove("candy")          # Remove by VALUE (first occurrence)
print(f"Remove:  {snacks}")

last_item = snacks.pop()        # Remove and get the LAST item
print(f"Pop:     {snacks}")
print(f"Popped:  {last_item}")

first_item = snacks.pop(0)      # Remove and get item at index 0
print(f"Pop(0):  {snacks}")
print(f"Popped:  {first_item}")
print()

# --------------------------------------------------
# Sorting
# --------------------------------------------------
print("--- Sorting ---")

numbers = [42, 17, 93, 8, 55, 31]
print(f"Original:   {numbers}")

numbers.sort()
print(f"Sorted:     {numbers}")

numbers.sort(reverse=True)
print(f"Reverse:    {numbers}")
print()

words = ["banana", "apple", "cherry", "date"]
print(f"Original:   {words}")
words.sort()
print(f"Sorted:     {words}")
print()

# --------------------------------------------------
# Other Useful Methods
# --------------------------------------------------
print("--- Other Methods ---")

grades = [85, 92, 78, 92, 95, 88, 92]
print(f"Grades: {grades}")
print(f"Count of 92: {grades.count(92)}")
print(f"Position of 78: {grades.index(78)}")
print(f"Min: {min(grades)}, Max: {max(grades)}")
print(f"Sum: {sum(grades)}, Average: {sum(grades) / len(grades):.1f}")
print()

# --------------------------------------------------
# Combining Lists
# --------------------------------------------------
print("--- Combining Lists ---")

team_a = ["Alice", "Bob"]
team_b = ["Charlie", "Diana"]

all_players = team_a + team_b  # Creates a NEW list
print(f"Team A: {team_a}")
print(f"Team B: {team_b}")
print(f"All:    {all_players}")
print()

# --------------------------------------------------
# Fun Example: Shopping List Manager
# --------------------------------------------------
print("--- Shopping List Manager ---")

shopping = []
print("Building a shopping list...")

items_to_add = ["milk", "bread", "eggs", "butter", "cheese", "apples"]
for item in items_to_add:
    shopping.append(item)
    print(f"  Added '{item}' -> {shopping}")

print()
print("Removing 'butter' (we already have some):")
shopping.remove("butter")
print(f"  Updated: {shopping}")

print("Sorting alphabetically:")
shopping.sort()
print(f"  Sorted: {shopping}")

print()
print("List operator! +10 XP!")

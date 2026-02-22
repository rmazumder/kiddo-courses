"""
==============================================
  MODULE 3 - LESSON 2: Else and Elif
==============================================

Two paths? Three paths? Ten paths?
Python can handle them all!
"""

print("=" * 50)
print("  ELSE AND ELIF: MULTIPLE PATHS!")
print("=" * 50)
print()

# --------------------------------------------------
# If/Else: Two Paths
# --------------------------------------------------
print("--- If/Else: Two Paths ---")

coins = 50
item_price = 75

if coins >= item_price:
    print("You bought the item!")
    coins = coins - item_price
    print(f"Coins left: {coins}")
else:
    print("Not enough coins!")
    print(f"You need {item_price - coins} more coins.")

print()

# --------------------------------------------------
# Elif: Multiple Paths
# --------------------------------------------------
print("--- Elif: Grading System ---")

score = 87

if score >= 90:
    grade = "A"
    message = "Outstanding!"
elif score >= 80:
    grade = "B"
    message = "Great job!"
elif score >= 70:
    grade = "C"
    message = "Not bad!"
elif score >= 60:
    grade = "D"
    message = "Keep trying!"
else:
    grade = "F"
    message = "Let's study more."

print(f"Score: {score}")
print(f"Grade: {grade} -- {message}")
print()

# --------------------------------------------------
# Fun Example: Day of the Week
# --------------------------------------------------
print("--- Day of the Week ---")

day_number = 3

if day_number == 1:
    day = "Monday"
elif day_number == 2:
    day = "Tuesday"
elif day_number == 3:
    day = "Wednesday"
elif day_number == 4:
    day = "Thursday"
elif day_number == 5:
    day = "Friday"
elif day_number == 6:
    day = "Saturday"
elif day_number == 7:
    day = "Sunday"
else:
    day = "Unknown"

print(f"Day {day_number} is {day}!")
print()

# --------------------------------------------------
# Real-World Example: Weather Advisor
# --------------------------------------------------
print("--- Weather Advisor ---")

temperature = 22

if temperature >= 35:
    print("It's extremely hot! Stay inside if you can.")
elif temperature >= 25:
    print("It's warm and nice! Great day for the beach.")
elif temperature >= 15:
    print("It's mild. A light jacket should do.")
elif temperature >= 5:
    print("It's cold! Wear a warm coat.")
else:
    print("It's freezing! Bundle up with layers!")

print(f"(Temperature: {temperature} degrees)")
print()

# --------------------------------------------------
# Interactive Example: Simple Adventure
# --------------------------------------------------
print("--- Mini Adventure ---")
try:
    print("You are in a dark cave. You see two paths.")
    choice = input("Do you go LEFT or RIGHT? ").strip().lower()

    if choice == "left":
        print("You found a treasure chest! You win!")
    elif choice == "right":
        print("You found a friendly dragon! It gives you a ride home!")
    else:
        print("You stand still and a bat flies over your head. Spooky!")
except EOFError:
    print("(Run this directly to try the adventure!)")

print()
print("Multi-path master! +10 XP!")

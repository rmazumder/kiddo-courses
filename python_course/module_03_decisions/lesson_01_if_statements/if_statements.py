"""
==============================================
  MODULE 3 - LESSON 1: If Statements
==============================================

Teach your program to make decisions!
"""

print("=" * 50)
print("  IF STATEMENTS: MAKING DECISIONS!")
print("=" * 50)
print()

# --------------------------------------------------
# Basic If Statement
# --------------------------------------------------
print("--- Basic If Statement ---")

age = 10

if age >= 8:
    print("You are old enough for this course!")
    print("Welcome aboard!")

print()  # This runs no matter what (not indented under if)

# --------------------------------------------------
# What Happens When the Condition is False?
# --------------------------------------------------
print("--- When Condition is False ---")

temperature = 15

if temperature > 30:
    print("It is hot! Wear shorts.")
    # This WON'T print because 15 is NOT greater than 30

print("(The temperature was only 15, so the if block was skipped.)")
print()

# --------------------------------------------------
# Comparing Things
# --------------------------------------------------
print("--- Different Comparisons ---")

score = 85

if score >= 90:
    print("You got an A!")

if score >= 80:
    print("You got at least a B!")

if score >= 70:
    print("You got at least a C!")

# Notice: multiple if statements each check independently.
# Score 85 triggers both the B and C checks!
print()

# --------------------------------------------------
# Checking Strings
# --------------------------------------------------
print("--- Checking Strings ---")

password = "secret123"
attempt = "secret123"

if attempt == password:
    print("Access granted! Welcome!")

wrong_attempt = "wrong"
if wrong_attempt == password:
    print("This will NOT print because the passwords don't match")

print()

# --------------------------------------------------
# Interactive Example: Ticket Checker
# --------------------------------------------------
print("--- Ticket Checker ---")

try:
    rider_age = int(input("How old are you? "))

    if rider_age >= 8:
        print("You can ride the roller coaster!")

    if rider_age < 8:
        print("Sorry, you must be at least 8 to ride.")

    print("Thanks for visiting the amusement park!")
except (ValueError, EOFError):
    print("(Run this directly to try the interactive part!)")

print()
print("Decision maker! +10 XP!")

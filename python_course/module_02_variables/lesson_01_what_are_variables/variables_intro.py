"""
==============================================
  MODULE 2 - LESSON 1: Variables in Action
==============================================

This program shows you how variables work.
Run it and watch what happens!
"""

print("=" * 50)
print("  VARIABLES IN ACTION!")
print("=" * 50)
print()

# --------------------------------------------------
# Creating variables
# --------------------------------------------------

# Let's create some variables about a character
character_name = "Luna"
character_age = 12
character_power = "invisibility"

# Now let's USE those variables
print("Meet our hero!")
print("Name:", character_name)
print("Age:", character_age)
print("Superpower:", character_power)
print()

# --------------------------------------------------
# Changing variables
# --------------------------------------------------

# Variables can CHANGE! That's why they're called "variables."
print("--- One year later... ---")
character_age = 13  # Luna had a birthday!
print("Name:", character_name)
print("Age:", character_age)
print("Superpower:", character_power)
print()

# --------------------------------------------------
# Using variables together
# --------------------------------------------------

# You can use multiple variables in one print statement
print(character_name, "is", character_age, "years old and has the power of", character_power)
print()

# --------------------------------------------------
# f-strings: A cool way to use variables in text
# --------------------------------------------------

# Python has a special trick called f-strings.
# Put an 'f' before the quotes, then use {variable_name}
# inside the text:

print("Using f-strings (a cool Python trick):")
print(f"{character_name} is {character_age} years old!")
print(f"Her power is {character_power}!")
print()

# --------------------------------------------------
# Variables can hold different types of information
# --------------------------------------------------

print("--- Different types of data ---")
pet_name = "Whiskers"      # This is TEXT (called a "string")
pet_age = 3                 # This is a WHOLE NUMBER (called an "integer")
pet_weight = 4.5            # This is a DECIMAL number (called a "float")
is_fluffy = True            # This is TRUE or FALSE (called a "boolean")

print(f"Pet name: {pet_name} (text)")
print(f"Pet age: {pet_age} (whole number)")
print(f"Pet weight: {pet_weight} kg (decimal number)")
print(f"Is fluffy: {is_fluffy} (true or false)")
print()

# --------------------------------------------------
# Common mistake: forgetting quotes
# --------------------------------------------------

# greeting = Hello     # ERROR! Python thinks Hello is a variable name
greeting = "Hello"     # CORRECT! The quotes tell Python it's text

print(f"Correct: {greeting}")
print()

print("You now understand variables! +10 XP!")

"""
==============================================
  MODULE 2 - LESSON 3: Strings Fun!
==============================================

Strings are text -- and Python has TONS
of cool things you can do with them!
"""

print("=" * 50)
print("  STRING TRICKS!")
print("=" * 50)
print()

# --------------------------------------------------
# Combining Strings (Concatenation)
# --------------------------------------------------
print("--- Combining Strings ---")

first_name = "Super"
last_name = "Coder"

# Method 1: Using the + operator
full_name = first_name + " " + last_name
print("Full name:", full_name)

# Method 2: Using f-strings (the cool way!)
print(f"Hello, {first_name} {last_name}!")
print()

# --------------------------------------------------
# String Length
# --------------------------------------------------
print("--- String Length ---")

message = "Python is awesome"
print(f"'{message}' has {len(message)} characters")
# len() counts EVERY character, including spaces!

short_word = "hi"
print(f"'{short_word}' has {len(short_word)} characters")
print()

# --------------------------------------------------
# String Methods (Built-in Tricks)
# --------------------------------------------------
print("--- String Methods ---")

text = "hello, world"

print(f"Original:     '{text}'")
print(f".upper():     '{text.upper()}'")      # ALL CAPS
print(f".lower():     '{text.lower()}'")      # all lowercase
print(f".title():     '{text.title()}'")      # Title Case
print(f".capitalize():'{text.capitalize()}'")  # First letter cap
print()

# Replace words
sentence = "I like cats"
new_sentence = sentence.replace("cats", "dogs")
print(f"Original: {sentence}")
print(f"Replaced: {new_sentence}")
print()

# Count occurrences
tongue_twister = "she sells sea shells by the sea shore"
print(f"How many 's' in the tongue twister? {tongue_twister.count('s')}")
print(f"How many 'sea' in the tongue twister? {tongue_twister.count('sea')}")
print()

# --------------------------------------------------
# String Indexing (Accessing Individual Characters)
# --------------------------------------------------
print("--- Indexing ---")
# Each character in a string has a position number.
# Positions start at 0 (not 1!).

word = "PYTHON"
print(f"Word: {word}")
print(f"Position 0: {word[0]}")    # P
print(f"Position 1: {word[1]}")    # Y
print(f"Position 2: {word[2]}")    # T
print(f"Position 3: {word[3]}")    # H
print(f"Position 4: {word[4]}")    # O
print(f"Position 5: {word[5]}")    # N
print()

# You can also count from the end using negative numbers!
print(f"Last character:  {word[-1]}")   # N
print(f"Second to last:  {word[-2]}")   # O
print()

# --------------------------------------------------
# String Slicing (Getting Parts of a String)
# --------------------------------------------------
print("--- Slicing ---")
message = "Hello, World!"

print(f"First 5 chars: {message[0:5]}")     # Hello
print(f"From index 7:  {message[7:]}")       # World!
print(f"Last 6 chars:  {message[-6:]}")      # orld!
print()

# --------------------------------------------------
# String Multiplication
# --------------------------------------------------
print("--- String Multiplication ---")
print("Ha" * 5)         # HaHaHaHaHa
print("-" * 30)
print("Go! " * 3)       # Go! Go! Go!
print()

# --------------------------------------------------
# Getting Input from the User
# --------------------------------------------------
print("--- User Input ---")
try:
    user_name = input("What is your name? ")
    print(f"Nice to meet you, {user_name}!")
    print(f"Your name has {len(user_name)} letters.")
    print(f"In ALL CAPS: {user_name.upper()}")
except EOFError:
    print("(Run this file directly to try the input part!)")

print()
print("String master! +10 XP!")

"""
==============================================
  MODULE 4 CHALLENGE: Number Guessing Game!
  Earn 30 XP and your LOOP LEGEND badge!
==============================================

YOUR MISSION:
  Build a number guessing game!

  Requirements:
  1. Generate a random number between 1 and 50
  2. Let the player guess using a while loop
  3. After each guess, say "Too high!" or "Too low!"
  4. Count how many guesses it takes
  5. When they guess correctly, tell them how many tries
  6. Give a rating based on guesses:
     - 1-3 guesses: "Incredible! You're psychic!"
     - 4-6 guesses: "Great job! Very impressive!"
     - 7-10 guesses: "Not bad! Keep practicing!"
     - 11+ guesses: "You got it! Practice makes perfect!"
  7. Ask if they want to play again

  HINTS:
  - import random
  - secret = random.randint(1, 50)
  - Use input() to get guesses
  - Use int() to convert the text input to a number
  - Use a while loop that continues until guess == secret
"""

import random

print("=" * 50)
print("   NUMBER GUESSING GAME")
print("=" * 50)
print()
print("I'm thinking of a number between 1 and 50.")
print("Can you guess what it is?")
print()

# YOUR CODE BELOW!

# Step 1: Generate a random number
# secret = random.randint(1, 50)

# Step 2: Set up variables
# guesses = 0
# correct = False

# Step 3: Create the game loop
# while not correct:
#     try:
#         guess = int(input("Your guess: "))
#         guesses += 1
#
#         if guess == secret:
#             correct = True
#             print(f"YOU GOT IT in {guesses} guesses!")
#         elif guess < secret:
#             print("Too low! Try higher.")
#         else:
#             print("Too high! Try lower.")
#     except ValueError:
#         print("Please enter a number!")

# Step 4: Give a rating
# if guesses <= 3:
#     print("Incredible! You're psychic!")
# elif guesses <= 6:
#     print("Great job! Very impressive!")
# elif guesses <= 10:
#     print("Not bad! Keep practicing!")
# else:
#     print("You got it! Practice makes perfect!")

print()
print("=" * 50)
print("Module 4 Complete!")
print("Badge Earned: [O] LOOP LEGEND")
print("Next: Module 5 - Functions!")
print("=" * 50)

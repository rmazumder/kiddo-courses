"""
==============================================
  MODULE 4 - LESSON 2: While Loops
==============================================

Keep going until you want to stop!
"""

print("=" * 50)
print("  WHILE LOOPS: KEEP GOING!")
print("=" * 50)
print()

# --------------------------------------------------
# Basic While Loop
# --------------------------------------------------
print("--- Basic While Loop ---")

count = 1
while count <= 5:
    print(f"Count: {count}")
    count = count + 1  # This is CRITICAL! Without it, infinite loop!

print(f"Loop ended. count is now {count}")
print()

# --------------------------------------------------
# Countdown with While
# --------------------------------------------------
print("--- Countdown ---")

seconds = 5
while seconds > 0:
    print(f"{seconds}...")
    seconds = seconds - 1

print("Time's up!")
print()

# --------------------------------------------------
# While with User Input
# --------------------------------------------------
print("--- Guessing Game ---")

secret_number = 7

# Since we can't always use input() in automated runs,
# let's simulate with a list of guesses:
guesses = [3, 5, 7]  # Pretend these are user guesses
guess_index = 0

print("I'm thinking of a number between 1 and 10.")
while guess_index < len(guesses):
    guess = guesses[guess_index]
    print(f"Your guess: {guess}")

    if guess == secret_number:
        print("You got it! The number was", secret_number)
        break  # EXIT the loop immediately!
    elif guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")

    guess_index += 1  # Move to next guess

print()

# --------------------------------------------------
# Break and Continue
# --------------------------------------------------
print("--- Break: Stop the Loop Early ---")

# break exits the loop immediately
for i in range(1, 100):
    if i == 5:
        print("Found 5! Breaking out of the loop.")
        break
    print(f"Checking: {i}")

print()

print("--- Continue: Skip One Iteration ---")

# continue skips the rest of THIS iteration and goes to the next
for i in range(1, 11):
    if i % 3 == 0:
        continue  # Skip multiples of 3
    print(i, end=" ")

print()
print("(Skipped 3, 6, and 9!)")
print()

# --------------------------------------------------
# Danger Zone: Infinite Loops!
# --------------------------------------------------
print("--- Infinite Loops (Don't Do This!) ---")
print("An infinite loop looks like this:")
print("  while True:")
print("      print('Help, I can't stop!')")
print()
print("If you accidentally make one, press Ctrl+C to stop it!")
print()

# Here's a SAFE while True loop (it has a break):
print("Safe 'while True' with break:")
counter = 0
while True:
    print(f"  Loop #{counter}")
    counter += 1
    if counter >= 3:
        print("  Breaking out!")
        break

print()
print("While loop warrior! +10 XP!")

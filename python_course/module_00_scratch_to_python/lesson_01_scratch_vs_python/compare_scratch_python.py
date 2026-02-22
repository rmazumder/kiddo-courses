"""
===================================================
  Lesson 1: Compare Scratch to Python
  Module 0 - From Scratch to Python!
===================================================

This file shows all 10 Scratch block equivalents
as real, working Python code. Run it and see what
each one does!

You are already a programmer - this is just Python spelling!
"""

import time


# ==================================================
# COMPARISON 1: Starting the Program
# In Scratch: "when green flag clicked"
# In Python:  if __name__ == "__main__":
# ==================================================

def main():
    """This function holds our main program - just like the green flag script."""
    print("Green flag clicked! Program started!")
    print()

    # ==================================================
    # COMPARISON 2: Saying Something
    # In Scratch: "say 'Hello, World!' for 2 secs"
    # In Python:  print("Hello, World!") then time.sleep(2)
    # ==================================================
    print("--- Comparison 2: Say Hello ---")
    print("Hello, World!")   # This is the "say" block
    print("(Waiting 2 seconds like Scratch's 'for 2 secs'...)")
    time.sleep(2)             # This is the "wait" part
    print()

    # ==================================================
    # COMPARISON 3: Moving (Changing a Position)
    # In Scratch: "move 10 steps"
    # In Python:  x += 10
    # ==================================================
    print("--- Comparison 3: Move 10 Steps ---")
    x = 0
    print(f"Sprite starts at x = {x}")
    x += 10   # In Scratch: "move 10 steps"
    print(f"After 'move 10 steps', x = {x}")
    x += 10
    print(f"After another 'move 10 steps', x = {x}")
    print()

    # ==================================================
    # COMPARISON 4: Repeat Loop
    # In Scratch: "repeat 10" block
    # In Python:  for i in range(10):
    # ==================================================
    print("--- Comparison 4: Repeat 10 Times ---")
    # In Scratch: repeat 10 { say i }
    for i in range(10):      # This IS the "repeat 10" block!
        print(f"  Step {i + 1} of 10")
    print()

    # ==================================================
    # COMPARISON 5: If Condition
    # In Scratch: "if <touching color?>" block
    # In Python:  if condition:
    # ==================================================
    print("--- Comparison 5: If Condition ---")
    score = 95
    # In Scratch: if <score > 90> { say "Amazing!" }
    if score > 90:           # This IS the "if" block!
        print("Amazing score! You win a star!")
    print()

    # ==================================================
    # COMPARISON 6: Set a Variable
    # In Scratch: "set [score] to [0]" orange block
    # In Python:  score = 0
    # ==================================================
    print("--- Comparison 6: Set Variable ---")
    score = 0           # In Scratch: "set score to 0"
    print(f"Score set to: {score}")
    score += 1          # In Scratch: "change score by 1"
    print(f"Score after adding 1: {score}")
    score += 1
    print(f"Score after adding 1 again: {score}")
    print()

    # ==================================================
    # COMPARISON 7: Wait / Pause
    # In Scratch: "wait 1 secs"
    # In Python:  time.sleep(1)
    # ==================================================
    print("--- Comparison 7: Wait ---")
    print("Starting countdown...")
    for count in range(3, 0, -1):
        print(f"  {count}...")
        time.sleep(1)   # In Scratch: "wait 1 secs"
    print("  GO!")
    print()

    # ==================================================
    # COMPARISON 8: Forever Loop
    # In Scratch: "forever" block
    # In Python:  while True:
    # ==================================================
    print("--- Comparison 8: Forever (Limited Demo) ---")
    print("In Scratch, 'forever' loops endlessly.")
    print("In Python, 'while True:' does the same.")
    print("Here we use a counter to stop after 5 so this demo ends:")
    counter = 0
    while counter < 5:   # Real game loops use: while True:
        counter += 1
        print(f"  Loop pass {counter} (forever would keep going!)")
    print("(A real game loop would never stop until you close the window)")
    print()

    # ==================================================
    # COMPARISON 9: Broadcast Message (Functions)
    # In Scratch: "broadcast [jump!]" and "when I receive [jump!]"
    # In Python:  define a function with def, then call it
    # ==================================================
    print("--- Comparison 9: Broadcast / Functions ---")
    # Calling a function is like "broadcast" in Scratch
    celebrate()      # This line is like: "broadcast [celebrate!]"
    print()

    # ==================================================
    # COMPARISON 10: Using Variables
    # In Scratch: orange variable blocks
    # In Python:  variable names with = sign
    # ==================================================
    print("--- Comparison 10: Variables ---")
    player_name = "Alex"         # In Scratch: "set player_name to 'Alex'"
    lives = 3                    # In Scratch: "set lives to 3"
    high_score = 0               # In Scratch: "set high_score to 0"

    print(f"Player: {player_name}")
    print(f"Lives: {lives}")
    print(f"High Score: {high_score}")

    # Using variables in expressions - just like Scratch!
    lives -= 1                   # In Scratch: "change lives by -1"
    high_score = 500             # In Scratch: "set high_score to 500"
    print(f"After playing... Lives: {lives}, High Score: {high_score}")
    print()

    print("=" * 50)
    print("You just saw ALL 10 Scratch blocks in Python!")
    print("Nice work! You are a real programmer!")
    print("=" * 50)


# ==================================================
# This is the function called in Comparison 9
# In Scratch: "when I receive [celebrate!]" script
# In Python:  def celebrate():
# ==================================================
def celebrate():
    """Called like a Scratch broadcast - runs when we call celebrate()."""
    print("  BROADCAST received! Celebrating...")
    print("  Woohoo! Great job!")


# ==================================================
# This is the "green flag" - it starts everything!
# In Scratch: the green flag button
# In Python:  if __name__ == "__main__":
# ==================================================
if __name__ == "__main__":
    main()

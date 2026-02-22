"""
==============================================
  MODULE 7 - FINAL PROJECT
  MY TEXT-BASED ADVENTURE GAME!
==============================================

This is YOUR game! Build it from scratch or
modify the starter game from Lesson 2.

Use everything you have learned:
- Variables and data types (Module 2)
- If/elif/else decisions (Module 3)
- Loops (Module 4)
- Functions (Module 5)
- Lists (Module 6)

REMEMBER THE REQUIREMENTS:
  [ ] At least 5 rooms with descriptions
  [ ] At least 3 items the player can find
  [ ] Player movement between rooms
  [ ] An inventory system
  [ ] A win condition
  [ ] A lose condition
  [ ] At least 3 custom functions
  [ ] A main game loop (while)

START BUILDING BELOW!
"""

import random


# ============================================================
# YOUR GAME DATA
# ============================================================

# Define your rooms here!
# Each room needs: description, items, exits
rooms = {
    # "Starting Room": {
    #     "description": "Describe this room...",
    #     "items": ["item1"],
    #     "exits": {"north": "Next Room"},
    # },
    # Add at least 5 rooms!
}

# Define your player here!
player = {
    "health": 100,
    "inventory": [],
    "current_room": "",  # Set to your starting room name
    "score": 0,
}


# ============================================================
# YOUR GAME FUNCTIONS
# ============================================================

# Function 1: Show the current room
# def show_room():
#     pass

# Function 2: Move the player
# def move(direction):
#     pass

# Function 3: Pick up an item
# def take_item(item_name):
#     pass

# Function 4: Show inventory
# def show_inventory():
#     pass

# Add more functions as needed!


# ============================================================
# YOUR MAIN GAME LOOP
# ============================================================

def play():
    """Main game function."""
    print("=" * 50)
    print("   [YOUR GAME TITLE HERE]")
    print("=" * 50)
    print()
    print("[Your opening story here...]")
    print()
    print("Type 'help' for commands.")
    print()

    # Show starting room
    # show_room()

    # Game loop
    game_over = False
    while not game_over:
        # Get player input
        try:
            command = input("\n> ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

        # Handle commands here!
        # if command == "help":
        #     ...
        # elif command.startswith("go "):
        #     direction = command[3:]
        #     move(direction)
        # elif command == "look":
        #     show_room()
        # ...

        # Check win/lose conditions
        # if [win condition]:
        #     print("YOU WIN!")
        #     game_over = True
        # if player["health"] <= 0:
        #     print("GAME OVER!")
        #     game_over = True

        pass  # Remove this 'pass' when you add real code

    print()
    print("=" * 50)
    print("   Thanks for playing!")
    print(f"   Final Score: {player['score']}")
    print("=" * 50)


# ============================================================
# START YOUR GAME!
# ============================================================

if __name__ == "__main__":
    play()

    print()
    print("*" * 50)
    print("  PYTHON QUEST COMPLETE!")
    print("*" * 50)
    print()
    print("  If your game works, you have earned:")
    print("    +100 XP!")
    print("    [G] GAME CREATOR badge!")
    print()
    print("  If you earned ALL 7 badges, you are now a")
    print("  PYTHON QUEST CHAMPION!")
    print()
    print("  Amazing work, programmer!")
    print("  Keep coding, keep creating, keep learning!")
    print()
    print("*" * 50)

"""
==============================================
  MODULE 7 - LESSON 1: MY Game Plan
==============================================

YOUR MISSION:
  Fill in this template with YOUR game design!
  This is your blueprint for the game you will
  build in the next two lessons.

  Think creatively! Here are some theme ideas:
  - Space station escape
  - Haunted house mystery
  - Underwater treasure hunt
  - Jungle expedition
  - Time travel adventure
  - Wizard school quest
"""

# ============================================================
# YOUR GAME DESIGN
# ============================================================

# --- 1. GAME TITLE ---
game_title = "___"  # What is your game called?

# --- 2. THE STORY ---
story = """
Setting: ___
Goal: ___
Conflict: ___
"""

# --- 3. YOUR MAP ---
# Draw your map using text! (at least 5 rooms)
game_map = """
    [Room 1]
       |
    [Room 2] -- [Room 3]
       |
    [Room 4]
       |
    [Room 5]
"""

# --- 4. YOUR ROOMS ---
# Fill in at least 5 rooms with descriptions, items, and exits.
rooms = {
    "___": {
        "description": "___",
        "items": [],
        "exits": {},
    },
    # Add more rooms!
}

# --- 5. YOUR ITEMS ---
# List all items the player can find.
items = {
    "___": "What does this item do?",
    # Add more items!
}

# --- 6. YOUR PLAYER ---
player = {
    "health": 100,
    "inventory": [],
    "current_room": "___",  # Starting room
    "score": 0,
}

# --- 7. WIN CONDITION ---
# How does the player win?
win_condition = "___"

# --- 8. LOSE CONDITION ---
# How does the player lose?
lose_condition = "___"

# ============================================================
# Display your plan
# ============================================================
print("=" * 50)
print(f"  GAME PLAN: {game_title}")
print("=" * 50)
print()
print(story)
print("MAP:")
print(game_map)
print(f"Win: {win_condition}")
print(f"Lose: {lose_condition}")
print()
print("Now head to lesson_02 to start building it!")

"""
==============================================
  MODULE 7 - LESSON 1: Game Design Template
==============================================

This file shows you how to plan a game.
Read through it to see how a game is designed
before any real code is written.
"""

print("=" * 50)
print("  GAME DESIGN TEMPLATE")
print("=" * 50)
print()

# ============================================================
# EXAMPLE GAME DESIGN: "The Dragon's Treasure"
# ============================================================

# --- 1. THE STORY ---
# Setting: A medieval castle
# Goal: Find the dragon's treasure and escape alive
# Conflict: Puzzles, locked doors, and a dragon!

# --- 2. THE MAP ---
# Here is a map of the game rooms:
#
#     [Tower]
#        |
#  [Library] -- [Great Hall] -- [Kitchen]
#                    |
#               [Dungeon]
#                    |
#            [Dragon's Lair]

# --- 3. THE ROOMS ---
game_rooms = {
    "Great Hall": {
        "description": "A large hall with stone walls and a roaring fireplace.",
        "items": ["torch"],
        "exits": {"north": "Library", "east": "Kitchen", "south": "Dungeon"},
    },
    "Library": {
        "description": "Shelves of dusty books fill the room. One book glows faintly.",
        "items": ["magic book"],
        "exits": {"south": "Great Hall", "up": "Tower"},
    },
    "Tower": {
        "description": "You can see the entire kingdom from up here! A key hangs on a hook.",
        "items": ["golden key"],
        "exits": {"down": "Library"},
    },
    "Kitchen": {
        "description": "Pots and pans everywhere. Something smells delicious!",
        "items": ["health potion"],
        "exits": {"west": "Great Hall"},
    },
    "Dungeon": {
        "description": "Dark and cold. You hear growling from deeper below.",
        "items": ["shield"],
        "exits": {"north": "Great Hall", "south": "Dragon's Lair"},
    },
    "Dragon's Lair": {
        "description": "A massive dragon guards a pile of gold and gems!",
        "items": ["treasure chest"],
        "exits": {"north": "Dungeon"},
    },
}

# --- 4. THE ITEMS ---
game_items = {
    "torch": "Lights up dark rooms.",
    "magic book": "Contains a spell to put the dragon to sleep.",
    "golden key": "Opens the treasure chest.",
    "health potion": "Restores 50 health points.",
    "shield": "Protects you from one dragon attack.",
    "treasure chest": "The dragon's treasure! (Need the golden key to open)",
}

# --- 5. THE PLAYER ---
player = {
    "health": 100,
    "inventory": [],
    "current_room": "Great Hall",
    "score": 0,
}

# --- Display the design ---
print("GAME: The Dragon's Treasure")
print()
print("STORY: You are a brave knight who must find the")
print("dragon's treasure and escape the castle alive!")
print()

print("ROOMS:")
for room_name, room_data in game_rooms.items():
    print(f"  [{room_name}]")
    print(f"    {room_data['description']}")
    print(f"    Items: {room_data['items']}")
    exits = ", ".join([f"{d}: {r}" for d, r in room_data['exits'].items()])
    print(f"    Exits: {exits}")
    print()

print("ITEMS:")
for item, desc in game_items.items():
    print(f"  {item}: {desc}")
print()

print("PLAYER STARTS WITH:")
print(f"  Health: {player['health']}")
print(f"  Room: {player['current_room']}")
print(f"  Inventory: (empty)")
print()

print("Now it's YOUR turn! Open my_game_plan.py")
print("and plan your own game!")

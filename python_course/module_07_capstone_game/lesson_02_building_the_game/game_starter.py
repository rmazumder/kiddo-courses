"""
==============================================
  MODULE 7 - LESSON 2: Game Starter
  A WORKING Text-Based Adventure Game!
==============================================

This is a complete, working adventure game.
Run it, play it, and study how it works!

Then modify it or build your own from scratch!

COMMANDS:
  go [direction]  - Move to another room (north, south, east, west, up, down)
  look            - Look around the current room
  take [item]     - Pick up an item
  use [item]      - Use an item from your inventory
  inventory       - Check what you are carrying
  health          - Check your health
  help            - Show available commands
  quit            - Exit the game
"""

import random
import time


# ============================================================
# GAME DATA
# ============================================================

def create_rooms():
    """Create and return all the game rooms."""
    rooms = {
        "Great Hall": {
            "description": "You stand in a grand hall with stone walls and a roaring fireplace. "
                          "Faded tapestries hang on the walls, showing ancient battles. "
                          "A chandelier flickers above.",
            "items": ["torch"],
            "exits": {"north": "Library", "east": "Kitchen", "south": "Dungeon"},
        },
        "Library": {
            "description": "Towering bookshelves line every wall. Dust motes float in "
                          "the dim light. One book on the table glows with a faint blue light.",
            "items": ["magic book"],
            "exits": {"south": "Great Hall", "up": "Tower"},
        },
        "Tower": {
            "description": "You climb to the top of the tower. The wind howls around you. "
                          "You can see the entire kingdom from here! A golden key "
                          "hangs on a hook by the window.",
            "items": ["golden key"],
            "exits": {"down": "Library"},
        },
        "Kitchen": {
            "description": "Pots and pans are scattered everywhere. A cauldron bubbles "
                          "on the stove. It smells like... chicken soup? A small vial "
                          "of red liquid sits on the counter.",
            "items": ["health potion"],
            "exits": {"west": "Great Hall"},
        },
        "Dungeon": {
            "description": "Cold, dark, and damp. Water drips from the ceiling. "
                          "Rusty chains hang from the walls. You hear a deep growling "
                          "sound from somewhere below. A sturdy shield leans against the wall.",
            "items": ["shield"],
            "exits": {"north": "Great Hall", "south": "Dragon's Lair"},
        },
        "Dragon's Lair": {
            "description": "A MASSIVE red dragon sits atop a mountain of gold coins! "
                          "Its yellow eyes stare at you. Smoke curls from its nostrils. "
                          "Behind it, you can see a glittering treasure chest.",
            "items": ["treasure chest"],
            "exits": {"north": "Dungeon"},
            "has_dragon": True,
            "dragon_awake": True,
        },
    }
    return rooms


def create_player():
    """Create and return the player data."""
    player = {
        "health": 100,
        "max_health": 100,
        "inventory": [],
        "current_room": "Great Hall",
        "score": 0,
        "has_treasure": False,
        "has_shield_active": False,
    }
    return player


# ============================================================
# GAME FUNCTIONS
# ============================================================

def show_room(rooms, player):
    """Display the current room's description and items."""
    room_name = player["current_room"]
    room = rooms[room_name]

    print()
    print("=" * 50)
    print(f"  {room_name}")
    print("=" * 50)
    print()
    print(room["description"])
    print()

    # Show items in the room
    if room["items"]:
        print("You see:")
        for item in room["items"]:
            print(f"  - {item}")
        print()

    # Show exits
    exits = ", ".join(room["exits"].keys())
    print(f"Exits: {exits}")


def move_player(rooms, player, direction):
    """Move the player in the given direction."""
    room = rooms[player["current_room"]]

    if direction in room["exits"]:
        new_room = room["exits"][direction]
        player["current_room"] = new_room
        print(f"\nYou go {direction}...")

        # Check for dragon encounter
        if rooms[new_room].get("has_dragon") and rooms[new_room].get("dragon_awake"):
            dragon_encounter(rooms, player)
        else:
            show_room(rooms, player)
    else:
        print(f"\nYou can't go {direction} from here.")


def take_item(rooms, player, item_name):
    """Pick up an item from the current room."""
    room = rooms[player["current_room"]]

    if item_name in room["items"]:
        # Special case: treasure chest needs golden key
        if item_name == "treasure chest":
            if "golden key" in player["inventory"]:
                room["items"].remove(item_name)
                player["has_treasure"] = True
                player["score"] += 100
                print("\nYou use the GOLDEN KEY to open the treasure chest!")
                print("Inside you find gold, gems, and a crown!")
                print("YOU FOUND THE TREASURE! +100 points!")
            else:
                print("\nThe treasure chest is locked! You need a key...")
            return

        room["items"].remove(item_name)
        player["inventory"].append(item_name)
        player["score"] += 10
        print(f"\nYou picked up the {item_name}! +10 points!")
    else:
        print(f"\nThere is no '{item_name}' here.")


def use_item(rooms, player, item_name):
    """Use an item from the inventory."""
    if item_name not in player["inventory"]:
        print(f"\nYou don't have a '{item_name}'.")
        return

    if item_name == "health potion":
        player["inventory"].remove(item_name)
        old_health = player["health"]
        player["health"] = min(player["health"] + 50, player["max_health"])
        healed = player["health"] - old_health
        print(f"\nYou drink the health potion! +{healed} HP!")
        print(f"Health: {player['health']}/{player['max_health']}")

    elif item_name == "magic book":
        if player["current_room"] == "Dragon's Lair":
            rooms["Dragon's Lair"]["dragon_awake"] = False
            print("\nYou read the magic spell from the book!")
            print("The dragon's eyes grow heavy... it falls asleep!")
            print("Zzzzzzz... The dragon is sleeping!")
            player["score"] += 50
        else:
            print("\nYou read the magic book. It contains a sleep spell.")
            print("This might be useful against something big and scary...")

    elif item_name == "shield":
        player["has_shield_active"] = True
        player["inventory"].remove(item_name)
        print("\nYou raise the shield! It will protect you from one attack.")

    elif item_name == "torch":
        print("\nThe torch flickers with warm light.")
        print("It helps you see in dark places.")

    else:
        print(f"\nYou can't figure out how to use the {item_name}.")


def show_inventory(player):
    """Display the player's inventory."""
    print("\n--- Your Inventory ---")
    if player["inventory"]:
        for item in player["inventory"]:
            print(f"  - {item}")
    else:
        print("  (empty)")
    print()
    print(f"Health: {player['health']}/{player['max_health']}")
    print(f"Score: {player['score']}")


def dragon_encounter(rooms, player):
    """Handle the dragon encounter."""
    print()
    print("!" * 50)
    print("  A DRAGON APPEARS!")
    print("!" * 50)
    print()
    print("The dragon ROARS and breathes fire at you!")

    if player["has_shield_active"]:
        print("Your SHIELD blocks the fire! The shield shatters.")
        player["has_shield_active"] = False
        print("You survived, but the dragon is still awake!")
    else:
        damage = random.randint(20, 40)
        player["health"] -= damage
        print(f"OUCH! You take {damage} damage!")
        print(f"Health: {player['health']}/{player['max_health']}")

    if player["health"] <= 0:
        print("\nYour health has reached 0...")
        return

    print()
    print("TIP: Maybe there is something in the castle")
    print("that can help you deal with this dragon?")
    show_room(rooms, player)


def show_help():
    """Display available commands."""
    print()
    print("--- Available Commands ---")
    print("  go [direction]  - Move (north, south, east, west, up, down)")
    print("  look            - Look around the room")
    print("  take [item]     - Pick up an item")
    print("  use [item]      - Use an item from your inventory")
    print("  inventory       - Check your items and stats")
    print("  health          - Check your health")
    print("  help            - Show this help message")
    print("  quit            - Exit the game")
    print()


def check_win(player):
    """Check if the player has won."""
    if player["has_treasure"] and player["current_room"] == "Great Hall":
        return True
    return False


# ============================================================
# MAIN GAME LOOP
# ============================================================

def play_game():
    """Main game function."""
    rooms = create_rooms()
    player = create_player()

    # Title screen
    print()
    print("=" * 50)
    print("       THE DRAGON'S TREASURE")
    print("    A Text-Based Adventure Game")
    print("=" * 50)
    print()
    print("You are a brave knight who has entered a")
    print("mysterious castle. Legend says a dragon")
    print("guards a fantastic treasure deep below.")
    print()
    print("Your quest: Find the treasure and escape!")
    print()
    print("Type 'help' for a list of commands.")

    # Show the starting room
    show_room(rooms, player)

    # Main game loop
    game_over = False

    while not game_over:
        # Check win condition
        if check_win(player):
            print()
            print("*" * 50)
            print("  CONGRATULATIONS! YOU WIN!")
            print("*" * 50)
            print()
            print("You escaped the castle with the dragon's treasure!")
            print(f"Final Score: {player['score']}")
            print()
            print("You are a true hero!")
            game_over = True
            break

        # Check lose condition
        if player["health"] <= 0:
            print()
            print("X" * 50)
            print("  GAME OVER")
            print("X" * 50)
            print()
            print("The dragon was too powerful...")
            print(f"Final Score: {player['score']}")
            print("Try again and use your items wisely!")
            game_over = True
            break

        # Get player command
        try:
            command = input("\n> ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye, brave knight!")
            break

        if not command:
            continue

        # Parse the command
        parts = command.split(" ", 1)
        action = parts[0]
        target = parts[1] if len(parts) > 1 else ""

        # Handle commands
        if action == "go":
            if target:
                move_player(rooms, player, target)
            else:
                print("Go where? (north, south, east, west, up, down)")

        elif action == "look":
            show_room(rooms, player)

        elif action == "take":
            if target:
                take_item(rooms, player, target)
            else:
                print("Take what?")

        elif action == "use":
            if target:
                use_item(rooms, player, target)
            else:
                print("Use what?")

        elif action == "inventory" or action == "inv" or action == "i":
            show_inventory(player)

        elif action == "health" or action == "hp":
            print(f"\nHealth: {player['health']}/{player['max_health']}")

        elif action == "help" or action == "h":
            show_help()

        elif action == "quit" or action == "q" or action == "exit":
            print("Goodbye, brave knight! See you next time!")
            game_over = True

        elif action in ["north", "south", "east", "west", "up", "down"]:
            move_player(rooms, player, action)

        else:
            print(f"I don't understand '{command}'. Type 'help' for commands.")


# ============================================================
# START THE GAME!
# ============================================================

if __name__ == "__main__":
    play_game()

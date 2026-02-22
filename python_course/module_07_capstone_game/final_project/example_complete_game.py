"""
==============================================
  EXAMPLE COMPLETE GAME:
  "THE LOST SPACE STATION"
==============================================

This is a COMPLETE, WORKING example game that
shows what your final project could look like.

Run this file to play!

This game uses ALL the skills from the course:
- Variables & Data Types (Module 2)
- If/Elif/Else Decisions (Module 3)
- Loops (Module 4)
- Functions (Module 5)
- Lists (Module 6)
"""

import random
import time


# ============================================================
# GAME DATA
# ============================================================

def create_rooms():
    """Create all the rooms on the space station."""
    return {
        "Control Room": {
            "description": (
                "Blinking lights and screens fill the room. "
                "The main computer displays a warning: "
                "'OXYGEN LEVEL LOW -- FIND THE REPAIR KIT!' "
                "A door leads south to the hallway."
            ),
            "items": ["flashlight"],
            "exits": {"south": "Hallway"},
        },
        "Hallway": {
            "description": (
                "A long, dimly lit corridor stretches in both directions. "
                "Emergency lights flash red. You hear a strange hissing "
                "sound from somewhere."
            ),
            "items": [],
            "exits": {
                "north": "Control Room",
                "east": "Lab",
                "west": "Living Quarters",
                "south": "Cargo Bay",
            },
        },
        "Lab": {
            "description": (
                "A science lab with beakers and microscopes. "
                "Most of the equipment is floating -- the gravity "
                "generator must be malfunctioning! A first aid kit "
                "sits on a shelf."
            ),
            "items": ["first aid kit", "keycard"],
            "exits": {"west": "Hallway"},
        },
        "Living Quarters": {
            "description": (
                "Bunk beds and personal lockers line the walls. "
                "A family photo floats in zero gravity. "
                "Someone left their space suit here!"
            ),
            "items": ["space suit"],
            "exits": {"east": "Hallway"},
        },
        "Cargo Bay": {
            "description": (
                "A huge room full of shipping containers. "
                "One container is open, revealing a repair kit! "
                "The airlock door to the south needs a keycard."
            ),
            "items": ["repair kit"],
            "exits": {"north": "Hallway", "south": "Airlock"},
            "locked_exits": {"south": "keycard"},
        },
        "Airlock": {
            "description": (
                "The airlock chamber. Through the small window, "
                "you can see the escape pod docked outside. "
                "If you have the repair kit, you can fix the "
                "oxygen system from here... or just escape!"
            ),
            "items": [],
            "exits": {"north": "Cargo Bay"},
            "is_airlock": True,
        },
    }


def create_player():
    """Create the player with starting stats."""
    return {
        "health": 100,
        "max_health": 100,
        "oxygen": 100,
        "inventory": [],
        "current_room": "Control Room",
        "score": 0,
        "turns": 0,
        "wearing_suit": False,
        "station_fixed": False,
    }


# ============================================================
# DISPLAY FUNCTIONS
# ============================================================

def show_title():
    """Display the title screen."""
    print()
    print("*" * 50)
    print("*" + " " * 48 + "*")
    print("*     THE LOST SPACE STATION                  *")
    print("*     A Python Quest Adventure                *")
    print("*" + " " * 48 + "*")
    print("*" * 50)
    print()
    print("You wake up on an abandoned space station.")
    print("The oxygen system is failing!")
    print("You must find the repair kit to fix it,")
    print("or find the escape pod to get out alive!")
    print()
    print("Type 'help' for a list of commands.")


def show_status(player):
    """Display the player's status bar."""
    h = player["health"]
    o = player["oxygen"]
    s = player["score"]
    t = player["turns"]

    # Health bar
    h_bar = "#" * (h // 10) + "-" * (10 - h // 10)
    o_bar = "#" * (o // 10) + "-" * (10 - o // 10)

    print(f"  HP:[{h_bar}] {h}  O2:[{o_bar}] {o}  Score:{s}  Turn:{t}")


def show_room(rooms, player):
    """Display the current room."""
    room_name = player["current_room"]
    room = rooms[room_name]

    print()
    print("-" * 50)
    print(f"  [{room_name}]")
    print("-" * 50)
    show_status(player)
    print()
    print(room["description"])

    if room["items"]:
        print()
        print("You see:")
        for item in room["items"]:
            print(f"  * {item}")

    exits_list = ", ".join(room["exits"].keys())
    print()
    print(f"Exits: {exits_list}")


def show_help():
    """Display help text."""
    print()
    print("=== COMMANDS ===")
    print("  go [direction]  - Move (north/south/east/west)")
    print("  look            - Look around")
    print("  take [item]     - Pick up an item")
    print("  use [item]      - Use an item")
    print("  inventory       - Check your items")
    print("  status          - View your stats")
    print("  help            - Show commands")
    print("  quit            - Exit game")
    print()


# ============================================================
# ACTION FUNCTIONS
# ============================================================

def move_player(rooms, player, direction):
    """Move the player to a new room."""
    room = rooms[player["current_room"]]

    if direction not in room["exits"]:
        print(f"\n  You can't go {direction} from here.")
        return

    target_room = room["exits"][direction]

    # Check for locked doors
    locked = room.get("locked_exits", {})
    if direction in locked:
        required = locked[direction]
        if required not in player["inventory"]:
            print(f"\n  The door is locked! You need a {required}.")
            return
        else:
            print(f"\n  You use the {required} to unlock the door!")

    player["current_room"] = target_room
    print(f"\n  You go {direction}...")
    show_room(rooms, player)


def take_item(rooms, player, item_name):
    """Pick up an item."""
    room = rooms[player["current_room"]]

    # Find the item (case insensitive)
    found = None
    for item in room["items"]:
        if item.lower() == item_name.lower():
            found = item
            break

    if found:
        room["items"].remove(found)
        player["inventory"].append(found)
        player["score"] += 10
        print(f"\n  You picked up: {found}! (+10 points)")
    else:
        print(f"\n  There is no '{item_name}' here.")


def use_item(rooms, player, item_name):
    """Use an item from inventory."""
    # Find the item (case insensitive)
    found = None
    for item in player["inventory"]:
        if item.lower() == item_name.lower():
            found = item
            break

    if not found:
        print(f"\n  You don't have '{item_name}' in your inventory.")
        return

    if found == "first aid kit":
        player["inventory"].remove(found)
        healed = min(50, player["max_health"] - player["health"])
        player["health"] = min(player["health"] + 50, player["max_health"])
        print(f"\n  You use the first aid kit! +{healed} HP!")

    elif found == "space suit":
        player["wearing_suit"] = True
        player["inventory"].remove(found)
        print("\n  You put on the space suit!")
        print("  Your oxygen will deplete much slower now.")

    elif found == "repair kit":
        if player["current_room"] == "Airlock":
            player["station_fixed"] = True
            player["inventory"].remove(found)
            player["score"] += 100
            print("\n  You use the repair kit to fix the oxygen system!")
            print("  The station hums back to life!")
            print("  OXYGEN RESTORED! (+100 points)")
        else:
            print("\n  You need to be at the Airlock to fix the station.")

    elif found == "flashlight":
        print("\n  The flashlight illuminates the area.")
        print("  Everything looks a bit less scary now.")

    else:
        print(f"\n  You can't figure out how to use the {found} here.")


def show_inventory(player):
    """Display inventory."""
    print()
    print("=== INVENTORY ===")
    if player["inventory"]:
        for item in player["inventory"]:
            print(f"  * {item}")
    else:
        print("  (empty)")

    if player["wearing_suit"]:
        print("  [Wearing: Space Suit]")


def random_event(player):
    """Maybe trigger a random event."""
    if random.random() < 0.2:  # 20% chance
        events = [
            "A pipe bursts! You dodge the steam. Lucky!",
            "You find a small oxygen canister! +10 O2!",
            "The station creaks ominously...",
            "A screen flickers: 'SYSTEM FAILURE IMMINENT'",
            "You hear footsteps... but no one is there.",
        ]
        event = random.choice(events)
        print(f"\n  ** {event}")
        if "oxygen canister" in event:
            player["oxygen"] = min(player["oxygen"] + 10, 100)


def update_oxygen(player):
    """Reduce oxygen each turn."""
    if player["station_fixed"]:
        return  # Station is fixed, oxygen is fine

    if player["wearing_suit"]:
        loss = 2  # Suit slows oxygen loss
    else:
        loss = 5  # Without suit, oxygen drops fast

    player["oxygen"] -= loss

    if player["oxygen"] <= 30 and player["oxygen"] > 0:
        print(f"\n  WARNING: Oxygen at {player['oxygen']}%!")
    elif player["oxygen"] <= 0:
        player["oxygen"] = 0


# ============================================================
# WIN/LOSE CHECKS
# ============================================================

def check_game_state(player):
    """Check for win or lose conditions. Returns 'win', 'lose', or 'playing'."""
    # Win: Fixed the station
    if player["station_fixed"]:
        return "win_fix"

    # Win: Escaped via airlock with suit
    if player["current_room"] == "Airlock" and player["wearing_suit"]:
        return "win_escape"

    # Lose: Out of oxygen
    if player["oxygen"] <= 0:
        return "lose_oxygen"

    # Lose: Out of health
    if player["health"] <= 0:
        return "lose_health"

    return "playing"


# ============================================================
# MAIN GAME LOOP
# ============================================================

def play():
    """Main game loop."""
    rooms = create_rooms()
    player = create_player()

    show_title()
    show_room(rooms, player)

    while True:
        state = check_game_state(player)

        if state == "win_fix":
            print()
            print("*" * 50)
            print("  YOU WIN! (Best Ending)")
            print("*" * 50)
            print()
            print("  You fixed the space station!")
            print("  The crew can return safely.")
            print("  You are a HERO!")
            player["score"] += 50
            print(f"  Final Score: {player['score']}")
            print(f"  Turns Used: {player['turns']}")
            break

        elif state == "win_escape":
            print()
            print("*" * 50)
            print("  YOU ESCAPED! (Good Ending)")
            print("*" * 50)
            print()
            print("  You made it to the escape pod!")
            print("  You are safe, but the station is lost...")
            print(f"  Final Score: {player['score']}")
            print(f"  Turns Used: {player['turns']}")
            break

        elif state == "lose_oxygen":
            print()
            print("X" * 50)
            print("  GAME OVER -- OUT OF OXYGEN")
            print("X" * 50)
            print()
            print("  You ran out of air...")
            print("  TIP: Find the space suit to slow oxygen loss!")
            print(f"  Final Score: {player['score']}")
            break

        elif state == "lose_health":
            print()
            print("X" * 50)
            print("  GAME OVER -- HEALTH DEPLETED")
            print("X" * 50)
            print(f"  Final Score: {player['score']}")
            break

        # Get player input
        try:
            raw = input("\n> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye, astronaut!")
            break

        if not raw:
            continue

        command = raw.lower()
        player["turns"] += 1

        # Parse command
        parts = command.split(" ", 1)
        action = parts[0]
        target = parts[1] if len(parts) > 1 else ""

        # Handle commands
        if action == "go" and target:
            move_player(rooms, player, target)
        elif action in ["north", "south", "east", "west", "up", "down"]:
            move_player(rooms, player, action)
        elif action == "look":
            show_room(rooms, player)
        elif action == "take" and target:
            take_item(rooms, player, target)
        elif action == "use" and target:
            use_item(rooms, player, target)
        elif action in ["inventory", "inv", "i"]:
            show_inventory(player)
        elif action in ["status", "stats"]:
            print()
            show_status(player)
        elif action in ["help", "h"]:
            show_help()
        elif action in ["quit", "q", "exit"]:
            print("\nGoodbye, astronaut! See you next mission!")
            break
        else:
            print(f"\n  Unknown command: '{raw}'. Type 'help' for commands.")
            player["turns"] -= 1  # Don't count bad commands
            continue

        # Per-turn events
        update_oxygen(player)
        random_event(player)


# ============================================================
# START!
# ============================================================

if __name__ == "__main__":
    play()

"""
==============================================
  MODULE 7 - LESSON 3: Game Extras
==============================================

Cool features you can add to make your
game even more awesome!

Pick and choose which ones you want to use.
"""

import random
import time

print("=" * 50)
print("  GAME EXTRAS: MAKE IT AWESOME!")
print("=" * 50)
print()

# ============================================================
# EXTRA 1: Slow Text Printing (Typewriter Effect)
# ============================================================
print("--- EXTRA 1: Slow Print ---")


def slow_print(text, delay=0.03):
    """Print text one character at a time, like a typewriter."""
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()  # New line at the end


# slow_print("You enter the dark cave...")  # Uncomment to try!
print("(Uncomment the slow_print line above to see the effect)")
print()

# ============================================================
# EXTRA 2: ASCII Art
# ============================================================
print("--- EXTRA 2: ASCII Art ---")


def show_dragon():
    print(r"""
                 __        __
                /  \      /  \
               / /\ \    / /\ \
              / /  \ \  / /  \ \
             / /    \_\/ /    \ \
            / /          \    /\/
           / /    ()  ()  \  /
          / /     __  __   \/
         / /     /  \/  \
        / /     | [  ]  |
        \/       \  /\  /
                  \/  \/
           THE DRAGON AWAITS!
    """)


def show_treasure():
    print(r"""
         ___________
        /           \
       /  $ $ $ $ $  \
      |  $ $ $ $ $ $  |
      |  $ TREASURE $ |
      |  $ $ $ $ $ $  |
       \  $ $ $ $ $  /
        \___________/
    """)


def show_sword():
    print(r"""
            /|
           / |
          /  |
         /   |
        /    |
       /     |
      /      |
     /       |
     \      /
      \    /
       \  /
        ||
        ||
       ====
       |  |
       |  |
        --
    """)


show_dragon()
show_treasure()
print()

# ============================================================
# EXTRA 3: Random Events
# ============================================================
print("--- EXTRA 3: Random Events ---")


def random_event():
    """Trigger a random event that might help or hurt the player."""
    events = [
        {"text": "You find a gold coin on the ground! +5 points!", "score": 5, "health": 0},
        {"text": "A bat swoops at your head! -5 health!", "score": 0, "health": -5},
        {"text": "You discover a secret passage! +10 points!", "score": 10, "health": 0},
        {"text": "You trip on a loose stone. -3 health!", "score": 0, "health": -3},
        {"text": "A friendly ghost gives you a hint! +5 points!", "score": 5, "health": 0},
        {"text": "Nothing happens. It's eerily quiet...", "score": 0, "health": 0},
    ]

    # 30% chance of a random event occurring
    if random.random() < 0.3:
        event = random.choice(events)
        print(f"  ** RANDOM EVENT: {event['text']}")
        return event
    return None


# Demo random events
print("Testing random events (run several times to see variety):")
for i in range(5):
    result = random_event()
    if result is None:
        print(f"  Turn {i + 1}: No event this turn.")

print()

# ============================================================
# EXTRA 4: Health Bar Display
# ============================================================
print("--- EXTRA 4: Health Bar ---")


def show_health_bar(current, maximum):
    """Display a visual health bar."""
    bar_length = 20
    filled = int(bar_length * current / maximum)
    empty = bar_length - filled

    if current > maximum * 0.6:
        status = "Healthy"
    elif current > maximum * 0.3:
        status = "Wounded"
    else:
        status = "Critical!"

    bar = "#" * filled + "-" * empty
    print(f"  HP: [{bar}] {current}/{maximum} ({status})")


show_health_bar(100, 100)
show_health_bar(65, 100)
show_health_bar(25, 100)
show_health_bar(5, 100)
print()

# ============================================================
# EXTRA 5: Turn Counter and Score Display
# ============================================================
print("--- EXTRA 5: Status Bar ---")


def show_status_bar(turns, score, room):
    """Display a compact status bar."""
    print(f"  Turn: {turns:3d} | Score: {score:4d} | Room: {room}")


show_status_bar(1, 0, "Great Hall")
show_status_bar(15, 120, "Dragon's Lair")
print()

# ============================================================
# EXTRA 6: Simple Riddle/Puzzle System
# ============================================================
print("--- EXTRA 6: Riddles ---")


def ask_riddle():
    """Ask the player a riddle to unlock something."""
    riddles = [
        {
            "question": "I have cities, but no houses.\nI have mountains, but no trees.\nI have water, but no fish.\nWhat am I?",
            "answer": "map",
        },
        {
            "question": "What has keys but no locks?\nWhat has space but no room?\nWhat has a return but no exit?",
            "answer": "keyboard",
        },
        {
            "question": "I speak without a mouth and hear without ears.\nI have no body, but I come alive with wind.\nWhat am I?",
            "answer": "echo",
        },
    ]

    riddle = random.choice(riddles)
    print("  THE SPHINX ASKS:")
    print(f"  {riddle['question']}")
    print(f"  (Answer: {riddle['answer']})")
    return riddle


ask_riddle()
print()

# ============================================================
# EXTRA 7: Multiple Difficulty Levels
# ============================================================
print("--- EXTRA 7: Difficulty Levels ---")


def get_difficulty_settings(level):
    """Return game settings based on difficulty."""
    settings = {
        "easy": {"health": 150, "damage_mult": 0.5, "hints": True},
        "medium": {"health": 100, "damage_mult": 1.0, "hints": True},
        "hard": {"health": 75, "damage_mult": 1.5, "hints": False},
    }
    return settings.get(level, settings["medium"])


for level in ["easy", "medium", "hard"]:
    s = get_difficulty_settings(level)
    print(f"  {level.upper():8s} -> Health: {s['health']}, "
          f"Damage x{s['damage_mult']}, Hints: {s['hints']}")

print()
print("Pick your favorite extras and add them to your game!")
print()
print("Extra features explorer! +10 XP!")

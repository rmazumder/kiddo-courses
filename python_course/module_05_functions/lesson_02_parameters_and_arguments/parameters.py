"""
==============================================
  MODULE 5 - LESSON 2: Parameters & Arguments
==============================================

Make your functions flexible and reusable!
"""

print("=" * 50)
print("  PARAMETERS: CUSTOMIZE YOUR FUNCTIONS!")
print("=" * 50)
print()

# --------------------------------------------------
# One Parameter
# --------------------------------------------------
print("--- One Parameter ---")


def greet(name):
    """Greet someone by name."""
    print(f"Hello, {name}! Welcome to Python Quest!")


greet("Alex")
greet("Jordan")
greet("Sam")
print()

# --------------------------------------------------
# Multiple Parameters
# --------------------------------------------------
print("--- Multiple Parameters ---")


def introduce(name, age, hobby):
    """Introduce a person."""
    print(f"Meet {name}! They are {age} years old and love {hobby}.")


introduce("Luna", 10, "painting")
introduce("Max", 12, "soccer")
print()

# --------------------------------------------------
# Parameters with Math
# --------------------------------------------------
print("--- Math Functions ---")


def add(a, b):
    """Add two numbers and print the result."""
    result = a + b
    print(f"{a} + {b} = {result}")


def multiply(a, b):
    print(f"{a} x {b} = {a * b}")


add(5, 3)
add(100, 200)
multiply(7, 8)
print()

# --------------------------------------------------
# Default Values
# --------------------------------------------------
print("--- Default Values ---")


# You can give parameters a DEFAULT value.
# If someone doesn't provide an argument, the default is used.
def power_up(player, boost=10):
    """Give a player a power boost."""
    print(f"{player} gets a +{boost} power boost!")


power_up("Warrior")          # Uses default: boost=10
power_up("Mage", 25)         # Override: boost=25
power_up("Archer", 15)       # Override: boost=15
print()

# --------------------------------------------------
# Functions Calling Functions!
# --------------------------------------------------
print("--- Functions Calling Functions ---")


def draw_line(length=20, char="-"):
    print(char * length)


def draw_box(title):
    draw_line(30, "=")
    print(f"  {title}")
    draw_line(30, "=")


draw_box("LEVEL COMPLETE!")
print()
draw_box("NEW HIGH SCORE!")
print()

# --------------------------------------------------
# Fun Example: Character Creator
# --------------------------------------------------
print("--- Character Creator ---")


def create_character(name, character_class, health=100, attack=10):
    print(f"  Name:   {name}")
    print(f"  Class:  {character_class}")
    print(f"  Health: {'*' * (health // 10)} ({health} HP)")
    print(f"  Attack: {'!' * attack} ({attack} ATK)")
    print()


create_character("Shadowblade", "Rogue", 80, 15)
create_character("Ironshield", "Knight", 150, 8)
create_character("Starweaver", "Mage", 60, 20)

print("Parameter pro! +10 XP!")

"""
========================================
  PYTHON QUEST -- Progress Tracker
========================================

Run this file to track your XP and badges
as you complete the Python Quest course!

How to use:
  1. Run this file: python progress_tracker.py
  2. Follow the menu to log your progress
  3. See how much XP you have earned!

"""

# ============================================================
# Your Progress Data
# (You can edit these as you complete lessons!)
# ============================================================

# Set each to True when you complete it
progress = {
    # --- Module 1: Welcome to Python! ---
    "m1_lesson1_what_is_programming": False,
    "m1_lesson2_setup_python": False,
    "m1_lesson3_hello_world": False,
    "m1_quiz": False,
    "m1_challenge": False,

    # --- Module 2: Variables & Data Types ---
    "m2_lesson1_what_are_variables": False,
    "m2_lesson2_numbers": False,
    "m2_lesson3_strings": False,
    "m2_lesson4_booleans": False,
    "m2_quiz": False,
    "m2_challenge": False,

    # --- Module 3: Making Decisions ---
    "m3_lesson1_if_statements": False,
    "m3_lesson2_else_and_elif": False,
    "m3_lesson3_comparisons_and_logic": False,
    "m3_quiz": False,
    "m3_challenge": False,

    # --- Module 4: Loops & Repetition ---
    "m4_lesson1_for_loops": False,
    "m4_lesson2_while_loops": False,
    "m4_lesson3_loop_patterns": False,
    "m4_quiz": False,
    "m4_challenge": False,

    # --- Module 5: Functions ---
    "m5_lesson1_what_are_functions": False,
    "m5_lesson2_parameters_and_arguments": False,
    "m5_lesson3_return_values": False,
    "m5_quiz": False,
    "m5_challenge": False,

    # --- Module 6: Lists & Collections ---
    "m6_lesson1_what_are_lists": False,
    "m6_lesson2_list_operations": False,
    "m6_lesson3_loops_and_lists": False,
    "m6_quiz": False,
    "m6_challenge": False,

    # --- Module 7: Capstone Game ---
    "m7_lesson1_game_design": False,
    "m7_lesson2_building_the_game": False,
    "m7_lesson3_polish_and_extras": False,
    "m7_final_project": False,
}

# ============================================================
# XP Values
# ============================================================
XP_LESSON = 10
XP_QUIZ = 20
XP_CHALLENGE = 30
XP_CAPSTONE = 100

# ============================================================
# Badge Definitions
# ============================================================
badges = {
    1: {"name": "Starter Spark",    "icon": "[*]", "requires": ["m1_lesson1_what_is_programming", "m1_lesson2_setup_python", "m1_lesson3_hello_world", "m1_quiz", "m1_challenge"]},
    2: {"name": "Data Wizard",      "icon": "[~]", "requires": ["m2_lesson1_what_are_variables", "m2_lesson2_numbers", "m2_lesson3_strings", "m2_lesson4_booleans", "m2_quiz", "m2_challenge"]},
    3: {"name": "Decision Master",  "icon": "[?]", "requires": ["m3_lesson1_if_statements", "m3_lesson2_else_and_elif", "m3_lesson3_comparisons_and_logic", "m3_quiz", "m3_challenge"]},
    4: {"name": "Loop Legend",      "icon": "[O]", "requires": ["m4_lesson1_for_loops", "m4_lesson2_while_loops", "m4_lesson3_loop_patterns", "m4_quiz", "m4_challenge"]},
    5: {"name": "Function Hero",    "icon": "[f]", "requires": ["m5_lesson1_what_are_functions", "m5_lesson2_parameters_and_arguments", "m5_lesson3_return_values", "m5_quiz", "m5_challenge"]},
    6: {"name": "List Ninja",       "icon": "[#]", "requires": ["m6_lesson1_what_are_lists", "m6_lesson2_list_operations", "m6_lesson3_loops_and_lists", "m6_quiz", "m6_challenge"]},
    7: {"name": "Game Creator",     "icon": "[G]", "requires": ["m7_lesson1_game_design", "m7_lesson2_building_the_game", "m7_lesson3_polish_and_extras", "m7_final_project"]},
}


def calculate_xp():
    """Calculate total XP earned so far."""
    total = 0
    for key, done in progress.items():
        if done:
            if "quiz" in key:
                total += XP_QUIZ
            elif "challenge" in key:
                total += XP_CHALLENGE
            elif "final_project" in key:
                total += XP_CAPSTONE
            else:
                total += XP_LESSON

    return total


def get_max_xp():
    """Calculate the maximum possible XP."""
    total = 0
    for key in progress:
        if "quiz" in key:
            total += XP_QUIZ
        elif "challenge" in key:
            total += XP_CHALLENGE
        elif "final_project" in key:
            total += XP_CAPSTONE
        else:
            total += XP_LESSON
    return total


def check_badges():
    """Check which badges have been earned."""
    earned = []
    for module_num, badge_info in badges.items():
        all_done = all(progress.get(req, False) for req in badge_info["requires"])
        earned.append({
            "module": module_num,
            "name": badge_info["name"],
            "icon": badge_info["icon"],
            "earned": all_done,
        })
    return earned


def display_progress():
    """Display a beautiful progress report."""
    xp = calculate_xp()
    max_xp = get_max_xp()
    badge_list = check_badges()
    earned_count = sum(1 for b in badge_list if b["earned"])

    print()
    print("=" * 50)
    print("    PYTHON QUEST -- Your Progress Report")
    print("=" * 50)
    print()

    # XP Bar
    bar_length = 30
    filled = int(bar_length * xp / max_xp) if max_xp > 0 else 0
    bar = "#" * filled + "-" * (bar_length - filled)
    print(f"  XP: [{bar}] {xp}/{max_xp}")
    print()

    # Badges
    print("  BADGES EARNED:")
    print("  " + "-" * 40)
    for b in badge_list:
        status = b["icon"] + " EARNED!" if b["earned"] else "[ ] not yet..."
        print(f"    Module {b['module']}: {b['name']:20s} {status}")
    print("  " + "-" * 40)
    print(f"  Total Badges: {earned_count} / {len(badge_list)}")
    print()

    # Champion check
    if earned_count == len(badge_list):
        print("  ***********************************************")
        print("  *                                             *")
        print("  *   YOU ARE A PYTHON QUEST CHAMPION!!!        *")
        print("  *   You completed the entire course!          *")
        print("  *   Amazing work, coder!                      *")
        print("  *                                             *")
        print("  ***********************************************")
    else:
        next_module = None
        for b in badge_list:
            if not b["earned"]:
                next_module = b
                break
        if next_module:
            print(f"  Next goal: Earn the '{next_module['name']}' badge!")
            print(f"  Keep going -- you are doing great!")

    print()
    print("=" * 50)


def mark_complete():
    """Interactive menu to mark items as complete."""
    items = list(progress.keys())
    print()
    print("Which item did you complete?")
    print("-" * 40)
    for i, item in enumerate(items):
        status = "[X]" if progress[item] else "[ ]"
        display_name = item.replace("_", " ").replace("m1 ", "M1: ").replace("m2 ", "M2: ").replace("m3 ", "M3: ").replace("m4 ", "M4: ").replace("m5 ", "M5: ").replace("m6 ", "M6: ").replace("m7 ", "M7: ")
        print(f"  {i + 1:2d}. {status} {display_name}")

    print()
    try:
        choice = int(input("Enter the number (or 0 to go back): "))
        if 1 <= choice <= len(items):
            key = items[choice - 1]
            progress[key] = True
            print(f"  Marked '{key}' as complete! Great job!")
        elif choice == 0:
            print("  Going back...")
        else:
            print("  Invalid number. Try again!")
    except ValueError:
        print("  Please enter a number!")


def main():
    """Main menu for the progress tracker."""
    print()
    print("=" * 50)
    print("    PYTHON QUEST -- Progress Tracker")
    print("=" * 50)
    print()
    print("  1. View my progress")
    print("  2. Mark something as complete")
    print("  3. Quit")
    print()

    while True:
        try:
            choice = input("Choose an option (1/2/3): ").strip()
            if choice == "1":
                display_progress()
            elif choice == "2":
                mark_complete()
            elif choice == "3":
                print("  Keep coding, adventurer! See you next time!")
                break
            else:
                print("  Please enter 1, 2, or 3.")
        except KeyboardInterrupt:
            print("\n  Bye! Keep coding!")
            break


if __name__ == "__main__":
    main()

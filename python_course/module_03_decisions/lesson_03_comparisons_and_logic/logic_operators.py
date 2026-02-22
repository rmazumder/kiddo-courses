"""
==============================================
  MODULE 3 - LESSON 3: Logic Operators
==============================================

Combine conditions like a master strategist!
"""

print("=" * 50)
print("  LOGIC OPERATORS: AND, OR, NOT")
print("=" * 50)
print()

# --------------------------------------------------
# AND -- Both conditions must be True
# --------------------------------------------------
print("--- AND ---")
print("Think: 'I need BOTH of these to be true.'")
print()

age = 10
height = 130  # cm

# To ride, you must be at least 8 AND at least 120cm tall
if age >= 8 and height >= 120:
    print(f"Age {age}, Height {height}cm -- You CAN ride!")
else:
    print(f"Age {age}, Height {height}cm -- Sorry, you can't ride yet.")

# What about someone too short?
age2 = 12
height2 = 110

if age2 >= 8 and height2 >= 120:
    print(f"Age {age2}, Height {height2}cm -- You CAN ride!")
else:
    print(f"Age {age2}, Height {height2}cm -- Sorry, not tall enough.")

print()

# --------------------------------------------------
# OR -- At least one condition must be True
# --------------------------------------------------
print("--- OR ---")
print("Think: 'I need AT LEAST ONE of these to be true.'")
print()

day = "Saturday"

if day == "Saturday" or day == "Sunday":
    print(f"{day} -- It's the weekend! Time to relax.")
else:
    print(f"{day} -- It's a school day. Time to learn!")

day2 = "Wednesday"
if day2 == "Saturday" or day2 == "Sunday":
    print(f"{day2} -- It's the weekend!")
else:
    print(f"{day2} -- It's a school day.")

print()

# --------------------------------------------------
# NOT -- Flips True/False
# --------------------------------------------------
print("--- NOT ---")
print("Think: 'Flip it! True becomes False, False becomes True.'")
print()

is_raining = False
print(f"Is it raining? {is_raining}")
print(f"Is it NOT raining? {not is_raining}")

if not is_raining:
    print("No rain! Let's play outside!")

print()

# --------------------------------------------------
# Combining Multiple Operators
# --------------------------------------------------
print("--- Combining Operators ---")

# A student can go on the field trip if:
# - They have permission AND
# - They have paid AND
# - They are NOT sick

has_permission = True
has_paid = True
is_sick = False

if has_permission and has_paid and not is_sick:
    print("You can go on the field trip!")
else:
    print("Sorry, you can't go this time.")

print()

# --------------------------------------------------
# Fun Example: Can You Adopt a Pet?
# --------------------------------------------------
print("--- Can You Adopt a Pet? ---")

your_age = 12
has_parent_permission = True
has_allergies = False
has_yard = True

if your_age >= 10 and has_parent_permission and not has_allergies:
    print("You can adopt a pet!")
    if has_yard:
        print("You have a yard -- a dog would be great!")
    else:
        print("No yard -- maybe a cat or hamster?")
else:
    if not has_parent_permission:
        print("Ask your parents first!")
    elif has_allergies:
        print("Maybe a fish? No allergies with fish!")
    else:
        print("Wait until you're a bit older.")

print()
print("Logic master! +10 XP!")

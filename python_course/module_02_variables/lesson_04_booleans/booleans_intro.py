"""
==============================================
  MODULE 2 - LESSON 4: Booleans (True/False)
==============================================

Booleans are like light switches -- ON or OFF,
True or False. Let's explore!
"""

print("=" * 50)
print("  BOOLEANS: TRUE OR FALSE!")
print("=" * 50)
print()

# --------------------------------------------------
# Creating Booleans
# --------------------------------------------------
print("--- Creating Booleans ---")

is_sunny = True
is_raining = False

print(f"Is it sunny? {is_sunny}")
print(f"Is it raining? {is_raining}")
print()

# IMPORTANT: True and False must start with a CAPITAL letter!
# true (lowercase) would cause an error.

# --------------------------------------------------
# Comparison Operators -- They Create Booleans!
# --------------------------------------------------
print("--- Comparison Operators ---")
print("These compare two values and give True or False:")
print()

# == means "is equal to?" (two equals signs, not one!)
print(f"5 == 5  -->  {5 == 5}")       # True
print(f"5 == 3  -->  {5 == 3}")       # False
print()

# != means "is NOT equal to?"
print(f"5 != 3  -->  {5 != 3}")       # True
print(f"5 != 5  -->  {5 != 5}")       # False
print()

# > means "is greater than?"
# < means "is less than?"
print(f"10 > 3  -->  {10 > 3}")       # True
print(f"3 > 10  -->  {3 > 10}")       # False
print(f"3 < 10  -->  {3 < 10}")       # True
print()

# >= means "is greater than or equal to?"
# <= means "is less than or equal to?"
print(f"5 >= 5  -->  {5 >= 5}")       # True
print(f"5 >= 6  -->  {5 >= 6}")       # False
print(f"3 <= 5  -->  {3 <= 5}")       # True
print()

# --------------------------------------------------
# Comparing Strings
# --------------------------------------------------
print("--- Comparing Strings ---")
name = "Python"
print(f"name == 'Python' -->  {name == 'Python'}")   # True
print(f"name == 'python' -->  {name == 'python'}")   # False (case matters!)
print()

# --------------------------------------------------
# Storing Comparisons in Variables
# --------------------------------------------------
print("--- Storing Comparisons ---")
age = 10
is_teenager = age >= 13
print(f"Age: {age}")
print(f"Is a teenager (age >= 13)? {is_teenager}")    # False

score = 95
passed = score >= 60
got_A = score >= 90
print(f"Score: {score}")
print(f"Passed (>= 60)? {passed}")     # True
print(f"Got an A (>= 90)? {got_A}")    # True
print()

# --------------------------------------------------
# The type() Function
# --------------------------------------------------
print("--- Checking Types ---")
print(f"Type of 42:       {type(42).__name__}")        # int
print(f"Type of 3.14:     {type(3.14).__name__}")      # float
print(f"Type of 'hello':  {type('hello').__name__}")   # str
print(f"Type of True:     {type(True).__name__}")      # bool
print()

# --------------------------------------------------
# Fun Example: Is It Bedtime?
# --------------------------------------------------
print("--- Is It Bedtime? ---")
current_hour = 21  # 9 PM (using 24-hour time)
bedtime_hour = 20  # 8 PM

past_bedtime = current_hour >= bedtime_hour
print(f"Current time: {current_hour}:00")
print(f"Bedtime: {bedtime_hour}:00")
print(f"Past bedtime? {past_bedtime}")
print()

print("Boolean genius! +10 XP!")

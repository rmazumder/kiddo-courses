"""
==============================================
  MODULE 2 - LESSON 2: Numbers & Math
==============================================

Python is an amazing calculator!
Run this file to see math in action.
"""

print("=" * 50)
print("  PYTHON: THE SUPER CALCULATOR")
print("=" * 50)
print()

# --------------------------------------------------
# Basic Math
# --------------------------------------------------
print("--- Basic Math ---")
print("5 + 3  =", 5 + 3)       # Addition
print("10 - 4 =", 10 - 4)      # Subtraction
print("3 * 7  =", 3 * 7)       # Multiplication
print("15 / 3 =", 15 / 3)      # Division (always gives a float!)
print()

# --------------------------------------------------
# Saving Results in Variables
# --------------------------------------------------
print("--- Saving Results ---")
apples = 12
apples_eaten = 3
apples_left = apples - apples_eaten
print(f"I had {apples} apples.")
print(f"I ate {apples_eaten}.")
print(f"I have {apples_left} left!")
print()

# --------------------------------------------------
# More Math Operations
# --------------------------------------------------
print("--- More Operations ---")
print("2 ** 3 =", 2 ** 3)      # 2 to the power of 3 = 8
print("2 ** 10 =", 2 ** 10)    # 2 to the power of 10 = 1024
print("7 // 2 =", 7 // 2)      # Floor division: 7 / 2 = 3 remainder 1, gives 3
print("7 % 2  =", 7 % 2)       # Modulo: gives the remainder, which is 1
print()

# --------------------------------------------------
# Real-World Example: Buying Treats
# --------------------------------------------------
print("--- Real-World Math: Buying Treats ---")
money = 20            # You have $20
candy_price = 3       # Each candy costs $3

candies_you_can_buy = money // candy_price  # Floor division
money_left_over = money % candy_price        # Remainder

print(f"You have ${money}")
print(f"Each candy costs ${candy_price}")
print(f"You can buy {candies_you_can_buy} candies")
print(f"You will have ${money_left_over} left over")
print()

# --------------------------------------------------
# Integers vs. Floats
# --------------------------------------------------
print("--- Integers vs. Floats ---")
whole_number = 42       # This is an integer (int)
decimal_number = 3.14   # This is a float

print(f"{whole_number} is an integer (type: {type(whole_number).__name__})")
print(f"{decimal_number} is a float (type: {type(decimal_number).__name__})")
print()

# Division ALWAYS gives a float, even if the answer is whole:
print("10 / 2 =", 10 / 2)     # Result: 5.0 (a float!)
print("10 // 2 =", 10 // 2)   # Result: 5 (an integer!)
print()

# --------------------------------------------------
# Fun: The input() Function -- Getting Numbers from the User
# --------------------------------------------------
print("--- Interactive Math ---")
print("Let's do some math together!")

# input() gets text from the user
# int() converts that text to a number
try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))

    print(f"{num1} + {num2} = {num1 + num2}")
    print(f"{num1} - {num2} = {num1 - num2}")
    print(f"{num1} * {num2} = {num1 * num2}")

    if num2 != 0:
        print(f"{num1} / {num2} = {num1 / num2}")
    else:
        print("Cannot divide by zero!")
except ValueError:
    print("(Skipping interactive part -- enter numbers when you run this!)")

print()
print("Math mastery! +10 XP!")

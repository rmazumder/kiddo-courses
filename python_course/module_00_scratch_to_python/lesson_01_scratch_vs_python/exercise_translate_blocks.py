"""
===================================================
  Lesson 1: Translate Scratch Blocks to Python!
  Module 0 - From Scratch to Python!
===================================================

YOUR CHALLENGE: Each exercise tells you what the
Scratch block does. Write the Python code to match it!

Fill in every section that says "# YOUR CODE HERE:"
Run the file when you are done to check your work.

You can do this - you already know how from Scratch!
"""

import time


print("=" * 50)
print("  Scratch to Python Exercises!")
print("=" * 50)
print()


# --------------------------------------------------
# Exercise 1: Say Hello
# --------------------------------------------------
# Scratch says: "say 'Hello, World!' for 2 secs"
# That means: show the text "Hello, World!" and pause 2 seconds.
#
# HINT: Use print() and time.sleep()
# TODO: Write the Python code below:

print("Exercise 1:")
# YOUR CODE HERE:


print()


# --------------------------------------------------
# Exercise 2: Set a Variable
# --------------------------------------------------
# Scratch says: "set score to 0"
# That means: create a variable called score and give it the value 0.
#
# HINT: variable_name = value
# TODO: Write the Python code below:

print("Exercise 2:")
# YOUR CODE HERE:

# When you are done, uncomment this line to test it:
# print(f"Score is: {score}")

print()


# --------------------------------------------------
# Exercise 3: Change a Variable
# --------------------------------------------------
# Scratch says:
#   "set lives to 3"
#   "change lives by -1"
#   "say lives"
#
# HINT: Create the variable, then subtract 1, then print it.
# TODO: Write the Python code below:

print("Exercise 3:")
# YOUR CODE HERE:

print()


# --------------------------------------------------
# Exercise 4: Repeat Loop
# --------------------------------------------------
# Scratch says: "repeat 5 { say 'Python is awesome!' }"
# That means: print "Python is awesome!" exactly 5 times.
#
# HINT: for i in range(5):
# TODO: Write the Python code below:

print("Exercise 4:")
# YOUR CODE HERE:

print()


# --------------------------------------------------
# Exercise 5: If Condition
# --------------------------------------------------
# Scratch says: "if <temperature > 30> { say 'It is hot!' }"
# That means: if temperature is greater than 30, print "It is hot!"
#
# Start with temperature = 35 so the condition is True.
# HINT: if temperature > 30:
# TODO: Write the Python code below:

print("Exercise 5:")
temperature = 35
# YOUR CODE HERE:

print()


# --------------------------------------------------
# Exercise 6: Forever Loop (Limited Version)
# --------------------------------------------------
# Scratch says: "forever { say 'Tick!' wait 1 secs }"
# That means: print "Tick!" every second, forever.
#
# We will only do it 4 times so the program ends.
# HINT: Use a for loop with range(4) and time.sleep(1)
# TODO: Write the Python code below:

print("Exercise 6:")
# YOUR CODE HERE:

print()


# --------------------------------------------------
# Exercise 7: If-Else
# --------------------------------------------------
# Scratch says:
#   "if <score >= 50> { say 'You passed!' }
#    else { say 'Try again!' }"
#
# HINT: if score >= 50: ... else: ...
# TODO: Write the Python code below:

print("Exercise 7:")
score = 45   # Change this to 60 after to test the other branch!
# YOUR CODE HERE:

print()


# --------------------------------------------------
# Exercise 8: Define and Call a Function
# --------------------------------------------------
# Scratch says: "define [cheer]" block containing "say 'Hip hip hooray!'"
# Then separately: "broadcast [cheer]"
#
# That means: define a function called cheer() that prints 'Hip hip hooray!'
# Then call that function.
#
# HINT:
#   def cheer():
#       print("Hip hip hooray!")
#   cheer()
# TODO: Write the Python code below (define ABOVE this print line):

print("Exercise 8:")
# YOUR FUNCTION DEFINITION HERE (def cheer):


# YOUR FUNCTION CALL HERE (cheer()):

print()


# --------------------------------------------------
# Exercise 9: Nested Loop (Harder!)
# --------------------------------------------------
# Scratch says:
#   "repeat 3 {
#       repeat 4 { say '*' }
#       say (new line)
#    }"
#
# That means: print a star 4 times on one line, do that 3 times.
# Result should look like:
#   * * * *
#   * * * *
#   * * * *
#
# HINT: Two for loops, one inside the other!
# TODO: Write the Python code below:

print("Exercise 9:")
# YOUR CODE HERE:

print()


# --------------------------------------------------
# Exercise 10: BOSS LEVEL - Mini Countdown Program
# --------------------------------------------------
# Scratch says:
#   "set countdown to 5"
#   "repeat 5 {
#       say countdown
#       wait 1 secs
#       change countdown by -1
#    }"
#   "say 'Blast off!'"
#
# That means: count down from 5 to 1, waiting 1 second each step,
# then print "Blast off!"
#
# HINT: Use a for loop with range(5, 0, -1) - that counts backwards!
# range(5, 0, -1) gives you: 5, 4, 3, 2, 1
# TODO: Write the Python code below:

print("Exercise 10 - BOSS LEVEL:")
# YOUR CODE HERE:

print()

# --------------------------------------------------
print("=" * 50)
print("Finished all 10 exercises? Amazing work!")
print("You just translated Scratch into Python!")
print("Earn your 10 XP and move to Lesson 2!")
print("=" * 50)

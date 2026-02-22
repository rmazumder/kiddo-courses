# Lesson 1: Scratch vs Python

## What Do Scratch Blocks Actually Do?

Every Scratch block is secretly a programming instruction. When you snap blocks
together in Scratch, you are writing a program - just with pictures instead of words.

Python is the *same ideas*, written as text. Once you see the connection, Python
feels totally familiar!

---

## 10 Side-by-Side Comparisons

| # | Scratch Block | What it Does | Python Equivalent |
|---|---|---|---|
| 1 | "when green flag clicked" | Starts the program | `if __name__ == "__main__":` |
| 2 | "say 'Hello!' for 2 secs" | Shows text on screen | `print("Hello!")` + `time.sleep(2)` |
| 3 | "move 10 steps" | Moves the sprite forward | `x += 10` |
| 4 | "repeat 10" | Loops a set number of times | `for i in range(10):` |
| 5 | "if touching color" | Checks if something is true | `if condition:` |
| 6 | "set x to 0" | Stores a value in a variable | `x = 0` |
| 7 | "wait 1 secs" | Pauses the program | `time.sleep(1)` |
| 8 | "forever" | Loops forever | `while True:` |
| 9 | "broadcast message" | Sends a signal to other code | calling a function `my_function()` |
| 10 | "my variable" (orange block) | Creates and uses a variable | `my_variable = 42` |

---

## The Big Secret

There is no magic in Scratch. Every block is just a shortcut for
real code. When you graduate from Scratch to Python, you are just
learning to *type* those instructions instead of *click* them.

You already know how to program. You are just learning a new language!

---

## Files in This Lesson

| File | What it Contains |
|---|---|
| `scratch_blocks_explained.md` | Visual ASCII art of each block next to its Python code |
| `compare_scratch_python.py` | All 10 comparisons as working Python code - run it! |
| `exercise_translate_blocks.py` | 10 exercises: translate Scratch blocks to Python yourself |

---

## How to Complete This Lesson

1. Read `scratch_blocks_explained.md` carefully
2. Run `compare_scratch_python.py` and watch what happens
3. Open `exercise_translate_blocks.py` and fill in the TODOs
4. When all 10 exercises work, you have earned **10 XP!**

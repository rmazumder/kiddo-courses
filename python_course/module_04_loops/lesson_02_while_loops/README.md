# Module 4, Lesson 2: While Loops

## Your Mission Today
Learn the other type of loop -- one that keeps going UNTIL a condition changes!

## Learning Objectives
By the end of this lesson, you will be able to:
- Use a `while` loop to repeat code as long as a condition is true
- Know the difference between `for` and `while` loops
- Avoid infinite loops (and know how to escape one!)

---

## For Loop vs. While Loop

- **For loop**: Use when you know HOW MANY times to repeat.
  "Do this 10 times."

- **While loop**: Use when you want to repeat UNTIL something changes.
  "Keep asking until the user says stop."

---

## How While Loops Work

```python
count = 0
while count < 5:
    print(count)
    count = count + 1
```

Think of it like this:
1. Check the condition -- is it True?
2. If yes, run the indented code.
3. Go back to step 1.
4. If the condition is False, stop.

IMPORTANT: Something inside the loop must eventually make the condition
False, or the loop will run forever (an "infinite loop")!

---

## Activity

Open `while_loops.py` to see examples,
then complete `exercise_while.py`!

---

## +10 XP -- Lesson Complete!
**Next up:** Lesson 3 -- Loop Patterns!

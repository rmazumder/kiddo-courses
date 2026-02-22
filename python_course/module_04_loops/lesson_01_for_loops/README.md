# Module 4, Lesson 1: For Loops

## Your Mission Today
Learn to make Python repeat things automatically -- like a tireless robot!

## Learning Objectives
By the end of this lesson, you will be able to:
- Use a `for` loop to repeat code a specific number of times
- Use `range()` to control how many times a loop runs
- Loop through the characters of a string

---

## Hook: The Lazy Programmer

Imagine you want to print "Hello!" 100 times. Would you write:

```python
print("Hello!")
print("Hello!")
print("Hello!")
# ... 97 more times?!
```

No way! A loop can do this in just 2 lines:

```python
for i in range(100):
    print("Hello!")
```

That is the power of loops -- they save you from writing the same
thing over and over again!

---

## How For Loops Work

```python
for i in range(5):
    print("Iteration:", i)
```

Output:
```
Iteration: 0
Iteration: 1
Iteration: 2
Iteration: 3
Iteration: 4
```

- `for` -- starts the loop
- `i` -- a variable that changes each time through the loop
- `range(5)` -- means "do this 5 times" (counting 0, 1, 2, 3, 4)
- The indented code runs each time

Think of it like a robot counting: "Do task 0, do task 1, do task 2..."

---

## Key Vocabulary

- **Loop**: Code that repeats
- **Iteration**: One trip through the loop
- **range()**: A function that creates a sequence of numbers
- **Loop variable**: The variable that changes each iteration (like `i`)

---

## Activity

Open `for_loops.py` to see loops in action,
then complete `exercise_for_loops.py`!

---

## +10 XP -- Lesson Complete!
**Next up:** Lesson 2 -- While Loops!

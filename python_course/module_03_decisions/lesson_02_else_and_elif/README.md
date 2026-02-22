# Module 3, Lesson 2: Else and Elif

## Your Mission Today
Learn how to handle ALL the possible paths your program can take!

## Learning Objectives
By the end of this lesson, you will be able to:
- Use `else` to handle what happens when a condition is False
- Use `elif` to check multiple conditions in a row
- Build a complete decision tree

---

## The Problem with Just If

With only `if`, we can check one thing. But what about the other case?

```python
age = 10
if age >= 18:
    print("You are an adult")
# What if they are NOT 18? Nothing happens!
```

That is where `else` comes in!

---

## If/Else: Two Paths

```python
age = 10
if age >= 18:
    print("You are an adult")
else:
    print("You are a kid")
```

- If the condition is True, the `if` block runs.
- If the condition is False, the `else` block runs.
- One of them ALWAYS runs. Never both, never neither.

---

## Elif: More Than Two Paths

What if you need more than two options? Use `elif` (short for "else if"):

```python
score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
```

Python checks each condition from top to bottom. The FIRST one that is
True runs, and then Python skips the rest.

---

## Activity

Open `else_elif.py` to see examples,
then complete `exercise_elif.py`!

---

## +10 XP -- Lesson Complete!
**Next up:** Lesson 3 -- Comparisons and Logic!

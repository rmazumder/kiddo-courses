# Module 3, Lesson 1: If Statements

## Your Mission Today
Teach your program to make decisions -- just like you do every day!

## Learning Objectives
By the end of this lesson, you will be able to:
- Write an `if` statement that runs code only when a condition is true
- Understand what **indentation** is and why it matters
- Use comparisons inside if statements

---

## Hook: Decisions, Decisions!

You make decisions all day long:
- **If** it is raining, you bring an umbrella.
- **If** you are hungry, you eat a snack.
- **If** your homework is done, you can play games.

Python can make decisions too! We use something called an **if statement**.

---

## How If Statements Work

```python
if condition:
    do_something
```

- The **condition** is something that is either True or False (a boolean!)
- If the condition is True, the indented code runs
- If the condition is False, Python skips it

### The Most Important Rule: INDENTATION

The code inside the if statement MUST be **indented** (pushed in) with
4 spaces or 1 tab. This tells Python which code belongs to the if.

```python
temperature = 35

if temperature > 30:
    print("It is hot outside!")    # This is indented -- it belongs to the if
    print("Drink lots of water!")  # This is also indented -- also belongs

print("Have a nice day!")          # Not indented -- runs no matter what
```

---

## Activity

Open `if_statements.py` to see if statements in action,
then complete `exercise_if.py`!

---

## +10 XP -- Lesson Complete!
**Next up:** Lesson 2 -- Else and Elif!

---

## Navigation

| | |
|:---|---:|
| [← Module Overview](../README.md) | [Module 3, Lesson 2: Else and Elif →](../lesson_02_else_and_elif/README.md) |

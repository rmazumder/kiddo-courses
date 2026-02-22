# Module 5, Lesson 3: Return Values

## Your Mission Today
Learn how to get information BACK from a function!

## Learning Objectives
By the end of this lesson, you will be able to:
- Use `return` to send a value back from a function
- Store returned values in variables
- Know the difference between printing and returning

---

## Print vs. Return

- `print()` shows something on the screen (for humans to read)
- `return` sends a value BACK to the code that called the function

Think of it this way:
- `print` is like a person SHOUTING an answer out loud.
- `return` is like a person HANDING you a piece of paper with the answer.

If you shout the answer (print), it is gone into the air.
If you hand it on paper (return), the caller can SAVE it and USE it later!

---

## How Return Works

```python
def add(a, b):
    return a + b

result = add(3, 5)      # result is now 8
print(result)            # Prints: 8
print(add(10, 20))       # Prints: 30
```

---

## Activity

Open `return_values.py` to see examples,
then complete `exercise_return.py`!

---

## +10 XP -- Lesson Complete!
**Next up:** Module 5 Quiz and Challenge!

---

## Navigation

| | |
|:---|---:|
| [← Module 5, Lesson 2: Parameters and Arguments](../lesson_02_parameters_and_arguments/README.md) | [Module Overview →](../README.md) |

# Module 3, Lesson 3: Comparisons and Logic

## Your Mission Today
Learn to combine conditions to make complex decisions -- like a master strategist!

## Learning Objectives
By the end of this lesson, you will be able to:
- Use `and`, `or`, and `not` to combine conditions
- Build complex decision logic
- Understand how Python evaluates combined conditions

---

## Logical Operators

| Operator | What It Means | Example |
|----------|--------------|---------|
| `and` | Both must be True | `age > 5 and age < 13` |
| `or` | At least one must be True | `day == "Sat" or day == "Sun"` |
| `not` | Flips True to False (and vice versa) | `not is_raining` |

### and -- Both Must Be True
```python
age = 10
has_ticket = True

if age >= 8 and has_ticket:
    print("You can enter!")
```

### or -- At Least One Must Be True
```python
day = "Saturday"

if day == "Saturday" or day == "Sunday":
    print("It's the weekend!")
```

### not -- Flip the Value
```python
is_raining = False

if not is_raining:
    print("No rain! Let's go outside!")
```

---

## Activity

Open `logic_operators.py` to see examples,
then complete `exercise_logic.py`!

---

## +10 XP -- Lesson Complete!
**Next up:** Module 3 Quiz and Challenge!

---

## Navigation

| | |
|:---|---:|
| [← Module 3, Lesson 2: Else and Elif](../lesson_02_else_and_elif/README.md) | [Module Overview →](../README.md) |

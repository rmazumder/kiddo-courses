# Module 2, Lesson 1: What Are Variables?

## Your Mission Today
Learn how to store information in your programs using variables -- like
labeled boxes that hold stuff!

## Learning Objectives
By the end of this lesson, you will be able to:
- Create a variable and give it a value
- Change the value of a variable
- Use variables inside print() statements

---

## Hook: The Labeled Box

Imagine you have a bunch of boxes. Each box has a **label** on it and
something **inside** it.

- A box labeled "name" might contain "Alex"
- A box labeled "age" might contain 10
- A box labeled "favorite_color" might contain "blue"

In Python, we call these boxes **variables**!

---

## Creating Variables

In Python, creating a variable is simple:

```python
name = "Alex"
age = 10
favorite_color = "blue"
```

The `=` sign does NOT mean "equals" like in math class.
In Python, `=` means **"put this value into this box."**

So `name = "Alex"` means: "Create a box called `name` and put `Alex` inside it."

---

## Rules for Variable Names

1. They can contain letters, numbers, and underscores (_)
2. They CANNOT start with a number (so `2cool` is not allowed, but `cool2` is fine)
3. They CANNOT have spaces (use underscores instead: `my_name` not `my name`)
4. They are case-sensitive (`Name` and `name` are different variables!)

**Good names:** `player_score`, `age`, `favorite_food`, `num_lives`
**Bad names:** `2nd_place`, `my name`, `@home`

---

## Using Variables

Once you create a variable, you can use it anywhere:

```python
name = "Alex"
print(name)         # Prints: Alex
print("Hello,", name)  # Prints: Hello, Alex
```

Notice: when you use a variable, you do NOT put quotes around it.
Quotes mean "this is literal text." No quotes mean "look up what is in this box."

---

## Key Vocabulary

- **Variable**: A named container that stores a value
- **Value**: The information stored inside a variable
- **Assignment**: Putting a value into a variable using `=`

---

## Activity

Open `variables_intro.py` to see variables in action,
then complete `exercise_variables.py`!

---

## +10 XP -- Lesson Complete!

**Next up:** Lesson 2 -- Numbers and Math!

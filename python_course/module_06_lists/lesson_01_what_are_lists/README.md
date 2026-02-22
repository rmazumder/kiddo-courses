# Module 6, Lesson 1: What Are Lists?

## Your Mission Today
Learn how to store a COLLECTION of items in a single variable!

## Learning Objectives
By the end of this lesson, you will be able to:
- Create a list with multiple items
- Access individual items using their index
- Know the difference between a single variable and a list

---

## Hook: The Backpack Problem

Imagine you are packing for a trip. You could create a separate variable
for each item:

```python
item1 = "water bottle"
item2 = "snacks"
item3 = "map"
item4 = "flashlight"
item5 = "first aid kit"
```

But what if you have 100 items? That is way too many variables!

A **list** is like a backpack -- one container that holds many items:

```python
backpack = ["water bottle", "snacks", "map", "flashlight", "first aid kit"]
```

One variable, five items. Much better!

---

## Creating Lists

```python
# A list of strings
fruits = ["apple", "banana", "cherry"]

# A list of numbers
scores = [95, 87, 92, 78, 100]

# A list of mixed types
my_info = ["Alex", 10, True, 4.5]

# An empty list
empty = []
```

Lists use **square brackets** `[]` and items are separated by **commas**.

---

## Accessing Items (Indexing)

Each item has a position number called an **index**.
Just like strings, indexes start at 0!

```python
fruits = ["apple", "banana", "cherry"]
#          index 0   index 1   index 2

print(fruits[0])    # apple
print(fruits[1])    # banana
print(fruits[2])    # cherry
print(fruits[-1])   # cherry (last item)
```

---

## Activity

Open `lists_intro.py` to see lists in action,
then complete `exercise_lists.py`!

---

## +10 XP -- Lesson Complete!
**Next up:** Lesson 2 -- List Operations!

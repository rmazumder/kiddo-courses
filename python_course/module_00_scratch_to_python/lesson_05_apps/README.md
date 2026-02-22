# Lesson 5: Apps!

## Games vs Apps

In the last lesson you built games. Games are fun, but Python can also build
*apps* - programs that do useful things!

| Games | Apps |
|---|---|
| Have a score | Do a task |
| Have win/lose | Provide information |
| Need fast reactions | Can be used slowly |
| Examples: Catch the Star, Turtle Race | Examples: Drawing app, Quiz app |

But here is the secret: **games and apps use the same code ideas!**
Both use loops, mouse/keyboard input, drawing, and functions.

---

## What Makes an App?

An app needs to:
1. **Display** something useful on screen
2. **Respond** to the user (clicks, key presses)
3. **Remember** information (variables)
4. **Update** what's shown based on user actions

Sound familiar? That is exactly what a Scratch project does!

---

## Mouse Events in Turtle

```python
# Click anywhere on screen
screen.onclick(handle_click)        # handle_click(x, y) called on click

# Key presses
screen.onkey(handle_key, "r")       # Press 'r' calls handle_key

# Mouse drag (click and hold while moving)
screen.ondrag(handle_drag)          # Very useful for drawing apps!
```

---

## Writing Text on Screen

```python
import turtle

pen = turtle.Turtle()
pen.penup()
pen.goto(-100, 50)
pen.color("black")

# Basic text
pen.write("Hello!", font=("Arial", 16, "normal"))

# Bold text
pen.write("Score: 100", font=("Arial", 20, "bold"))

# Italic text
pen.write("Press R for red", font=("Arial", 12, "italic"))
```

---

## Files in This Lesson

| File | What it Contains |
|---|---|
| `drawing_app.py` | A full mini paint app - draw, pick colours, change brush size! |
| `quiz_app.py` | A graphical quiz with clickable answer buttons |
| `exercise_build_app.py` | Two app templates for you to complete |

---

## How to Complete This Lesson

1. Run `drawing_app.py` - try drawing something! Use r/g/b/p to change colour.
2. Run `quiz_app.py` - answer the Python questions!
3. Study the code - notice how mouse clicks and key presses work.
4. Open `exercise_build_app.py` and build one of the two apps.

Finish the exercise to earn **10 XP!**

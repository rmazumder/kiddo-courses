# Lesson 2: Turtle Graphics

## What is Turtle Graphics?

Remember Scratch's **pen blocks**? You could put the pen down and drag
your sprite around to draw lines and shapes.

Python's `turtle` module works the same way! You control a little turtle
(the cursor) and it draws wherever it walks.

The best part: **turtle is built into Python**. No downloads, no installs -
just type `import turtle` and start drawing!

---

## The Turtle = Your Scratch Sprite with a Pen

| Scratch Pen Block | Turtle Command | What it Does |
|---|---|---|
| "pen down" | `turtle.pendown()` | Start drawing |
| "pen up" | `turtle.penup()` | Stop drawing (move without lines) |
| "move 100 steps" | `turtle.forward(100)` | Move forward 100 pixels |
| "move -100 steps" | `turtle.backward(100)` | Move backward |
| "turn right 90 degrees" | `turtle.right(90)` | Turn clockwise |
| "turn left 90 degrees" | `turtle.left(90)` | Turn counter-clockwise |
| "set pen color to red" | `turtle.color("red")` | Change drawing color |
| "go to x:0 y:0" | `turtle.goto(0, 0)` | Jump to a position |
| "set pen size to 3" | `turtle.pensize(3)` | Make lines thicker |
| "clear" | `turtle.clear()` | Erase all drawing |

---

## Common Turtle Commands

```python
import turtle

turtle.forward(100)     # Move forward 100 pixels
turtle.backward(50)     # Move backward 50 pixels
turtle.right(90)        # Turn right 90 degrees
turtle.left(45)         # Turn left 45 degrees
turtle.penup()          # Lift the pen (stop drawing)
turtle.pendown()        # Put pen down (start drawing)
turtle.color("red")     # Set color by name
turtle.color("#FF6600") # Set color by hex code
turtle.pensize(3)       # Make lines 3 pixels wide
turtle.speed(5)         # Drawing speed (1=slow, 10=fast, 0=instant)
turtle.goto(100, -50)   # Jump to x=100, y=-50
turtle.home()           # Jump back to center (0, 0)
turtle.circle(50)       # Draw a circle with radius 50
turtle.write("Hello!")  # Write text on screen
turtle.done()           # Keep window open when finished
```

---

## The Coordinate System

Turtle uses X and Y coordinates, just like Scratch!

```
          Y (up)
          |
          |
----------+----------  X (right)
          |
          |
         (0,0) is the centre of the screen
```

- Going right increases X
- Going up increases Y
- Turtle starts at (0, 0) facing right

---

## Files in This Lesson

| File | What it Contains |
|---|---|
| `turtle_intro.py` | Draw a house with turtle - every command explained |
| `draw_shapes.py` | Square, triangle, circle, star, pentagon with functions |
| `exercise_draw_art.py` | 5 creative drawing challenges for you to complete |
| `colorful_spiral.py` | A spectacular rainbow spiral - run it and be amazed! |

---

## How to Complete This Lesson

1. Run `turtle_intro.py` and watch the turtle draw a house
2. Run `draw_shapes.py` to see all the shapes
3. Study the code in both files - can you understand how each shape is drawn?
4. Open `exercise_draw_art.py` and complete the 5 TODO tasks
5. Run `colorful_spiral.py` for a bonus - try changing the colours!

When you finish the exercises, you have earned **10 XP!**

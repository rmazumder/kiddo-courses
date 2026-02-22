# Lesson 3: Animations

## What is Animation?

In Scratch, you have seen animations - sprites that move across the screen,
glide to positions, change costumes. That is animation: showing slightly
different pictures many times per second to create the illusion of movement.

Python can do the same thing with turtle!

---

## How Animation Works

Think of a flip book - each page is a tiny bit different from the last.
When you flip through them quickly, the drawing seems to move.

Computer animation works the same way:

```
1. Draw everything on screen
2. Wait a tiny moment (1/30th of a second)
3. ERASE everything
4. Move objects slightly
5. Draw everything again
6. Go back to step 2 (forever)
```

This loop is called the **game loop** or **animation loop**.

---

## Scratch vs Python Animation

| Scratch | Python Turtle | What it Does |
|---|---|---|
| "glide 1 secs to x:100 y:50" | Update x, y in a loop | Move character smoothly |
| "move 10 steps" | `x += 10` in loop | Move each frame |
| "if on edge, bounce" | `if x > 300: speed_x *= -1` | Reverse direction at wall |
| "forever" block | `while True:` | The animation loop |
| Stage refreshes | `screen.update()` | Redraw the screen |
| "repeat until" | `while condition:` | Stop after something happens |

---

## Key Animation Commands

```python
import turtle

screen = turtle.Screen()
screen.tracer(0)          # Turn off auto-drawing (manual control)

t = turtle.Turtle()

# Animation loop:
while True:
    screen.update()       # Draw the current frame to screen
    t.clear()             # Erase the turtle's drawing
    x += speed_x          # Move the object
    t.goto(x, y)          # Draw at new position
```

---

## Key Concepts

**tracer(0)** - Turns off automatic drawing. You control exactly when the
screen refreshes. This prevents flickering and gives smooth animation.

**screen.update()** - Redraws the screen with the latest positions.
Call this once per frame.

**t.clear()** - Erases everything drawn by that turtle.
Call this each frame before redrawing.

**Frame rate** - How many times per second we redraw. Games aim for
30 or 60 frames per second. We use `time.sleep(0.016)` for about 60 FPS.

---

## Files in This Lesson

| File | What it Contains |
|---|---|
| `turtle_animation.py` | An animated character bouncing back and forth |
| `bouncing_ball.py` | A ball bouncing off walls with score tracking |
| `exercise_animate.py` | 3 animation exercises for you to complete |

---

## How to Complete This Lesson

1. Run `turtle_animation.py` - watch the character move!
2. Run `bouncing_ball.py` - count those bounces!
3. Study the code - can you see the animation loop?
4. Open `exercise_animate.py` and complete all 3 exercises

Finish all exercises to earn **10 XP!**

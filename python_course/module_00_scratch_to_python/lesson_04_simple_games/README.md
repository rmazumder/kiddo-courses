# Lesson 4: Simple Games

## Building Games - Just Like Scratch!

In Scratch, you probably built games with:
- A player sprite that moves with arrow keys
- Enemies or targets to avoid or collect
- A score that goes up and down
- A win or lose condition

Python can do ALL of this! The ingredients are the same:

```
Every game needs:
  1. A PLAYER     (a turtle that responds to keyboard input)
  2. A GOAL       (something to catch, avoid, or reach)
  3. SCORE        (a variable that changes based on actions)
  4. WIN/LOSE     (a condition that ends the game)
  5. A GAME LOOP  (the "forever" block that keeps things running)
```

---

## Keyboard Input: Scratch vs Python

| Scratch | Python Turtle | What it Does |
|---|---|---|
| "when [left arrow] pressed" | `screen.onkey(func, "Left")` | Bind a key to an action |
| "when [space] pressed" | `screen.onkey(func, "space")` | Bind the spacebar |
| "if key [up] pressed?" | check in game loop | Check key state each frame |
| "go to x:0 y:0" | `player.goto(0, 0)` | Jump to position |

### How to Set Up Keyboard Controls

```python
import turtle

screen = turtle.Screen()
screen.listen()             # Tell Python to listen for key presses

def move_left():
    player_x -= 20

def move_right():
    player_x += 20

screen.onkey(move_left, "Left")    # Left arrow calls move_left
screen.onkey(move_right, "Right")  # Right arrow calls move_right
```

---

## Mouse Input

```python
def on_click(x, y):
    print(f"Clicked at x={x}, y={y}")

screen.onclick(on_click)    # Any click calls on_click with coordinates
```

---

## The Game Loop Pattern

Every game file in this lesson uses this structure:

```python
# Setup
screen = turtle.Screen()
player = turtle.Turtle()
score = 0
game_over = False

# Key bindings
screen.listen()
screen.onkey(move_left, "Left")

# Game loop
while not game_over:
    move_targets()
    check_collisions()
    update_score()
    draw_hud()
    screen.update()
    time.sleep(0.016)
```

---

## Files in This Lesson

| File | What it Contains |
|---|---|
| `catch_the_star.py` | Full game: catch falling stars with a paddle! |
| `turtle_race.py` | Bet on a turtle race - 5 turtles, random speed! |
| `exercise_build_game.py` | Templates for 2 mini-games to build yourself |

---

## How to Complete This Lesson

1. Run `catch_the_star.py` and play it! Try to beat your own score.
2. Run `turtle_race.py` and bet on a turtle.
3. Study the code in both - identify the game loop, player, score, and win/lose.
4. Open `exercise_build_game.py` and build one of the mini-games.

Finish the exercise to earn **10 XP!**

---

## Navigation

| | |
|:---|---:|
| [← Lesson 3: Animations](../lesson_03_animations/README.md) | [Lesson 5: Apps! →](../lesson_05_apps/README.md) |

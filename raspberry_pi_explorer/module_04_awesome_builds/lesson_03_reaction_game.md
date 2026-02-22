# 🎮 Raspberry Pi Explorer — Module 4, Lesson 3: Reaction Speed Game! 🎮

```
 ╔══════════════════════════════════════════════════════════╗
 ║  MODULE 4: AWESOME BUILDS  🏗️                           ║
 ║  Lesson 3 of 3 + Final Project                          ║
 ║  XP Available: 300 XP  |  Badge: 🎮 Game Dev            ║
 ╚══════════════════════════════════════════════════════════╝
```

---

## 🌟 Your Mission Today

**Mission Briefing:** You're going to build a REAL 2-player reaction speed
game! 🎮 When the light turns on, both players race to press their button.
The fastest player wins the round! It keeps score, announces the winner, and
even tracks the fastest reaction time ever! Are you ready to challenge your
friends? 🏆

---

## 🎯 Learning Objectives

By the end of this lesson, you will be able to:
- ✅ Build a multiplayer game with physical buttons and LEDs
- ✅ Measure reaction time precisely using Python's `time` module
- ✅ Implement scoring, rounds, and game state management
- ✅ Handle multiple button inputs simultaneously
- ✅ Create an engaging, fun gaming experience!

---

## 🪝 Hook — Build Your Own Arcade Game! 🕹️

What if you could build a game that LIVES on your desk? Not on a screen — a
REAL, physical game with buttons you press, lights that flash, and a buzzer
that celebrates the winner?

Today, you're building the **Pi Reaction Challenge** — a game where two players
face off to see who has the FASTEST reflexes! 🏎️💨

---

## 🧠 Hardware Setup

### What You Need:

```
□ 🍓 Raspberry Pi
□ 💡 1x LED (the "GO!" light — any color, preferably bright)
□ 🔘 2x Push Buttons (Player 1 and Player 2)
□ 💡 1x Green LED (Player 1 win indicator)
□ 💡 1x Blue LED (Player 2 win indicator)
□ ⚡ 3x 220Ω Resistors (for LEDs)
□ 🔔 1x Buzzer (for sound effects)
□ 🔗 Jumper wires
□ 🍞 Breadboard
```

### Wiring Diagram:

```
    🍓 RASPBERRY PI                    🍞 BREADBOARD

    GPIO 17 (Pin 11) ──[220Ω]── 🟡 GO LED (+)     → GND
    GPIO 27 (Pin 13) ──[220Ω]── 🟢 Player 1 LED   → GND
    GPIO 22 (Pin 15) ──[220Ω]── 🔵 Player 2 LED   → GND
    GPIO 18 (Pin 12) ────────── 🔔 Buzzer (+)      → GND

    GPIO 5  (Pin 29) ────────── 🔘 Player 1 Button → 3.3V
    GPIO 6  (Pin 31) ────────── 🔘 Player 2 Button → 3.3V

    LAYOUT:

    ┌────────────────────────────────────────────────────┐
    │                                                    │
    │    [Player 1]         [GO!]          [Player 2]    │
    │     🔘 Button         🟡 LED          🔘 Button   │
    │     🟢 LED                            🔵 LED      │
    │                                                    │
    │              🔔 Buzzer (center)                    │
    │                                                    │
    │    GPIO 5            GPIO 17           GPIO 6      │
    │    GPIO 27                             GPIO 22     │
    │                      GPIO 18                       │
    │                                                    │
    └────────────────────────────────────────────────────┘
```

---

## 🧠 The Complete Reaction Game Code:

```python
#!/usr/bin/env python3
# =============================================
# 🎮 PI REACTION CHALLENGE!
# 2-Player Reaction Speed Game
# Raspberry Pi Explorer - Module 4, Lesson 3
# =============================================

import RPi.GPIO as GPIO
import time
import random

# --- PIN CONFIGURATION ---
GO_LED = 17          # Yellow/White LED — "GO!" signal
P1_LED = 27          # Green LED — Player 1 wins
P2_LED = 22          # Blue LED — Player 2 wins
BUZZER = 18          # Buzzer for sound effects

P1_BUTTON = 5        # Player 1 button
P2_BUTTON = 6        # Player 2 button

# --- GAME SETTINGS ---
TOTAL_ROUNDS = 5     # Number of rounds per game
MIN_WAIT = 2         # Minimum wait before GO (seconds)
MAX_WAIT = 6         # Maximum wait before GO (seconds)
FALSE_START_PENALTY = 1  # Points deducted for pressing too early

# --- SETUP ---
GPIO.setmode(GPIO.BCM)
GPIO.setup(GO_LED, GPIO.OUT)
GPIO.setup(P1_LED, GPIO.OUT)
GPIO.setup(P2_LED, GPIO.OUT)
GPIO.setup(BUZZER, GPIO.OUT)
GPIO.setup(P1_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(P2_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# --- GAME STATE ---
p1_score = 0
p2_score = 0
p1_best_time = float('inf')
p2_best_time = float('inf')
round_history = []

# --- SOUND EFFECTS ---
def beep(duration=0.1, times=1):
    """Quick beep sound"""
    for _ in range(times):
        GPIO.output(BUZZER, GPIO.HIGH)
        time.sleep(duration)
        GPIO.output(BUZZER, GPIO.LOW)
        time.sleep(0.05)

def victory_sound():
    """Winner celebration sound!"""
    for _ in range(3):
        GPIO.output(BUZZER, GPIO.HIGH)
        time.sleep(0.08)
        GPIO.output(BUZZER, GPIO.LOW)
        time.sleep(0.05)
    GPIO.output(BUZZER, GPIO.HIGH)
    time.sleep(0.3)
    GPIO.output(BUZZER, GPIO.LOW)

def false_start_sound():
    """Buzz for false start"""
    GPIO.output(BUZZER, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(BUZZER, GPIO.LOW)

def countdown_beep():
    """Single countdown beep"""
    GPIO.output(BUZZER, GPIO.HIGH)
    time.sleep(0.05)
    GPIO.output(BUZZER, GPIO.LOW)

# --- DISPLAY FUNCTIONS ---
def all_off():
    """Turn everything off"""
    GPIO.output(GO_LED, GPIO.LOW)
    GPIO.output(P1_LED, GPIO.LOW)
    GPIO.output(P2_LED, GPIO.LOW)
    GPIO.output(BUZZER, GPIO.LOW)

def show_title():
    """Display the game title"""
    print()
    print("  ╔══════════════════════════════════════════════╗")
    print("  ║                                              ║")
    print("  ║    🎮  PI REACTION CHALLENGE!  🎮             ║")
    print("  ║                                              ║")
    print("  ║    👤 Player 1 (GREEN)  vs  Player 2 (BLUE) 👤║")
    print("  ║                                              ║")
    print("  ║    When the light turns ON — PRESS YOUR       ║")
    print("  ║    BUTTON as FAST as you can!                 ║")
    print("  ║                                              ║")
    print("  ║    ⚠️  Press BEFORE the light = FALSE START!  ║")
    print("  ║                                              ║")
    print(f"  ║    Best of {TOTAL_ROUNDS} rounds!                         ║")
    print("  ║                                              ║")
    print("  ╚══════════════════════════════════════════════╝")
    print()

def show_scoreboard(current_round):
    """Display the current score"""
    print(f"  ┌─────────── ROUND {current_round}/{TOTAL_ROUNDS} ───────────┐")
    print(f"  │  🟢 Player 1: {p1_score:2d} pts", end="")
    print(f"  │  🔵 Player 2: {p2_score:2d} pts  │")
    print(f"  └──────────────────────────────────┘")

def show_final_results():
    """Display final game results with ALL the details!"""
    print()
    print("  ╔══════════════════════════════════════════════╗")
    print("  ║          🏆 FINAL RESULTS 🏆                 ║")
    print("  ╠══════════════════════════════════════════════╣")
    print(f"  ║  🟢 Player 1: {p1_score} points                       ║")
    print(f"  ║  🔵 Player 2: {p2_score} points                       ║")
    print("  ║                                              ║")

    if p1_score > p2_score:
        print("  ║  🏆 PLAYER 1 WINS! 🟢🎉🎉🎉                ║")
        winner_led = P1_LED
    elif p2_score > p1_score:
        print("  ║  🏆 PLAYER 2 WINS! 🔵🎉🎉🎉                ║")
        winner_led = P2_LED
    else:
        print("  ║  🤝 IT'S A TIE! Both players are AMAZING! 🤝║")
        winner_led = None

    print("  ║                                              ║")

    if p1_best_time < float('inf'):
        print(f"  ║  🟢 P1 Best Reaction: {p1_best_time*1000:.0f} ms              ║")
    if p2_best_time < float('inf'):
        print(f"  ║  🔵 P2 Best Reaction: {p2_best_time*1000:.0f} ms              ║")

    print("  ║                                              ║")
    print("  ║  ─── Round History ───                       ║")
    for i, result in enumerate(round_history):
        print(f"  ║  Round {i+1}: {result:<36}  ║")

    print("  ║                                              ║")
    print("  ╚══════════════════════════════════════════════╝")

    # Victory light show!
    if winner_led:
        for _ in range(10):
            GPIO.output(winner_led, GPIO.HIGH)
            beep(0.05)
            time.sleep(0.15)
            GPIO.output(winner_led, GPIO.LOW)
            time.sleep(0.15)
    else:
        # Tie — flash both!
        for _ in range(10):
            GPIO.output(P1_LED, GPIO.HIGH)
            GPIO.output(P2_LED, GPIO.HIGH)
            time.sleep(0.2)
            GPIO.output(P1_LED, GPIO.LOW)
            GPIO.output(P2_LED, GPIO.LOW)
            time.sleep(0.2)

# --- GAME ROUND ---
def play_round(round_num):
    """Play a single round of the reaction game"""
    global p1_score, p2_score, p1_best_time, p2_best_time

    all_off()
    print(f"\n  🎮 ROUND {round_num}!")
    show_scoreboard(round_num)
    print()

    # Countdown: 3... 2... 1...
    for count in [3, 2, 1]:
        print(f"  ⏳ {count}...")
        countdown_beep()
        time.sleep(1)

    # Random wait (this is the suspense!)
    wait_time = random.uniform(MIN_WAIT, MAX_WAIT)
    print("  👀 Get ready... WAIT for the light!")

    # Check for false starts during the wait!
    start_wait = time.time()
    while time.time() - start_wait < wait_time:
        if GPIO.input(P1_BUTTON) == GPIO.HIGH:
            false_start_sound()
            GPIO.output(P1_LED, GPIO.HIGH)
            print("  ❌ Player 1 — FALSE START! (-1 point)")
            p1_score = max(0, p1_score - FALSE_START_PENALTY)
            round_history.append("❌ P1 False Start!")
            time.sleep(2)
            GPIO.output(P1_LED, GPIO.LOW)
            return

        if GPIO.input(P2_BUTTON) == GPIO.HIGH:
            false_start_sound()
            GPIO.output(P2_LED, GPIO.HIGH)
            print("  ❌ Player 2 — FALSE START! (-1 point)")
            p2_score = max(0, p2_score - FALSE_START_PENALTY)
            round_history.append("❌ P2 False Start!")
            time.sleep(2)
            GPIO.output(P2_LED, GPIO.LOW)
            return

        time.sleep(0.01)

    # GO! Light turns on!
    GPIO.output(GO_LED, GPIO.HIGH)
    beep(0.05)
    print("\n  💡💡💡 GO! GO! GO! 💡💡💡\n")
    go_time = time.time()

    # Wait for a button press!
    while True:
        p1_pressed = GPIO.input(P1_BUTTON) == GPIO.HIGH
        p2_pressed = GPIO.input(P2_BUTTON) == GPIO.HIGH

        if p1_pressed and p2_pressed:
            # Both pressed at nearly the same time!
            reaction_time = time.time() - go_time
            print(f"  🤝 TIE! Both pressed at {reaction_time*1000:.0f} ms!")
            p1_score += 1
            p2_score += 1
            round_history.append(f"🤝 TIE at {reaction_time*1000:.0f}ms")
            beep(0.1, 2)
            break

        elif p1_pressed:
            reaction_time = time.time() - go_time
            p1_score += 2  # Winner gets 2 points!
            if reaction_time < p1_best_time:
                p1_best_time = reaction_time
            print(f"  🟢 PLAYER 1 WINS THIS ROUND! ⚡")
            print(f"  ⏱️  Reaction time: {reaction_time*1000:.0f} ms")
            round_history.append(f"🟢 P1 wins ({reaction_time*1000:.0f}ms)")
            GPIO.output(P1_LED, GPIO.HIGH)
            victory_sound()
            break

        elif p2_pressed:
            reaction_time = time.time() - go_time
            p2_score += 2
            if reaction_time < p2_best_time:
                p2_best_time = reaction_time
            print(f"  🔵 PLAYER 2 WINS THIS ROUND! ⚡")
            print(f"  ⏱️  Reaction time: {reaction_time*1000:.0f} ms")
            round_history.append(f"🔵 P2 wins ({reaction_time*1000:.0f}ms)")
            GPIO.output(P2_LED, GPIO.HIGH)
            victory_sound()
            break

        # Timeout after 5 seconds
        if time.time() - go_time > 5:
            print("  ⏰ TIME'S UP! Nobody pressed! No points.")
            round_history.append("⏰ Timeout — no winner")
            beep(0.3)
            break

        time.sleep(0.001)  # Check every 1ms for precision!

    # Pause between rounds
    GPIO.output(GO_LED, GPIO.LOW)
    time.sleep(2)
    all_off()

# --- MAIN GAME LOOP ---
show_title()

print("  🔘 Player 1: Press your button to confirm READY!")
while GPIO.input(P1_BUTTON) == GPIO.LOW:
    time.sleep(0.1)
GPIO.output(P1_LED, GPIO.HIGH)
beep()
print("  🟢 Player 1 is READY!")

time.sleep(0.5)

print("  🔘 Player 2: Press your button to confirm READY!")
while GPIO.input(P2_BUTTON) == GPIO.LOW:
    time.sleep(0.1)
GPIO.output(P2_LED, GPIO.HIGH)
beep()
print("  🔵 Player 2 is READY!")

time.sleep(1)
all_off()

print("\n  🎮 LET THE GAMES BEGIN! 🎮")
time.sleep(1)

try:
    for round_num in range(1, TOTAL_ROUNDS + 1):
        play_round(round_num)
        time.sleep(1)

    # Game Over!
    show_final_results()

except KeyboardInterrupt:
    print("\n\n  🛑 Game interrupted!")

finally:
    all_off()
    GPIO.cleanup()
    print("  🧹 Cleaned up! Thanks for playing! 🎮")
```

---

## 🎮 Activity 1: Build and Play! 🏗️

**+100 XP**

```
┌──────────────────────────────────────────────────┐
│         🎮 REACTION GAME BUILD CHECKLIST         │
├──────────────────────────────────────────────────┤
│                                                  │
│  □ GO LED wired to GPIO 17                       │
│  □ Player 1 LED wired to GPIO 27                 │
│  □ Player 2 LED wired to GPIO 22                 │
│  □ Buzzer wired to GPIO 18                       │
│  □ Player 1 Button wired to GPIO 5               │
│  □ Player 2 Button wired to GPIO 6               │
│  □ Code runs without errors                      │
│  □ Both players confirmed READY                  │
│  □ Played at least one full 5-round game!        │
│  □ Recorded fastest reaction time: ___ ms        │
│                                                  │
└──────────────────────────────────────────────────┘
```

---

## 🎮 Activity 2: Tournament Mode! 🏆

**+75 XP**

Play a tournament with friends or family! Record the results:

```
┌──────────────────────────────────────────────────┐
│            🏆 REACTION TOURNAMENT                │
├──────────────────────────────────────────────────┤
│                                                  │
│  Match 1: _________ vs _________ Winner: _____  │
│  Match 2: _________ vs _________ Winner: _____  │
│  Match 3: _________ vs _________ Winner: _____  │
│                                                  │
│  CHAMPION: _________________________ 🏆          │
│                                                  │
│  Fastest Reaction Time EVER: ___ ms              │
│  By: _________________________                   │
│                                                  │
└──────────────────────────────────────────────────┘
```

---

## 🎮 Activity 3: Mod the Game! 🔧

**+50 XP**

Customize the game! Try at least 2 modifications:

```
□ Change TOTAL_ROUNDS to 10 for a longer game
□ Change MIN_WAIT / MAX_WAIT to make it harder
□ Add a "BEST 2 OUT OF 3" mode
□ Make the GO LED flash instead of staying solid
□ Add a sound that gets faster during the wait
□ Keep a high-score file that persists between games
□ Add a 3rd player!
```

---

## ⚡ Quick Quiz

**Q1:** Why does the game have a random wait time before the GO signal?
- A) Because the code has a bug
- B) To prevent players from guessing when to press — testing TRUE reaction time!
- C) To save battery
- D) Because random numbers are fun

**Q2:** What is a "false start"?
- A) When the game crashes
- B) When a player presses their button BEFORE the light turns on
- C) When neither player presses
- D) When the LED doesn't work

<details>
<summary>🔍 Click to reveal answers!</summary>

- **Q1: B** — Random wait means you can't predict when the light will turn on!
- **Q2: B** — Pressing before GO = false start = penalty! Patience is key!

</details>

---

## 🏅 Lesson Complete — Game Dev Badge Earned!

```
 ╔══════════════════════════════════════════════╗
 ║                                              ║
 ║     🎉 YOU MADE A REAL GAME! 🎉              ║
 ║                                              ║
 ║     You've earned the:                       ║
 ║                                              ║
 ║        🎮 GAME DEV BADGE 🎮                   ║
 ║                                              ║
 ║     A real physical game with buttons,       ║
 ║     LEDs, scoring, and sound! AMAZING! 🕹️    ║
 ║                                              ║
 ║     XP Earned: up to 300 XP                  ║
 ║                                              ║
 ╚══════════════════════════════════════════════╝
```

---

## 🔍 Coming Up Next...

**THE FINAL PROJECT!** 🏆 Combine everything you've learned to create YOUR OWN
invention! This is where YOU become the designer! 🎨🔧

---

*You just built a physical arcade game! Game designers everywhere are proud of you!* 🕹️🏆

# 🎮 Raspberry Pi Explorer — Module 2, Lesson 3: Python + GPIO = Magic! 🐍⚡

```
 ╔══════════════════════════════════════════════════════════╗
 ║  MODULE 2: GPIO & ELECTRONICS  ⚡                       ║
 ║  Lesson 3 of 3                                          ║
 ║  XP Available: 275 XP  |  Badge: 🐍 Code Wizard         ║
 ╚══════════════════════════════════════════════════════════╝
```

---

## 🌟 Your Mission Today

**Mission Briefing:** The circuit is built. The LED is waiting. Now it's time
to bring it to LIFE with **Python code!** 🐍 You'll write programs that make
LEDs blink, build a traffic light with 3 LEDs, and even read button presses!
This is where software meets hardware — and MAGIC happens! ✨

---

## 🎯 Learning Objectives

By the end of this lesson, you will be able to:
- ✅ Use the RPi.GPIO Python library to control GPIO pins
- ✅ Make an LED blink with a Python program
- ✅ Build and code a 3-LED traffic light system
- ✅ Read button presses with GPIO input
- ✅ Understand GPIO.setup(), GPIO.output(), and GPIO.input()

---

## 🪝 Hook — Code That Controls the REAL World! 🌍

Until now, every program you've written only did things on SCREEN — print text,
do math, show pictures. But TODAY, your code reaches OUT of the screen and
controls something in the REAL WORLD!

When you type `GPIO.output(17, GPIO.HIGH)` and press Enter, a REAL LED lights
up on your desk. 💡 That's not just coding — that's ENGINEERING! 🔧

---

## 🧠 Learning Point 1: The RPi.GPIO Library 📚

### What is RPi.GPIO?

**RPi.GPIO** is a Python library (a collection of pre-written code) that lets
you control the Raspberry Pi's GPIO pins with Python.

> 💡 **Analogy:** Think of RPi.GPIO as a TRANSLATOR 🗣️:
> - You speak PYTHON (the programming language)
> - The GPIO pins speak ELECTRICITY
> - RPi.GPIO translates your Python commands into electrical signals!

### The Basic Template — Memorize This! 🧠

Every GPIO program follows this pattern:

```python
# Step 1: Import the library
import RPi.GPIO as GPIO
import time

# Step 2: Set the pin numbering mode
GPIO.setmode(GPIO.BCM)          # Use BCM pin numbers

# Step 3: Set up your pins
GPIO.setup(17, GPIO.OUT)        # GPIO 17 is an OUTPUT pin

# Step 4: Do stuff with the pins!
GPIO.output(17, GPIO.HIGH)      # Turn ON (send 3.3V)
GPIO.output(17, GPIO.LOW)       # Turn OFF (send 0V)

# Step 5: Clean up when done
GPIO.cleanup()                  # Reset all pins
```

### Breaking Down Each Command:

| Command | What It Does | Analogy |
|---------|-------------|---------|
| `import RPi.GPIO as GPIO` | Loads the GPIO library | Opening your toolbox 🧰 |
| `import time` | Lets us use `time.sleep()` for pauses | Getting a stopwatch ⏱️ |
| `GPIO.setmode(GPIO.BCM)` | Use BCM pin numbers | Setting the language to "BCM" |
| `GPIO.setup(17, GPIO.OUT)` | Set pin 17 as OUTPUT | Telling the pin: "You'll be SENDING power!" |
| `GPIO.setup(17, GPIO.IN)` | Set pin 17 as INPUT | Telling the pin: "You'll be LISTENING!" |
| `GPIO.output(17, GPIO.HIGH)` | Send 3.3V out (ON) | Flipping the switch UP! 💡 |
| `GPIO.output(17, GPIO.LOW)` | Send 0V out (OFF) | Flipping the switch DOWN! ⚫ |
| `GPIO.input(17)` | Read the pin (HIGH or LOW?) | Checking: "Is something happening?" |
| `time.sleep(1)` | Wait 1 second | Pause for 1 second ⏸️ |
| `GPIO.cleanup()` | Reset all pins to default | Putting your tools away 🧹 |

---

## 🧠 Learning Point 2: Your First GPIO Program — Blink! 💡

### Project: Blinking LED

**What you need:**
- The LED circuit from Lesson 2 (LED + resistor on GPIO 17)
- Your Pi powered on with the circuit connected

### The Code:

Open **Thonny** (Pi Menu → Programming → Thonny) and type this:

```python
# =============================================
# 💡 BLINKING LED - My First GPIO Program!
# Raspberry Pi Explorer - Module 2, Lesson 3
# =============================================

import RPi.GPIO as GPIO     # Import the GPIO library
import time                 # Import time for sleep()

# --- SETUP ---
LED_PIN = 17                # Our LED is on GPIO 17

GPIO.setmode(GPIO.BCM)      # Use BCM numbering
GPIO.setup(LED_PIN, GPIO.OUT)  # Set GPIO 17 as OUTPUT

print("💡 LED Blink Program Started!")
print("Press Ctrl+C to stop")
print()

# --- MAIN LOOP ---
try:
    blink_count = 0
    while True:                         # Loop forever!
        GPIO.output(LED_PIN, GPIO.HIGH) # LED ON! 💡
        print(f"  💡 LED ON  (blink #{blink_count + 1})")
        time.sleep(1)                   # Wait 1 second

        GPIO.output(LED_PIN, GPIO.LOW)  # LED OFF! ⚫
        print(f"  ⚫ LED OFF")
        time.sleep(1)                   # Wait 1 second

        blink_count += 1

except KeyboardInterrupt:
    print(f"\n🛑 Stopped after {blink_count} blinks!")

finally:
    GPIO.cleanup()                      # Clean up!
    print("🧹 GPIO cleaned up. Goodbye!")
```

### How to Run It:

1. Save the file as `blink.py`
2. Click the **Run** button (▶️) in Thonny
3. **Watch your LED blink!** 💡⚫💡⚫💡⚫
4. Press **Ctrl+C** to stop the program

### What Happens Step by Step:

```
Time 0s: GPIO 17 → HIGH (3.3V) → LED ON  💡
Time 1s: GPIO 17 → LOW  (0V)  → LED OFF ⚫
Time 2s: GPIO 17 → HIGH (3.3V) → LED ON  💡
Time 3s: GPIO 17 → LOW  (0V)  → LED OFF ⚫
...repeats forever until you press Ctrl+C!
```

```
⚠️ IMPORTANT:
Always include GPIO.cleanup() in your programs!
Without it, the pins stay in their last state,
which can cause problems with future programs.

The try/except/finally structure makes sure cleanup
happens even if you stop the program with Ctrl+C!
```

---

## 🧠 Learning Point 3: Traffic Light Project! 🚦

Now let's level up! You'll build a traffic light with **3 LEDs** — just like
a real traffic signal!

### What You Need:

```
□ 1x Red LED 🔴
□ 1x Yellow LED 🟡 (or orange)
□ 1x Green LED 🟢
□ 3x 220Ω Resistors
□ 4x Jumper wires (male-to-female)
□ Breadboard
```

### Circuit Diagram:

```
    🍓 RASPBERRY PI               🍞 BREADBOARD

    GPIO 17 (Pin 11) ──────── [220Ω] ──── 🔴 RED LED ──┐
                                                         │
    GPIO 27 (Pin 13) ──────── [220Ω] ──── 🟡 YEL LED ──┤
                                                         │
    GPIO 22 (Pin 15) ──────── [220Ω] ──── 🟢 GRN LED ──┤
                                                         │
    GND (Pin 6) ─────────────────────────────────────────┘
                              (all LED short legs share GND)
```

### Breadboard Wiring Detail:

```
    ┌────────────────────────────────────────────┐
    │  GND rail: ●━━━━━━━━━━━━━━━━━━━━━━━━━━━  │  ← Connect to Pi GND
    │                                            │
    │     a  b  c  d  e     f  g  h  i  j       │
    │  1  [===220Ω===]  ○   ○  ○  ○  ○  ○      │  ← Red resistor
    │  2  ○  ○  ○  ○  ○   ○  ○  ○  ○  ○       │
    │  3  ○  [R+]  ○  ○   ○  ○  ○  ○  ○       │  ← Red LED long leg
    │  4  ○  [R-]  ○  ○   ○  ○  ○  ○  ○       │  ← Red LED short leg→GND
    │  5  ○  ○  ○  ○  ○   ○  ○  ○  ○  ○       │
    │  6  [===220Ω===]  ○   ○  ○  ○  ○  ○      │  ← Yellow resistor
    │  7  ○  ○  ○  ○  ○   ○  ○  ○  ○  ○       │
    │  8  ○  [Y+]  ○  ○   ○  ○  ○  ○  ○       │  ← Yellow LED long leg
    │  9  ○  [Y-]  ○  ○   ○  ○  ○  ○  ○       │  ← Yellow LED short leg→GND
    │ 10  ○  ○  ○  ○  ○   ○  ○  ○  ○  ○       │
    │ 11  [===220Ω===]  ○   ○  ○  ○  ○  ○      │  ← Green resistor
    │ 12  ○  ○  ○  ○  ○   ○  ○  ○  ○  ○       │
    │ 13  ○  [G+]  ○  ○   ○  ○  ○  ○  ○       │  ← Green LED long leg
    │ 14  ○  [G-]  ○  ○   ○  ○  ○  ○  ○       │  ← Green LED short leg→GND
    │                                            │
    └────────────────────────────────────────────┘

    Wire connections:
    GPIO 17 → row 1 (red resistor)
    GPIO 27 → row 6 (yellow resistor)
    GPIO 22 → row 11 (green resistor)
    GND → GND rail (connect each LED short leg to this rail)
```

### The Traffic Light Code:

```python
# =============================================
# 🚦 TRAFFIC LIGHT PROJECT
# Raspberry Pi Explorer - Module 2, Lesson 3
# =============================================

import RPi.GPIO as GPIO
import time

# --- PIN SETUP ---
RED = 17      # Red LED on GPIO 17
YELLOW = 27   # Yellow LED on GPIO 27
GREEN = 22    # Green LED on GPIO 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(RED, GPIO.OUT)
GPIO.setup(YELLOW, GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)

# --- HELPER FUNCTION ---
def all_off():
    """Turn off all LEDs"""
    GPIO.output(RED, GPIO.LOW)
    GPIO.output(YELLOW, GPIO.LOW)
    GPIO.output(GREEN, GPIO.LOW)

# --- TRAFFIC LIGHT SEQUENCE ---
def traffic_light_cycle():
    """Run one complete traffic light cycle"""

    # 🟢 GREEN - GO!
    all_off()
    GPIO.output(GREEN, GPIO.HIGH)
    print("🟢 GREEN  - GO!")
    time.sleep(5)                    # Green for 5 seconds

    # 🟡 YELLOW - SLOW DOWN!
    all_off()
    GPIO.output(YELLOW, GPIO.HIGH)
    print("🟡 YELLOW - SLOW DOWN!")
    time.sleep(2)                    # Yellow for 2 seconds

    # 🔴 RED - STOP!
    all_off()
    GPIO.output(RED, GPIO.HIGH)
    print("🔴 RED    - STOP!")
    time.sleep(5)                    # Red for 5 seconds

    # 🔴🟡 RED + YELLOW - GET READY!
    GPIO.output(YELLOW, GPIO.HIGH)   # Add yellow (red still on)
    print("🔴🟡 RED+YELLOW - GET READY!")
    time.sleep(2)                    # Both for 2 seconds

# --- MAIN PROGRAM ---
print("=" * 40)
print("🚦 TRAFFIC LIGHT SYSTEM ACTIVE! 🚦")
print("=" * 40)
print("Press Ctrl+C to stop\n")

try:
    cycle_count = 0
    while True:
        cycle_count += 1
        print(f"--- Cycle {cycle_count} ---")
        traffic_light_cycle()

except KeyboardInterrupt:
    print(f"\n🛑 Traffic light stopped after {cycle_count} cycles!")

finally:
    all_off()
    GPIO.cleanup()
    print("🧹 All LEDs off. GPIO cleaned up!")
```

---

## 🧠 Learning Point 4: Button Input — Pi Listens! 🔘

Now let's make the Pi LISTEN to you! We'll add a push button.

### Button Circuit:

```
    🍓 RASPBERRY PI               🍞 BREADBOARD

    GPIO 18 (Pin 12) ──────────── [BUTTON] ──── 3.3V (Pin 1)
                                     │
                                  [10KΩ]  ← Pull-down resistor
                                     │
                                    GND

    OR, use the internal pull-down (easier!):
    GPIO 18 (Pin 12) ──────────── [BUTTON] ──── 3.3V (Pin 1)
    (No external resistor needed when using GPIO.PUD_DOWN!)
```

### Button + LED Code:

```python
# =============================================
# 🔘 BUTTON-CONTROLLED LED
# Press the button to turn the LED on!
# Raspberry Pi Explorer - Module 2, Lesson 3
# =============================================

import RPi.GPIO as GPIO
import time

# --- PIN SETUP ---
LED_PIN = 17       # LED on GPIO 17
BUTTON_PIN = 18    # Button on GPIO 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
# PUD_DOWN means the pin reads LOW by default,
# and HIGH when the button is pressed!

print("🔘 Button + LED Program Started!")
print("Press the button to toggle the LED!")
print("Press Ctrl+C to stop\n")

try:
    led_on = False
    last_state = GPIO.LOW

    while True:
        current_state = GPIO.input(BUTTON_PIN)  # Read the button

        # Detect button PRESS (goes from LOW to HIGH)
        if current_state == GPIO.HIGH and last_state == GPIO.LOW:
            led_on = not led_on    # Toggle! (on→off, off→on)

            if led_on:
                GPIO.output(LED_PIN, GPIO.HIGH)
                print("  💡 LED ON! (button pressed)")
            else:
                GPIO.output(LED_PIN, GPIO.LOW)
                print("  ⚫ LED OFF! (button pressed)")

            time.sleep(0.3)  # Debounce delay (prevents multiple triggers)

        last_state = current_state
        time.sleep(0.05)  # Small delay to prevent CPU overload

except KeyboardInterrupt:
    print("\n🛑 Program stopped!")

finally:
    GPIO.cleanup()
    print("🧹 GPIO cleaned up!")
```

> 🔑 **Key Vocabulary:**
> - **Pull-down resistor** = Keeps the pin at LOW (0V) by default
> - **Debounce** = A short delay to prevent the button from registering multiple presses
> - **Toggle** = Switch between two states (on/off, true/false)

---

## 🎮 Activity 1: Make It Blink! 💡

**+50 XP** (Building project!)

1. Make sure your LED circuit from Lesson 2 is connected
2. Type the **Blinking LED** code into Thonny
3. Run it and watch your LED blink!
4. **Challenge:** Modify the code to blink FASTER (change `time.sleep(1)` to `time.sleep(0.2)`)!

```
□ LED blinks at 1 second intervals
□ LED blinks at 0.2 second intervals (speed mode!)
□ I understand every line of the code
```

---

## 🎮 Activity 2: Build the Traffic Light! 🚦

**+100 XP** (Major building project!)

1. Wire up 3 LEDs (red, yellow, green) with resistors
2. Type the **Traffic Light** code into Thonny
3. Run it and watch the traffic light sequence!

```
□ All 3 LEDs are wired correctly
□ Red light works
□ Yellow light works
□ Green light works
□ The sequence runs: Green → Yellow → Red → Red+Yellow → repeat
□ I took a photo/video of my traffic light! 📸
```

---

## 🎮 Activity 3: Code Challenge — Custom Pattern! 🧩

**+25 XP**

Write your OWN LED pattern! Use the traffic light circuit and create a
fun light show. Here's a starter:

```python
# =============================================
# ✨ MY CUSTOM LED PATTERN
# =============================================

import RPi.GPIO as GPIO
import time

RED = 17
YELLOW = 27
GREEN = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(RED, GPIO.OUT)
GPIO.setup(YELLOW, GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)

try:
    while True:
        # YOUR PATTERN HERE!
        # Example: Knight Rider scanner effect
        for pin in [RED, YELLOW, GREEN, YELLOW]:
            GPIO.output(pin, GPIO.HIGH)
            time.sleep(0.2)
            GPIO.output(pin, GPIO.LOW)

except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
```

**Ideas for patterns:**
- 🚨 Police siren (red/blue alternating)
- 🎄 Christmas lights (random twinkling)
- 📡 Loading bar (one by one, then all off)
- 🆘 SOS in morse code!

---

## ⚡ Quick Quiz — Earn Bonus XP!

**+20 XP per correct answer!**

**Q1:** What does `GPIO.output(17, GPIO.HIGH)` do?
- A) Reads the state of pin 17
- B) Turns off pin 17
- C) Sends 3.3V out of pin 17 (turns LED on)
- D) Deletes pin 17

**Q2:** What does `GPIO.cleanup()` do?
- A) Deletes all your code
- B) Resets all GPIO pins to their default state
- C) Cleans your keyboard
- D) Updates the Pi software

**Q3:** What happens if you don't use a resistor with an LED?
- A) Nothing, it works fine
- B) The LED changes color
- C) Too much current flows and the LED can burn out
- D) The LED blinks automatically

<details>
<summary>🔍 Click to reveal answers!</summary>

- **Q1: C** — HIGH sends 3.3V, which lights up the LED! 💡
- **Q2: B** — It resets pins to default. Always clean up after yourself! 🧹
- **Q3: C** — Without a resistor, too much current = burned LED! Always use 220Ω! 🛡️

</details>

---

## 🏅 Lesson Complete — Code Wizard Badge Earned!

```
 ╔══════════════════════════════════════════════╗
 ║                                              ║
 ║     🎉 YOU'RE A CODE WIZARD NOW! 🎉          ║
 ║                                              ║
 ║     You've earned the:                       ║
 ║                                              ║
 ║        🐍 CODE WIZARD BADGE 🐍                ║
 ║                                              ║
 ║     You wrote Python code that controls      ║
 ║     REAL electronics! That's INCREDIBLE! ⚡   ║
 ║                                              ║
 ║     XP Earned This Lesson:                   ║
 ║     📖 Reading: +50 XP                       ║
 ║     🏗️ Activity 1 (Blink): +50 XP            ║
 ║     🏗️ Activity 2 (Traffic Light): +100 XP   ║
 ║     🎮 Activity 3 (Custom Pattern): +25 XP   ║
 ║     ⚡ Quiz: up to +60 XP                    ║
 ║     ─────────────────────                    ║
 ║     💰 TOTAL: up to 285 XP                   ║
 ║                                              ║
 ╚══════════════════════════════════════════════╝
```

---

## 🔍 Coming Up Next...

**Module 2 Quiz!** 📝 Then on to **Module 3: Cool Projects** where you'll
build LED patterns, read sensors, play music with buzzers, and MORE! 🎵🌡️📏

---

*You just connected CODE to the REAL WORLD. You're not just a coder now — you're an INVENTOR!* 🔧✨

---

## Navigation

| | |
|:---|---:|
| [← 🎮 Raspberry Pi Explorer — Module 2, Lesson 2: LEDs and Circuits! 💡](lesson_02_leds_and_circuits.md) | [Module Overview →](README.md) |

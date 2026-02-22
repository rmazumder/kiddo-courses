# 🎮 Raspberry Pi Explorer — Module 3, Lesson 1: LED Patterns! ✨

```
 ╔══════════════════════════════════════════════════════════╗
 ║  MODULE 3: COOL PROJECTS  🎨                            ║
 ║  Lesson 1 of 3                                          ║
 ║  XP Available: 225 XP  |  Badge: ✨ Pattern Pro          ║
 ╚══════════════════════════════════════════════════════════╝
```

---

## 🌟 Your Mission Today

**Mission Briefing:** Time to get CREATIVE! 🎨 You've learned to blink a single
LED. Now you'll create amazing LED PATTERNS — flashing morse code, building a
binary counter, and creating light shows! By the end, you'll be a pattern
programming PRO! ✨

---

## 🎯 Learning Objectives

By the end of this lesson, you will be able to:
- ✅ Create complex LED patterns using loops and timing
- ✅ Send messages in Morse code using an LED
- ✅ Build a binary counter that displays numbers with LEDs
- ✅ Use Python lists and loops to make elegant pattern code

---

## 🪝 Hook — LEDs Are the New Fireworks! 🎆

What if you could send SECRET MESSAGES using just a flashlight? Spies, sailors,
and soldiers did this for over 100 years using **Morse Code** — a system of short
and long flashes that represent letters!

Today, YOU'll program your Raspberry Pi to send Morse code messages AND build
a binary counter that shows numbers using only LEDs. Let's make some light magic! ✨

---

## 🧠 Learning Point 1: Pattern Techniques 🔄

### Using Lists for LED Groups

Instead of writing separate code for each LED, we can use **lists** (arrays):

```python
import RPi.GPIO as GPIO
import time

# Define ALL our LED pins in a list!
LEDS = [17, 27, 22, 5]  # 4 LEDs on GPIO 17, 27, 22, and 5

GPIO.setmode(GPIO.BCM)

# Set ALL pins as output using a loop!
for led in LEDS:
    GPIO.setup(led, GPIO.OUT)
```

### Pattern: Chase / Scanner (Knight Rider!) 🚗

```python
# =============================================
# 🚗 KNIGHT RIDER SCANNER EFFECT
# LEDs light up one by one, back and forth!
# =============================================

import RPi.GPIO as GPIO
import time

LEDS = [17, 27, 22, 5]  # 4 LEDs
SPEED = 0.15              # Seconds between each LED

GPIO.setmode(GPIO.BCM)
for led in LEDS:
    GPIO.setup(led, GPIO.OUT)
    GPIO.output(led, GPIO.LOW)

print("🚗 Knight Rider Scanner Active!")
print("Press Ctrl+C to stop\n")

try:
    while True:
        # Scan forward →
        for led in LEDS:
            GPIO.output(led, GPIO.HIGH)
            time.sleep(SPEED)
            GPIO.output(led, GPIO.LOW)

        # Scan backward ←
        for led in reversed(LEDS):
            GPIO.output(led, GPIO.HIGH)
            time.sleep(SPEED)
            GPIO.output(led, GPIO.LOW)

except KeyboardInterrupt:
    print("\n🛑 Scanner stopped!")
finally:
    GPIO.cleanup()
```

### Pattern: Fill Up / Loading Bar 📊

```python
# =============================================
# 📊 LOADING BAR EFFECT
# LEDs fill up one by one, then all turn off!
# =============================================

import RPi.GPIO as GPIO
import time

LEDS = [17, 27, 22, 5]

GPIO.setmode(GPIO.BCM)
for led in LEDS:
    GPIO.setup(led, GPIO.OUT)
    GPIO.output(led, GPIO.LOW)

print("📊 Loading Bar Active!")

try:
    while True:
        # Fill up one by one
        for led in LEDS:
            GPIO.output(led, GPIO.HIGH)
            print(f"  Loading: {'█' * (LEDS.index(led) + 1)}{'░' * (len(LEDS) - LEDS.index(led) - 1)}")
            time.sleep(0.5)

        print("  ✅ LOADED!")
        time.sleep(1)

        # All off at once
        for led in LEDS:
            GPIO.output(led, GPIO.LOW)
        time.sleep(0.5)

except KeyboardInterrupt:
    print("\n🛑 Stopped!")
finally:
    GPIO.cleanup()
```

---

## 🧠 Learning Point 2: Morse Code Flasher! 📡

### What is Morse Code?

**Morse Code** is a system where each letter is represented by a combination of
**dots (short)** and **dashes (long)**.

```
MORSE CODE ALPHABET:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
A  ● ━━━        N  ━━━ ●
B  ━━━ ● ● ●    O  ━━━ ━━━ ━━━
C  ━━━ ● ━━━ ●  P  ● ━━━ ━━━ ●
D  ━━━ ● ●      Q  ━━━ ━━━ ● ━━━
E  ●             R  ● ━━━ ●
F  ● ● ━━━ ●    S  ● ● ●
G  ━━━ ━━━ ●    T  ━━━
H  ● ● ● ●      U  ● ● ━━━
I  ● ●           V  ● ● ● ━━━
J  ● ━━━ ━━━ ━━━ W  ● ━━━ ━━━
K  ━━━ ● ━━━    X  ━━━ ● ● ━━━
L  ● ━━━ ● ●    Y  ━━━ ● ━━━ ━━━
M  ━━━ ━━━      Z  ━━━ ━━━ ● ●

● = dot (short flash)     ━━━ = dash (long flash)

Famous code: SOS = ● ● ●  ━━━ ━━━ ━━━  ● ● ●
```

### Morse Code LED Program:

```python
# =============================================
# 📡 MORSE CODE FLASHER
# Send secret messages with your LED!
# Raspberry Pi Explorer - Module 3, Lesson 1
# =============================================

import RPi.GPIO as GPIO
import time

LED_PIN = 17

# Timing (in seconds)
DOT_TIME = 0.2       # Short flash
DASH_TIME = 0.6      # Long flash (3x dot)
SYMBOL_GAP = 0.2     # Gap between dots/dashes
LETTER_GAP = 0.6     # Gap between letters
WORD_GAP = 1.4       # Gap between words

# Morse Code Dictionary
MORSE_CODE = {
    'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',
    'E': '.',     'F': '..-.',  'G': '--.',   'H': '....',
    'I': '..',    'J': '.---',  'K': '-.-',   'L': '.-..',
    'M': '--',    'N': '-.',    'O': '---',   'P': '.--.',
    'Q': '--.-',  'R': '.-.',   'S': '...',   'T': '-',
    'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',
    'Y': '-.--',  'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.',
    ' ': ' '
}

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.output(LED_PIN, GPIO.LOW)

def flash_dot():
    """Short flash = dot"""
    GPIO.output(LED_PIN, GPIO.HIGH)
    print("  ● ", end="", flush=True)
    time.sleep(DOT_TIME)
    GPIO.output(LED_PIN, GPIO.LOW)
    time.sleep(SYMBOL_GAP)

def flash_dash():
    """Long flash = dash"""
    GPIO.output(LED_PIN, GPIO.HIGH)
    print("  ━━━ ", end="", flush=True)
    time.sleep(DASH_TIME)
    GPIO.output(LED_PIN, GPIO.LOW)
    time.sleep(SYMBOL_GAP)

def send_morse(message):
    """Send a complete message in Morse code!"""
    message = message.upper()
    print(f"\n📡 Sending: '{message}'\n")

    for char in message:
        if char == ' ':
            print("  [space]", end="")
            time.sleep(WORD_GAP)
        elif char in MORSE_CODE:
            print(f"  {char}: ", end="")
            for symbol in MORSE_CODE[char]:
                if symbol == '.':
                    flash_dot()
                elif symbol == '-':
                    flash_dash()
            print()  # New line after each letter
            time.sleep(LETTER_GAP)

    print("\n✅ Message sent!")

# --- MAIN PROGRAM ---
print("=" * 40)
print("📡 MORSE CODE FLASHER 📡")
print("=" * 40)

try:
    while True:
        message = input("\nType a message to flash (or 'quit'): ")
        if message.lower() == 'quit':
            break
        send_morse(message)

except KeyboardInterrupt:
    print("\n🛑 Stopped!")

finally:
    GPIO.cleanup()
    print("🧹 Cleaned up!")
```

---

## 🧠 Learning Point 3: Binary Counter with LEDs! 🔢

### What is Binary?

Computers think in **binary** — a number system with only two digits: **0** and **1**.

```
DECIMAL (how we count):   BINARY (how computers count):
        0           =     0000
        1           =     0001
        2           =     0010
        3           =     0011
        4           =     0100
        5           =     0101
        6           =     0110
        7           =     0111
        8           =     1000
        9           =     1001
       10           =     1010
       15           =     1111    ← All LEDs on!

Each LED represents a binary digit (bit):
   LED4  LED3  LED2  LED1
    8     4     2     1      ← Value of each position!

Example: Number 13 = 1101 in binary
   LED4  LED3  LED2  LED1
    ON    ON    OFF   ON     = 8 + 4 + 0 + 1 = 13!
```

### Binary Counter Code:

```python
# =============================================
# 🔢 BINARY COUNTER WITH LEDs
# Count from 0 to 15 using 4 LEDs!
# Raspberry Pi Explorer - Module 3, Lesson 1
# =============================================

import RPi.GPIO as GPIO
import time

# 4 LEDs representing 4 binary digits
# LED order: MSB (8) → LSB (1)
LEDS = [5, 22, 27, 17]   # GPIO pins for bit3, bit2, bit1, bit0
#        8    4    2   1   ← Binary values

GPIO.setmode(GPIO.BCM)
for led in LEDS:
    GPIO.setup(led, GPIO.OUT)
    GPIO.output(led, GPIO.LOW)

def display_number(number):
    """Display a number (0-15) on 4 LEDs in binary!"""
    # Convert number to 4-bit binary string
    binary = format(number, '04b')  # e.g., 5 → "0101"

    led_display = ""
    for i, bit in enumerate(binary):
        if bit == '1':
            GPIO.output(LEDS[i], GPIO.HIGH)
            led_display += "💡"
        else:
            GPIO.output(LEDS[i], GPIO.LOW)
            led_display += "⚫"

    print(f"  {number:2d} = {binary} = {led_display}")

# --- MAIN PROGRAM ---
print("=" * 40)
print("🔢 BINARY COUNTER")
print("=" * 40)
print("  #  = Binary = LEDs")
print("  8s   4s  2s  1s")
print("-" * 40)

try:
    while True:
        for number in range(16):   # Count 0 to 15
            display_number(number)
            time.sleep(1)          # 1 second per number
        print("\n🔄 Starting over!\n")

except KeyboardInterrupt:
    print("\n🛑 Counter stopped!")

finally:
    for led in LEDS:
        GPIO.output(led, GPIO.LOW)
    GPIO.cleanup()
    print("🧹 Cleaned up!")
```

---

## 🎮 Activity 1: SOS Flasher! 🆘

**+50 XP**

Use the Morse Code program to flash **SOS** (the international distress signal):

```
S = ● ● ●         (3 short flashes)
O = ━━━ ━━━ ━━━   (3 long flashes)
S = ● ● ●         (3 short flashes)
```

1. Run the Morse Code program
2. Type `SOS` when asked for a message
3. Watch your LED flash the SOS pattern!

```
□ LED flashes SOS pattern correctly
□ I can see the difference between dots (short) and dashes (long)
□ I tried flashing my own name in Morse code!
```

---

## 🎮 Activity 2: Build the Binary Counter! 🔢

**+75 XP**

Wire up 4 LEDs and run the binary counter program!

1. Connect 4 LEDs with resistors to GPIO 17, 27, 22, and 5
2. Run the binary counter code
3. Watch as it counts from 0 to 15 in binary!

**Challenge:** Can you look at the LEDs and tell what number is displayed?

```
Quiz yourself — what number do these LEDs show?

💡⚫💡⚫ = ___  (answer: 10 — binary 1010 = 8+0+2+0)
⚫⚫💡💡 = ___  (answer: 3  — binary 0011 = 0+0+2+1)
💡💡💡💡 = ___  (answer: 15 — binary 1111 = 8+4+2+1)
⚫💡⚫💡 = ___  (answer: 5  — binary 0101 = 0+4+0+1)
```

---

## 🎮 Activity 3: Design Your Own Pattern! 🎨

**+25 XP**

Create your own unique LED pattern! Pick one and code it:

- 🎄 **Christmas lights** — random LEDs blink at random speeds
- 🚨 **Emergency sirens** — two LEDs alternate fast
- 🌊 **Ocean wave** — LEDs fade in and out like waves
- 🎲 **Random dice** — press a button, random number of LEDs light up

---

## ⚡ Quick Quiz — Earn Bonus XP!

**+20 XP per correct answer!**

**Q1:** In Morse code, what does SOS look like?
- A) Three long, three short, three long
- B) Three short, three long, three short
- C) One long, one short, one long
- D) Six short flashes

**Q2:** What does the binary number 0101 equal in decimal?
- A) 3
- B) 5
- C) 7
- D) 10

**Q3:** In our binary counter, what does each LED represent?
- A) A color
- B) A letter
- C) A power of 2 (1, 2, 4, 8)
- D) A random number

<details>
<summary>🔍 Click to reveal answers!</summary>

- **Q1: B** — SOS = ● ● ● (short short short) ━━━ ━━━ ━━━ (long long long) ● ● ● (short short short)
- **Q2: B** — 0101 = 0+4+0+1 = 5!
- **Q3: C** — Each LED represents a power of 2: 1, 2, 4, 8

</details>

---

## 🏅 Lesson Complete — Pattern Pro Badge Earned!

```
 ╔══════════════════════════════════════════════╗
 ║                                              ║
 ║     🎉 PATTERN MASTER! 🎉                    ║
 ║                                              ║
 ║     You've earned the:                       ║
 ║                                              ║
 ║       ✨ PATTERN PRO BADGE ✨                  ║
 ║                                              ║
 ║     XP Earned: up to 225 XP                  ║
 ║                                              ║
 ╚══════════════════════════════════════════════╝
```

---

## 🔍 Coming Up Next...

**Lesson 3.2: Sensors!** 🌡️📏 Your Pi is about to learn how to SENSE the world
around it — temperature, humidity, and distance! 🔬

---

*You're creating real light shows with code! That's AMAZING!* ✨

---

## Navigation

| | |
|:---|---:|
| [← Module Overview](README.md) | [🎮 Raspberry Pi Explorer — Module 3, Lesson 2: Sensors! 🌡️📏 →](lesson_02_sensors.md) |

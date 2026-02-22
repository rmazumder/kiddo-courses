# 🎮 Raspberry Pi Explorer — Module 3, Lesson 3: Buzzer & Sound! 🎵

```
 ╔══════════════════════════════════════════════════════════╗
 ║  MODULE 3: COOL PROJECTS  🎨                            ║
 ║  Lesson 3 of 3                                          ║
 ║  XP Available: 250 XP  |  Badge: 🎵 Music Maker         ║
 ╚══════════════════════════════════════════════════════════╝
```

---

## 🌟 Your Mission Today

**Mission Briefing:** Your Pi can see with sensors and control with LEDs. Now
it's time to give it a VOICE! 🗣️ You'll use a buzzer to make beeps, play melodies
(including the Mario theme! 🍄), and even build an alarm system! Time to make
some noise! 🎵

---

## 🎯 Learning Objectives

By the end of this lesson, you will be able to:
- ✅ Know the difference between active and passive buzzers
- ✅ Wire a buzzer to the Raspberry Pi
- ✅ Make sounds with Python code
- ✅ Play a melody (Mario theme!) using frequency and timing
- ✅ Build a simple alarm system with a buzzer and sensor

---

## 🪝 Hook — Your Pi Learns to Sing! 🎤

What if your Pi could BEEP when someone walks too close? Or play your favorite
video game theme song? Or SCREAM like an alarm when someone opens your door?

With a tiny component called a **buzzer**, your Pi gets a voice! And today,
you're going to teach it to SING! 🎶

---

## 🧠 Learning Point 1: Active vs. Passive Buzzers 🔔

### Two Types of Buzzers:

```
    ACTIVE BUZZER                    PASSIVE BUZZER
    ┌─────────────┐                  ┌─────────────┐
    │  ┌───────┐  │                  │  ┌───────┐  │
    │  │ ●     │  │                  │  │       │  │
    │  │ BEEP! │  │                  │  │ ♪ ♫ ♪ │  │
    │  │       │  │                  │  │       │  │
    │  └───────┘  │                  │  └───────┘  │
    │  (sticker   │                  │  (no sticker│
    │   on top)   │                  │   OR open   │
    └──┬───────┬──┘                  │   holes)    │
       │       │                     └──┬───────┬──┘
      (+)     (-)                       │       │
       ▲                               │       │
    Has a (+) mark!                   No mark

    BEEP! (one tone)                 ♪ ♫ ♪ (any frequency!)
```

| Feature | Active Buzzer 🔔 | Passive Buzzer 🎵 |
|---------|-----------------|-------------------|
| Built-in oscillator? | YES | NO |
| How it works | Just add power = BEEP! | You control the frequency |
| Sound variety | ONE tone only | ANY note/frequency! |
| Code difficulty | Easy (just on/off) | Medium (need PWM) |
| Best for | Alarms, simple beeps | Music, melodies! |
| How to identify | Sticker/label on top; (+) mark | Open holes; no mark |

> 🔑 **Key Vocabulary:**
> - **Active Buzzer** = Has a built-in oscillator. Just power it = BEEP!
> - **Passive Buzzer** = YOU control the sound frequency. Can play melodies!
> - **PWM** = Pulse Width Modulation — a way to create different frequencies
> - **Frequency** = How fast something vibrates. Higher = higher pitch!
> - **Hz** = Hertz — the unit for frequency (vibrations per second)

---

## 🧠 Learning Point 2: Wiring the Buzzer 🔌

### Simple Buzzer Circuit:

```
    🍓 RASPBERRY PI               🍞 BREADBOARD

    GPIO 18 (Pin 12) ─────────── Buzzer (+) positive leg
    GND (Pin 6) ──────────────── Buzzer (-) negative leg

    It's THAT simple! No resistor needed for most buzzers!

    ┌──────────┐         ┌──────────┐
    │  Pi      │         │  Buzzer  │
    │          │         │  ┌──┐    │
    │ GPIO 18 ─┼─────────┼──│+ │   │
    │          │         │  │🔔│    │
    │ GND ─────┼─────────┼──│- │   │
    │          │         │  └──┘    │
    └──────────┘         └──────────┘
```

```
⚠️ IMPORTANT:
The buzzer has a positive (+) and negative (-) leg!
- (+) leg goes to GPIO pin
- (-) leg goes to GND
If you wire it backwards, it won't work (but won't break!)
```

---

## 🧠 Learning Point 3: Making Sounds with Code! 🎵

### Active Buzzer — Simple Beeps:

```python
# =============================================
# 🔔 ACTIVE BUZZER — BEEP PATTERNS
# Simple beeps using an active buzzer
# =============================================

import RPi.GPIO as GPIO
import time

BUZZER_PIN = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

def beep(duration=0.2):
    """Make a single beep!"""
    GPIO.output(BUZZER_PIN, GPIO.HIGH)
    time.sleep(duration)
    GPIO.output(BUZZER_PIN, GPIO.LOW)
    time.sleep(0.1)

def beep_pattern(pattern):
    """Play a pattern: S=short, L=long, P=pause"""
    for char in pattern:
        if char == 'S':
            beep(0.1)    # Short beep
        elif char == 'L':
            beep(0.4)    # Long beep
        elif char == 'P':
            time.sleep(0.3)  # Pause

print("🔔 Beep Pattern Demo!")

try:
    print("  Pattern 1: Alert!")
    beep_pattern("SSS")           # Three quick beeps
    time.sleep(1)

    print("  Pattern 2: Warning!")
    beep_pattern("SLSLSL")        # Alternating short/long
    time.sleep(1)

    print("  Pattern 3: SOS!")
    beep_pattern("SSSPLLLPSSS")   # SOS in buzzer!
    time.sleep(1)

    print("  Pattern 4: Doorbell!")
    beep_pattern("LP")            # Ding dong!
    beep_pattern("LP")

    print("\n✅ Demo complete!")

except KeyboardInterrupt:
    print("\n🛑 Stopped!")

finally:
    GPIO.output(BUZZER_PIN, GPIO.LOW)
    GPIO.cleanup()
```

---

### Passive Buzzer — Playing Notes! 🎶

With a **passive buzzer**, we use **PWM** (Pulse Width Modulation) to create
specific frequencies — which means specific MUSICAL NOTES!

### Musical Note Frequencies:

```
🎵 MUSICAL NOTE FREQUENCY CHART 🎵

Note    Freq(Hz)     Note    Freq(Hz)
─────────────────────────────────────
C4      262          C5      523
D4      294          D5      587
E4      330          E5      659
F4      349          F5      698
G4      392          G5      784
A4      440          A5      880
B4      494          B5      988

Higher frequency = Higher pitch! ⬆️
Lower frequency  = Lower pitch!  ⬇️
```

### Playing Notes with PWM:

```python
# =============================================
# 🎵 PASSIVE BUZZER — PLAY MUSICAL NOTES!
# Use PWM to create different frequencies
# =============================================

import RPi.GPIO as GPIO
import time

BUZZER_PIN = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

# Create a PWM object on the buzzer pin
buzzer_pwm = GPIO.PWM(BUZZER_PIN, 440)  # Start at 440 Hz (A4 note)

# Note frequencies (Hz)
NOTES = {
    'C4': 262, 'D4': 294, 'E4': 330, 'F4': 349,
    'G4': 392, 'A4': 440, 'B4': 494,
    'C5': 523, 'D5': 587, 'E5': 659, 'F5': 698,
    'G5': 784, 'A5': 880, 'B5': 988,
    'REST': 0
}

def play_note(note, duration=0.4):
    """Play a single musical note"""
    if note == 'REST' or note not in NOTES:
        buzzer_pwm.stop()
        time.sleep(duration)
    else:
        buzzer_pwm.ChangeFrequency(NOTES[note])
        buzzer_pwm.start(50)  # 50% duty cycle
        print(f"  ♪ {note} ({NOTES[note]} Hz)", end="\r")
        time.sleep(duration)
        buzzer_pwm.stop()
        time.sleep(0.05)  # Tiny gap between notes

def play_melody(melody):
    """Play a list of (note, duration) tuples"""
    for note, duration in melody:
        play_note(note, duration)

# --- SIMPLE SCALE ---
print("🎵 Playing C Major Scale!")
scale = [
    ('C4', 0.4), ('D4', 0.4), ('E4', 0.4), ('F4', 0.4),
    ('G4', 0.4), ('A4', 0.4), ('B4', 0.4), ('C5', 0.8),
]
play_melody(scale)
print("\n✅ Scale complete!")

time.sleep(1)

# --- TWINKLE TWINKLE LITTLE STAR ---
print("\n⭐ Playing Twinkle Twinkle Little Star!")
twinkle = [
    ('C4', 0.4), ('C4', 0.4), ('G4', 0.4), ('G4', 0.4),
    ('A4', 0.4), ('A4', 0.4), ('G4', 0.8),
    ('F4', 0.4), ('F4', 0.4), ('E4', 0.4), ('E4', 0.4),
    ('D4', 0.4), ('D4', 0.4), ('C4', 0.8),
]
play_melody(twinkle)
print("\n✅ Twinkle complete!")

buzzer_pwm.stop()
GPIO.cleanup()
```

---

## 🧠 Learning Point 4: MARIO THEME! 🍄⭐

The moment you've been waiting for — the **Super Mario Bros. theme song**!

```python
# =============================================
# 🍄 SUPER MARIO BROS. THEME SONG!
# Play the iconic melody on your Raspberry Pi!
# Raspberry Pi Explorer - Module 3, Lesson 3
# =============================================

import RPi.GPIO as GPIO
import time

BUZZER_PIN = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

buzzer = GPIO.PWM(BUZZER_PIN, 440)

# Extended note frequencies
NOTES = {
    'C4': 262, 'CS4': 277, 'D4': 294, 'DS4': 311, 'E4': 330,
    'F4': 349, 'FS4': 370, 'G4': 392, 'GS4': 415, 'A4': 440,
    'AS4': 466, 'B4': 494,
    'C5': 523, 'CS5': 554, 'D5': 587, 'DS5': 622, 'E5': 659,
    'F5': 698, 'FS5': 740, 'G5': 784, 'GS5': 831, 'A5': 880,
    'AS5': 932, 'B5': 988,
    'C6': 1047, 'D6': 1175, 'E6': 1319, 'F6': 1397, 'G6': 1568,
    'REST': 0
}

def play(note, duration):
    """Play a note for a duration"""
    if note == 'REST':
        buzzer.stop()
    else:
        buzzer.ChangeFrequency(NOTES[note])
        buzzer.start(50)
    time.sleep(duration)
    buzzer.stop()
    time.sleep(0.02)

# Tempo
T = 0.125  # Base tempo unit

print("=" * 40)
print("🍄 SUPER MARIO BROS. THEME 🍄")
print("=" * 40)
print("🎵 Playing now...\n")

try:
    # Main Theme - Opening
    play('E5', T*3); play('E5', T*3); play('REST', T*3); play('E5', T*3)
    play('REST', T*3); play('C5', T*3); play('E5', T*3)
    play('REST', T*3)
    play('G5', T*3)
    play('REST', T*9)
    play('G4', T*3)
    play('REST', T*9)

    # Part 2
    play('C5', T*6); play('REST', T*3)
    play('G4', T*6); play('REST', T*3)
    play('E4', T*6); play('REST', T*3)

    play('A4', T*3); play('REST', T*3)
    play('B4', T*3); play('REST', T*3)
    play('AS4', T*3); play('A4', T*3)
    play('REST', T*3)

    play('G4', T*2); play('E5', T*2); play('G5', T*2)
    play('A5', T*3); play('REST', T*3)
    play('F5', T*3); play('G5', T*3)
    play('REST', T*3)
    play('E5', T*3); play('REST', T*3)
    play('C5', T*3); play('D5', T*3); play('B4', T*3)

    print("\n🍄 IT'S-A ME, MARIO! 🍄")
    print("✅ Song complete!")

except KeyboardInterrupt:
    print("\n🛑 Music stopped!")

finally:
    buzzer.stop()
    GPIO.cleanup()
    print("🧹 Cleaned up!")
```

---

## 🧠 Learning Point 5: Alarm System Project! 🚨

Combine a buzzer with the distance sensor for a simple alarm:

```python
# =============================================
# 🚨 SIMPLE PROXIMITY ALARM
# Buzzer sounds when something gets too close!
# =============================================

import RPi.GPIO as GPIO
import time

BUZZER_PIN = 18
TRIG_PIN = 23
ECHO_PIN = 24
LED_PIN = 17
ALARM_DISTANCE = 30  # cm — trigger alarm if closer than this!

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(TRIG_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)

def measure_distance():
    """Measure distance with HC-SR04"""
    GPIO.output(TRIG_PIN, GPIO.LOW)
    time.sleep(0.05)
    GPIO.output(TRIG_PIN, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(TRIG_PIN, GPIO.LOW)

    timeout = time.time() + 1
    while GPIO.input(ECHO_PIN) == GPIO.LOW:
        pulse_start = time.time()
        if time.time() > timeout:
            return -1

    timeout = time.time() + 1
    while GPIO.input(ECHO_PIN) == GPIO.HIGH:
        pulse_end = time.time()
        if time.time() > timeout:
            return -1

    distance = (pulse_end - pulse_start) * 34300 / 2
    return round(distance, 1)

print("🚨 PROXIMITY ALARM ACTIVE!")
print(f"   Alarm triggers at {ALARM_DISTANCE} cm")
print("   Press Ctrl+C to stop\n")

try:
    while True:
        dist = measure_distance()
        if 0 < dist < ALARM_DISTANCE:
            # ALARM! Something is too close!
            print(f"  🚨 ALARM! Object at {dist} cm!")
            GPIO.output(BUZZER_PIN, GPIO.HIGH)
            GPIO.output(LED_PIN, GPIO.HIGH)
            time.sleep(0.2)
            GPIO.output(BUZZER_PIN, GPIO.LOW)
            GPIO.output(LED_PIN, GPIO.LOW)
            time.sleep(0.2)
        else:
            print(f"  ✅ Clear: {dist} cm")
            GPIO.output(BUZZER_PIN, GPIO.LOW)
            GPIO.output(LED_PIN, GPIO.LOW)
            time.sleep(0.5)

except KeyboardInterrupt:
    print("\n🛑 Alarm deactivated!")
finally:
    GPIO.output(BUZZER_PIN, GPIO.LOW)
    GPIO.output(LED_PIN, GPIO.LOW)
    GPIO.cleanup()
```

---

## 🎮 Activity 1: Play a Melody! 🎶

**+75 XP**

Wire up a passive buzzer and play one of these songs:
- ⭐ Twinkle Twinkle Little Star
- 🍄 Mario Theme
- 🎵 C Major Scale

```
□ Buzzer is wired correctly
□ I can hear the melody playing!
□ I tried changing the tempo (making it faster or slower)
```

---

## 🎮 Activity 2: Create Your Own Song! 🎤

**+50 XP**

Write a melody using the note system! Here's a template:

```python
# My custom song!
my_song = [
    ('C4', 0.4), ('E4', 0.4), ('G4', 0.4),  # Your notes here!
    ('C5', 0.8),  # End on a high note!
]
play_melody(my_song)
```

Try composing:
- Your name spelled out in notes
- A doorbell sound
- A victory fanfare
- A spooky melody

---

## 🎮 Activity 3: Proximity Alarm! 🚨

**+50 XP**

Build the alarm system using a buzzer + distance sensor!

```
□ Buzzer beeps when hand is close to the sensor
□ Buzzer stops when hand moves away
□ LED flashes along with the buzzer
□ I can adjust the alarm distance in the code
```

---

## ⚡ Quick Quiz — Earn Bonus XP!

**+20 XP per correct answer!**

**Q1:** What's the difference between an active and passive buzzer?
- A) Active is louder
- B) Active makes one tone; passive can play different frequencies
- C) They're the same
- D) Passive needs more power

**Q2:** What does PWM stand for?
- A) Power With Music
- B) Pin Width Management
- C) Pulse Width Modulation
- D) Passive Wire Module

**Q3:** What note is 440 Hz?
- A) C4 (Middle C)
- B) G4
- C) A4
- D) E4

<details>
<summary>🔍 Click to reveal answers!</summary>

- **Q1: B** — Active = one built-in tone. Passive = YOU control the frequency!
- **Q2: C** — Pulse Width Modulation — controls the frequency of signals!
- **Q3: C** — A4 (440 Hz) is the standard tuning note for all instruments! 🎵

</details>

---

## 🏅 Lesson Complete — Music Maker Badge Earned!

```
 ╔══════════════════════════════════════════════╗
 ║                                              ║
 ║     🎉 YOUR PI CAN SING! 🎉                  ║
 ║                                              ║
 ║     You've earned the:                       ║
 ║                                              ║
 ║        🎵 MUSIC MAKER BADGE 🎵                ║
 ║                                              ║
 ║     You played melodies and built an alarm!  ║
 ║     XP Earned: up to 250 XP                  ║
 ║                                              ║
 ╚══════════════════════════════════════════════╝
```

---

## 🔍 Coming Up Next...

**Module 3 Quiz!** Then on to **Module 4: Awesome Builds** where you'll create
FULL projects: a weather station, burglar alarm, and reaction game! 🌤️🚨🎮

---

*Your Pi can now see, feel, AND speak! It's becoming a real invention machine!* 🤖

# 🎮 Raspberry Pi Explorer — Module 4, Lesson 2: Burglar Alarm! 🚨

```
 ╔══════════════════════════════════════════════════════════╗
 ║  MODULE 4: AWESOME BUILDS  🏗️                           ║
 ║  Lesson 2 of 3 + Final Project                          ║
 ║  XP Available: 300 XP  |  Badge: 🚨 Alarm Expert        ║
 ╚══════════════════════════════════════════════════════════╝
```

---

## 🌟 Your Mission Today

**Mission Briefing:** Time to build a SECURITY SYSTEM! 🛡️ You'll combine a
distance sensor, buzzer, LEDs, and a button to create a burglar alarm that
detects intruders, sounds an alarm, and can be armed/disarmed with a secret
button press! Guard your room like a SPY! 🕵️

---

## 🎯 Learning Objectives

By the end of this lesson, you will be able to:
- ✅ Build a complete alarm system with multiple components
- ✅ Use a distance sensor as a motion/proximity detector
- ✅ Implement arm/disarm functionality with a button
- ✅ Create visual and audio alerts (LEDs + buzzer)
- ✅ Write a more complex Python program with multiple states

---

## 🪝 Hook — Guard Your Room! 🛡️

Ever wished you could KNOW when someone enters your room? What if your desk
had a FORCE FIELD that detected intruders? 🛡️

Today you're building exactly that — a real alarm system that:
- 🔍 DETECTS anyone who gets too close
- 🚨 SOUNDS a loud alarm
- 💡 FLASHES warning lights
- 🔘 Has an ARM/DISARM button (like a real security system!)

---

## 🧠 Hardware Setup

### What You Need:

```
□ 🍓 Raspberry Pi
□ 📏 HC-SR04 Ultrasonic Distance Sensor
□ 🔔 Active Buzzer (or Passive)
□ 💡 Red LED (alarm indicator)
□ 💡 Green LED (armed/disarmed indicator)
□ 🔘 Push Button
□ ⚡ 2x 220Ω Resistors (LEDs)
□ ⚡ 1x 1KΩ Resistor (voltage divider)
□ ⚡ 1x 2KΩ Resistor (voltage divider)
□ 🔗 Jumper wires
□ 🍞 Breadboard
```

### Complete Wiring Diagram:

```
    🍓 RASPBERRY PI                    🍞 BREADBOARD

    ┌─────────────┐
    │             │
    │  5V (Pin 2) ┼───────────────── HC-SR04 VCC
    │             │
    │  GPIO 23    ┼───────────────── HC-SR04 TRIG
    │  (Pin 16)   │
    │             │            ┌──── HC-SR04 ECHO
    │  GPIO 24    ┼──[1KΩ]──┤
    │  (Pin 18)   │           [2KΩ]
    │             │            └──── GND
    │  GND (Pin 6)┼───────────────── HC-SR04 GND
    │             │
    │  GPIO 18    ┼───────────────── Buzzer (+)
    │  (Pin 12)   │                  Buzzer (-) ──── GND
    │             │
    │  GPIO 17    ┼──[220Ω]──────── 🔴 Red LED (+)
    │  (Pin 11)   │                  Red LED (-) ──── GND
    │             │
    │  GPIO 27    ┼──[220Ω]──────── 🟢 Green LED (+)
    │  (Pin 13)   │                  Green LED (-) ── GND
    │             │
    │  GPIO 22    ┼───────────────── Button ──── 3.3V (Pin 1)
    │  (Pin 15)   │
    │             │
    └─────────────┘

    COMPONENT LAYOUT ON BREADBOARD:

    ┌────────────────────────────────────────────────┐
    │                                                │
    │    HC-SR04          Red LED    Green LED        │
    │   ┌──────┐         ┌──┐       ┌──┐            │
    │   │🔊  🎤│         │🔴│       │🟢│            │
    │   └┬─┬─┬─┘        [220Ω]    [220Ω]           │
    │    │ │ │ │          │          │               │
    │    V T E G         GPIO17    GPIO27            │
    │    C R C N                                     │
    │    C I H D     Buzzer        Button            │
    │      G O          ┌──┐       ┌──┐             │
    │                   │🔔│       │🔘│             │
    │                   └──┘       └──┘             │
    │                  GPIO18     GPIO22             │
    │                                                │
    └────────────────────────────────────────────────┘
```

---

## 🧠 The Complete Burglar Alarm Code:

```python
#!/usr/bin/env python3
# =============================================
# 🚨 BURGLAR ALARM SYSTEM
# Full security system with arm/disarm!
# Raspberry Pi Explorer - Module 4, Lesson 2
# =============================================

import RPi.GPIO as GPIO
import time
from datetime import datetime

# --- PIN CONFIGURATION ---
TRIG_PIN = 23       # HC-SR04 Trigger
ECHO_PIN = 24       # HC-SR04 Echo
BUZZER_PIN = 18     # Buzzer
RED_LED = 17        # Red LED (alarm/intruder!)
GREEN_LED = 27      # Green LED (system status)
BUTTON_PIN = 22     # Arm/Disarm button

# --- SETTINGS ---
ALARM_DISTANCE = 50     # cm — trigger if object closer than this
COOLDOWN_TIME = 3       # seconds before re-triggering
ARM_DELAY = 5           # seconds delay when arming (get out of the way!)

# --- SETUP ---
GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)
GPIO.setup(BUZZER_PIN, GPIO.OUT)
GPIO.setup(RED_LED, GPIO.OUT)
GPIO.setup(GREEN_LED, GPIO.OUT)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# --- STATE ---
system_armed = False
alarm_triggered = False
last_trigger_time = 0
alarm_log = []

# --- FUNCTIONS ---
def all_off():
    """Turn everything off"""
    GPIO.output(RED_LED, GPIO.LOW)
    GPIO.output(GREEN_LED, GPIO.LOW)
    GPIO.output(BUZZER_PIN, GPIO.LOW)

def measure_distance():
    """Measure distance with HC-SR04"""
    GPIO.output(TRIG_PIN, GPIO.LOW)
    time.sleep(0.05)
    GPIO.output(TRIG_PIN, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(TRIG_PIN, GPIO.LOW)

    timeout = time.time() + 1
    pulse_start = time.time()
    while GPIO.input(ECHO_PIN) == GPIO.LOW:
        pulse_start = time.time()
        if time.time() > timeout:
            return -1

    timeout = time.time() + 1
    pulse_end = time.time()
    while GPIO.input(ECHO_PIN) == GPIO.HIGH:
        pulse_end = time.time()
        if time.time() > timeout:
            return -1

    distance = (pulse_end - pulse_start) * 34300 / 2
    return round(distance, 1)

def sound_alarm(duration=3):
    """Sound the alarm with buzzer and flashing LED!"""
    print("  🚨🚨🚨 INTRUDER DETECTED! 🚨🚨🚨")
    start = time.time()
    while time.time() - start < duration:
        GPIO.output(BUZZER_PIN, GPIO.HIGH)
        GPIO.output(RED_LED, GPIO.HIGH)
        time.sleep(0.15)
        GPIO.output(BUZZER_PIN, GPIO.LOW)
        GPIO.output(RED_LED, GPIO.LOW)
        time.sleep(0.15)

        # Check if button pressed to disarm during alarm
        if GPIO.input(BUTTON_PIN) == GPIO.HIGH:
            return True  # Disarmed!
    return False  # Not disarmed

def arm_system():
    """Arm the alarm system with a countdown"""
    global system_armed
    print("\n  🔒 ARMING SYSTEM...")
    print(f"  ⏳ You have {ARM_DELAY} seconds to move away!")

    # Countdown with beeps
    for i in range(ARM_DELAY, 0, -1):
        print(f"  ⏳ {i}...")
        GPIO.output(GREEN_LED, GPIO.HIGH)
        GPIO.output(BUZZER_PIN, GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(BUZZER_PIN, GPIO.LOW)
        GPIO.output(GREEN_LED, GPIO.LOW)
        time.sleep(0.9)

    system_armed = True
    GPIO.output(GREEN_LED, GPIO.HIGH)  # Solid green = armed
    print("  🔒 SYSTEM ARMED! 🟢")
    print("  ───────────────────────────────────")

    # Double beep to confirm
    for _ in range(2):
        GPIO.output(BUZZER_PIN, GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(BUZZER_PIN, GPIO.LOW)
        time.sleep(0.1)

def disarm_system():
    """Disarm the alarm system"""
    global system_armed, alarm_triggered
    system_armed = False
    alarm_triggered = False
    all_off()

    # Friendly disarm sound
    for _ in range(3):
        GPIO.output(GREEN_LED, GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(GREEN_LED, GPIO.LOW)
        time.sleep(0.1)

    print("  🔓 SYSTEM DISARMED! ✅")
    print("  ───────────────────────────────────")

def show_status():
    """Display current system status"""
    print("\n╔══════════════════════════════════════════╗")
    print("║      🚨 BURGLAR ALARM SYSTEM 🚨          ║")
    print("╠══════════════════════════════════════════╣")
    if system_armed:
        print("║   Status: 🔒 ARMED        🟢 LED: ON    ║")
    else:
        print("║   Status: 🔓 DISARMED     ⚫ LED: OFF   ║")
    print(f"║   Detection Range: < {ALARM_DISTANCE} cm              ║")
    print(f"║   Alerts triggered: {len(alarm_log):<20}  ║")
    print("║                                          ║")
    print("║   🔘 Press BUTTON to ARM/DISARM           ║")
    print("║   ⌨️  Press Ctrl+C to shutdown             ║")
    print("╚══════════════════════════════════════════╝")

# --- MAIN PROGRAM ---
print()
print("  ██████╗ ██╗   ██╗██████╗  ██████╗ ██╗      █████╗ ██████╗ ")
print("  ██╔══██╗██║   ██║██╔══██╗██╔════╝ ██║     ██╔══██╗██╔══██╗")
print("  ██████╔╝██║   ██║██████╔╝██║  ███╗██║     ███████║██████╔╝")
print("  ██╔══██╗██║   ██║██╔══██╗██║   ██║██║     ██╔══██║██╔══██╗")
print("  ██████╔╝╚██████╔╝██║  ██║╚██████╔╝███████╗██║  ██║██║  ██║")
print("  ╚═════╝  ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝")
print("                    🚨 ALARM SYSTEM 🚨")
print()

show_status()

try:
    last_button_state = GPIO.LOW

    while True:
        # Check button for arm/disarm toggle
        button_state = GPIO.input(BUTTON_PIN)
        if button_state == GPIO.HIGH and last_button_state == GPIO.LOW:
            if system_armed:
                disarm_system()
            else:
                arm_system()
            show_status()
            time.sleep(0.5)  # Debounce

        last_button_state = button_state

        # If armed, check for intruders!
        if system_armed:
            distance = measure_distance()

            if 0 < distance < ALARM_DISTANCE:
                current_time = time.time()

                # Only trigger if cooldown has passed
                if current_time - last_trigger_time > COOLDOWN_TIME:
                    last_trigger_time = current_time
                    timestamp = datetime.now().strftime('%H:%M:%S')
                    alarm_log.append({
                        'time': timestamp,
                        'distance': distance
                    })

                    print(f"\n  🚨 ALERT at {timestamp}!")
                    print(f"  📏 Object detected at {distance} cm!")

                    # Sound alarm (returns True if disarmed during alarm)
                    was_disarmed = sound_alarm(duration=5)
                    if was_disarmed:
                        disarm_system()
                        show_status()
                    else:
                        GPIO.output(GREEN_LED, GPIO.HIGH)  # Re-enable armed LED
                        print("  🔒 System still armed. Monitoring...")
            else:
                # Show monitoring status periodically
                pass

        time.sleep(0.1)

except KeyboardInterrupt:
    print("\n\n🛑 Alarm system shutting down!")
    if alarm_log:
        print(f"\n📋 ALERT LOG ({len(alarm_log)} alerts):")
        for entry in alarm_log:
            print(f"   ⚠️  {entry['time']} — Object at {entry['distance']} cm")

finally:
    all_off()
    GPIO.cleanup()
    print("🧹 System powered down safely. Goodbye! 🔐")
```

---

## 🧠 How It Works — System States:

```
┌─────────────────────────────────────────────────┐
│                                                 │
│   🔓 DISARMED                                   │
│   ├── Green LED: OFF                            │
│   ├── Red LED: OFF                              │
│   ├── Buzzer: OFF                               │
│   └── Sensor: Not checking                      │
│       │                                         │
│       │ [BUTTON PRESS]                          │
│       ▼                                         │
│   ⏳ ARMING (5 second countdown)                │
│   ├── Green LED: Blinking                       │
│   ├── Buzzer: Countdown beeps                   │
│   └── "Get away from the sensor!"               │
│       │                                         │
│       ▼                                         │
│   🔒 ARMED                                      │
│   ├── Green LED: Solid ON                       │
│   ├── Sensor: Checking continuously             │
│   └── Waiting for intruder...                   │
│       │                                         │
│       ├── [OBJECT DETECTED < 50cm]              │
│       │   ▼                                     │
│       │   🚨 ALARM!                             │
│       │   ├── Red LED: Flashing                 │
│       │   ├── Buzzer: BEEPING LOUD              │
│       │   └── Logs the event                    │
│       │       │                                 │
│       │       ├── [BUTTON PRESS] → DISARMED     │
│       │       └── [5 seconds] → Back to ARMED   │
│       │                                         │
│       └── [BUTTON PRESS] → DISARMED             │
│                                                 │
└─────────────────────────────────────────────────┘
```

---

## 🎮 Activity 1: Build the Burglar Alarm! 🏗️

**+100 XP**

```
┌──────────────────────────────────────────────────┐
│         🚨 BURGLAR ALARM BUILD CHECKLIST         │
├──────────────────────────────────────────────────┤
│                                                  │
│  □ HC-SR04 wired with voltage divider            │
│  □ Buzzer wired to GPIO 18                       │
│  □ Red LED wired to GPIO 17                      │
│  □ Green LED wired to GPIO 27                    │
│  □ Button wired to GPIO 22                       │
│  □ All ground wires connected                    │
│  □ Code runs without errors                      │
│  □ Button arms/disarms the system                │
│  □ Alarm triggers when hand gets close!          │
│  □ Alarm sounds and LED flashes                  │
│  □ Took a photo/video! 📸                        │
│                                                  │
└──────────────────────────────────────────────────┘
```

---

## 🎮 Activity 2: Customize Your Alarm! 🔧

**+50 XP**

Modify the code to personalize your alarm:

```
□ Change the ALARM_DISTANCE (try 30 cm or 100 cm)
□ Change the ARM_DELAY (make it longer or shorter)
□ Add a custom alarm sound pattern
□ Make the alarm flash faster or slower
□ Add a "silent mode" (LED only, no buzzer)
```

---

## 🎮 Activity 3: Guard Your Room! 🛡️

**+50 XP**

Set up the alarm to actually guard something!

```
□ Point the sensor at your doorway
□ Arm the system
□ Walk through the doorway — does it trigger?
□ Have a friend or sibling try to sneak past!
□ Check the alert log at the end
```

---

## ⚡ Quick Quiz

**Q1:** What does the arm delay do?
- A) Makes the alarm louder
- B) Gives you time to move away before the sensor starts checking
- C) Charges the battery
- D) Updates the software

**Q2:** Why do we log alarm events with timestamps?
- A) To know exactly WHEN something was detected
- B) Because the buzzer needs timestamps
- C) To make the LEDs brighter
- D) To connect to Wi-Fi

<details>
<summary>🔍 Click to reveal answers!</summary>

- **Q1: B** — The arm delay gives you time to walk away before the system starts detecting!
- **Q2: A** — Logging timestamps tells you exactly when each detection happened!

</details>

---

## 🏅 Lesson Complete — Alarm Expert Badge Earned!

```
 ╔══════════════════════════════════════════════╗
 ║                                              ║
 ║     🎉 SECURITY SYSTEM OPERATIONAL! 🎉       ║
 ║                                              ║
 ║     You've earned the:                       ║
 ║                                              ║
 ║       🚨 ALARM EXPERT BADGE 🚨                ║
 ║                                              ║
 ║     XP Earned: up to 300 XP                  ║
 ║                                              ║
 ╚══════════════════════════════════════════════╝
```

---

## 🔍 Coming Up Next...

**Lesson 4.3: Reaction Speed Game!** 🎮 Build a 2-player game with buttons,
LEDs, and scorekeeping! Challenge your friends! 🏆

---

*You just built a real security system! Your room has never been safer!* 🔐

---

## Navigation

| | |
|:---|---:|
| [← 🎮 Raspberry Pi Explorer — Module 4, Lesson 1: Weather Station! 🌤️](lesson_01_weather_station.md) | [🎮 Raspberry Pi Explorer — Module 4, Lesson 3: Reaction Speed Game! 🎮 →](lesson_03_reaction_game.md) |

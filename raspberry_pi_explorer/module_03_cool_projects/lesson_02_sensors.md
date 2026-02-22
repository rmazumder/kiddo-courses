# 🎮 Raspberry Pi Explorer — Module 3, Lesson 2: Sensors! 🌡️📏

```
 ╔══════════════════════════════════════════════════════════╗
 ║  MODULE 3: COOL PROJECTS  🎨                            ║
 ║  Lesson 2 of 3                                          ║
 ║  XP Available: 250 XP  |  Badge: 🌡️ Sensor Master       ║
 ╚══════════════════════════════════════════════════════════╝
```

---

## 🌟 Your Mission Today

**Mission Briefing:** Your Pi can now control LEDs and read buttons. But what
if it could SENSE the world around it? 🌍 Today, you'll give your Pi the
ability to read **temperature**, **humidity**, and **distance** using real
electronic sensors! Your Pi is about to get superpowers! 🦸

---

## 🎯 Learning Objectives

By the end of this lesson, you will be able to:
- ✅ Understand what sensors are and how they work
- ✅ Wire and read a DHT11 temperature/humidity sensor
- ✅ Wire and read an HC-SR04 ultrasonic distance sensor
- ✅ Write Python code to collect real-world data!

---

## 🪝 Hook — Give Your Pi Super Senses! 👃👁️👂

Humans have 5 senses: sight, hearing, touch, taste, and smell. Your Raspberry Pi
starts with NONE of those. But with **sensors**, you can give it superpowers!

- 🌡️ **Temperature sensor** = Give your Pi the sense of TOUCH (hot/cold!)
- 📏 **Distance sensor** = Give your Pi the sense of SIGHT (how far!)
- 💧 **Humidity sensor** = Give your Pi the sense of FEEL (dry/moist!)

Imagine what you could build: a weather station, a burglar alarm, a robot that
avoids walls... the possibilities are ENDLESS! 🚀

---

## 🧠 Learning Point 1: What Are Sensors? 🔬

A **sensor** is an electronic component that detects something in the real world
and converts it into an electrical signal your Pi can read.

> 💡 **Analogy:** Sensors are like your Pi's EYES, EARS, and FINGERS!
> They detect things in the real world and report back to the Pi's brain.

### Common Sensors:

| Sensor | Detects | Symbol |
|--------|---------|--------|
| 🌡️ DHT11 | Temperature & Humidity | Temp/Humidity |
| 📏 HC-SR04 | Distance (using sound!) | Ultrasonic |
| 🔆 LDR | Light level | Light sensor |
| 🧲 Hall Effect | Magnetic fields | Magnet sensor |
| 🔊 Microphone | Sound | Sound sensor |
| 🔴 PIR | Motion (body heat) | Motion sensor |
| 💧 Soil Moisture | Wetness | Water sensor |

---

## 🧠 Learning Point 2: DHT11 — Temperature & Humidity! 🌡️💧

### What is the DHT11?

The **DHT11** is a small, blue sensor that reads **temperature** (0-50°C) and
**humidity** (20-80%). It's perfect for beginners!

```
    DHT11 Sensor (Front View):

    ┌─────────────┐
    │  ┌───────┐  │
    │  │ DHT11 │  │  ← Blue plastic case
    │  │       │  │
    │  │ ░░░░░ │  │  ← Sensing grid
    │  │ ░░░░░ │  │
    │  └───────┘  │
    │             │
    └──┬──┬──┬──┬─┘
       │  │  │  │
       1  2  3  4    ← 4 pins (but we only use 3!)

    Pin 1 = VCC (Power: 3.3V or 5V)
    Pin 2 = DATA (sends readings to Pi)
    Pin 3 = Not used (leave empty)
    Pin 4 = GND (Ground)
```

### Wiring the DHT11:

```
    🍓 RASPBERRY PI               🍞 BREADBOARD

    3.3V (Pin 1)  ─────────────── DHT11 Pin 1 (VCC)
    GPIO 4 (Pin 7) ──────────────  DHT11 Pin 2 (DATA)
                                   (Not connected) DHT11 Pin 3
    GND (Pin 6)    ─────────────── DHT11 Pin 4 (GND)

    Circuit Diagram:

    Pi Pin 1 (3.3V) ────────────────── DHT11 VCC
                                          │
    Pi Pin 7 (GPIO 4) ─────────────── DHT11 DATA
                                          │
                                       (skip pin 3)
                                          │
    Pi Pin 6 (GND) ────────────────── DHT11 GND
```

### Install the DHT Library:

Open the Terminal and type:
```bash
sudo pip3 install adafruit-circuitpython-dht
sudo apt install libgpiod2 -y
```

### DHT11 Python Code:

```python
# =============================================
# 🌡️ DHT11 TEMPERATURE & HUMIDITY READER
# Read real temperature and humidity!
# Raspberry Pi Explorer - Module 3, Lesson 2
# =============================================

import adafruit_dht
import board
import time

# Set up the DHT11 sensor on GPIO 4
dht_sensor = adafruit_dht.DHT11(board.D4)

print("=" * 45)
print("🌡️  TEMPERATURE & HUMIDITY READER  💧")
print("=" * 45)
print("Reading every 2 seconds... (Ctrl+C to stop)\n")

reading_count = 0

try:
    while True:
        try:
            # Read temperature and humidity
            temperature_c = dht_sensor.temperature
            humidity = dht_sensor.humidity

            if temperature_c is not None and humidity is not None:
                reading_count += 1
                temperature_f = temperature_c * 9/5 + 32  # Convert to Fahrenheit

                print(f"  📊 Reading #{reading_count}")
                print(f"  🌡️  Temperature: {temperature_c:.1f}°C ({temperature_f:.1f}°F)")
                print(f"  💧 Humidity:    {humidity:.1f}%")

                # Fun comments based on temperature!
                if temperature_c < 15:
                    print("  🥶 Brrr! It's cold!")
                elif temperature_c < 25:
                    print("  😊 Nice and comfortable!")
                elif temperature_c < 30:
                    print("  ☀️  Getting warm!")
                else:
                    print("  🔥 It's HOT!")

                print()
            else:
                print("  ⚠️  Sensor returned None, retrying...")

        except RuntimeError as e:
            # DHT sensors can sometimes fail to read — that's normal!
            print(f"  ⚠️  Sensor hiccup: {e}")
            print("  (This is normal! Trying again...)")

        time.sleep(2)  # Wait 2 seconds between readings

except KeyboardInterrupt:
    print(f"\n🛑 Stopped after {reading_count} readings!")

finally:
    dht_sensor.exit()
    print("🧹 Sensor cleaned up!")
```

> 💡 **Note:** The DHT11 sometimes fails to read — that's completely NORMAL!
> The code handles this with a try/except block. Just wait for the next reading!

---

## 🧠 Learning Point 3: HC-SR04 — Ultrasonic Distance Sensor! 📏

### What is the HC-SR04?

The **HC-SR04** measures distance using **ultrasonic sound waves** — sound so
high-pitched that humans can't hear it! (But bats can! 🦇)

```
    How it works:

    HC-SR04         Object (wall, hand, etc.)
    ┌──────┐              │
    │ 🔊   │ ──PING!──→   │   ← Sends out a sound pulse
    │      │              │
    │ 🎤   │ ←──echo────  │   ← Listens for the echo
    └──────┘              │

    Distance = (Time for echo to return) × Speed of Sound ÷ 2

    The "÷ 2" is because the sound travels THERE and BACK!
```

### HC-SR04 Pins:

```
    HC-SR04 (Front View):

    ┌─────────────────────────┐
    │   ┌─────┐  ┌─────┐     │
    │   │ 🔊  │  │ 🎤  │     │  ← Speaker + Microphone
    │   │TRIG │  │ECHO │     │
    │   └─────┘  └─────┘     │
    │                         │
    └──┬──────┬──────┬──────┬─┘
       │      │      │      │
      VCC   TRIG   ECHO    GND
      (5V)  (out)  (in)

    VCC  = Power (5V — this sensor needs 5V!)
    TRIG = Trigger (Pi sends a pulse OUT)
    ECHO = Echo (Pi reads the return IN)
    GND  = Ground
```

### ⚠️ IMPORTANT: Voltage Divider Needed!

```
⚠️ WARNING:
The ECHO pin sends back 5V, but GPIO pins can only handle 3.3V!
We need a VOLTAGE DIVIDER to reduce 5V to a safe 3.3V!

A voltage divider uses TWO resistors:

    ECHO pin ───── [1KΩ resistor] ──┬── GPIO 24
                                     │
                               [2KΩ resistor]
                                     │
                                    GND

This reduces 5V to about 3.3V — safe for your Pi! ✅
```

### Wiring Diagram:

```
    🍓 RASPBERRY PI               HC-SR04

    5V (Pin 2) ──────────────────── VCC
    GPIO 23 (Pin 16) ───────────── TRIG
    GPIO 24 (Pin 18) ──[1KΩ]──┬── ECHO
                               │
                            [2KΩ]
                               │
    GND (Pin 6) ──────────────┴── GND
```

### HC-SR04 Python Code:

```python
# =============================================
# 📏 ULTRASONIC DISTANCE SENSOR
# Measure distance with sound waves!
# Raspberry Pi Explorer - Module 3, Lesson 2
# =============================================

import RPi.GPIO as GPIO
import time

TRIG_PIN = 23   # Trigger (OUTPUT — sends the ping)
ECHO_PIN = 24   # Echo (INPUT — listens for the return)

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)

def measure_distance():
    """Measure distance in centimeters using HC-SR04"""

    # Send a 10 microsecond pulse to trigger
    GPIO.output(TRIG_PIN, GPIO.LOW)
    time.sleep(0.05)  # Let sensor settle
    GPIO.output(TRIG_PIN, GPIO.HIGH)
    time.sleep(0.00001)  # 10 microseconds
    GPIO.output(TRIG_PIN, GPIO.LOW)

    # Wait for echo to start (pin goes HIGH)
    timeout = time.time() + 1  # 1 second timeout
    while GPIO.input(ECHO_PIN) == GPIO.LOW:
        pulse_start = time.time()
        if time.time() > timeout:
            return -1  # Timeout!

    # Wait for echo to end (pin goes LOW)
    timeout = time.time() + 1
    while GPIO.input(ECHO_PIN) == GPIO.HIGH:
        pulse_end = time.time()
        if time.time() > timeout:
            return -1  # Timeout!

    # Calculate distance
    pulse_duration = pulse_end - pulse_start
    # Speed of sound = 34300 cm/s
    # Distance = (time × speed) / 2 (there and back!)
    distance = (pulse_duration * 34300) / 2

    return round(distance, 1)

# --- MAIN PROGRAM ---
print("=" * 45)
print("📏 ULTRASONIC DISTANCE SENSOR 📏")
print("=" * 45)
print("Measuring every 1 second... (Ctrl+C to stop)\n")

try:
    while True:
        distance = measure_distance()

        if distance > 0 and distance < 400:  # Valid range: 2-400 cm
            # Visual distance bar
            bar_length = min(int(distance / 5), 40)
            bar = "█" * bar_length

            print(f"  📏 Distance: {distance:6.1f} cm  |{bar}")

            # Fun distance descriptions!
            if distance < 10:
                print("     🤏 Super close!")
            elif distance < 30:
                print("     ✋ About a hand's length")
            elif distance < 100:
                print("     📐 About arm's length")
            elif distance < 200:
                print("     🚶 A couple steps away")
            else:
                print("     🏃 Pretty far!")
        else:
            print("  ⚠️  Out of range or error")

        time.sleep(1)

except KeyboardInterrupt:
    print("\n🛑 Sensor stopped!")

finally:
    GPIO.cleanup()
    print("🧹 Cleaned up!")
```

---

## 🎮 Activity 1: Temperature Logger! 📊

**+75 XP**

Wire up the DHT11 and run the temperature reader! Record the temperature in
different places:

```
┌──────────────────────────────────────────────────┐
│         🌡️ TEMPERATURE LOG                       │
├──────────────────────────────────────────────────┤
│                                                  │
│  Location 1: _____________ Temp: ___°C  ___°F   │
│  Location 2: _____________ Temp: ___°C  ___°F   │
│  Location 3: _____________ Temp: ___°C  ___°F   │
│                                                  │
│  Warmest place: _____________                    │
│  Coolest place: _____________                    │
│  Humidity right now: ____%                       │
│                                                  │
│  Bonus: Breathe on the sensor! What happens      │
│  to the humidity? ________________________       │
│                                                  │
└──────────────────────────────────────────────────┘
```

---

## 🎮 Activity 2: Distance Explorer! 📏

**+75 XP**

Wire up the HC-SR04 and measure distances!

```
┌──────────────────────────────────────────────────┐
│         📏 DISTANCE EXPERIMENTS                  │
├──────────────────────────────────────────────────┤
│                                                  │
│  1. Hold your hand 10 cm away                    │
│     Sensor reads: ___ cm   Accurate? YES / NO    │
│                                                  │
│  2. Hold your hand 30 cm away                    │
│     Sensor reads: ___ cm   Accurate? YES / NO    │
│                                                  │
│  3. Measure to the wall                          │
│     Sensor reads: ___ cm                         │
│     Tape measure says: ___ cm                    │
│     Difference: ___ cm                           │
│                                                  │
│  4. Slowly move your hand closer                 │
│     What's the MINIMUM distance it can read?     │
│     Answer: ___ cm                               │
│                                                  │
│  5. Point at something far away                  │
│     What's the MAXIMUM distance it reads?        │
│     Answer: ___ cm                               │
│                                                  │
└──────────────────────────────────────────────────┘
```

---

## 🎮 Activity 3: Sensor Data Scientist! 📈

**+25 XP**

Modify the temperature code to save readings to a file!

```python
# Add this to your DHT11 code to save data:

with open("temperature_log.txt", "a") as f:
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    f.write(f"{timestamp}, {temperature_c}°C, {humidity}%\n")
    print("  💾 Saved to temperature_log.txt!")
```

After 10 readings, open the file and look at your data!

```bash
cat temperature_log.txt
```

---

## ⚡ Quick Quiz — Earn Bonus XP!

**+20 XP per correct answer!**

**Q1:** What does the DHT11 sensor measure?
- A) Distance and speed
- B) Temperature and humidity
- C) Light and color
- D) Sound and volume

**Q2:** How does the HC-SR04 measure distance?
- A) With a laser beam
- B) With a camera
- C) With ultrasonic sound waves (too high for humans to hear)
- D) With a ruler inside

**Q3:** Why do we need a voltage divider on the HC-SR04's ECHO pin?
- A) To make it louder
- B) To change the color
- C) Because ECHO outputs 5V but GPIO only handles 3.3V safely
- D) To make it measure farther

<details>
<summary>🔍 Click to reveal answers!</summary>

- **Q1: B** — Temperature AND humidity! Two readings from one sensor!
- **Q2: C** — Ultrasonic sound waves! Like a bat! 🦇
- **Q3: C** — 5V would DAMAGE the GPIO pin! The voltage divider makes it safe. 🛡️

</details>

---

## 🏅 Lesson Complete — Sensor Master Badge Earned!

```
 ╔══════════════════════════════════════════════╗
 ║                                              ║
 ║     🎉 SENSOR POWERS UNLOCKED! 🎉            ║
 ║                                              ║
 ║     You've earned the:                       ║
 ║                                              ║
 ║       🌡️ SENSOR MASTER BADGE 🌡️               ║
 ║                                              ║
 ║     Your Pi can now sense temperature,       ║
 ║     humidity, and distance! INCREDIBLE! 🔬   ║
 ║                                              ║
 ║     XP Earned: up to 250 XP                  ║
 ║                                              ║
 ╚══════════════════════════════════════════════╝
```

---

## 🔍 Coming Up Next...

**Lesson 3.3: Buzzer & Sound!** 🎵 Your Pi learns to make MUSIC! Beeps, melodies,
and even the Mario theme song! 🍄

---

*Your Pi can now feel temperature and see distance! What a superpower upgrade!* 🦸

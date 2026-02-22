# 🎮 Raspberry Pi Explorer — Module 4, Lesson 1: Weather Station! 🌤️

```
 ╔══════════════════════════════════════════════════════════╗
 ║  MODULE 4: AWESOME BUILDS  🏗️                           ║
 ║  Lesson 1 of 3 + Final Project                          ║
 ║  XP Available: 300 XP  |  Badge: 🌤️ Weather Wizard      ║
 ╚══════════════════════════════════════════════════════════╝
```

---

## 🌟 Your Mission Today

**Mission Briefing:** You're about to build a COMPLETE weather station! 🌤️
This is your first FULL PROJECT — combining sensors, code, data logging, and
display into one awesome system. Real meteorologists use similar setups!
You're basically becoming a weather scientist! 🔬

---

## 🎯 Learning Objectives

By the end of this lesson, you will be able to:
- ✅ Build a complete weather station with the DHT11 sensor
- ✅ Display live temperature and humidity readings
- ✅ Log data to a file for tracking over time
- ✅ Create ASCII art weather displays in the terminal
- ✅ Understand how real weather monitoring works

---

## 🪝 Hook — Be Your Own Weather Reporter! 📺

Every morning, someone on TV tells you the weather. But what if YOU could be
the weather reporter? What if you had your OWN weather station, right on your
desk, giving you LIVE data?

That's EXACTLY what you're building today! 🌡️📊

---

## 🧠 The Full Weather Station — Hardware Setup

### What You Need:

```
□ 🍓 Raspberry Pi (powered and running)
□ 🌡️ DHT11 Temperature/Humidity Sensor
□ 💡 3 LEDs (Blue, Green, Red) — for temperature indicators
□ ⚡ 3x 220Ω Resistors
□ 🔗 Jumper wires
□ 🍞 Breadboard
```

### Wiring Diagram:

```
    🍓 RASPBERRY PI               🍞 BREADBOARD

    3.3V (Pin 1) ─────────────── DHT11 VCC (Pin 1)
    GPIO 4 (Pin 7) ──────────── DHT11 DATA (Pin 2)
    GND (Pin 6) ──────────────── DHT11 GND (Pin 4)

    GPIO 17 (Pin 11) ──[220Ω]── 🔵 Blue LED   (COLD)
    GPIO 27 (Pin 13) ──[220Ω]── 🟢 Green LED  (COMFORTABLE)
    GPIO 22 (Pin 15) ──[220Ω]── 🔴 Red LED    (HOT)

    All LED negative legs ────── GND rail

    ┌──────────────────────────────────────────────┐
    │                                              │
    │  DHT11        Blue LED   Green LED   Red LED │
    │  ┌───┐        ┌─┐        ┌─┐        ┌─┐    │
    │  │ T │        │🔵│       │🟢│       │🔴│    │
    │  │   │        │  │        │  │        │  │    │
    │  └┬┬┬┘       [220]      [220]      [220]   │
    │   │││          │          │          │      │
    │   │││        GPIO17    GPIO27     GPIO22    │
    │   ││└── GND    └──────────┴──────────┘      │
    │   │└─── GPIO4                    GND        │
    │   └──── 3.3V                                │
    │                                              │
    └──────────────────────────────────────────────┘
```

---

## 🧠 The Full Weather Station Code:

```python
#!/usr/bin/env python3
# =============================================
# 🌤️ RASPBERRY PI WEATHER STATION
# Full project with data logging & display!
# Raspberry Pi Explorer - Module 4, Lesson 1
# =============================================

import RPi.GPIO as GPIO
import adafruit_dht
import board
import time
import os
from datetime import datetime

# --- PIN CONFIGURATION ---
DHT_PIN = board.D4      # DHT11 data pin
COLD_LED = 17           # Blue LED — cold
COMFY_LED = 27          # Green LED — comfortable
HOT_LED = 22            # Red LED — hot

# --- TEMPERATURE THRESHOLDS ---
COLD_THRESHOLD = 18     # Below this = COLD
HOT_THRESHOLD = 28      # Above this = HOT

# --- SETUP ---
GPIO.setmode(GPIO.BCM)
GPIO.setup(COLD_LED, GPIO.OUT)
GPIO.setup(COMFY_LED, GPIO.OUT)
GPIO.setup(HOT_LED, GPIO.OUT)

dht_sensor = adafruit_dht.DHT11(DHT_PIN)

# Data log file
LOG_FILE = "/home/pi/weather_log.csv"

# --- HELPER FUNCTIONS ---
def all_leds_off():
    """Turn off all indicator LEDs"""
    GPIO.output(COLD_LED, GPIO.LOW)
    GPIO.output(COMFY_LED, GPIO.LOW)
    GPIO.output(HOT_LED, GPIO.LOW)

def set_temperature_led(temp):
    """Light up the appropriate LED based on temperature"""
    all_leds_off()
    if temp < COLD_THRESHOLD:
        GPIO.output(COLD_LED, GPIO.HIGH)     # 🔵 Cold!
        return "COLD 🥶"
    elif temp > HOT_THRESHOLD:
        GPIO.output(HOT_LED, GPIO.HIGH)      # 🔴 Hot!
        return "HOT 🔥"
    else:
        GPIO.output(COMFY_LED, GPIO.HIGH)    # 🟢 Just right!
        return "COMFORTABLE 😊"

def get_humidity_description(humidity):
    """Describe the humidity level"""
    if humidity < 30:
        return "DRY 🏜️"
    elif humidity < 60:
        return "NORMAL 👍"
    else:
        return "HUMID 💦"

def create_temp_bar(temp, min_temp=0, max_temp=50):
    """Create a visual temperature bar"""
    bar_length = 30
    filled = int((temp - min_temp) / (max_temp - min_temp) * bar_length)
    filled = max(0, min(filled, bar_length))
    return "█" * filled + "░" * (bar_length - filled)

def create_humidity_bar(humidity):
    """Create a visual humidity bar"""
    bar_length = 30
    filled = int(humidity / 100 * bar_length)
    return "█" * filled + "░" * (bar_length - filled)

def display_weather(temp_c, humidity, reading_num):
    """Display weather data with ASCII art!"""
    temp_f = temp_c * 9/5 + 32
    temp_status = set_temperature_led(temp_c)
    humidity_status = get_humidity_description(humidity)

    # Choose weather icon based on conditions
    if temp_c > HOT_THRESHOLD:
        weather_icon = """
        \\   |   /
         \\  |  /
      ----☀️----
         /  |  \\
        /   |   \\
        """
    elif temp_c < COLD_THRESHOLD:
        weather_icon = """
          ❄️  ❄️
        ❄️  ❄️  ❄️
          ❄️  ❄️
        ❄️  ❄️  ❄️
          ❄️  ❄️
        """
    else:
        weather_icon = """
           .-~~~-.
      .- ~ ~-(  )- ~-.
     (                )
      '- ._ ~ ~ _.- '
            ~~~
        """

    # Clear screen and display
    os.system('clear')

    print("╔══════════════════════════════════════════════════════╗")
    print("║         🌤️  RASPBERRY PI WEATHER STATION  🌤️        ║")
    print("╠══════════════════════════════════════════════════════╣")
    print(f"║  📊 Reading #{reading_num:<6}                              ║")
    print(f"║  🕐 {datetime.now().strftime('%Y-%m-%d %H:%M:%S'):<42}    ║")
    print("║                                                      ║")
    for line in weather_icon.strip().split('\n'):
        print(f"║  {line:<52}  ║")
    print("║                                                      ║")
    print("║  ─── TEMPERATURE ───────────────────────────────────  ║")
    print(f"║  🌡️  {temp_c:.1f}°C  ({temp_f:.1f}°F)  [{temp_status:<20}]    ║")
    print(f"║  [{create_temp_bar(temp_c)}] {temp_c:.0f}°C     ║")
    print("║                                                      ║")
    print("║  ─── HUMIDITY ──────────────────────────────────────  ║")
    print(f"║  💧 {humidity:.1f}%  [{humidity_status:<20}]              ║")
    print(f"║  [{create_humidity_bar(humidity)}] {humidity:.0f}%      ║")
    print("║                                                      ║")
    print("║  ─── INDICATOR LEDs ────────────────────────────────  ║")
    cold_state  = "💡ON " if temp_c < COLD_THRESHOLD else "⚫OFF"
    comfy_state = "💡ON " if COLD_THRESHOLD <= temp_c <= HOT_THRESHOLD else "⚫OFF"
    hot_state   = "💡ON " if temp_c > HOT_THRESHOLD else "⚫OFF"
    print(f"║  🔵 Cold: {cold_state}  🟢 Comfy: {comfy_state}  🔴 Hot: {hot_state}     ║")
    print("║                                                      ║")
    print("╠══════════════════════════════════════════════════════╣")
    print("║  Press Ctrl+C to stop | Data saved to weather_log   ║")
    print("╚══════════════════════════════════════════════════════╝")

def log_data(temp_c, humidity, reading_num):
    """Save data to a CSV log file"""
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Create file with headers if it doesn't exist
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, 'w') as f:
            f.write("Reading,Timestamp,Temperature_C,Temperature_F,Humidity_%\n")

    temp_f = temp_c * 9/5 + 32
    with open(LOG_FILE, 'a') as f:
        f.write(f"{reading_num},{timestamp},{temp_c:.1f},{temp_f:.1f},{humidity:.1f}\n")

# --- MAIN PROGRAM ---
print("🌤️ Weather Station Starting...")
print("Warming up sensor...\n")
time.sleep(2)

reading_count = 0

try:
    while True:
        try:
            temp_c = dht_sensor.temperature
            humidity = dht_sensor.humidity

            if temp_c is not None and humidity is not None:
                reading_count += 1
                display_weather(temp_c, humidity, reading_count)
                log_data(temp_c, humidity, reading_count)

        except RuntimeError as e:
            # DHT11 sometimes fails — just try again!
            pass

        time.sleep(3)  # Read every 3 seconds

except KeyboardInterrupt:
    print(f"\n\n🛑 Weather Station stopped after {reading_count} readings!")
    print(f"📁 Data saved to: {LOG_FILE}")
    print(f"   View with: cat {LOG_FILE}")

finally:
    all_leds_off()
    dht_sensor.exit()
    GPIO.cleanup()
    print("🧹 All cleaned up! Goodbye! 🌤️")
```

---

## 🎮 Activity 1: Build and Run the Weather Station! 🏗️

**+100 XP**

Follow the wiring diagram and run the complete weather station code!

```
┌──────────────────────────────────────────────────┐
│         🌤️ WEATHER STATION CHECKLIST             │
├──────────────────────────────────────────────────┤
│                                                  │
│  □ DHT11 sensor wired correctly                  │
│  □ 3 LEDs wired with resistors                   │
│  □ Code typed into Thonny                        │
│  □ Weather station displays on screen            │
│  □ Correct LED lights up based on temperature    │
│  □ Data is logging to weather_log.csv            │
│  □ Let it run for at least 10 minutes            │
│  □ Took a photo of the setup! 📸                 │
│                                                  │
└──────────────────────────────────────────────────┘
```

---

## 🎮 Activity 2: Weather Data Scientist! 📈

**+50 XP**

After running the weather station for at least 10 readings:

1. Open the log file: `cat /home/pi/weather_log.csv`
2. Answer these questions:

```
Highest temperature recorded: ___°C
Lowest temperature recorded:  ___°C
Average humidity:             ___%
Did the temperature go up or down over time? ___
What time of day was it warmest? ___
```

---

## 🎮 Activity 3: Weather Experiment! 🧪

**+50 XP**

Try these experiments with your weather station running:

```
□ 1. Breathe on the sensor — what happens to humidity?
     Answer: ___________________________________

□ 2. Put the sensor near a window — does temperature change?
     Answer: ___________________________________

□ 3. Put a cup of hot water near the sensor (carefully!)
     Answer: ___________________________________

□ 4. Cover the sensor with your hands
     Answer: ___________________________________
```

---

## ⚡ Quick Quiz — Earn Bonus XP!

**+20 XP per correct answer!**

**Q1:** Why do we log weather data to a CSV file?
- A) Because it looks cool
- B) To track changes over time and analyze trends
- C) Because the Pi needs a file to work
- D) To make the LEDs brighter

**Q2:** In our weather station, what color LED lights up when it's comfortable?
- A) 🔵 Blue
- B) 🔴 Red
- C) 🟢 Green
- D) 🟡 Yellow

<details>
<summary>🔍 Click to reveal answers!</summary>

- **Q1: B** — Data logging lets you see how temperature and humidity change over time!
- **Q2: C** — Green means comfortable! 🟢 Blue = cold, Red = hot.

</details>

---

## 🏅 Lesson Complete — Weather Wizard Badge Earned!

```
 ╔══════════════════════════════════════════════╗
 ║                                              ║
 ║     🎉 YOU BUILT A WEATHER STATION! 🎉       ║
 ║                                              ║
 ║     You've earned the:                       ║
 ║                                              ║
 ║       🌤️ WEATHER WIZARD BADGE 🌤️              ║
 ║                                              ║
 ║     XP Earned: up to 300 XP                  ║
 ║                                              ║
 ╚══════════════════════════════════════════════╝
```

---

## 🔍 Coming Up Next...

**Lesson 4.2: Burglar Alarm!** 🚨 Build a full security system with a distance
sensor, buzzer, LEDs, and arm/disarm controls!

---

*You just built a REAL weather monitoring system! That's professional-level stuff!* 🌤️⭐

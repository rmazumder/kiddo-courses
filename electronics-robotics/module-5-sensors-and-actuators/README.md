# Module 5: Sensors and Actuators

**Difficulty:** Star-4 Advanced
**Total Lessons:** 8
**Recommended Age:** 6--12 years
**Prerequisites:** Module 4 (Arduino Microcontroller)
**Total XP Available:** 1,640 XP

---

## What This Module Is About

Your Arduino has learned to blink, beep, and display messages. But right now it is **blind, deaf, and numb** to the world around it. Time to change that! In this module, you are going to give your Arduino real-world superpowers -- the ability to feel temperature, see light, hear echoes, sense motion, and respond by moving motors and flashing alerts.

Think of sensors as the **eyes, ears, and skin** of your Arduino, and actuators as its **arms and legs**. By the end of this module, you will build a complete **Smart Room System** that monitors temperature, detects motion, measures distance, and reacts automatically -- a real miniature smart home!

---

## Lessons in This Module

| Lesson | Topic | Fun Factor | XP |
|--------|-------|-----------|-----|
| [Lesson 35](lesson-35-temperature-sensor.md) | Temperature Sensor (DHT11) | Build your own weather station! | 210 |
| [Lesson 36](lesson-36-light-sensor.md) | Light Sensor (LDR) | Auto night light + Wand sees resistance change! | 190 |
| [Lesson 37](lesson-37-ultrasonic-distance-sensor.md) | Ultrasonic Distance Sensor (HC-SR04) | Parking sensor with LEDs and buzzer! | 185 |
| [Lesson 38](lesson-38-servo-motors.md) | Servo Motors | Control angle with a knob! | 185 |
| [Lesson 39](lesson-39-dc-motors-and-motor-driver.md) | DC Motors and Motor Driver (L298N) | Spin motors forward, backward, fast, slow! | 195 |
| [Lesson 40](lesson-40-ir-sensor-and-remote.md) | IR Sensor and Remote Control | Decode invisible light signals! | 165 |
| [Lesson 41](lesson-41-pir-motion-sensor.md) | PIR Motion Sensor | Smart night light with motion detection! | 190 |
| [Lesson 42](lesson-42-project-smart-room.md) | Project: Smart Room System | All sensors + actuators in one epic build! | 320 |

---

## Gamification System

### XP (Experience Points)
Every activity, experiment, and quiz question earns XP. Track your total across all 8 lessons!

**XP Ranks:**
| Rank | XP Required |
|------|-------------|
| Sensor Apprentice | 0--400 |
| Sensor Explorer | 401--800 |
| Sensor Specialist | 801--1,200 |
| Sensor Engineer | 1,201--1,500 |
| Sensor Champion | 1,501--1,640 |

### Badges
Earn one badge per lesson:

| Badge | Lesson | Earned? |
|-------|--------|---------|
| Weather Wizard | 35 | |
| Light Detective | 36 | |
| Echo Master | 37 | |
| Servo Commander | 38 | |
| Motor Master | 39 | |
| IR Code Breaker | 40 | |
| Motion Guardian | 41 | |
| Module 5 Champion | 42 | |

---

## Module Goals

By the end of this module, your child will:

- Interface 5+ different sensors with Arduino (temperature, light, distance, infrared, motion)
- Control servo motors and DC motors with speed and direction control
- Understand the difference between digital and analog sensors
- Use the `map()` function to scale sensor values
- Install and use Arduino libraries (DHT, Servo, IRremote, LiquidCrystal_I2C)
- **Use the multimeter confidently** to verify sensor power supplies, measure pin voltages, and debug circuits
- Build a complete Smart Room System integrating multiple sensors and actuators
- Write Arduino sketches that combine sensor inputs with actuator outputs

---

## The Magic Measurement Wand (Multimeter) in Module 5

The multimeter continues its role as the "Magic Measurement Wand" throughout this module. Every lesson includes a dedicated **Wand Check** section where children use the multimeter to verify their circuits and understand what is happening electrically.

**Wand Checks by lesson:**

| Lesson | What the Wand Measures |
|--------|----------------------|
| 35 -- Temperature Sensor | DHT11 VCC pin voltage (should be ~5V) and signal pin idle voltage |
| 36 -- Light Sensor | LDR resistance in bright light, room light, dim, and total darkness |
| 37 -- Ultrasonic Sensor | Trigger and echo pin voltages during operation |
| 38 -- Servo Motors | PWM signal average voltage at different servo angles |
| 39 -- DC Motors | Motor driver output voltage at 0%, 25%, 50%, 75%, and 100% speed |
| 40 -- IR Sensor | IR receiver output pin voltage (idle vs receiving signal) |
| 41 -- PIR Sensor | PIR output pin HIGH (~3.3V) vs LOW (~0V) |
| 42 -- Smart Room Project | Full 7-point system verification (5V rail, all sensor power, all sensor outputs) |

---

## Materials Needed for the Whole Module

| Item | Qty | Where to Get |
|------|-----|-------------|
| Arduino Uno + USB cable | 1 | Amazon |
| DHT11 temperature/humidity sensor | 1 | Amazon |
| LDR (photoresistor) | 2 | Amazon |
| HC-SR04 ultrasonic sensor | 1 | Amazon |
| HC-SR501 PIR motion sensor | 1 | Amazon |
| IR receiver module (VS1838B) | 1 | Amazon |
| Any IR remote control | 1 | (use an old TV/DVD remote!) |
| SG90 micro servo motor | 1 | Amazon |
| Small DC motor (3-6V) | 1 | Amazon |
| L298N motor driver module | 1 | Amazon |
| 16x2 LCD with I2C backpack | 1 | Amazon |
| 10k-ohm potentiometer | 1 | Amazon |
| Resistors: 330-ohm | 6 | Amazon |
| Resistors: 10k-ohm | 3 | Amazon |
| LEDs (red, green, yellow, blue) | 3 each | Amazon |
| Active buzzer | 1 | Amazon |
| Push buttons | 2 | Amazon |
| 9V battery + clip | 1 | Amazon |
| 830-point breadboard | 1 | Amazon |
| Jumper wires (pack of 65+) | 1 | Amazon |
| **Digital multimeter (Magic Measurement Wand)** | **1** | **Amazon (~$12)** |

> **Tip:** Most of these components are included in Arduino sensor kits available on Amazon for $15--25. If you have been following from Module 4, you likely already have the Arduino, breadboard, jumper wires, and multimeter.

---

## Parent/Instructor Notes

- Sessions of **40--45 minutes** work best for lessons 35--41. The project lesson (42) may need 60--75 minutes or can be split across two sessions.
- **Test one sensor at a time** before combining them. This is the most important debugging habit to teach.
- The PIR sensor (Lesson 41) needs a 30--60 second warm-up. Plan activities to fill that time.
- Ages 6--8: Focus on the hands-on wiring and observing the results. Simplify the code explanations -- emphasize what each section DOES rather than the syntax details.
- Ages 9--12: Encourage them to modify thresholds, add features, and explain WHY the code works.
- The Wand Check sections are especially powerful in this module because children can directly see the relationship between sensor readings and electrical signals.
- **Take photos or videos** of the Smart Room project -- kids love showing off complex builds!
- **Track XP visually** -- use a poster, whiteboard, or notebook. The gamification only works if kids can see their progress!
- If any sensor fails or is unavailable, the Smart Room project can still work with 3 out of 4 features.
- This module directly prepares for Module 6 (Robotics) -- the motor and sensor skills transfer to building mobile robots.

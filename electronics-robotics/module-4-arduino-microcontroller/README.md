# Module 4: Arduino Microcontroller

**Difficulty:** Star-3 Intermediate
**Total Lessons:** 10
**Recommended Age:** 6--12 years
**Prerequisites:** Module 3 -- Integrated Circuits (ICs)
**Total XP Available:** 2,750 XP

---

## What This Module Is About

You have learned components, circuits, and ICs. Now it is time to meet the most powerful tool in modern electronics: the **microcontroller**. A microcontroller is a tiny computer on a single chip, and you will program it to control LEDs, read buttons, play music, and display messages on a screen.

In this module, kids will set up an **Arduino Uno**, learn the basics of programming (variables, loops, conditions), and build increasingly impressive projects -- culminating in a **Digital Piano with LCD Display** that they programmed entirely themselves!

The **Magic Measurement Wand** (multimeter) continues to play a key role, helping kids verify that their code is actually producing the voltages they expect on each pin.

---

## Lessons in This Module

| Lesson | Topic | Fun Factor | XP |
|--------|-------|-----------|-----|
| [Lesson 25](lesson-25-what-is-a-microcontroller.md) | What is a Microcontroller? | First program upload! | 250 |
| [Lesson 26](lesson-26-your-first-sketch-blink.md) | Your First Sketch -- Blink | External LED blinks! | 250 |
| [Lesson 27](lesson-27-variables-and-serial-monitor.md) | Variables and Serial Monitor | Arduino talks back! | 250 |
| [Lesson 28](lesson-28-reading-digital-inputs-buttons.md) | Reading Digital Inputs -- Buttons | Button-controlled LED! | 250 |
| [Lesson 29](lesson-29-analog-inputs.md) | Analog Inputs | Potentiometer + Wand comparison! | 250 |
| [Lesson 30](lesson-30-pwm-dimming-leds.md) | PWM -- Dimming LEDs | Smooth LED fade + Wand proof! | 250 |
| [Lesson 31](lesson-31-for-loops-and-arrays.md) | For Loops and Arrays | Knight Rider LED chaser! | 250 |
| [Lesson 32](lesson-32-piezo-buzzer-and-tones.md) | Piezo Buzzer and Tones | Play Twinkle Twinkle! | 250 |
| [Lesson 33](lesson-33-lcd-display.md) | LCD Display (16x2) | Countdown timer on screen! | 250 |
| [Lesson 34](lesson-34-project-digital-piano.md) | Project: Digital Piano + Display | Build a real instrument! | 500 |

---

## Gamification System

### XP (Experience Points)
Every activity, experiment, and quiz question earns XP. Track your total across all 10 lessons!

**XP Ranks:**
| Rank | XP Required |
|------|-------------|
| Arduino Apprentice | 0--600 |
| Arduino Explorer | 601--1,200 |
| Arduino Builder | 1,201--1,800 |
| Arduino Engineer | 1,801--2,400 |
| Arduino Champion | 2,401--2,750 |

### Badges
Earn one badge per lesson:

| Badge | Lesson | Earned? |
|-------|--------|---------|
| Microcontroller Explorer | 25 | |
| Blink Master | 26 | |
| Variable Wizard | 27 | |
| Input Handler | 28 | |
| Analog Adventurer | 29 | |
| PWM Wizard | 30 | |
| Loop Legend | 31 | |
| Melody Maker | 32 | |
| Display Commander | 33 | |
| Module 4 Champion | 34 | |

---

## Module Goals

By the end of this module, your child will:

- Understand what a microcontroller is and identify parts of an Arduino Uno
- Write Arduino sketches using setup(), loop(), variables, if statements, and for loops
- Control digital outputs (LEDs, buzzers) and read digital inputs (buttons)
- Read analog inputs (potentiometers) and use PWM for analog-like output
- Use arrays to manage multiple components efficiently
- Play musical tones with specific frequencies
- Display text and live data on a 16x2 LCD screen
- **Use the multimeter to verify pin voltages, PWM averages, and debug circuits**
- Build a fully functional Digital Piano with display

---

## The Magic Measurement Wand (Multimeter) in Module 4

The Wand continues its role from earlier modules, now applied to Arduino circuits:

**Module 4 Wand Activities:**
1. **Lesson 25:** Measure the Arduino's 5V and 3.3V power pins
2. **Lesson 26:** Measure LED pin voltage when HIGH vs LOW
3. **Lesson 27:** Verify blinking pin voltage matches the code
4. **Lesson 28:** Measure button pin voltage (pressed vs not pressed with pull-up)
5. **Lesson 29:** Compare potentiometer voltage: Arduino reading vs Wand reading
6. **Lesson 30:** Measure PWM average voltage at different analogWrite values
7. **Lesson 31:** Quick pin verification for all 6 LEDs
8. **Lesson 32:** Observe tone signal average voltage on the buzzer pin
9. **Lesson 33:** Verify LCD power connections
10. **Lesson 34:** Full system debugging with the Wand

---

## Materials Needed for the Whole Module

| Item | Qty | Where to Get |
|------|-----|-------------|
| Arduino Uno board | 1 | Amazon / Adafruit |
| USB A-to-B cable | 1 | Amazon (often included with Arduino) |
| 830-point breadboard | 1 | Amazon |
| LEDs -- assorted colors | 10 | Amazon |
| 330-ohm resistors | 10 | Amazon |
| Push buttons (tactile switches) | 10 | Amazon |
| 10k-ohm potentiometer | 1 | Amazon |
| Piezo buzzer (passive type) | 1 | Amazon |
| 16x2 LCD display with I2C backpack | 1 | Amazon |
| Jumper wires (pack of 65+) | 1 | Amazon |
| Female-to-male jumper wires (for LCD) | 4 | Amazon |
| Computer with Arduino IDE installed | 1 | arduino.cc (free) |
| **Digital multimeter (Magic Measurement Wand)** | **1** | **Amazon (about $12)** |

> **Tip:** An "Arduino Starter Kit" (about $25--35 on Amazon) usually includes the Arduino Uno, breadboard, LEDs, resistors, buttons, potentiometer, buzzer, and jumper wires. Add an I2C LCD module (about $8) and a multimeter (about $12) separately.

---

## Parent/Instructor Notes

- Sessions of **40--45 minutes** work best for most lessons. The final project (Lesson 34) may take 60--75 minutes or can be split across two sessions.
- **Typing code** is part of the learning. Resist the urge to type for the child. Let them hunt-and-peck on the keyboard -- it builds familiarity with code syntax.
- **Debugging is learning.** When code does not work, walk through it line by line together. Use Serial.println() to print values at each step. Use the multimeter to verify hardware.
- Ages 6--8: Focus on the hands-on wiring and the visual results (blinking LEDs, sounds, LCD messages). Let them modify existing code rather than writing from scratch. Explain code in plain English rather than technical terms.
- Ages 9--12: Encourage them to write code modifications independently. Introduce the math (voltage conversion, PWM duty cycle). Challenge them with the bonus activities in each lesson.
- **Track XP visually** -- continue the poster or whiteboard from previous modules. The gamification works best when kids can see their cumulative progress.
- The multimeter ("Magic Measurement Wand") activities in this module are excellent for building the habit of measuring and verifying. The comparison between Arduino readings and Wand readings (Lesson 29) is particularly powerful for building confidence in both tools.
- **Save all sketches!** Create a folder on the computer for each lesson. Kids love going back and running their old programs.

# Module 6: Robotics Projects (FINAL MODULE)

**Difficulty:** Star-5 Expert
**Total Lessons:** 8 (Lessons 43--50)
**Recommended Age:** 6--12 years
**Prerequisites:** Modules 1--5 completed
**Total XP Available:** 2,490 XP

---

## THIS IS THE FINAL MODULE!

This is it -- the grand finale of the Electronics to Robotics course! Everything your child has learned across five modules -- components, circuits, ICs, Arduino programming, sensors, and motors -- comes together here. By the end of this module, they will have built a REAL, working, thinking robot.

---

## What This Module Is About

In Module 6, kids go from having a pile of parts to having a fully functioning robot that can drive, follow lines, avoid obstacles, respond to remote control, flash lights, make sounds, and even pick things up with a robot arm. The final lesson is a capstone project where they choose their own robot challenge and present it to an audience.

The **Magic Measurement Wand** (multimeter) continues to play a central role -- kids use it to verify motor voltage and current, check sensor signals, diagnose Bluetooth connections, and run a full robot health check before their final demo.

---

## Lessons in This Module

| Lesson | Topic | Fun Factor | XP |
|--------|-------|-----------|-----|
| [Lesson 43](lesson-43-robot-basics.md) | Robot Basics -- Chassis, Motors, Power | First time the robot MOVES! | 280 |
| [Lesson 44](lesson-44-robot-movement-functions.md) | Robot Movement Functions | Drive in a square and figure-8! | 240 |
| [Lesson 45](lesson-45-line-following-robot.md) | Line-Following Robot | Autonomous line tracking! | 270 |
| [Lesson 46](lesson-46-obstacle-avoiding-robot.md) | Obstacle-Avoiding Robot | Robot dodges obstacles like a bat! | 250 |
| [Lesson 47](lesson-47-buzzer-and-leds-robot-personality.md) | Buzzer and LEDs -- Robot Personality | Robot gets eyes and a voice! | 220 |
| [Lesson 48](lesson-48-remote-controlled-robot-bluetooth.md) | Remote-Controlled Robot (Bluetooth) | Drive from your phone! | 260 |
| [Lesson 49](lesson-49-robot-arm-introduction.md) | Robot Arm Introduction | Build a pick-and-place arm! | 250 |
| [Lesson 50](lesson-50-final-capstone-project.md) | Final Capstone Project | Choose your challenge + demo day! | 310 |

---

## Gamification System

### XP (Experience Points)
Every activity, experiment, and quiz question earns XP. Track your total across all 8 lessons!

**Module 6 XP Ranks:**
| Rank | XP Required |
|------|-------------|
| Robot Rookie | 0--500 |
| Robot Builder | 501--1,000 |
| Robot Programmer | 1,001--1,500 |
| Robot Engineer | 1,501--2,000 |
| Robot Master | 2,001--2,490 |

### Badges
Earn one badge per lesson:

| Badge | Lesson | Earned? |
|-------|--------|---------|
| Robot Builder | 43 | |
| Movement Master | 44 | |
| Line Tracker | 45 | |
| Obstacle Navigator | 46 | |
| Robot Personality Designer | 47 | |
| Wireless Commander | 48 | |
| Robot Arm Engineer | 49 | |
| Robot Master + Circuit Champion | 50 | |

---

## Module Goals

By the end of this module, your child will:

- Assemble a robot chassis with motors and power systems
- Write clean, reusable movement functions for robot control
- Build a line-following robot using IR sensors
- Build an obstacle-avoiding robot using ultrasonic sensing
- Add LED indicators and buzzer sound effects to communicate robot state
- Control a robot wirelessly via Bluetooth from a smartphone
- Build and control a 3-DOF servo-based robot arm
- Complete a capstone project demonstrating combined skills
- **Run a full robot diagnostic using the Magic Measurement Wand**
- Present and explain their robot to an audience

---

## The Magic Measurement Wand in Module 6

The multimeter is used in EVERY lesson of this module for increasingly sophisticated measurements:

| Lesson | Wand Activity |
|--------|--------------|
| 43 | Measure motor battery voltage, motor terminal voltage, motor current draw |
| 44 | Measure L298N output voltage during forward, backward, and stop states |
| 45 | Measure IR sensor output voltage on black vs white surfaces |
| 46 | Measure ultrasonic sensor VCC, trigger pin pulse, servo signal voltage |
| 47 | Measure LED voltage drops, resistor voltage, buzzer signal average |
| 48 | Measure HC-05 VCC, TX/RX pin voltages, voltage divider output |
| 49 | Measure servo power rail under load, signal pin voltages, current draw |
| 50 | Full robot health diagnostic -- batteries, motors, sensors, continuity |

---

## Materials Needed for This Module

| Item | Qty | Where to Get |
|------|-----|-------------|
| 2WD robot chassis kit (chassis, 2x DC motors, wheels, caster) | 1 | Amazon |
| L298N motor driver module | 1 | Amazon |
| Arduino Uno (from Module 4) | 1 | Already have |
| 4x AA battery holder + batteries | 1 | Amazon / any store |
| 9V battery + clip (for Arduino) | 1 | Any store |
| IR line sensor modules (TCRT5000) | 2 | Amazon |
| HC-SR04 ultrasonic sensor (from Module 5) | 1 | Already have |
| SG90 servo motors | 3 | Amazon |
| Servo mounting bracket | 1 | Amazon |
| HC-05 Bluetooth module | 1 | Amazon |
| LEDs -- green, red, blue | 2 each + 1 | Already have |
| 330-ohm resistors | 5 | Already have |
| 1k-ohm and 2k-ohm resistors (for voltage divider) | 1 each | Already have |
| Passive or active buzzer | 1 | Already have |
| 10k-ohm potentiometers | 3 | Already have |
| Popsicle sticks, cardboard (for robot arm) | 10 + several | Craft store |
| Black electrical tape | 1 roll | Hardware store |
| White poster board | 1 | Office supply |
| Hot glue gun (adult supervised) | 1 | Craft store |
| **Digital multimeter (Magic Measurement Wand!)** | **1** | **Already have** |

> **Tip:** Search "2WD robot chassis kit" on Amazon -- complete kits with motors, wheels, and chassis plate cost about $10--15.

---

## Capstone Project Options (Lesson 50)

Students choose ONE of these for their final project:

| Project | Type | Key Components |
|---------|------|---------------|
| A: Maze Solver | Navigation | Ultrasonic sensor, servo scanner |
| B: Delivery Bot | Line following + stations | IR sensors, buzzer, counter |
| C: Security Bot | Patrol + detection | PIR sensor, ultrasonic, alarm system |
| D: Robot Arm Game | Manual control + timer | 3 servos, potentiometers, score system |

All projects require at least 3 sensors/modules, autonomous behavior, and a live demonstration.

---

## Parent/Instructor Notes

- This module is the most complex and exciting. Plan for **50--60 minute sessions** (Lesson 50 may take 2--3 sessions).
- **Let the robot fail!** Debugging is the most valuable learning activity. Guide kids to use the multimeter to find problems.
- The Bluetooth lesson (48) requires a smartphone. Android works best with HC-05. For iOS, consider an HM-10 BLE module.
- Robot arm construction (Lesson 49) requires hot glue -- an adult should handle the glue gun.
- **Demo Day (Lesson 50) is critical!** Invite family or friends. Presenting builds confidence and solidifies learning through teaching.
- Consider printing a certificate of completion with the child's name.
- Track cumulative XP across all 6 modules on a poster -- the journey from 0 to 13,520 XP is an incredible visual of growth.
- This module transforms kids from "students" into "engineers." Celebrate that transformation!

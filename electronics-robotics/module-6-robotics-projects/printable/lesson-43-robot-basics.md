# Lesson 43: Robot Basics — Chassis, Motors, Power -- Quick Reference

**Age:** 6--12 years | **Time:** 50--60 min | **XP:** 240

---

## What is a Robot?

**A robot is a machine that moves and makes decisions:**
- It has **motors** (muscles) to move
- It has **sensors** (eyes) to see
- It has an **Arduino** (brain) to think
- It has **power** (battery) to run

---

## The Chassis

![Robot Chassis Assembly](../images/lesson-43-robot-chassis-assembly.png)

**Your robot's body contains:**
- **2 DC Motors** - Drive the wheels left and right
- **2 Wheels** - Attached to the motors
- **1 Caster Wheel** - Keeps the robot balanced (like a skateboard)
- **Chassis Plate** - The plastic skeleton holding everything

---

## How Robots Turn

![Differential Drive Steering](../images/lesson-43-differential-drive-steering.png)

**Tank steering (differential drive):**

| Movement | Left Motor | Right Motor | Result |
|----------|-----------|------------|--------|
| Forward | FAST | FAST | Go straight |
| Backward | SLOW | SLOW | Go backward |
| Turn Right | FAST | SLOW | Curve right |
| Turn Left | SLOW | FAST | Curve left |
| Spin Right | FAST | BACKWARD | Spin in place |

**Key idea:** Different wheel speeds = robot turns!

---

## Motor Control with L298N

![L298N Motor Driver Wiring](../images/lesson-43-l298n-motor-wiring.png)

**The L298N is a motor "traffic cop":**
- Receives control signals from Arduino
- Tells each motor how fast to go
- Supplies power to the motors

**Pin connections:**

| L298N Pin | Arduino Pin |
|-----------|------------|
| IN1 | Digital 2 |
| IN2 | Digital 3 |
| IN3 | Digital 4 |
| IN4 | Digital 5 |
| OUT1 | Left motor (+) |
| OUT2 | Left motor (-) |
| OUT3 | Right motor (+) |
| OUT4 | Right motor (-) |
| +5V | Arduino 5V |
| GND | Arduino GND |
| VCC Motor | Battery pack (9V) |

---

## Quick Quiz

**Q1:** What does a DC motor do in the robot?
**A:** It converts electrical power into spinning motion to drive the wheels.

**Q2:** How does a robot turn right?
**A:** The left motor goes FAST and the right motor goes SLOW.

**Q3:** What is the L298N?
**A:** A motor driver that controls how fast each motor spins.

---

## Challenge

**Mission: Make your robot drive in a square!**
- Forward for 2 seconds
- Right turn for 1 second
- Repeat 4 times

Use the motor control functions to accomplish this!

---

*Print this with the motor wiring diagram for quick reference!*

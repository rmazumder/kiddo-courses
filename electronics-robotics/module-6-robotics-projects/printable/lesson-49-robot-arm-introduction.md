# Lesson 49: Robot Arm Introduction (Servo-Based) -- Quick Reference

**Age:** 6--12 years | **Time:** 90--100 min | **XP:** 340

---

## Degrees of Freedom (DOF)

![DOF Human Arm Analogy](../images/lesson-49-dof-human-arm.png)

**Each joint in an arm = 1 degree of freedom (DOF)**

| Joint | Movement | Example |
|-------|----------|---------|
| Shoulder | Up/down, side/side | Rotate servo |
| Elbow | Bend forward/back | Rotate servo |
| Wrist | Twist/rotate | Rotate servo |

**A robot arm with 3 servo motors = 3 DOF**

**Analogy:** Your human arm has similar joints, so your robot arm moves like your arm!

```
Human Arm:           Robot Arm:
SHOULDER (blue)  →   SERVO 1
ELBOW (orange)   →   SERVO 2
WRIST (yellow)   →   SERVO 3
```

---

## Control Servo with Potentiometer

![Potentiometer Servo Control](../images/lesson-49-potentiometer-servo-control.png)

**Turn a knob → servo arm moves to match!**

```cpp
#include <Servo.h>

Servo armServo;
int potPin = A0;

void setup() {
  armServo.attach(9);  // Servo on pin 9
}

void loop() {
  int potValue = analogRead(potPin);        // 0-1023
  int angle = map(potValue, 0, 1023, 0, 180);  // Convert to 0-180°
  armServo.write(angle);                    // Move servo to angle
  delay(15);
}
```

**The `map()` function converts one range to another:**
- Input: 0–1023 (potentiometer)
- Output: 0–180° (servo angle)

---

## Preset Positions (Pick-and-Place)

![Robot Arm Pickup Sequence](../images/lesson-49-robot-arm-pickup-sequence.png)

**Program specific arm positions for tasks:**

```cpp
// Define preset positions
#define HOME 90
#define REACH_FORWARD 45
#define GRAB 30
#define PLACE 120

void setup() {
  armServo.attach(9);
}

void pickAndPlace() {
  // Start at HOME position
  armServo.write(HOME);
  delay(1000);

  // REACH forward
  armServo.write(REACH_FORWARD);
  delay(1000);

  // GRAB (close gripper)
  grabGripper();
  delay(500);

  // PLACE item
  armServo.write(PLACE);
  delay(1000);

  // Release gripper
  releaseGripper();

  // Return HOME
  armServo.write(HOME);
}
```

---

## Servo Motor Basics

| Property | Value |
|----------|-------|
| **Power** | 5V (from Arduino) |
| **Signal** | PWM on digital pin |
| **Angle Range** | 0° to 180° |
| **Speed** | ~60°/second typical |
| **Torque** | Depends on servo model |
| **Response Time** | 15ms delay minimum |

---

## Real-World Robot Arms

- 🤖 **Industrial robots** - Factory assembly arms (6-8 DOF)
- 🦾 **Prosthetic limbs** - Helping people with disabilities
- 🛰️ **Space robots** - Robotic arms on space stations (like Canadarm)
- 🏭 **Welding robots** - Precise movements in factories
- 🧪 **Lab automation** - Medical and scientific applications

---

## Quick Quiz

**Q1:** What is a degree of freedom (DOF)?
**A:** Each movable joint in the arm. A 3-servo arm has 3 DOF.

**Q2:** What does the `map()` function do?
**A:** Converts values from one range (like potentiometer 0–1023) to another range (like servo angle 0–180).

**Q3:** What is the typical angle range for a servo?
**A:** 0° to 180°.

---

## Challenge

**Multi-joint control:** Add a second servo and potentiometer to control both the arm and a rotating wrist. Program preset positions for pick-and-place!

---

*Print this with the DOF diagram and servo control flowchart for reference!*

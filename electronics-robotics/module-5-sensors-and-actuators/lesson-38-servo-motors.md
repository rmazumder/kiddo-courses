# Lesson 38: Servo Motors -- Precision Arm Muscles

**Module:** 5 -- Sensors and Actuators
**Difficulty:** Star-4 Advanced
**Session Time:** 40--45 minutes
**Age:** 6--12 years
**XP Available:** 275 XP

---

## Your Mission Today

Circuit Explorer, so far your Arduino can sense the world -- temperature, light, and distance. But it cannot DO anything about it! Today that changes. You are going to learn about **servo motors** -- small motors that can move to an exact angle, like a robot arm joint. You will make a servo sweep back and forth, control it with a knob, and even build a scanning sonar system using your ultrasonic sensor from last lesson!

---

## Learning Objectives

By the end of this lesson, you will be able to:
- Explain what a servo motor is and how it differs from a regular motor
- Wire a servo motor to Arduino
- Write code to move a servo to a specific angle (0 to 180 degrees)
- Control a servo with a potentiometer (dial)
- Use your Magic Measurement Wand to measure the servo signal voltage

---

## What You Need

| Item | Qty |
|------|-----|
| Arduino Uno + USB cable | 1 |
| SG90 micro servo motor | 1 |
| 10k-ohm potentiometer | 1 |
| Breadboard | 1 |
| Jumper wires | 8 |
| Multimeter (your Magic Measurement Wand!) | 1 |
| Small arrow or pointer (tape + paper) to attach to servo horn | 1 |

---

## How to Teach This Lesson

### Step 1: Hook -- The Robot Arm Dream (5 min)

> "Close your eyes and imagine a robot arm picking up a ball, moving it across the table, and setting it down gently. How does that arm move so precisely? It does not just spin wildly -- it moves to EXACT positions. The secret? Servo motors!"

Show them the SG90 servo:

> "This tiny blue box has a gear system inside and a small motor. But unlike a regular motor that just spins and spins, a servo can move to a specific angle and HOLD that position. Tell it 'go to 90 degrees' and it goes exactly there. Tell it '45 degrees' and it moves there. It is like a motor that follows orders!"

Let them feel the servo horn and try to turn it manually (with no power) -- they will feel the resistance of the gears.

**Award: +10 XP for learning about servos!**

---

### Step 2: How a Servo Works (8 min)

**The Clock Hand Analogy:**

> "Think of a clock hand. It can point to 12 o'clock, 3 o'clock, 6 o'clock -- any position in a half circle. A servo does the same thing, moving from 0 degrees (all the way left) to 180 degrees (all the way right). And just like a clock hand, it STAYS where you tell it to go."

**Inside the servo:**

```
  Inside an SG90 Servo:
  +---------------------------+
  |   [Gear train]            |
  |   Small DC motor          |
  |   Position sensor (pot)   |
  |   Control circuit board   |
  +---------------------------+
       |    |    |
     Brown  Red  Orange
     (GND) (VCC) (Signal)
```

**Key vocabulary:**

- **Servo motor:** A motor with built-in position control. Moves to a commanded angle and holds there.
- **Horn:** The plastic arm/disc on top that connects to whatever you want to move.
- **PWM signal:** The signal wire receives Pulse Width Modulation -- tiny electrical pulses that tell the servo what angle to go to. Short pulse = 0 degrees. Long pulse = 180 degrees.
- **SG90:** A very popular, inexpensive micro servo. Moves 0 to 180 degrees.

**The three wires:**

| Wire Color | Function | Connects To |
|-----------|---------|------------|
| Brown (or black) | Ground (GND) | Arduino GND |
| Red | Power (VCC) | Arduino 5V |
| Orange (or yellow) | Signal | Arduino PWM pin |

**Award: +10 XP for understanding servo internals!**

---

### Step 3: Wiring the Servo (5 min)

**Wiring diagram:**

```
  Servo               Arduino
  --------            --------
  Brown  (GND) -----> GND
  Red    (VCC) -----> 5V
  Orange (SIG) -----> Pin 9 (PWM)
```

> "Only three wires! Brown to ground, red to power, orange to a PWM pin. But here is an important warning..."

**Safety note:**
> "If you are using more than one servo, do NOT power them all from Arduino's 5V pin. Servos can draw a lot of current when they move. One SG90 is fine on Arduino's 5V, but for multiple servos or larger servos, use a separate 5V power supply with a shared GND."

**Award: +10 XP for wiring the servo!**

---

### Step 4: Your First Servo Movement (10 min)

**Sweep Code -- Back and Forth:**

```cpp
#include <Servo.h>

Servo myServo;

void setup() {
  myServo.attach(9);  // Servo on pin 9
  Serial.begin(9600);
  Serial.println("Servo Ready!");
}

void loop() {
  // Sweep from 0 to 180 degrees
  for (int angle = 0; angle <= 180; angle += 5) {
    myServo.write(angle);
    Serial.print("Angle: ");
    Serial.println(angle);
    delay(50);
  }

  // Sweep back from 180 to 0 degrees
  for (int angle = 180; angle >= 0; angle -= 5) {
    myServo.write(angle);
    Serial.print("Angle: ");
    Serial.println(angle);
    delay(50);
  }
}
```

**Watch it go!**

> "See how it sweeps smoothly? Each step is 5 degrees, with a 50 millisecond pause. If you make the delay shorter, it sweeps faster. Longer delay = slower sweep."

**Try these experiments:**
- Change the step from 5 to 1 -- smoother but slower
- Change delay from 50 to 10 -- much faster!
- Try `myServo.write(90)` alone -- it goes to the center and stops
- Try specific angles: 0, 45, 90, 135, 180

**Make a paper pointer:** Tape a small paper arrow to the servo horn so you can see the angle clearly!

**Award: +20 XP for your first servo sweep!**

---

### Step 5: Control with a Potentiometer (8 min)

Now add a potentiometer to control the servo angle with a dial:

```cpp
#include <Servo.h>

Servo myServo;
int potPin = A0;

void setup() {
  myServo.attach(9);
  Serial.begin(9600);
}

void loop() {
  int potValue = analogRead(potPin);           // 0 to 1023
  int angle = map(potValue, 0, 1023, 0, 180);  // Map to 0-180

  myServo.write(angle);

  Serial.print("Pot: ");
  Serial.print(potValue);
  Serial.print("  Angle: ");
  Serial.println(angle);

  delay(20);
}
```

**Potentiometer wiring:**

```
  Potentiometer         Arduino
  ---------------       --------
  Left pin   ---------> GND
  Middle pin ---------> A0
  Right pin  ---------> 5V
```

> "Now you are the servo controller! Turn the knob left, servo goes to 0 degrees. Turn it right, servo goes to 180. You could use this to control a robot arm, a camera mount, or a door lock!"

**Award: +30 XP for potentiometer control!**

---

### Step 6: Wand Check -- Measure the Signal Voltage (5 min)

> "The servo signal wire carries a PWM signal -- tiny pulses that tell the servo where to go. Let us see if your Wand can detect them!"

**Wand Test -- Signal Pin Voltage at Different Angles:**

1. Set your Wand to DC Volts
2. Connect black probe to GND
3. Touch red probe to the signal wire (orange wire, pin 9)
4. Use the potentiometer to set different angles
5. Record the average voltage your Wand shows

```
| Servo Angle | Expected Avg Voltage | Your Wand Reads | Points |
|-------------|---------------------|----------------|--------|
| 0 degrees   | ~0.3-0.8V           |                | +10 XP |
| 90 degrees  | ~1.0-1.5V           |                | +10 XP |
| 180 degrees | ~1.5-2.5V           |                | +10 XP |
```

> "Your Wand is averaging the PWM signal. At 0 degrees, the pulses are very short (about 1 millisecond), so the average voltage is low. At 180 degrees, the pulses are longer (about 2 milliseconds), so the average is higher. You are seeing the control signal as voltage!"

**Award: +30 XP for measuring the servo signal with your Wand!**

---

### Step 7: Bonus -- Servo Positions Game (Optional) (5 min)

Make a game: Write angle commands on cards (0, 30, 45, 60, 90, 120, 150, 180). Shuffle and draw one at a time. Try to guess where the servo will point before uploading the angle!

```cpp
// Quick test: change the angle and upload
void setup() {
  Servo s;
  s.attach(9);
  s.write(45);  // Change this number and guess!
}
void loop() {}
```

**Award: +15 XP for playing the angle guessing game!**

---

## Quick Quiz -- Earn Bonus XP!

**Question 1:** What is the main difference between a servo motor and a regular DC motor?
- A) A servo is bigger
- B) A servo can move to a specific angle and hold that position
- C) A servo spins continuously

**(Correct: B -- +15 XP!)**

**Question 2:** What are the three wires on an SG90 servo?
- A) Hot, Cold, Signal
- B) Ground (brown), Power (red), Signal (orange)
- C) Plus, Minus, Data

**(Correct: B -- +15 XP!)**

**Question 3:** What range of angles can a typical hobby servo reach?
- A) 0 to 360 degrees (full circle)
- B) 0 to 180 degrees (half circle)
- C) 0 to 90 degrees (quarter circle)

**(Correct: B -- +15 XP!)**

**Question 4:** Why should you NOT power multiple servos from Arduino's 5V pin?
- A) It will break the Arduino's screen
- B) Servos draw a lot of current and can overload the Arduino's voltage regulator
- C) Because servos need 12V

**(Correct: B -- +15 XP!)**

---

## Lesson 38 Complete!

```
  =============================================

     SERVO COMMANDER BADGE UNLOCKED!

     Skills unlocked:
     [check] Wire and control a servo motor
     [check] Sweep servo through full range
     [check] Control servo with a potentiometer
     [check] Measured PWM signal voltage with the Wand

  =============================================
```

**XP Breakdown:**
| Activity | XP |
|----------|-----|
| Hook -- robot arm dream | 10 |
| Understanding servos | 10 |
| Wiring the servo | 10 |
| First servo sweep | 20 |
| Potentiometer control | 30 |
| Wand Check (3 angles) | 30 |
| Angle guessing game bonus | 15 |
| Quiz (4 questions) | 60 |
| **TOTAL POSSIBLE** | **185** |

---

## Coming Up Next...

In **Lesson 39**, you will meet the **DC motor and L298N motor driver** -- the kind of motor that spins wheels on a robot! Unlike the servo, a DC motor spins continuously and you will learn to control its speed AND direction using the motor driver board. Your Wand will measure the output voltage at different speeds!

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| Servo does not move at all | Check the signal wire -- is it on a PWM pin (3, 5, 6, 9, 10, 11)? |
| Servo jitters or vibrates in place | This can happen with cheap servos or noisy power. Add a 100 microfarad capacitor between 5V and GND near the servo |
| Servo only moves a small range | Make sure you are using `Servo.h` library and `write()` with values 0-180 |
| Potentiometer control jumps around | Add a small delay (15-20ms) in the loop -- servos need time to reach position |
| Arduino resets when servo moves | Servo draws too much current. Use external 5V power for the servo |
| Servo makes grinding noise | It is hitting its mechanical limit. Do not command angles past 0 or 180 |

---

## Navigation

| | |
|:---|---:|
| [← Lesson 37: Ultrasonic Distance Sensor -- Your Arduino's Echolocation (HC-SR04)](lesson-37-ultrasonic-distance-sensor.md) | [Lesson 39: DC Motors and Motor Driver -- Spin Those Wheels! (L298N) →](lesson-39-dc-motors-and-motor-driver.md) |

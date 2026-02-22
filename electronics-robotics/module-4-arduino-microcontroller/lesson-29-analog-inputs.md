# Lesson 29: Analog Inputs -- Reading the In-Between

**Module:** 4 -- Arduino Microcontroller
**Difficulty:** Star-3 Intermediate
**Session Time:** 40--45 minutes
**Age:** 6--12 years
**XP Available:** 250 XP

---

## Your Mission Today

Circuit Explorer, so far the Arduino has only dealt with ON or OFF -- HIGH or LOW -- like a light switch. But the real world is not just black and white! A volume knob does not go from silent to max with nothing in between. Today you will learn how the Arduino reads **analog values** -- numbers from 0 to 1023 that represent anything in between 0V and 5V. You will hook up a potentiometer (that twisty knob from Module 1!) and watch the Arduino read every tiny turn. This is how real sensors work!

---

## Learning Objectives

By the end of this lesson, you will be able to:
- Explain the difference between digital and analog signals
- Connect a potentiometer to an Arduino analog pin
- Use `analogRead()` to read values from 0 to 1023
- Convert analog readings to voltage using math
- Measure potentiometer voltage with the Wand and compare to Arduino readings

---

## What You Need

| Item | Qty |
|------|-----|
| Arduino Uno + USB cable | 1 |
| Breadboard | 1 |
| 10k-ohm potentiometer | 1 |
| LED (any color) | 1 |
| 330-ohm resistor | 1 |
| Jumper wires | 5 |
| Multimeter (Magic Measurement Wand!) | 1 |

---

## How to Teach This Lesson

### Step 1: Hook -- The Light Switch Problem (3 min)

> "Imagine you only had two volume levels on your music player: SILENT and FULL BLAST. That would be terrible! You need all the levels in between."

> "Digital is like a light switch -- ON or OFF, 1 or 0, HIGH or LOW. Analog is like a dimmer -- it can be anywhere in between. The Arduino has 6 special analog pins (A0 through A5) that can read these in-between values."

**The Big Numbers:**

- Digital: just 2 values -- HIGH (5V) or LOW (0V)
- Analog: **1024 values** -- from 0 (0V) all the way to 1023 (5V)

> "1024 steps from off to full! That is like having 1024 volume levels instead of just 2."

**Award: +10 XP for understanding digital vs analog!**

---

### Step 2: Build the Potentiometer Circuit (8 min)

**How a Potentiometer Works (Refresher):**

> "Remember from Module 1? A potentiometer is a variable resistor with a twisty knob. It has 3 legs. The middle leg gives you a voltage that changes as you turn the knob."

**Wiring Diagram:**

```
  Arduino Uno                    Breadboard
  +---------+
  | 5V      |----[wire]----+---- Potentiometer Left Leg
  |         |
  | A0      |----[wire]----+---- Potentiometer Middle Leg (wiper)
  |         |
  | GND     |----[wire]----+---- Potentiometer Right Leg
  +---------+

  Potentiometer:
  +-------+
  |       |
  |  (o)  |  <-- twist the knob
  |       |
  +--+--+-+
     |  |  |
   Left Mid Right
   5V  A0  GND
```

**Steps:**

1. Place the potentiometer on the breadboard
2. Connect the **left leg** to **Arduino 5V**
3. Connect the **right leg** to **Arduino GND**
4. Connect the **middle leg** (wiper) to **Arduino A0**

> "The middle leg gives a voltage between 0V and 5V depending on the knob position. Turned all the way to the 5V side = 5V. All the way to GND = 0V. Halfway = about 2.5V."

**Award: +20 XP for wiring the potentiometer!**

---

### Step 3: Read the Potentiometer with Code (10 min)

**The Code:**

```cpp
// Lesson 29: Reading Analog Input from a Potentiometer

void setup() {
  Serial.begin(9600);
  Serial.println("=== Analog Reader Ready! ===");
}

void loop() {
  int sensorValue = analogRead(A0);         // Read potentiometer (0-1023)
  float voltage = sensorValue * (5.0 / 1023.0);  // Convert to volts

  Serial.print("Raw Value: ");
  Serial.print(sensorValue);
  Serial.print("  |  Voltage: ");
  Serial.print(voltage, 2);  // 2 decimal places
  Serial.println(" V");

  delay(200);  // Read 5 times per second
}
```

**Upload and open the Serial Monitor!**

Now twist the potentiometer knob slowly. You should see:

```
=== Analog Reader Ready! ===
Raw Value: 0      |  Voltage: 0.00 V
Raw Value: 256    |  Voltage: 1.25 V
Raw Value: 512    |  Voltage: 2.50 V
Raw Value: 768    |  Voltage: 3.76 V
Raw Value: 1023   |  Voltage: 5.00 V
```

> "The Arduino is reading 1024 different levels! When you turn the knob slowly, you can see every tiny step. This is how real sensors report temperature, light level, sound volume, and much more."

**Award: +30 XP for reading analog values!**

---

### Step 4: The Math Behind It (5 min)

> "How do we convert the number 512 into 2.5 volts? Simple math!"

**The Formula:**

```
voltage = analogRead value * (5.0 / 1023.0)
```

**Why?**

- The analog pin reads 0 to 1023 (1024 steps)
- 0 means 0 volts, 1023 means 5 volts
- So each step = 5.0 / 1023.0 = about 0.00489 volts
- A reading of 512 = 512 * 0.00489 = about 2.50 volts

**Quick Practice:**

| Raw Value | Voltage (calculate!) |
|-----------|---------------------|
| 0 | 0.00 V |
| 200 | ? |
| 512 | ? |
| 800 | ? |
| 1023 | 5.00 V |

**Answers:** 200 = 0.98V, 512 = 2.50V, 800 = 3.91V

**Award: +10 XP for doing the voltage math!**

---

### Step 5: Wand Check -- Compare Arduino to the Wand (8 min)

> "The Arduino says it is reading 2.50 volts on A0. But is it REALLY 2.5 volts? Let us double-check with the Magic Measurement Wand!"

**Setup:**
1. Set the Wand to **DC Voltage**
2. Black probe on **GND**
3. Red probe on the **middle leg** of the potentiometer (or on the wire going to A0)

**The Comparison Test:**

Turn the knob to 5 different positions. At each position, read both the Serial Monitor AND the Wand:

```
| Knob Position | Serial Monitor Says | Wand Reads | Match? |
|---------------|-------------------|------------|--------|
| All left      |                   |            |        |
| Quarter turn  |                   |            |        |
| Half turn     |                   |            |        |
| Three-quarter |                   |            |        |
| All right     |                   |            |        |
```

> "They should be very close! The Arduino and the Wand are both measuring the same voltage. If they differ by a little (like 0.05V), that is normal -- neither instrument is perfectly exact. But they should agree within a few percent."

**Award: +40 XP for completing the comparison test!**

---

### Step 6: Bonus -- Control LED Blink Speed with the Knob (5 min)

**The Code:**

```cpp
int ledPin = 7;

void setup() {
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  int potValue = analogRead(A0);            // 0 to 1023
  int blinkDelay = potValue;                // Use raw value as delay

  digitalWrite(ledPin, HIGH);
  delay(blinkDelay);
  digitalWrite(ledPin, LOW);
  delay(blinkDelay);

  Serial.print("Delay: ");
  Serial.print(blinkDelay);
  Serial.println(" ms");
}
```

> "Now twist the knob! The LED blinks fast when the knob is turned to one side and slow on the other. You just built a real speed controller!"

**Award: +20 XP for controlling blink speed with the potentiometer!**

---

## Quick Quiz -- Earn Bonus XP!

**Question 1:** What is the range of values `analogRead()` returns?
- A) 0 to 255
- B) HIGH or LOW
- C) 0 to 1023

**(Correct: C -- +20 XP!)**

**Question 2:** If `analogRead()` returns 512, approximately what voltage is that?
- A) 1.0V
- B) 2.5V
- C) 5.0V

**(Correct: B -- +20 XP!)**

**Question 3:** Which Arduino pins can read analog values?
- A) Pins 0 through 13
- B) Pins A0 through A5
- C) Only pin 13

**(Correct: B -- +20 XP!)**

---

## Lesson 29 Complete!

```
  =============================================

     ANALOG ADVENTURER BADGE UNLOCKED!

     Skills unlocked:
     [check] Understand digital vs analog
     [check] Wire a potentiometer to Arduino
     [check] Read analog values with analogRead()
     [check] Convert raw values to voltage
     [check] Verified readings with the Wand
     [check] Controlled LED speed with a knob

  =============================================
```

**XP Breakdown:**
| Activity | XP |
|----------|-----|
| Hook discussion | 10 |
| Potentiometer wiring | 20 |
| Analog reading code | 30 |
| Voltage math practice | 10 |
| Wand Check (5 comparisons) | 40 |
| LED speed controller bonus | 20 |
| Quiz (3 questions) | 60 |
| **TOTAL POSSIBLE** | **250** |

---

## Coming Up Next...

In **Lesson 30**, you will learn the coolest trick in Arduino: **PWM (Pulse Width Modulation)**. Instead of just ON or OFF, you will make an LED FADE smoothly from dark to bright and back! It is like the opposite of analog input -- it is analog-like OUTPUT. And you will use the Wand to see something really surprising about how it works.

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| Serial Monitor shows 0 all the time | Check that the potentiometer middle leg is connected to A0, not a digital pin |
| Reading jumps around wildly | Make sure all three potentiometer legs are connected (5V, A0, GND) |
| Reading stuck at 1023 | The middle leg might be connected to 5V instead of A0 |
| Wand and Arduino disagree a lot | Make sure both are measuring the same point (middle leg of the pot) |
| LED blink speed does not change | Make sure you are using the potValue as the delay in the LED code |

# Lesson 26: Your First Sketch -- Blink an External LED

**Module:** 4 -- Arduino Microcontroller
**Difficulty:** Star-3 Intermediate
**Session Time:** 40--45 minutes
**Age:** 6--12 years
**XP Available:** 250 XP

---

## Your Mission Today

Circuit Explorer, last lesson you made the tiny built-in LED blink. That was cool, but tiny. Today you are going to wire up a BIG, bright LED on a breadboard and control it with your own Arduino code. You will learn the two most important functions every Arduino sketch needs: `setup()` and `loop()`. By the end, you will have a blinking LED that YOU built and YOU programmed. Let us light it up!

---

## Learning Objectives

By the end of this lesson, you will be able to:
- Wire an external LED and resistor to an Arduino digital pin on a breadboard
- Understand the structure of every Arduino sketch: `setup()` and `loop()`
- Use `pinMode()`, `digitalWrite()`, and `delay()` in your code
- Measure the voltage on an LED pin when it is HIGH vs LOW with the Wand

---

## What You Need

| Item | Qty |
|------|-----|
| Arduino Uno + USB cable | 1 |
| Breadboard | 1 |
| LED (any color) | 1 |
| 330-ohm resistor | 1 |
| Jumper wires | 3 |
| Multimeter (Magic Measurement Wand!) | 1 |

---

## How to Teach This Lesson

### Step 1: Hook -- Why External LEDs? (3 min)

> "Last time we blinked the tiny LED built into the Arduino. But what if you want to blink a BIG LED? Or two LEDs? Or ten? Or a hundred? You need to connect EXTERNAL LEDs on a breadboard and tell the Arduino which pin to use."

Show the kid the small built-in LED vs a full-size 5mm LED:

> "See the difference? The big one is much brighter and you can put it anywhere you want. But the Arduino does not know about it yet -- you have to TEACH it by writing code."

**Award: +10 XP for understanding why external LEDs matter!**

---

### Step 2: Build the Circuit (10 min)

**Wiring Diagram:**

```
  Arduino Uno                    Breadboard
  +---------+
  | Pin 7   |----[wire]----+
  |         |              |
  |         |         [330-ohm resistor]
  |         |              |
  |         |         LED (+) anode (long leg)
  |         |         LED (-) cathode (short leg)
  |         |              |
  | GND     |----[wire]----+
  +---------+

  Breadboard Detail:
  Row 10: Pin 7 wire --> resistor leg 1
  Row 15: resistor leg 2 --> LED long leg (+)
  Row 15: LED short leg (-) on next row
  Row 16: LED short leg --> wire to GND
```

**Step-by-step wiring:**

1. Place the **LED** on the breadboard. Remember: long leg is positive (+), short leg is negative (-)
2. Connect a **330-ohm resistor** from **Arduino pin 7** to the **long leg (+)** of the LED
3. Connect a wire from the **short leg (-)** of the LED to **Arduino GND**

> "The resistor protects the LED -- just like in Module 1! Without it, too much current flows and the LED burns out."

**Award: +20 XP for building the circuit correctly!**

---

### Step 3: The Anatomy of a Sketch (10 min)

Every Arduino sketch has exactly two required parts:

**Part 1 -- setup():**

```cpp
void setup() {
  // Code here runs ONCE when Arduino starts
}
```

> "setup() is like waking up in the morning and getting dressed. You do it ONCE to get ready for the day."

**Part 2 -- loop():**

```cpp
void loop() {
  // Code here runs OVER AND OVER forever
}
```

> "loop() is like breathing. You do it over and over and over without stopping."

**The Three Key Commands:**

| Command | What It Does | Analogy |
|---------|-------------|---------|
| `pinMode(pin, OUTPUT)` | Tells the Arduino "this pin will SEND signals" | Labeling a door as EXIT |
| `digitalWrite(pin, HIGH)` | Sets the pin to 5V (ON) | Flipping a light switch ON |
| `digitalWrite(pin, LOW)` | Sets the pin to 0V (OFF) | Flipping a light switch OFF |
| `delay(milliseconds)` | Waits for a certain time | Saying "pause for a moment" |

> "1000 milliseconds = 1 second. So delay(500) waits half a second."

**Award: +10 XP for learning the anatomy of a sketch!**

---

### Step 4: Write and Upload the Code (8 min)

Open the Arduino IDE and type this code (or modify the Blink example):

```cpp
// Lesson 26: Blink an External LED on Pin 7

int ledPin = 7;  // Our LED is connected to pin 7

void setup() {
  pinMode(ledPin, OUTPUT);  // Set pin 7 as an output
}

void loop() {
  digitalWrite(ledPin, HIGH);  // Turn LED ON (5 volts on pin 7)
  delay(1000);                 // Wait 1 second
  digitalWrite(ledPin, LOW);   // Turn LED OFF (0 volts on pin 7)
  delay(1000);                 // Wait 1 second
}
```

**Upload It:**

1. Click the **Upload** button (right arrow)
2. Wait for "Done uploading"
3. Watch your external LED blink!

> "HIGH means ON (5 volts). LOW means OFF (0 volts). The Arduino is flipping pin 7 between 5V and 0V like a tiny light switch, one thousand times... well, once per second."

**Award: +30 XP for a blinking external LED!**

---

### Step 5: Experiment Time! (5 min)

**Challenge 1 -- Speed Racer:**
Change both delays to `100`. Upload. The LED blinks super fast!

**Challenge 2 -- SOS in Morse Code:**

```cpp
void loop() {
  // S = three short blinks
  digitalWrite(ledPin, HIGH); delay(200);
  digitalWrite(ledPin, LOW);  delay(200);
  digitalWrite(ledPin, HIGH); delay(200);
  digitalWrite(ledPin, LOW);  delay(200);
  digitalWrite(ledPin, HIGH); delay(200);
  digitalWrite(ledPin, LOW);  delay(500);

  // O = three long blinks
  digitalWrite(ledPin, HIGH); delay(600);
  digitalWrite(ledPin, LOW);  delay(200);
  digitalWrite(ledPin, HIGH); delay(600);
  digitalWrite(ledPin, LOW);  delay(200);
  digitalWrite(ledPin, HIGH); delay(600);
  digitalWrite(ledPin, LOW);  delay(500);

  // S = three short blinks
  digitalWrite(ledPin, HIGH); delay(200);
  digitalWrite(ledPin, LOW);  delay(200);
  digitalWrite(ledPin, HIGH); delay(200);
  digitalWrite(ledPin, LOW);  delay(200);
  digitalWrite(ledPin, HIGH); delay(200);
  digitalWrite(ledPin, LOW);  delay(1500);  // Long pause before repeat
}
```

> "You just made an SOS signal! Sailors and pilots use this to say HELP ME."

**Award: +20 XP for completing the SOS challenge!**

---

### Step 6: Wand Check -- Measure the LED Pin (8 min)

> "Your LED is blinking, but what is actually happening electrically? Let us measure it with the Magic Measurement Wand!"

**Setup:**
1. Set your Wand to **DC Voltage** mode
2. Touch the **black probe** to **GND** on the Arduino
3. Touch the **red probe** to **pin 7** on the Arduino

**What You Should See:**

The voltage jumps between two values as the LED blinks:

```
| LED State | Pin 7 Voltage | What the Code Says     |
|-----------|---------------|------------------------|
| ON        | ~5.0V         | digitalWrite(7, HIGH)  |
| OFF       | ~0.0V         | digitalWrite(7, LOW)   |
```

**Bonus Measurement -- Voltage Across the LED:**

1. Touch the **red probe** to the LED's **long leg** (+)
2. Touch the **black probe** to the LED's **short leg** (-)
3. When the LED is ON, you should see about **1.8V -- 2.2V** (the LED's forward voltage)

> "The full 5V from the pin is shared between the resistor and the LED. The LED uses about 2V, and the resistor takes the rest. Your Wand just proved it!"

**Award: +40 XP for measuring pin voltage and LED voltage!**

---

## Quick Quiz -- Earn Bonus XP!

**Question 1:** What does `setup()` do?
- A) Runs over and over forever
- B) Runs once at the start
- C) Turns off the Arduino

**(Correct: B -- +20 XP!)**

**Question 2:** What does `digitalWrite(7, HIGH)` do?
- A) Reads pin 7
- B) Sets pin 7 to 0 volts
- C) Sets pin 7 to 5 volts

**(Correct: C -- +20 XP!)**

**Question 3:** How many milliseconds is 2 seconds?
- A) 200
- B) 2000
- C) 20

**(Correct: B -- +20 XP!)**

---

## Lesson 26 Complete!

```
  =============================================

     BLINK MASTER BADGE UNLOCKED!

     Skills unlocked:
     [check] Wired external LED to Arduino
     [check] Understand setup() and loop()
     [check] Used pinMode, digitalWrite, delay
     [check] Wrote SOS Morse code
     [check] Measured pin voltage with the Wand

  =============================================
```

**XP Breakdown:**
| Activity | XP |
|----------|-----|
| Hook discussion | 10 |
| Build the circuit | 20 |
| Sketch anatomy lesson | 10 |
| Upload blink code | 30 |
| SOS challenge | 20 |
| Wand Check (pin + LED voltage) | 40 |
| Quiz (3 questions) | 60 |
| **TOTAL POSSIBLE** | **250** |

---

## Coming Up Next...

In **Lesson 27**, you will learn about **variables** and the **Serial Monitor** -- a secret window that lets your Arduino talk back to you! You will print messages on your computer screen and use variables to control your LED's behavior. It is like giving your Arduino a voice!

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| LED does not light up | Check LED polarity -- long leg (+) goes to the resistor side, short leg (-) to GND |
| LED is very dim | Make sure you are using pin 7 (not an analog pin) and a 330-ohm resistor (not 10k) |
| Code does not upload | Check that Board and Port are set correctly in Tools menu |
| LED stays on all the time | Make sure you have both HIGH and LOW in your loop() with delays |
| Wand reads 0V on pin 7 | Check your wire connection from pin 7 to the breadboard; make sure it is firmly inserted |

---

## Navigation

| | |
|:---|---:|
| [← Lesson 25: What is a Microcontroller? -- The Brain of Every Gadget](lesson-25-what-is-a-microcontroller.md) | [Lesson 27: Variables and the Serial Monitor -- Give Your Arduino a Voice →](lesson-27-variables-and-serial-monitor.md) |

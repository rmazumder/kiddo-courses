# Lesson 23: Building a Simple Counter

**Module:** 3 -- Integrated Circuits (ICs)
**Difficulty:** Star-3 Intermediate
**Session Time:** 45--50 minutes
**Age:** 6--12 years
**XP Available:** 300 XP

---

## Your Mission Today

Get ready for one of the coolest circuits in this module! Today you will combine TWO ICs -- the 555 timer you already know and a brand new chip called the **4017 decade counter**. The 555 generates pulses, and the 4017 counts them. The result? Ten LEDs that light up one at a time in sequence, like a light show! You are about to build your own LED chaser.

---

## Learning Objectives

By the end of this lesson, you will be able to:
- Explain what a counter IC does (counts pulses and activates outputs in sequence)
- Identify the 4017 decade counter IC pins
- Build a 555 + 4017 LED chaser circuit
- Control the chaser speed by adjusting the 555 timing components
- Use your Magic Measurement Wand to trace which output is active

---

## What You Need

| Item | Qty |
|------|-----|
| 555 timer IC | 1 |
| 4017 decade counter IC | 1 |
| LEDs (any colors -- a mix is fun!) | 10 |
| 330-ohm resistors | 10 |
| Resistor: 1k-ohm (R1 for 555) | 1 |
| Resistor: 10k-ohm (R2 for 555) | 1 |
| Resistor: 47k-ohm (R2 swap for slower speed) | 1 |
| Electrolytic capacitor: 10 microfarad (C1 for 555) | 1 |
| Electrolytic capacitor: 47 microfarad (C1 swap) | 1 |
| Ceramic capacitor: 0.01 microfarad (noise filter) | 1 |
| 9V battery + clip | 1 |
| Breadboard (830-point recommended) | 1 |
| Jumper wires | 25 |
| Multimeter (Magic Measurement Wand!) | 1 |

---

## How to Teach This Lesson

### Step 1: Hook -- The Knight Rider Light Show (5 min)

> "Have you ever seen those movie cars with lights that sweep back and forth across the front? Or a row of lights on a stage that chase each other? That is called a light chaser, and it is exactly what we are building today!"

> "But here is the clever part -- we are not going to use a computer. We are using just TWO chips: the 555 timer to generate a clock signal (tick... tick... tick...) and the 4017 counter to count each tick and light up the next LED."

Draw a simple picture:

```
  555 Timer        4017 Counter         LEDs
  [tick tick] ---> [0, 1, 2, 3...] ---> [LED0] [LED1] [LED2] ...
  (clock)          (counts pulses)       (light up in sequence)
```

**Award: +10 XP for understanding how two ICs work together!**

---

### Step 2: Meet the 4017 Decade Counter (8 min)

**What is a decade counter?**

> "A decade counter is a chip that counts from 0 to 9 (that is 10 steps -- a decade means ten). Every time it receives a pulse on its CLOCK pin, it moves to the next output. Output 0 goes HIGH, then output 1, then output 2, and so on. When it reaches output 9, it loops back to 0 and starts over."

**Key vocabulary:**
- **Clock signal:** A repeating pulse (HIGH-LOW-HIGH-LOW) that tells the counter to advance one step
- **Decade counter:** Counts from 0 to 9 (ten steps) and then resets
- **Carry out:** A signal that goes HIGH after the counter completes a full cycle (useful for chaining counters)

**The 4017 IC pinout:**

```
  4017 Decade Counter -- Top View

        Notch
          U
    +----------+
    |  1    16 | <-- Pin 16 = VCC (+9V)
    |  2    15 |
    |  3    14 | <-- Pin 14 = Clock input
    |  4    13 | <-- Pin 13 = Clock Enable (connect to GND)
    |  5    12 |
    |  6    11 |
    |  7    10 |
    |  8     9 |
    +----------+
       ^
    Pin 8 = GND

  Output pins:
  Pin 3  = Output 0 (Q0)
  Pin 2  = Output 1 (Q1)
  Pin 4  = Output 2 (Q2)
  Pin 7  = Output 3 (Q3)
  Pin 10 = Output 4 (Q4)
  Pin 1  = Output 5 (Q5)
  Pin 5  = Output 6 (Q6)
  Pin 6  = Output 7 (Q7)
  Pin 9  = Output 8 (Q8)
  Pin 11 = Output 9 (Q9)

  Pin 15 = Reset (connect to GND for normal counting)
  Pin 12 = Carry Out
```

> "Notice the pin numbers are not in order -- they jump around! This is normal for ICs. Always check the datasheet."

**Award: +10 XP for learning the 4017 pin layout!**

---

### Step 3: Build the 555 Clock Circuit First (8 min)

> "Before we wire the counter, let us build the 555 timer in astable mode. This will be our clock -- the heartbeat that tells the counter when to step forward."

**555 Astable Circuit (same as Lesson 18, but faster):**

```
  +9V ----+
          |
         [R1] 1k-ohm
          |
          +---- Pin 7 (Discharge)
          |
         [R2] 10k-ohm
          |
          +---- Pin 6 (Threshold) + Pin 2 (Trigger)
          |
         [C1] 10uF
          |
         GND

  Pin 8 = VCC (+9V)
  Pin 1 = GND
  Pin 4 = +9V (Reset -- keep enabled)
  Pin 5 = 0.01uF to GND (noise filter)
  Pin 3 = Output (goes to 4017 clock input)
```

**With R1=1k, R2=10k, C1=10uF:**

```
  Frequency = 1.44 / ((1000 + 20000) x 0.00001)
            = 1.44 / 0.21
            = about 6.9 Hz (roughly 7 blinks per second)
```

> "That is fast enough to see the LEDs chase but slow enough to follow with your eyes."

**Test: Connect an LED to Pin 3 temporarily to confirm the 555 is working before connecting the 4017.**

**Award: +20 XP for building the working 555 clock!**

---

### Step 4: Wire the 4017 Counter and LEDs (12 min)

> "Now let us add the counter chip and all 10 LEDs. This is the biggest circuit we have built so far! Take it step by step."

**Step-by-step wiring:**

1. Place the 4017 IC on the breadboard (on the same board or a second one connected with jumper wires)
2. Pin 16 (VCC) to + rail
3. Pin 8 (GND) to - rail
4. Pin 13 (Clock Enable) to - rail (GND = counting enabled)
5. Pin 15 (Reset) to - rail (GND = no reset, count normally)
6. Pin 14 (Clock Input) to **Pin 3 of the 555** (the clock signal!)

**Now wire the 10 LEDs:**

For each output pin on the 4017, connect:
- Output pin --> 330-ohm resistor --> LED (long leg +) --> LED (short leg) --> GND rail

```
| 4017 Pin | Output | LED Color (your choice) |
|----------|--------|------------------------|
| Pin 3    | Q0     |                        |
| Pin 2    | Q1     |                        |
| Pin 4    | Q2     |                        |
| Pin 7    | Q3     |                        |
| Pin 10   | Q4     |                        |
| Pin 1    | Q5     |                        |
| Pin 5    | Q6     |                        |
| Pin 6    | Q7     |                        |
| Pin 9    | Q8     |                        |
| Pin 11   | Q9     |                        |
```

> "Connect the battery. Watch the LEDs! They should light up one at a time, chasing across the row. LED 0 lights, then LED 1, then LED 2... all the way to LED 9, then it starts over!"

**Award: +40 XP for building the full 10-LED chaser circuit!**

---

### Step 5: Speed Control (5 min)

> "Let us play DJ again! Change the 555 components to adjust the chase speed."

**Experiment:**

```
| R2 Value | C1 Value | Expected Speed | Looks Like |
|----------|----------|---------------|------------|
| 10k      | 10uF     | Fast (~7 Hz)  |            |
| 47k      | 10uF     | Medium (~1.5 Hz) |         |
| 10k      | 47uF     | Slow (~1.5 Hz) |           |
| 47k      | 47uF     | Very slow (~0.3 Hz) |      |
```

> "Make it go as fast as you can! Then slow it down so you can count each step. Which speed looks coolest?"

**Award: +20 XP for testing different speeds!**

---

### Step 6: Wand Check -- Trace the Active Output! (8 min)

> "Only one output is HIGH at any time. Let us prove it with the Wand!"

**Slow the circuit down** (use R2=47k, C1=47uF for very slow stepping).

1. Set the Wand to DC Voltage
2. Black probe on GND
3. Touch the red probe to each 4017 output pin, one at a time

**What you should see:**
- Most pins read close to **0V** (LOW -- LED off)
- One pin reads close to **9V** (HIGH -- LED on)
- As the 555 ticks, a different pin goes HIGH

> "At any moment, ONLY ONE output is HIGH. The counter moves the HIGH signal from one pin to the next with each clock pulse. It is like passing a baton in a relay race!"

**Activity -- Find the active pin:**

```
| Clock Tick | Which Pin is HIGH? | Wand Voltage |
|------------|-------------------|-------------|
| Tick 1     |                   |             |
| Tick 2     |                   |             |
| Tick 3     |                   |             |
| Tick 4     |                   |             |
| Tick 5     |                   |             |
```

**Bonus: Measure the clock signal**

Touch the red probe to Pin 14 (Clock Input). Watch the voltage flip between HIGH and LOW with each 555 pulse.

**Award: +50 XP for tracing the active output across 5 ticks!**

---

## Fun Game: Light Show Patterns (Optional Extension)

Instead of 10 separate-color LEDs, try patterns:
- Alternating red and green for a holiday theme
- All one color for a smooth wave effect
- Use only 5 outputs (connect Pin 5/Q6 Reset to stop at 5 and loop)

**To make a 5-LED loop:** Connect the output of Q5 (Pin 1) to the Reset pin (Pin 15). Now the counter resets after 5 instead of 10!

---

## Quick Quiz -- Earn Bonus XP!

**Question 1:** What does the 4017 decade counter do?
- A) Generates a clock signal
- B) Counts clock pulses and activates one output at a time, 0 through 9
- C) Measures voltage

**(Correct: B -- +20 XP!)**

**Question 2:** What provides the clock signal to the 4017 in our circuit?
- A) The battery
- B) The 555 timer in astable mode
- C) The LEDs

**(Correct: B -- +20 XP!)**

**Question 3:** At any given moment, how many 4017 outputs are HIGH?
- A) All 10
- B) 5
- C) Just 1

**(Correct: C -- +20 XP!)**

**Question 4:** To make the LED chase SLOWER, you should:
- A) Add more LEDs
- B) Use a bigger R2 or bigger C1 in the 555 circuit
- C) Remove the 4017

**(Correct: B -- +20 XP!)**

---

## Lesson 23 Complete!

```
  =============================================

     LIGHT CHASER CHAMPION BADGE UNLOCKED!

     Skills unlocked:
     [check] Understand the 4017 decade counter
     [check] Combined 555 timer + 4017 counter
     [check] Built a 10-LED chaser circuit
     [check] Controlled chaser speed
     [check] Traced active outputs with the Wand

  =============================================
```

**XP Breakdown:**
| Activity | XP |
|----------|-----|
| Two-IC concept understanding | 10 |
| Learn 4017 pinout | 10 |
| Build 555 clock circuit | 20 |
| Build full 10-LED chaser | 40 |
| Speed control experiments | 20 |
| Wand Check (trace 5 ticks) | 50 |
| Quiz (4 questions) | 80 |
| **TOTAL POSSIBLE** | **230** |

---

## Coming Up Next...

In **Lesson 24** -- the **Module 3 Grand Finale** -- you will build a **Digital Dice**! Press a button and a random number from 1 to 6 appears. It uses everything you have learned: the 555 timer, the 4017 counter, and LEDs arranged in a dice pattern. Let us roll!

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| LEDs do not chase -- all off | Check that Pin 14 (Clock) is receiving the 555 output |
| LEDs do not chase -- one stays on | Pin 13 (Clock Enable) must be connected to GND |
| Counter seems stuck at 0 | Pin 15 (Reset) must be connected to GND for normal counting |
| LEDs chase but skip some | Check the wiring from each output pin -- the pin numbers are NOT in sequential order |
| Chase is too fast to see | Use bigger R2 and/or bigger C1 in the 555 circuit |
| Only some LEDs light up | Check each LED polarity and that each has its own 330-ohm resistor |
| One LED lights but is dim | That LED might be inserted backwards -- check polarity (long leg = +) |

---

## Navigation

| | |
|:---|---:|
| [← Lesson 22: IC 7-Segment Display](lesson-22-seven-segment-display.md) | [Lesson 24: Module 3 Project -- Digital Dice →](lesson-24-project-digital-dice.md) |

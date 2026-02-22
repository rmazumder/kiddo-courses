# Lesson 20: Logic Gates -- AND, OR, NOT

**Module:** 3 -- Integrated Circuits (ICs)
**Difficulty:** Star-3 Intermediate
**Session Time:** 40--45 minutes
**Age:** 6--12 years
**XP Available:** 300 XP

---

## Your Mission Today

Welcome to the world of **digital logic**, Circuit Explorer! Everything a computer does -- playing games, showing videos, sending messages -- comes down to just a few simple rules about ON and OFF. Today you will learn the three basic logic gates: AND, OR, and NOT. These are the tiny decision-makers inside every phone, computer, and video game console on the planet!

---

## Learning Objectives

By the end of this lesson, you will be able to:
- Explain what a logic gate is and what HIGH and LOW mean
- Describe how AND, OR, and NOT gates work using truth tables
- Build real logic gate circuits using IC chips on a breadboard
- Use your Magic Measurement Wand to measure HIGH and LOW voltages at gate outputs

---

## What You Need

| Item | Qty |
|------|-----|
| 7408 AND gate IC | 1 |
| 7432 OR gate IC | 1 |
| 7404 NOT gate IC | 1 |
| LEDs (any color) | 3 |
| 330-ohm resistors | 3 |
| 10k-ohm resistors (pull-down) | 4 |
| Push buttons (tactile switch) | 2 |
| 9V battery + clip (or 5V USB power) | 1 |
| Breadboard | 1 |
| Jumper wires | 15 |
| Multimeter (Magic Measurement Wand!) | 1 |

**Important note about power supply:** Logic gate ICs in the 74xx family work best at **5V**. If you are using a 9V battery, add a **7805 voltage regulator** to get a steady 5V, or use a USB charger that provides 5V. If using 9V directly, the chips may still work but voltages will be higher.

---

## How to Teach This Lesson

### Step 1: Hook -- The World Runs on Yes or No (5 min)

> "Here is a question: Is the light switch ON or OFF? There is no 'kind of on.' It is one or the other. Computers think the same way -- everything is either a 1 or a 0. ON or OFF. YES or NO. HIGH or LOW."

> "Every single thing your phone does -- showing a photo, playing a sound, connecting to Wi-Fi -- it all comes down to billions of tiny circuits asking 'Is this a 1 or a 0?' and making decisions based on the answer."

**Key vocabulary:**
- **Logic gate:** A tiny circuit that takes one or two inputs (1 or 0) and gives one output (1 or 0) based on a rule
- **HIGH (1):** Voltage is ON -- about 5V (or close to the power supply voltage)
- **LOW (0):** Voltage is OFF -- about 0V (close to ground)
- **Truth table:** A chart that shows every possible combination of inputs and what the output will be

**Award: +10 XP for entering the world of digital logic!**

---

### Step 2: The AND Gate -- Both Must Be ON (8 min)

**The Guard Dog Analogy:**

> "Imagine a treasure chest with TWO locks. You need Key A AND Key B to open it. If you only have one key, the chest stays locked. Both keys = chest opens. That is exactly how an AND gate works!"

**Truth Table for AND:**

```
  AND Gate: Output is 1 ONLY when BOTH inputs are 1

  +-----+-----+--------+
  |  A  |  B  | Output |
  +-----+-----+--------+
  |  0  |  0  |   0    |
  |  0  |  1  |   0    |
  |  1  |  0  |   0    |
  |  1  |  1  |   1    |  <-- Only this one!
  +-----+-----+--------+
```

**Real-world AND examples:**
- A car starts only if the key is turned AND you press the brake pedal
- You can buy a toy only if you have enough money AND the store is open
- A spaceship launches only if all systems are GO AND the countdown reaches zero

**The 7408 AND gate IC has FOUR AND gates inside:**

```
  7408 Quad AND Gate -- Top View

        Notch
          U
    +----------+
    |  1    14 | <-- Pin 14 = VCC (+5V)
    |  2    13 |
    |  3    12 |
    |  4    11 |
    |  5    10 |
    |  6     9 |
    |  7     8 |
    +----------+
       ^
    Pin 7 = GND

  Gate 1: Inputs = Pin 1, Pin 2  -->  Output = Pin 3
  Gate 2: Inputs = Pin 4, Pin 5  -->  Output = Pin 6
  Gate 3: Inputs = Pin 9, Pin 10 -->  Output = Pin 8
  Gate 4: Inputs = Pin 12, Pin 13 --> Output = Pin 11
```

**Build the AND gate circuit:**

1. Place 7408 on breadboard, notch up
2. Pin 14 (VCC) to + rail, Pin 7 (GND) to - rail
3. Connect a push button from + rail to Pin 1, with a 10k pull-down resistor from Pin 1 to GND
4. Connect a push button from + rail to Pin 2, with a 10k pull-down resistor from Pin 2 to GND
5. Connect Pin 3 (Output) to 330-ohm resistor to LED to GND

**Test all 4 combinations:**
- Both buttons NOT pressed: LED off
- Only button A pressed: LED off
- Only button B pressed: LED off
- BOTH buttons pressed: LED ON!

**Award: +30 XP for building and testing the AND gate!**

---

### Step 3: The OR Gate -- Either One Works (8 min)

**The Door Analogy:**

> "Imagine a room with TWO doors. You can get in through Door A OR Door B. Either one works! You just need at least one door open. That is an OR gate."

**Truth Table for OR:**

```
  OR Gate: Output is 1 if ANY input is 1

  +-----+-----+--------+
  |  A  |  B  | Output |
  +-----+-----+--------+
  |  0  |  0  |   0    |
  |  0  |  1  |   1    |  <-- This one!
  |  1  |  0  |   1    |  <-- This one!
  |  1  |  1  |   1    |  <-- This one too!
  +-----+-----+--------+
```

**Real-world OR examples:**
- A doorbell rings if the front button OR the back button is pressed
- You pass the test if you get question 1 right OR question 2 right (or both!)
- An alarm sounds if the smoke detector OR the heat detector goes off

**Build the OR gate circuit (7432):**

Same wiring as the AND gate, but using the 7432 IC instead. Pin layout is identical to the 7408.

**Test all 4 combinations:**
- Both buttons NOT pressed: LED off
- Button A only: LED ON!
- Button B only: LED ON!
- Both buttons: LED ON!

**Award: +30 XP for building and testing the OR gate!**

---

### Step 4: The NOT Gate -- The Opposite Machine (8 min)

**The Mirror Analogy:**

> "A NOT gate is the simplest gate of all. It does exactly ONE thing: it flips the input to the opposite. If you put in a 1, you get a 0. If you put in a 0, you get a 1. It is like a mirror that shows you the opposite of what you are!"

**Truth Table for NOT:**

```
  NOT Gate: Output is the OPPOSITE of the input

  +-------+--------+
  | Input | Output |
  +-------+--------+
  |   0   |   1    |
  |   1   |   0    |
  +-------+--------+
```

**The NOT gate is also called an "inverter" -- it inverts (flips) the signal.**

**Real-world NOT examples:**
- A refrigerator light: door OPEN (1) = light ON. Door CLOSED (0) = light OFF. Wait -- that IS a NOT relationship! When the door switch is pressed (closed), the light is OFF.
- An "occupied" sign on a bathroom door: door LOCKED (1) = sign shows OCCUPIED. Door UNLOCKED (0) = sign shows VACANT

**Build the NOT gate circuit (7404):**

The 7404 has SIX NOT gates (inverters) inside:

```
  7404 Hex Inverter -- Top View

        Notch
          U
    +----------+
    |  1    14 | <-- Pin 14 = VCC (+5V)
    |  2    13 |
    |  3    12 |
    |  4    11 |
    |  5    10 |
    |  6     9 |
    |  7     8 |
    +----------+
       ^
    Pin 7 = GND

  Inverter 1: Input = Pin 1  --> Output = Pin 2
  Inverter 2: Input = Pin 3  --> Output = Pin 4
  Inverter 3: Input = Pin 5  --> Output = Pin 6
```

1. Place 7404 on breadboard, notch up
2. Pin 14 to + rail, Pin 7 to - rail
3. Connect a push button with pull-down resistor to Pin 1 (Input)
4. Connect Pin 2 (Output) to 330-ohm resistor to LED to GND

**Test it:**
- Button NOT pressed (input = 0): LED is ON! (output = 1)
- Button pressed (input = 1): LED is OFF! (output = 0)

> "It is backwards from what you expect! When the button is up, the LED is on. Press the button, and the LED turns off. The NOT gate flips everything!"

**Award: +20 XP for building and testing the NOT gate!**

---

### Step 5: Wand Check -- Measure HIGH and LOW Voltages! (8 min)

> "We keep saying HIGH and LOW. But what voltage IS high? What voltage IS low? Let us measure it with the Wand and find out!"

**Measurement Activity:**

Set the Wand to DC Voltage mode. For each gate you built, measure the output pin voltage for each input combination.

```
| Gate | Input(s)  | LED State | Wand Reads (Output) | HIGH or LOW? |
|------|-----------|-----------|--------------------|----|
| AND  | Both off  | Off       |                    |    |
| AND  | Both on   | On        |                    |    |
| OR   | One on    | On        |                    |    |
| OR   | Both off  | Off       |                    |    |
| NOT  | Off       | On        |                    |    |
| NOT  | On        | Off       |                    |    |
```

**What you should discover:**
- **HIGH** voltage reads close to the power supply voltage (about 5V if using 5V, or about 8-9V if using 9V)
- **LOW** voltage reads close to 0V (usually 0.1V to 0.3V)

> "Now you know exactly what HIGH and LOW look like on the Wand! HIGH is close to the power supply voltage. LOW is close to zero. There is nothing in between -- digital circuits are either ON or OFF, with nothing in the middle."

**Bonus: Measure the input pins too!**
- When a button is pressed: input pin should read HIGH
- When a button is not pressed (pull-down resistor): input pin should read LOW (close to 0V)

**Award: +50 XP for measuring all 6 input/output combinations with the Wand!**

---

## Fun Game: Logic Gate Charades (Optional Extension)

One person acts as the "gate." Two other people are the "inputs." The inputs each hold up a hand (up = 1, down = 0). The "gate" person has to show the correct output (hand up or down) based on which gate they are pretending to be. The other players guess which gate it is!

---

## Quick Quiz -- Earn Bonus XP!

**Question 1:** An AND gate gives output 1 when:
- A) Any input is 1
- B) All inputs are 1
- C) No inputs are 1

**(Correct: B -- +20 XP!)**

**Question 2:** An OR gate gives output 1 when:
- A) All inputs are 0
- B) Both inputs are exactly 1
- C) At least one input is 1

**(Correct: C -- +20 XP!)**

**Question 3:** A NOT gate has how many inputs?
- A) One
- B) Two
- C) Three

**(Correct: A -- +20 XP!)**

**Question 4:** When you measure a logic HIGH with the Wand, you should see a voltage close to:
- A) 0V
- B) The power supply voltage (about 5V)
- C) 100V

**(Correct: B -- +20 XP!)**

---

## Lesson 20 Complete!

```
  =============================================

     LOGIC EXPLORER BADGE UNLOCKED!

     Skills unlocked:
     [check] Understand AND, OR, and NOT gates
     [check] Read and fill in truth tables
     [check] Built all three gates on a breadboard
     [check] Measured HIGH and LOW voltages with the Wand
     [check] Know real-world logic gate examples

  =============================================
```

**XP Breakdown:**
| Activity | XP |
|----------|-----|
| Digital logic intro | 10 |
| Build AND gate | 30 |
| Build OR gate | 30 |
| Build NOT gate | 20 |
| Wand Check (6 measurements) | 50 |
| Quiz (4 questions) | 80 |
| **TOTAL POSSIBLE** | **220** |

---

## Coming Up Next...

In **Lesson 21**, you will meet three MORE logic gates: **NAND, NOR, and XOR**. NAND is especially cool because it is called the "universal gate" -- you can build ANY other gate using only NAND gates! You will prove it with your own circuits.

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| LED stays on no matter what | Check pull-down resistors on inputs -- without them, inputs float HIGH |
| LED never turns on | Verify VCC and GND are connected (Pin 14 and Pin 7 on most 74xx ICs) |
| Output seems random | Unconnected inputs pick up noise -- always tie unused inputs to GND or VCC |
| IC gets hot | Wrong IC in the circuit or power/ground pins reversed -- check immediately |
| Wand reads something between HIGH and LOW | Input might be "floating" -- add pull-down (10k to GND) or pull-up (10k to VCC) |
| Button does not seem to work | Test button with Wand continuity mode -- make sure it beeps when pressed |

---

## Navigation

| | |
|:---|---:|
| [← Lesson 19: The 555 Timer -- One-Shot Mode (Monostable)](lesson-19-555-timer-one-shot-mode.md) | [Lesson 21: Logic Gates -- NAND, NOR, XOR →](lesson-21-logic-gates-nand-nor-xor.md) |

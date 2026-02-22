# Lesson 21: Logic Gates -- NAND, NOR, XOR

**Module:** 3 -- Integrated Circuits (ICs)
**Difficulty:** Star-3 Intermediate
**Session Time:** 45--50 minutes
**Age:** 6--12 years
**XP Available:** 300 XP

---

## Your Mission Today

You already know AND, OR, and NOT. Now it is time to meet their clever cousins: **NAND, NOR, and XOR**. These three gates have some amazing tricks. NAND is so powerful it can pretend to be ANY other gate -- it is the Swiss Army knife of logic. And XOR has a special talent for telling you when things are different. Let us explore!

---

## Learning Objectives

By the end of this lesson, you will be able to:
- Explain how NAND, NOR, and XOR gates work using truth tables
- Build each gate on a breadboard using IC chips
- Prove that a NAND gate can act as a NOT gate
- Use your Magic Measurement Wand to verify gate outputs

---

## What You Need

| Item | Qty |
|------|-----|
| 7400 NAND gate IC | 1 |
| 7402 NOR gate IC | 1 |
| 7486 XOR gate IC | 1 |
| LEDs (any color) | 3 |
| 330-ohm resistors | 3 |
| 10k-ohm resistors (pull-down) | 4 |
| Push buttons (tactile switch) | 2 |
| 9V battery + clip (or 5V power) | 1 |
| Breadboard | 1 |
| Jumper wires | 15 |
| Multimeter (Magic Measurement Wand!) | 1 |

---

## How to Teach This Lesson

### Step 1: Hook -- The Gate Family Reunion (5 min)

> "Last lesson you met the original three gates: AND, OR, and NOT. Think of them as the founding members of the Gate family. Today we meet three more relatives who each have their own personality."

> "NAND is the rebel -- it does the OPPOSITE of AND. NOR is the contrarian -- it does the OPPOSITE of OR. And XOR is the detective -- it only cares when things are DIFFERENT."

**Quick review:**
- AND: output is 1 only when ALL inputs are 1
- OR: output is 1 when ANY input is 1
- NOT: flips the input to the opposite

> "Ready to expand the family? Let us go!"

**Award: +10 XP for reviewing the first three gates!**

---

### Step 2: The NAND Gate -- AND's Opposite (8 min)

**What is NAND?**

> "NAND stands for NOT-AND. It does an AND operation, then flips the answer with a NOT. It gives you the OPPOSITE of what AND would give."

**Truth Table for NAND:**

```
  NAND Gate: Output is the OPPOSITE of AND

  +-----+-----+-----+--------+
  |  A  |  B  | AND | NAND   |
  +-----+-----+-----+--------+
  |  0  |  0  |  0  |   1    |  <-- Flipped!
  |  0  |  1  |  0  |   1    |  <-- Flipped!
  |  1  |  0  |  0  |   1    |  <-- Flipped!
  |  1  |  1  |  1  |   0    |  <-- Flipped!
  +-----+-----+-----+--------+

  The only time NAND gives 0 is when BOTH inputs are 1.
```

**The Rule:** NAND outputs 0 ONLY when both inputs are 1. Every other combination gives 1.

**The 7400 NAND IC has four NAND gates inside.** Pin layout is the same as the 7408 (AND):
- Gate 1: Inputs Pin 1, Pin 2 --> Output Pin 3
- VCC = Pin 14, GND = Pin 7

**Build and test the NAND gate** using the same wiring as the AND gate (Lesson 20, Step 2), but with the 7400 IC instead.

**Test all 4 combinations:**
- Both buttons off: LED ON (opposite of AND!)
- Button A only: LED ON
- Button B only: LED ON
- Both buttons on: LED OFF

**Award: +20 XP for building and testing the NAND gate!**

---

### Step 3: NAND's Superpower -- The Universal Gate (8 min)

> "Here is something amazing: if you have enough NAND gates, you can build ANY other logic gate. AND, OR, NOT -- all of them! That is why NAND is called the UNIVERSAL gate. Computer engineers love it because they only need ONE type of gate to build an entire computer."

**Demo: Build a NOT gate using a NAND gate**

Take one NAND gate and connect BOTH inputs together:

```
  Input A ----+---- Pin 1
              |
              +---- Pin 2
                     |
                    Pin 3 = Output

  If Input = 0: both inputs are 0, NAND gives 1 (it IS a NOT!)
  If Input = 1: both inputs are 1, NAND gives 0 (it IS a NOT!)
```

**Wire it up:**
1. On the 7400, connect Pin 1 and Pin 2 together with a jumper wire
2. Connect a button with pull-down to the joined pins
3. Connect Pin 3 (Output) to 330-ohm resistor to LED to GND

**Test it:**
- Button not pressed: LED ON (input 0, output 1)
- Button pressed: LED OFF (input 1, output 0)

> "You just built a NOT gate using a NAND gate! The NAND is so versatile it can pretend to be other gates. That is its superpower!"

**Award: +30 XP for proving NAND can act as NOT!**

---

### Step 4: The NOR Gate -- OR's Opposite (6 min)

**What is NOR?**

> "NOR stands for NOT-OR. It does an OR, then flips it. The output is 1 ONLY when both inputs are 0."

**Truth Table for NOR:**

```
  NOR Gate: Output is the OPPOSITE of OR

  +-----+-----+----+--------+
  |  A  |  B  | OR | NOR    |
  +-----+-----+----+--------+
  |  0  |  0  |  0 |   1    |  <-- Only this one!
  |  0  |  1  |  1 |   0    |
  |  1  |  0  |  1 |   0    |
  |  1  |  1  |  1 |   0    |
  +-----+-----+----+--------+
```

**The Rule:** NOR outputs 1 ONLY when both inputs are 0. Any other combination gives 0.

**Real-world NOR example:**

> "Think of a security system. The alarm is ON (safe mode) only when there are NO intruders at door A AND NO intruders at door B. If EITHER door is breached, the alarm output turns OFF and the siren kicks in."

**Build the NOR gate using the 7402 IC.** Note: The 7402 has a slightly different pin layout!

```
  7402 Quad NOR Gate -- Top View

  Gate 1: Output = Pin 1, Inputs = Pin 2, Pin 3
  (Output comes FIRST on the 7402!)
  VCC = Pin 14, GND = Pin 7
```

**Award: +20 XP for building and testing the NOR gate!**

---

### Step 5: The XOR Gate -- The Difference Detector (8 min)

**What is XOR?**

> "XOR stands for Exclusive OR. It outputs 1 only when the inputs are DIFFERENT. Same inputs = 0. Different inputs = 1. Think of it as the 'disagree detector.'"

**Truth Table for XOR:**

```
  XOR Gate: Output is 1 when inputs are DIFFERENT

  +-----+-----+--------+
  |  A  |  B  | Output |
  +-----+-----+--------+
  |  0  |  0  |   0    |  Same = 0
  |  0  |  1  |   1    |  Different = 1!
  |  1  |  0  |   1    |  Different = 1!
  |  1  |  1  |   0    |  Same = 0
  +-----+-----+--------+
```

**The Light Switch Analogy:**

> "Think about a hallway with a light switch at each end. If both switches are in the same position (both up or both down), the light is OFF. If they are in DIFFERENT positions, the light is ON. That is exactly XOR!"

**Real-world XOR uses:**
- Adding binary numbers (the basis of all computer math!)
- Comparing two signals to see if they match
- Error detection in data transmission

**Build the XOR gate using the 7486 IC.** Pin layout is the same as the 7408:
- Gate 1: Inputs Pin 1, Pin 2 --> Output Pin 3
- VCC = Pin 14, GND = Pin 7

**Test all 4 combinations:**
- Both buttons off: LED OFF (same)
- Button A only: LED ON (different!)
- Button B only: LED ON (different!)
- Both buttons on: LED OFF (same)

**Award: +30 XP for building and testing the XOR gate!**

---

### Step 6: Wand Check -- Verify All Gate Outputs! (6 min)

> "Let us do a full Wand scan of all three new gates. For each gate, measure the output voltage for at least two input combinations."

**Set the Wand to DC Voltage. Black probe on GND.**

```
| Gate | Inputs | LED State | Wand Output (V) | Expected |
|------|--------|-----------|-----------------|----------|
| NAND | 0, 0   | On        |                 | HIGH     |
| NAND | 1, 1   | Off       |                 | LOW      |
| NOR  | 0, 0   | On        |                 | HIGH     |
| NOR  | 1, 0   | Off       |                 | LOW      |
| XOR  | 0, 1   | On        |                 | HIGH     |
| XOR  | 1, 1   | Off       |                 | LOW      |
```

> "Every gate follows the same rule: HIGH means close to VCC, LOW means close to 0V. The Wand confirms what the truth tables predicted!"

**Award: +40 XP for verifying all three gates with the Wand!**

---

## Fun Game: Gate Master Challenge (Optional Extension)

Draw these truth tables with the OUTPUT column blank. See if the kid can fill in the correct outputs WITHOUT looking at the notes:

```
GATE MASTER CHALLENGE

Gate: _____ (mystery gate!)
| A | B | Output |
|---|---|--------|
| 0 | 0 |        |
| 0 | 1 |        |
| 1 | 0 |        |
| 1 | 1 |        |

Output: 1, 1, 1, 0
What gate is this? _____
```

---

## Quick Quiz -- Earn Bonus XP!

**Question 1:** NAND gives an output of 0 when:
- A) Both inputs are 0
- B) Both inputs are 1
- C) One input is 0

**(Correct: B -- +20 XP!)**

**Question 2:** Why is NAND called the "universal gate"?
- A) It is used in every country
- B) You can build any other logic gate using only NAND gates
- C) It is the biggest gate

**(Correct: B -- +20 XP!)**

**Question 3:** XOR outputs 1 when:
- A) Both inputs are the same
- B) Both inputs are 0
- C) The inputs are different

**(Correct: C -- +20 XP!)**

---

## Lesson 21 Complete!

```
  =============================================

     GATE MASTER BADGE UNLOCKED!

     Skills unlocked:
     [check] Understand NAND, NOR, and XOR gates
     [check] Built all three gates on a breadboard
     [check] Proved NAND can act as NOT
     [check] Verified outputs with the Wand
     [check] Know all six fundamental logic gates

  =============================================
```

**XP Breakdown:**
| Activity | XP |
|----------|-----|
| Review of AND/OR/NOT | 10 |
| Build NAND gate | 20 |
| NAND-as-NOT proof | 30 |
| Build NOR gate | 20 |
| Build XOR gate | 30 |
| Wand Check (6 measurements) | 40 |
| Quiz (3 questions) | 60 |
| **TOTAL POSSIBLE** | **210** |

---

## Coming Up Next...

In **Lesson 22**, you will work with a **7-Segment Display** -- the glowing number displays you see on digital clocks and scoreboards! You will learn how to light up each segment individually, then use a decoder IC to display any digit from 0 to 9 just by flipping switches.

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| NAND output seems same as AND | Double-check you are using the 7400 (NAND), not the 7408 (AND) |
| NOR output is always LOW | The 7402 has a different pin layout -- output is Pin 1, inputs are Pin 2 and Pin 3 |
| XOR LED never turns on | Make sure both inputs have pull-down resistors to GND |
| NAND-as-NOT does not work | Verify both inputs (Pin 1 and Pin 2) are connected together with a jumper wire |
| Multiple gates interfere with each other | Build one gate at a time; unused IC inputs should be tied to GND |
| IC gets hot immediately | Power and ground pins are likely reversed -- remove power and check |

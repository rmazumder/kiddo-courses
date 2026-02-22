# Lesson 12: Parallel Circuits -- Multiple Paths, Shared Voltage

**Module:** 2 -- Building Simple Circuits
**Difficulty:** Star-2 Easy-Medium
**Session Time:** 45--50 minutes
**Age:** 6--12 years
**XP Available:** 230 XP

---

## Your Mission Today

Circuit Explorer, last lesson you built a series circuit -- one track, one path. Today you are going to build a **parallel circuit**, where electricity gets CHOICES! Multiple paths, multiple lanes, and a whole new mystery to solve. You will unlock a brand-new superpower of your Magic Measurement Wand: measuring **current** in Amps! Get ready to become a branch detective!

---

## Learning Objectives

By the end of this lesson, you will be able to:
- Explain what a parallel circuit is and how it differs from series
- Know that voltage is the SAME across all parallel branches
- Measure current in each branch using ammeter mode (a new Wand skill!)
- Prove that branch currents add up to the total current
- Predict what happens when one branch is removed

---

## What You Need

| Item | Qty |
|------|-----|
| 9V battery + clip | 1 |
| Breadboard | 1 |
| Resistors: 330-ohm, 470-ohm, 1k-ohm | 2 each |
| LEDs: red, green, yellow | 1 each |
| Jumper wires | 10 |
| Alligator clip wires | 2 |
| Multimeter (Magic Measurement Wand) | 1 |
| Paper + pencil | 1 set |

---

## How to Teach This Lesson

### Step 1: Hook -- The Highway vs. the Country Road (5 min)

> "Imagine you are driving to school. There is only ONE road. If a tree falls across it, NOBODY can get through. That is a series circuit."

> "Now imagine there are THREE roads to school. A tree falls on Road 1 -- no problem! You take Road 2 or Road 3. Some cars take one road, some take another. That is a **parallel circuit**."

> "In a parallel circuit, electricity has multiple paths. If one path breaks, the others keep working. And here is the cool part: each path gets the FULL voltage from the battery!"

**Draw this together:**

```
  SERIES (one road):
  Battery --> [R1] --> [R2] --> [R3] --> back
  If R2 breaks: everything stops!

  PARALLEL (multiple roads):
                  +--[R1]--+
                  |        |
  Battery (+) ---+--[R2]--+--- Battery (-)
                  |        |
                  +--[R3]--+
  If R2 breaks: R1 and R3 keep working!
```

**Award: +10 XP for explaining the difference between series and parallel in your own words!**

---

### Step 2: Rules of Parallel Circuits (8 min)

**The key rules -- side by side with series:**

| Rule | Series Circuit | Parallel Circuit |
|------|---------------|-----------------|
| **Paths** | ONE path for current | MULTIPLE paths for current |
| **Current** | Same current everywhere | Current SPLITS between branches |
| **Voltage** | Voltage splits between components | Same voltage across all branches |
| **One breaks** | Everything stops | Other branches keep working |
| **Adding resistors** | Total R goes UP | Total R goes DOWN (surprising!) |

> "The biggest surprise: adding MORE paths in parallel actually makes it EASIER for electricity to flow, not harder! More lanes on the highway = more total traffic."

**Kirchhoff's Current Law (the "splitting" rule):**

> "The total current going IN equals the total current coming OUT. If 30 mA leaves the battery, and 10 mA goes through R1 and 20 mA goes through R2, that adds up to 30 mA!"

```
  Total current IN:   I_total = 30 mA
  Branch 1:           I_1 = 10 mA
  Branch 2:           I_2 = 20 mA
  Total OUT:          I_1 + I_2 = 30 mA   (matches!)
```

**Award: +10 XP for understanding the splitting rule!**

---

### Step 3: Build a Parallel LED Circuit (10 min)

**Circuit -- Three LEDs in Parallel:**

```
  Circuit diagram:

                       +--[330-ohm]--[RED LED]---+
                       |                          |
  9V (+) ----+---------+--[330-ohm]--[GREEN LED]--+--------+---- 9V (-)
                       |                          |
                       +--[330-ohm]--[YELLOW LED]-+

  On breadboard:
  1. Battery clip: red wire to + rail, black wire to - rail
  2. Branch 1: jumper from + rail to row 5, R1 (330 ohm) row 5 to row 7,
     red LED long leg row 7, short leg row 9, jumper row 9 to - rail
  3. Branch 2: jumper from + rail to row 12, R2 (330 ohm) row 12 to row 14,
     green LED long leg row 14, short leg row 16, jumper row 16 to - rail
  4. Branch 3: jumper from + rail to row 19, R3 (330 ohm) row 19 to row 21,
     yellow LED long leg row 21, short leg row 23, jumper row 23 to - rail
```

> "Each LED has its OWN path from + to -. They share the battery, but they each have their own private road."

**Observation:**

> "Look at the brightness. Are these LEDs brighter or dimmer than the three series LEDs from last lesson?"

They should be BRIGHTER! Each LED gets the full 9V minus its own resistor drop -- not sharing with other LEDs.

**Award: +20 XP for building the three-LED parallel circuit!**

---

### Step 4: Wand Check -- Voltage Is the Same Everywhere! (8 min)

> "Let us prove that every branch gets the same voltage."

Set your Wand to **DC Volts** (20V range).

**Measure voltage across each LED:**

```
| Branch | Across Resistor | Across LED | Total (R + LED) |
|--------|----------------|-----------|----------------|
| Red    | _____ V        | _____ V   | _____ V        |
| Green  | _____ V        | _____ V   | _____ V        |
| Yellow | _____ V        | _____ V   | _____ V        |
| Battery| _____ V        |           |                |
```

> "What do you notice? Each branch's total (resistor + LED) should be about 9V -- the same as the battery! In parallel, every branch sees the FULL battery voltage."

> "Compare this to series: in series, the voltage was SPLIT. In parallel, each branch gets ALL of it!"

**Award: +30 XP for proving voltage is the same across all parallel branches!**

---

### Step 5: NEW Wand Superpower -- Measuring Current! (12 min)

> "Until now, your Wand has measured voltage (push) and resistance (blocking) and tested continuity (beep). Today you unlock a NEW superpower: measuring **current** -- how much electricity is actually flowing! This is called **ammeter mode**."

**SAFETY RULES FOR AMMETER MODE (very important!):**

> "Measuring current is DIFFERENT from measuring voltage. Here are the rules:"

```
  AMMETER SAFETY RULES
  =====================

  Rule 1: Move the RED probe to the "A" or "mA" hole on the multimeter.
          (It was in V/ohm before. Now it moves!)

  Rule 2: The Wand must be wired IN SERIES with the branch you want to measure.
          That means you BREAK the circuit and insert the Wand into the gap.

  Rule 3: NEVER connect the ammeter directly across the battery (+ to -).
          That is a short circuit through the Wand -- it will blow the fuse!

  Rule 4: Start on the HIGHEST current range (like 10A or 200mA) first.
          Switch to lower ranges for more accuracy.
```

> "Think of it this way: measuring VOLTAGE is like putting a stethoscope on your chest -- you just listen from the outside. Measuring CURRENT is like cutting a water pipe and putting a flow meter IN the pipe. You have to be part of the circuit!"

**How to measure current in one branch:**

```
  BEFORE (normal circuit):
  + rail ---- [330-ohm] ---- [RED LED] ---- - rail

  TO MEASURE CURRENT:
  + rail ---- [330-ohm] ---- BREAK HERE ---- [RED LED] ---- - rail
                              |          |
                           Wand RED   Wand BLACK
                           (in mA hole) (in COM hole)
```

**Practical steps:**

1. Move the RED probe to the **mA** or **A** jack on the Wand
2. Set the dial to **DCA** (DC Amps) or **mA** range
3. Disconnect one end of the LED from the circuit (lift a jumper wire)
4. Touch one Wand probe to the loose wire, the other to where it was
5. Read the current! The Wand is now PART of the circuit, measuring the flow.

> "Using alligator clips makes this easier -- clip one to each side of the break so your hands are free."

**Measure current in each branch:**

```
| Branch | Current (mA) |
|--------|-------------|
| Red LED    |         |
| Green LED  |         |
| Yellow LED |         |
| TOTAL (add them up) | |
```

Expected: Each branch should read about 20--22 mA (with 330-ohm resistors).

**Now measure the TOTAL current** (break the wire between + rail and the junction point where all branches split):

> "The total should be about 60--65 mA -- the sum of all three branches!"

```
  I_total = I_red + I_green + I_yellow
  about 60 mA = 20 + 20 + 20 mA
```

> "Kirchhoff's Current Law confirmed! The total current splits into branches, and the branches add back up to the total!"

**Award: +50 XP for measuring current in all three branches AND the total!**

---

### Step 6: The Independence Test (5 min)

> "Here is the best thing about parallel circuits. Let us prove it."

**Remove the green LED** (pull it out of the breadboard).

> "What happened to the red and yellow LEDs?"

They stay ON!

> "In parallel, each branch is independent. Removing one branch does not break the others. The remaining branches still have a complete path from + to -."

**Wand check:** Measure the current in the red LED branch now. Is it the same as before? It should be!

> "The current in each surviving branch does NOT change when you remove another branch. Each branch only cares about its own voltage and resistance."

**Award: +20 XP for proving parallel branch independence!**

---

### Step 7: Series vs. Parallel -- Side by Side (3 min)

Build BOTH circuits at the same time (if space allows) and compare:

```
| Feature | Series (3 LEDs) | Parallel (3 LEDs) |
|---------|----------------|-------------------|
| Brightness | Dim | Bright |
| Remove one LED | All go dark | Others stay on |
| Current | Same everywhere | Splits between branches |
| Voltage | Splits between LEDs | Same across each branch |
| Total resistance | R1 + R2 + R3 (high) | Less than smallest R (low) |
```

> "Series and parallel each have their superpowers. Series is simpler. Parallel is more reliable."

**Award: +10 XP for building the side-by-side comparison!**

---

## Quick Quiz -- Earn Bonus XP!

**Question 1:** In a parallel circuit, what stays the SAME across every branch?
- A) Current
- B) Resistance
- C) Voltage

**(Correct: C -- +20 XP!)**

**Question 2:** You have 3 branches in parallel. Branch 1 carries 10 mA, Branch 2 carries 15 mA, Branch 3 carries 25 mA. What is the total current from the battery?
- A) 10 mA
- B) 25 mA
- C) 50 mA

**(Correct: C -- 10 + 15 + 25 = 50 mA -- +20 XP!)**

**Question 3:** You remove one LED from a parallel circuit with 3 LEDs. What happens?
- A) All LEDs go dark (like series)
- B) The other two LEDs stay on -- they have their own paths
- C) The other two LEDs get dimmer

**(Correct: B -- +20 XP!)**

**Bonus question for older kids (10+):**
> "Why does adding more parallel branches make the TOTAL resistance go DOWN?"
>
> "Because each new branch is a new path for current. More paths = easier for electricity to flow = lower total resistance. It is like opening more checkout lanes at a store -- the line moves faster!"

**(+20 XP bonus for a good explanation!)**

---

## Lesson 12 Complete!

```
  =============================================

     PARALLEL CIRCUIT PRO BADGE UNLOCKED!

     Skills unlocked:
     [check] Built parallel circuits with multiple branches
     [check] Proved voltage is the same across all branches
     [check] Measured current in each branch (new ammeter skill!)
     [check] Proved branch currents add up (Kirchhoff's Current Law)
     [check] Demonstrated branch independence

  =============================================
```

**XP Breakdown:**
| Activity | XP |
|----------|-----|
| Hook -- series vs parallel explanation | 10 |
| Understand the splitting rule | 10 |
| Build three-LED parallel circuit | 20 |
| Wand -- voltage across all branches | 30 |
| NEW ammeter skill -- measure all currents | 50 |
| Independence test | 20 |
| Side-by-side comparison | 10 |
| Quiz (3 questions) | 60 |
| Bonus question | 20 |
| **TOTAL POSSIBLE** | **230** |

---

## Coming Up Next...

In **Lesson 13**, we learn about **voltage dividers** -- a clever trick that uses two resistors to create ANY voltage you want from a single battery. You will use a formula to PREDICT the output voltage, then use your Magic Measurement Wand to see if the formula told the truth!

---

## Troubleshooting

| Problem | Likely Cause | Fix |
|---------|-------------|-----|
| Wand reads 0 mA in ammeter mode | Red probe still in V/ohm jack | Move red probe to mA or A jack |
| Wand reads 0 mA | Wand not wired in series | The Wand must BREAK the circuit and be inserted into the gap |
| Wand reads "OL" in current mode | Current too high for selected range | Switch to higher current range (10A range) |
| One LED brighter than others | Different LED colors have different forward voltages | Blue/white use more voltage, leaving less for the resistor, changing current slightly |
| Current does not add up | Measurement error or loose wires | Recheck all connections; measure one branch at a time |
| Wand blows a fuse | Ammeter connected directly across battery | Replace fuse; remember -- ammeter goes IN SERIES, never across the battery |

---

## Parent/Instructor Notes

- **Ammeter mode is the one mode that can damage the multimeter** if used incorrectly. Before the child attempts current measurement, review the safety rules together. Consider having an adult do the first measurement while the child watches, then let the child try.
- Most basic multimeters have a fuse for the mA range. If it blows, fuses are cheap and easy to replace (usually a standard glass fuse inside the battery compartment).
- **Ages 6--8:** Focus on the brightness comparison (parallel is brighter than series) and the independence test (removing one LED). Skip the current measurement or do it together with heavy supervision. The key takeaway is "parallel means each branch has its own path."
- **Ages 9--12:** The current measurements are the star of this lesson. Have them predict branch currents using Ohm's Law first (I = V/R = 7V/330 = 21 mA), then measure. The act of predicting and confirming builds deep understanding.
- Alligator clip wires make ammeter measurements MUCH easier. Consider getting a set if you do not have them already.
- The side-by-side comparison (Step 7) is very impactful if you can have both circuits powered at the same time. The brightness difference is stark and memorable.

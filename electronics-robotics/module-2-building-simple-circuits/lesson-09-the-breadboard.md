# Lesson 9: The Breadboard -- Your Circuit Building Playground

**Module:** 2 -- Building Simple Circuits
**Difficulty:** Star-2 Easy-Medium
**Session Time:** 40--45 minutes
**Age:** 6--12 years
**XP Available:** 230 XP

---

## Your Mission Today

Welcome back, Circuit Explorer! You have used a breadboard a few times already -- but today, you are going to learn EXACTLY how it works. You will use your Magic Measurement Wand to explore the invisible highways hidden inside the breadboard. By the end of this mission, you will know every secret passageway and be able to build circuits confidently!

---

## Learning Objectives

By the end of this lesson, you will be able to:
- Explain how breadboard rows and columns are connected internally
- Identify power rails, terminal strips, and the center gap
- Use continuity mode to map the breadboard's hidden connections
- Build a simple circuit using proper breadboard technique
- Troubleshoot common breadboard mistakes

---

## What You Need

| Item | Qty |
|------|-----|
| 830-point breadboard | 1 |
| Digital multimeter (Magic Measurement Wand) | 1 |
| LEDs (red, green) | 2 |
| 330-ohm resistors | 2 |
| 9V battery + clip | 1 |
| Jumper wires (assorted colors) | 10 |
| Paper + colored pencils | 1 set |

---

## How to Teach This Lesson

### Step 1: Hook -- The Mystery Hotel (5 min)

Hold up a breadboard.

> "Imagine a hotel with hundreds of rooms. Some rooms are connected by secret tunnels -- if you walk into one room, you can get to certain OTHER rooms without going into the hallway. But which rooms are connected? That is a mystery!"

> "This breadboard is like that hotel. There are over 800 holes, but they are NOT all separate. Some holes are secretly connected underneath. Today, your Magic Measurement Wand is going to help you discover every secret tunnel!"

> "And here is the best part -- once you know the tunnels, you can build ANY circuit you want without soldering a single wire."

**Award: +10 XP for being ready to explore the breadboard hotel!**

---

### Step 2: The Breadboard Map (10 min)

Draw this on paper together -- or print it out:

```
  Breadboard top view:

  + + + + + + + + + + + + + + + + + + + +    <-- Red power rail (+ row)
  - - - - - - - - - - - - - - - - - - - -    <-- Blue ground rail (- row)

  a b c d e       f g h i j
  [ ][ ][ ][ ][ ]     [ ][ ][ ][ ][ ]   Row 1
  [ ][ ][ ][ ][ ]     [ ][ ][ ][ ][ ]   Row 2
  [ ][ ][ ][ ][ ]     [ ][ ][ ][ ][ ]   Row 3
  [ ][ ][ ][ ][ ]     [ ][ ][ ][ ][ ]   Row 4
  [ ][ ][ ][ ][ ]     [ ][ ][ ][ ][ ]   Row 5
  ...               GAP                  ...
  [ ][ ][ ][ ][ ]     [ ][ ][ ][ ][ ]   Row 30
  (continues for 30 or 63 rows depending on breadboard size)

  - - - - - - - - - - - - - - - - - - - -    <-- Blue ground rail (- row)
  + + + + + + + + + + + + + + + + + + + +    <-- Red power rail (+ row)
```

**Three zones to learn:**

| Zone | What It Is | How It Connects |
|------|-----------|----------------|
| **Power Rails** | The long rows at the top and bottom, marked + and - | All holes in one rail row are connected horizontally across the entire board |
| **Terminal Strips** | The main grid of holes (a-e and f-j) | Holes in the SAME ROW on the SAME SIDE of the gap are connected (a-b-c-d-e together, f-g-h-i-j together) |
| **Center Gap** | The empty channel down the middle | NOTHING crosses the gap! Left side (a-e) and right side (f-j) are separate |

> "Think of it this way: each row on one side of the gap is a tiny bus. Everyone sitting on the same bus shares the same electrical connection. But the bus does NOT cross the gap in the middle!"

**Key vocabulary:**

| Word | Kid-Friendly Definition |
|------|------------------------|
| **Power rail** | The long highway at the top and bottom for + and - from the battery |
| **Terminal strip** | The main area where you plug in components -- rows of 5 connected holes |
| **Center gap** | The valley down the middle that separates left from right |
| **Bus** | A shared electrical highway -- every hole on the same bus is connected |

**Award: +20 XP for labeling all three zones on your breadboard map!**

---

### Step 3: Wand Check -- Prove the Connections! (12 min)

> "You learned the RULES of how the breadboard works. But are they true? Let us use your Magic Measurement Wand to PROVE it!"

Set your Wand to **continuity mode** (the sound wave / speaker symbol).

**Experiment 1 -- Same Row, Same Side:**

1. Touch one probe to hole A1 (row 1, column a)
2. Touch the other probe to hole E1 (row 1, column e)
3. Listen: BEEP! They ARE connected!

> "The Wand just proved it -- holes a through e in the same row share a secret tunnel!"

**Experiment 2 -- Same Row, Different Side:**

1. Touch one probe to hole A1
2. Touch the other probe to hole F1 (row 1, column f -- other side of gap)
3. Listen: NO BEEP. They are NOT connected!

> "The gap blocks the tunnel! Even though they are in the same row number, they are on opposite sides of the gap."

**Experiment 3 -- Different Rows, Same Side:**

1. Touch one probe to hole A1
2. Touch the other probe to hole A2 (row 2, column a)
3. Listen: NO BEEP. They are NOT connected!

> "Row 1 and Row 2 are separate buses. They do not talk to each other."

**Experiment 4 -- Power Rail Test:**

1. Touch one probe to the first hole in the + rail
2. Touch the other probe to the LAST hole in the + rail
3. Listen: BEEP! The entire rail is one long highway!

> "The power rail runs the entire length of the board. Every hole in the + rail is connected to every other hole in the + rail."

**Important note for some breadboards:**

> "On some larger breadboards, the power rails have a BREAK in the middle. If your Wand does not beep from one end to the other, look for a small gap in the printed line. You will need a jumper wire to bridge it!"

**Fill in your Wand investigation results:**

```
| Test | Probe 1 | Probe 2 | Beep? | Connected? |
|------|---------|---------|-------|-----------|
| 1    | A1      | E1      |       |           |
| 2    | A1      | F1      |       |           |
| 3    | A1      | A2      |       |           |
| 4    | + rail (first) | + rail (last) | |    |
| 5    | + rail  | - rail  |       |           |
| 6    | A5      | B5      |       |           |
| 7    | E5      | F5      |       |           |
```

**Bonus test (Test 5):** The + rail and - rail should NOT beep -- they are separate!

**Bonus test (Test 6):** A5 and B5 should beep -- same row, same side!

**Bonus test (Test 7):** E5 and F5 should NOT beep -- different sides of the gap!

**Award: +50 XP for completing all 7 Wand tests!**

---

### Step 4: Draw the Invisible Map (5 min)

Now that the Wand has confirmed everything, have the kid draw the connections on a blank breadboard picture:

> "Color all the holes that are secretly connected in the SAME color. Use a different color for each group."

**Example:**
- Row 1 left side (a-e): red
- Row 1 right side (f-j): blue
- Row 2 left side: green
- + power rail: orange
- - power rail: black

> "You just drew the invisible wiring diagram of your breadboard! Keep this map -- it is your cheat sheet for building circuits."

**Award: +20 XP for completing the breadboard map drawing!**

---

### Step 5: Build a Circuit the Right Way (10 min)

> "Now that you know how the breadboard works, let us build a circuit using PROPER technique."

**Circuit: Two LEDs, each with a resistor, sharing the same power source.**

```
  Breadboard layout:

  + rail: connected to 9V battery (+)
  - rail: connected to 9V battery (-)

  Row 5:  330-ohm resistor -- one leg in + rail, other leg in row 5 (column a)
  Row 5:  LED 1 long leg (+) in row 5 (column b)
  Row 7:  LED 1 short leg (-) in row 7 (column b)
  Row 7:  Jumper wire from row 7 (column a) to - rail

  Row 10: 330-ohm resistor -- one leg in + rail, other leg in row 10 (column a)
  Row 10: LED 2 long leg (+) in row 10 (column b)
  Row 12: LED 2 short leg (-) in row 12 (column b)
  Row 12: Jumper wire from row 12 (column a) to - rail
```

**Step-by-step build:**

1. Connect battery clip: red wire to + rail, black wire to - rail
2. Place first resistor: one leg in + rail, other leg in row 5
3. Place first LED: long leg in row 5 (same row as resistor -- they are connected!), short leg in row 7
4. Jumper wire: row 7 to - rail
5. Repeat for second LED in rows 10 and 12
6. Connect battery -- both LEDs should light up!

> "Each LED has its own row for the resistor connection. The resistor and the LED's long leg share a row -- so electricity flows from the resistor INTO the LED through the breadboard's secret tunnel!"

**Award: +30 XP for building the two-LED circuit correctly!**

---

### Step 6: Wand Check -- Verify Your Circuit! (5 min)

> "Before we celebrate, let us use the Wand to check our circuit."

**Verification 1 -- Continuity check (battery DISCONNECTED):**

Set Wand to continuity mode. Remove the battery.

1. Touch probes between + rail and row 5 column a (where resistor connects): BEEP! Good -- resistor leg is in the + rail.
2. Touch probes between row 5 column a and row 5 column b (LED long leg): BEEP! Good -- same row, connected.
3. Touch probes between row 7 column b and row 7 column a (LED short leg to jumper wire): BEEP! Good.

> "Every connection checked! Your circuit is wired correctly."

**Verification 2 -- Voltage check (battery CONNECTED):**

Set Wand to DC Volts. Connect the battery.

1. Measure across the + and - rails: should read about 9V.
2. Measure across an LED (red probe on long leg row, black probe on short leg row): should read about 2V (the LED's forward voltage).
3. Measure across a resistor: should read about 7V (9V minus 2V used by the LED).

> "The voltage across the resistor PLUS the voltage across the LED equals 9V! All the battery's push is accounted for. Nothing is wasted."

**Award: +30 XP for completing both Wand verifications!**

---

### Step 7: Common Breadboard Mistakes (3 min)

Show these mistakes and have the kid identify what is wrong:

**Mistake 1 -- Component across the gap:**
> "If you put a resistor so one leg is in column e and the other is in column f, the two legs are NOT connected to each other through the breadboard. The gap blocks them!"

**Mistake 2 -- Two components in different rows thinking they connect:**
> "If the resistor is in row 5 and the LED is in row 6, they are NOT connected. They need to share a row!"

**Mistake 3 -- Forgetting the return path:**
> "Every circuit needs a path back to the battery's minus terminal. If you forget the ground wire, the loop is broken."

**Mistake 4 -- Power rail break:**
> "On some boards, the power rail has a gap halfway. Use a jumper to bridge it!"

**Award: +10 XP for identifying at least 2 mistakes!**

---

## Quick Quiz -- Earn Bonus XP!

**Question 1:** On a breadboard, which holes are connected to each other?
- A) All holes in the same column (a1, a2, a3, etc.)
- B) All holes in the same row on the same side of the gap (a1-b1-c1-d1-e1)
- C) Every single hole is connected

**(Correct: B -- +20 XP!)**

**Question 2:** What does the center gap do?
- A) It makes the breadboard look cool
- B) It separates the left side from the right side -- no connection crosses the gap
- C) It connects the top and bottom power rails

**(Correct: B -- +20 XP!)**

**Question 3:** You plug a resistor into hole A5 and an LED into hole C5. Are they connected through the breadboard?
- A) Yes -- same row, same side of the gap
- B) No -- different columns means no connection
- C) Only if you add a jumper wire

**(Correct: A -- +20 XP!)**

---

## Lesson 9 Complete!

```
  =============================================

     BREADBOARD NAVIGATOR BADGE UNLOCKED!

     Skills unlocked:
     [check] Mapped all three breadboard zones
     [check] Proved connections with the Wand
     [check] Built a proper two-LED circuit
     [check] Verified circuit with continuity AND voltage
     [check] Know the 4 common breadboard mistakes

  =============================================
```

**XP Breakdown:**
| Activity | XP |
|----------|-----|
| Hook -- ready to explore | 10 |
| Label three zones | 20 |
| Wand Check -- 7 continuity tests | 50 |
| Draw the invisible map | 20 |
| Build two-LED circuit | 30 |
| Wand verify circuit | 30 |
| Identify breadboard mistakes | 10 |
| Quiz (3 questions) | 60 |
| **TOTAL POSSIBLE** | **230** |

---

## Coming Up Next...

In **Lesson 10**, we discover **Ohm's Law** -- the most important formula in all of electronics! You will learn to PREDICT what your Wand will read BEFORE you even touch the probes. It is like having the power to see the future!

---

## Troubleshooting

| Problem | Likely Cause | Fix |
|---------|-------------|-----|
| Wand does not beep on same-row test | Probe not firmly in hole | Press probe tip firmly into the hole |
| LED does not light up | LED reversed | Flip the LED (long leg = +) |
| LED does not light up | Components in wrong rows | Check that resistor and LED share a row |
| One LED works, the other does not | Bad connection | Use Wand continuity to trace each path |
| Power rail does not beep end-to-end | Power rail has a break | Add a jumper wire across the break |
| Wand beeps when it should not | Stray wire touching | Remove loose wires and retest |

---

## Parent/Instructor Notes

- This lesson is foundational. If the child does not understand the breadboard, every future circuit will be frustrating. Take extra time here if needed.
- The Wand continuity tests are the BEST way to teach breadboard connections. Let the child explore beyond the prescribed tests -- encourage them to test random pairs of holes and predict beep/no-beep before testing.
- For ages 6--8: Focus on the "hotel with secret tunnels" analogy. Skip the lettered columns (a-j) and just use "left side" and "right side" of the gap.
- For ages 9--12: Have them draw a complete connection diagram and predict all 7 Wand tests before measuring.
- Some breadboards have labels printed on them (row numbers, column letters). If yours does not, consider writing numbers on the side with a fine marker. This makes communication much easier.
- The two-LED circuit in Step 5 is a gentle preview of parallel circuits (Lesson 12). Do not explain it as parallel yet -- just let them see that two LEDs can share a power source.

# Lesson 11: Series Circuits -- The Single-Track Train

**Module:** 2 -- Building Simple Circuits
**Difficulty:** Star-2 Easy-Medium
**Session Time:** 45--50 minutes
**Age:** 6--12 years
**XP Available:** 220 XP

---

## Your Mission Today

Circuit Explorer, today you are going on a **voltage treasure hunt**! You will build a circuit where components are lined up one after another -- like train cars on a single track. Then you will use your Magic Measurement Wand to discover how the battery's voltage gets SPLIT between each component. Every volt will be accounted for -- nothing is lost, nothing appears from nowhere. This is series circuit magic!

---

## Learning Objectives

By the end of this lesson, you will be able to:
- Explain what a series circuit is and how it works
- Know that current is the SAME everywhere in a series circuit
- Measure voltage drops across each component with the Wand
- Prove that all voltage drops add up to the battery voltage (Kirchhoff's Voltage Law)
- Predict what happens when one component is removed

---

## What You Need

| Item | Qty |
|------|-----|
| 9V battery + clip | 1 |
| Breadboard | 1 |
| Resistors: 330-ohm, 470-ohm, 1k-ohm | 2 each |
| LEDs: red, green, yellow | 1 each |
| Jumper wires | 8 |
| Multimeter (Magic Measurement Wand) | 1 |
| Paper + pencil | 1 set |

---

## How to Teach This Lesson

### Step 1: Hook -- The Holiday Lights Mystery (5 min)

> "Have you ever had a string of old-fashioned holiday lights where ONE bulb burns out and the ENTIRE string goes dark? Every. Single. Light. Off. Why?"

Let the kid guess.

> "Those old lights were wired in SERIES -- one after another on a single track. If ONE breaks, the track is broken and electricity cannot get through to ANY of them."

> "Today you are going to build a series circuit, understand WHY one broken bulb kills them all, and use your Magic Measurement Wand to hunt for voltage at every stop along the track!"

**Award: +10 XP for guessing why the whole string goes dark!**

---

### Step 2: What Is a Series Circuit? (8 min)

**The Train Track Analogy:**

```
  SERIES CIRCUIT = A single-track railroad

  Battery
    |
    v
  [Component 1] --> [Component 2] --> [Component 3]
    ^                                       |
    |                                       v
    +----------- back to battery -----------+

  ONE path. ONE track. If any piece of track is missing, the train stops.
```

> "In a series circuit, electricity has only ONE path to follow. It goes through every component one at a time, like a train that must stop at every station."

**Key rules of series circuits:**

| Rule | Explanation |
|------|------------|
| **One path** | Electricity has only ONE route -- no shortcuts |
| **Same current everywhere** | The amount of electricity flowing is the same at every point |
| **Voltage gets split** | Each component "uses up" some of the battery's push |
| **Voltages add up** | All the voltage drops add up to the battery voltage |
| **Remove one = all stop** | Break the chain anywhere and current stops everywhere |

> "Think of the current like water in a single pipe. The same amount of water flows past every point. But the water PRESSURE drops at every obstacle it passes."

**Award: +10 XP for explaining the series circuit rules in your own words!**

---

### Step 3: Build a Series Circuit (10 min)

**Circuit 1 -- Two Resistors in Series:**

```
  Circuit diagram:

  9V (+) ---- [330-ohm R1] ---- [470-ohm R2] ---- 9V (-)

  On breadboard:
  1. Battery clip: red to + rail, black to - rail
  2. Jumper wire: + rail to row 5
  3. Resistor R1 (330 ohm): one leg in row 5, other leg in row 8
  4. Resistor R2 (470 ohm): one leg in row 8, other leg in row 11
  5. Jumper wire: row 11 to - rail
```

> "See how R1 and R2 share row 8? The output of R1 feeds directly into R2. One track, two stops."

**Award: +20 XP for building the two-resistor series circuit!**

---

### Step 4: Wand Check -- The Voltage Treasure Hunt! (12 min)

> "Now the fun part. We are going hunting for voltage! Your Wand is going to measure how much voltage each resistor 'uses up.' Ready?"

Set your Wand to **DC Volts** (20V range).

**Measurement 1 -- Total voltage (across the battery):**

Touch red probe to + rail, black probe to - rail.
> "This is the total push from the battery. Write it down!"

Expected: about 9V

**Measurement 2 -- Voltage across R1 (330 ohm):**

Touch red probe to the + side of R1 (row 5), black probe to the - side (row 8).
> "How much voltage did R1 use up?"

Expected: about 3.7V

**Measurement 3 -- Voltage across R2 (470 ohm):**

Touch red probe to the + side of R2 (row 8), black probe to the - side (row 11).
> "How much did R2 use?"

Expected: about 5.3V

**The Big Reveal:**

```
| Measurement | Wand Reads |
|------------|-----------|
| Battery voltage (total) | _____ V |
| Voltage across R1 (330 ohm) | _____ V |
| Voltage across R2 (470 ohm) | _____ V |
| R1 + R2 together | _____ V |
```

> "Add V_R1 + V_R2 together. What do you get?"

Expected: 3.7 + 5.3 = 9.0V -- the SAME as the battery!

> "EVERY volt from the battery is accounted for! The battery pushes 9 volts, and those 9 volts get shared between the two resistors. This rule has a fancy name: **Kirchhoff's Voltage Law** -- but you can call it the 'All Adds Up' rule."

**For ages 9--12 -- Verify with Ohm's Law:**

```
  Total resistance = R1 + R2 = 330 + 470 = 800 ohms
  Total current = V / R = 9 / 800 = 0.01125 A = 11.25 mA

  V_R1 = I x R1 = 0.01125 x 330 = 3.7V  (matches Wand!)
  V_R2 = I x R2 = 0.01125 x 470 = 5.3V  (matches Wand!)
```

> "The math predicted EXACTLY what the Wand measured. Ohm's Law and Kirchhoff's Law working together!"

**Award: +50 XP for completing the voltage treasure hunt!**

---

### Step 5: Three LEDs in Series (10 min)

**Circuit 2 -- Three LEDs in Series:**

```
  9V (+) ---- [330-ohm] ---- RED LED ---- GREEN LED ---- YELLOW LED ---- 9V (-)

  On breadboard:
  1. Jumper wire: + rail to row 3
  2. Resistor (330 ohm): row 3 to row 5
  3. Red LED: long leg row 5, short leg row 7
  4. Green LED: long leg row 7, short leg row 9
  5. Yellow LED: long leg row 9, short leg row 11
  6. Jumper wire: row 11 to - rail
```

> "All three LEDs are on the same track. Each one 'uses up' some voltage."

**Observation before measuring:**

> "Look at the LEDs. Are they as bright as when you had just one LED? They should be dimmer!"

> "Why? Because each LED uses about 2V. Three LEDs use about 6V. That leaves only 3V for the resistor -- less push means less current, which means dimmer LEDs."

**Wand Check -- Voltage across each LED:**

```
| Component | Wand Reads | Expected |
|-----------|-----------|---------|
| Resistor (330 ohm) | _____ V | about 2.5--3.5V |
| Red LED | _____ V | about 1.8--2.0V |
| Green LED | _____ V | about 2.0--2.2V |
| Yellow LED | _____ V | about 2.0--2.2V |
| TOTAL | _____ V | about 9V |
```

> "Does the total add up to 9V? It should! Every volt is accounted for."

**Award: +30 XP for building and measuring the three-LED series circuit!**

---

### Step 6: The Break Test (5 min)

> "Remember the holiday lights? Let us prove it."

**Remove the green LED from the circuit** (pull it out of the breadboard).

> "What happened to the red and yellow LEDs?"

They all go dark!

> "In a series circuit, removing ONE component breaks the entire chain. The current has nowhere to go."

**Wand proof:**

Set Wand to DC Volts. Measure across the gap where the green LED was.

> "The Wand reads about 9V across the gap! All the battery's push is 'stuck' at the break point, pushing against an open door that will not open."

> "Now put the green LED back. Everything lights up again!"

**Award: +20 XP for proving that removing one component kills the whole series chain!**

---

### Step 7: Series Resistors -- Adding Resistance (3 min)

One more important rule:

> "In a series circuit, resistances ADD UP."

```
  Series: R_total = R1 + R2 + R3 + ...

  Example: 330 ohm + 470 ohm + 1000 ohm = 1,800 ohms total
```

**Wand verification:**

1. Disconnect the battery
2. Remove everything except R1 (330 ohm) and R2 (470 ohm) in series
3. Measure resistance across BOTH resistors (probe on one end of R1, other probe on far end of R2)
4. Wand should read about 800 ohms (330 + 470)!

> "Your Wand just proved that series resistances add up!"

**Award: +20 XP for measuring total series resistance with the Wand!**

---

## Quick Quiz -- Earn Bonus XP!

**Question 1:** In a series circuit with a 9V battery, you measure 3V across R1 and 4V across an LED. How much voltage is across R2?
- A) 7V
- B) 2V
- C) 9V

**(Correct: B -- 9 - 3 - 4 = 2V -- +20 XP!)**

**Question 2:** You remove one LED from a series circuit with three LEDs. What happens to the other two?
- A) They get brighter
- B) They stay the same
- C) They go dark -- the circuit is broken

**(Correct: C -- +20 XP!)**

**Question 3:** Two resistors in series: 100 ohms and 200 ohms. What is the total resistance?
- A) 100 ohms
- B) 300 ohms
- C) 150 ohms

**(Correct: B -- +20 XP!)**

---

## Lesson 11 Complete!

```
  =============================================

     SERIES CIRCUIT SPECIALIST BADGE UNLOCKED!

     Skills unlocked:
     [check] Built series circuits with resistors and LEDs
     [check] Measured voltage drop across every component
     [check] Proved voltages add up to battery voltage
     [check] Verified series resistance adds up
     [check] Understand why one break kills the whole chain

  =============================================
```

**XP Breakdown:**
| Activity | XP |
|----------|-----|
| Hook -- holiday lights guess | 10 |
| Explain series rules | 10 |
| Build two-resistor series circuit | 20 |
| Voltage treasure hunt (3 measurements) | 50 |
| Three-LED series circuit | 30 |
| Break test | 20 |
| Series resistance verification | 20 |
| Quiz (3 questions) | 60 |
| **TOTAL POSSIBLE** | **220** |

---

## Coming Up Next...

In **Lesson 12**, we explore **parallel circuits** -- where electricity gets CHOICES! Instead of one track, there are multiple paths. You will discover that CURRENT splits in a parallel circuit, and you will use your Magic Measurement Wand in a brand-new way: measuring current like a real ammeter!

---

## Troubleshooting

| Problem | Likely Cause | Fix |
|---------|-------------|-----|
| LEDs do not light in series | Not enough voltage for all LEDs | With 9V, you can only run about 3 red LEDs in series (each uses 2V). 4 LEDs need 8V+ just for LEDs, leaving almost nothing for the resistor |
| Voltage readings do not add up to 9V | Battery is not fully charged | Measure the battery alone first; a tired battery reads less than 9V |
| Wand reads negative voltage | Probes are reversed | Swap red and black probes -- the sign will flip to positive |
| One LED is much dimmer than others | Different colored LEDs have different forward voltages | Blue/white LEDs use more voltage (3V+), leaving less for others in series |

---

## Parent/Instructor Notes

- The "voltage treasure hunt" is the highlight of this lesson. The moment the kid adds up the voltage drops and they equal the battery voltage is a genuine "wow" moment. Celebrate it!
- **Ages 6--8:** Focus on the hands-on: build it, measure it, see that numbers add up. Skip the Ohm's Law verification math. The key takeaway is "voltage gets shared" and "one break kills everything."
- **Ages 9--12:** Have them predict BEFORE measuring. Use Ohm's Law from Lesson 10 to calculate expected voltages, then compare to Wand readings. This builds the predict-measure-compare loop that is the foundation of scientific thinking.
- The series resistance verification (Step 7) is quick but powerful. Measuring two resistors in series and seeing the number is their sum is very satisfying.
- Kirchhoff's Voltage Law is introduced by name, but the "All Adds Up" nickname makes it memorable for younger kids.
- Common confusion: kids may think voltage is "used up" and disappears. Clarify that it is converted to other forms of energy (light in LEDs, heat in resistors). The total energy is always conserved.

---

## Navigation

| | |
|:---|---:|
| [← Lesson 10: Ohm's Law -- The Superpower Formula](lesson-10-ohms-law.md) | [Lesson 12: Parallel Circuits -- Multiple Paths, Shared Voltage →](lesson-12-parallel-circuits.md) |

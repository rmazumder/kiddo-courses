# Lesson 15: Power Sources -- Batteries, Volts, and Energy

**Module:** 2 -- Building Simple Circuits
**Difficulty:** Star-2 Easy-Medium
**Session Time:** 45--50 minutes
**Age:** 6--12 years
**XP Available:** 210 XP

---

## Your Mission Today

Circuit Explorer, every circuit needs POWER. You have been using a 9V battery this whole time, but did you know there are dozens of different battery types? Today you are going to build a **Battery Lab** -- testing every type of battery you can find with your Magic Measurement Wand! You will also discover two amazing tricks: wiring batteries in SERIES to get more voltage, and in PARALLEL to get more capacity. Let us power up!

---

## Learning Objectives

By the end of this lesson, you will be able to:
- Name common battery types and their voltages (9V, AA, AAA, coin cell)
- Measure the voltage of any battery using the Wand
- Test whether a battery is fresh or dying
- Wire batteries in series (voltages ADD up)
- Wire batteries in parallel (capacity adds up, voltage stays the same)
- Understand basic battery safety

---

## What You Need

| Item | Qty |
|------|-----|
| 9V battery (fresh) | 2 |
| 9V battery (old/used, if available) | 1 |
| AA batteries (1.5V, fresh) | 4 |
| AAA battery (1.5V) | 2 |
| CR2032 coin cell battery (3V) | 2 |
| 9V battery clip | 1 |
| AA battery holder (2-cell or 4-cell) | 1 |
| Breadboard | 1 |
| LEDs (red, green) | 2 |
| 330-ohm resistors | 2 |
| Jumper wires | 8 |
| Alligator clip wires | 4 |
| Multimeter (Magic Measurement Wand) | 1 |
| Paper + pencil | 1 set |

---

## How to Teach This Lesson

### Step 1: Hook -- The Battery Museum (5 min)

Lay out every battery you have on the table. Make it look like a museum exhibit.

> "Welcome to the Battery Museum! Every single one of these stores ELECTRICITY inside a chemical reaction. Some are tiny. Some are big. Some push hard (high voltage). Some push gently (low voltage). But they ALL have the same job: to push electrons around a circuit."

> "Here is a challenge: WITHOUT looking at any labels, can you guess which battery pushes the HARDEST? Which has the most voltage?"

Let the kid guess. They might think the biggest battery has the most voltage -- but the tiny 9V battery actually pushes harder than the big AA battery!

> "Size does NOT equal voltage! A 9V battery is SMALLER than a AA battery, but it pushes 6 times harder. Let us prove it with your Wand."

**Award: +10 XP for guessing which battery has the most voltage!**

---

### Step 2: The Battery Lab -- Measure Everything! (10 min)

![A "Battery Museum" display with four batteries on individual pedestals under spotlights, arranged like exhibits in a museum gallery. Pedestal 1: a 9V battery (tall rectangle with snap connector on top), placard reads "9V - The Powerhouse, great for our projects." Pedestal 2: an AA battery (cylinder), placard reads "AA - 1.5V, the everyday hero." Pedestal 3: an AAA battery (thinner cylinder), placard reads "AAA - 1.5V, slim and light." Pedestal 4: a coin cell battery (small disc), placard reads "CR2032 - 3V, tiny but mighty!" Each battery has a red/orange "+" label on its positive terminal and a green "-" on its negative terminal. Size comparison lines show relative heights. A cartoon museum guide robot holds a pointer and stands beside the exhibits. A velvet rope lines the display. A banner at the top reads "The Battery Museum."](images/lesson-15-battery-museum.png)

> "Set your Wand to DC Volts, 20V range. Let us test every battery in the museum!"

**How to measure any battery:**

1. Touch RED probe to the **+** terminal
2. Touch BLACK probe to the **-** terminal
3. Read the voltage!

**For a 9V battery:** The + terminal is the smaller round snap. The - terminal is the larger round snap.

**For AA/AAA:** The + is the bump on top. The - is the flat bottom.

**For a coin cell (CR2032):** The + is the flat face with writing. The - is the smooth bottom.

**Battery Lab Data Sheet:**

```
| Battery Type | Rated Voltage | Wand Reads | Fresh or Tired? | Notes |
|-------------|--------------|-----------|----------------|-------|
| 9V (new)    | 9.0V         |           |                |       |
| 9V (old)    | 9.0V         |           |                |       |
| AA (new)    | 1.5V         |           |                |       |
| AAA         | 1.5V         |           |                |       |
| CR2032      | 3.0V         |           |                |       |
```

**How to tell if a battery is fresh or tired:**

```
| Battery Type | Fresh (Good) | Getting Tired | Dead |
|-------------|-------------|--------------|------|
| 9V          | 9.0--9.6V   | 7.0--8.9V    | Under 7V |
| AA / AAA    | 1.5--1.6V   | 1.2--1.4V    | Under 1.1V |
| CR2032      | 3.0--3.3V   | 2.5--2.9V    | Under 2.5V |
```

> "Your Wand just became a battery tester! Any time someone asks 'Is this battery dead?', you can answer in seconds."

**Fun activity:** Have the kid go around the house, find old batteries from remotes and toys, and test them all!

**Award: +30 XP for measuring all batteries and filling in the data sheet!**

---

### Step 3: What Is Inside a Battery? (5 min)

> "A battery is like a tiny chemical factory. Inside, chemicals react with each other. That reaction pushes electrons from the - terminal to the + terminal. When you connect a circuit, the electrons flow through the circuit, doing work (like lighting LEDs), and then return to the battery."

```
  Inside a battery:

  +-----------------------------------+
  |                                   |
  |   Chemical A  |  Chemical B       |
  |   (anode)     |  (cathode)        |
  |               |                   |
  |   Reaction pushes electrons -->   |
  |                                   |
  +----(-) terminal-----(+) terminal--+
```

**Battery vocabulary:**

| Word | Kid-Friendly Definition |
|------|------------------------|
| **Voltage** | How hard the battery pushes (more voltage = stronger push) |
| **Capacity (mAh)** | How LONG the battery can push before it runs out |
| **mAh** | Milliamp-hours -- like "fuel tank size" for batteries |

> "A 9V battery pushes HARDER than a AA, but a AA has MORE capacity (it lasts longer). A 9V battery is like a strong sprinter. A AA battery is like a steady marathon runner."

```
| Battery | Voltage | Typical Capacity |
|---------|---------|-----------------|
| 9V      | 9V      | about 500 mAh (sprinter) |
| AA      | 1.5V    | about 2500 mAh (marathon runner) |
| AAA     | 1.5V    | about 1000 mAh (jogger) |
| CR2032  | 3V      | about 225 mAh (short walk) |
```

**Award: +10 XP for understanding the difference between voltage and capacity!**

---

### Step 4: Batteries in Series -- Voltage Stacking! (10 min)

![A two-panel comparison of battery wiring configurations. Left panel labeled "Series (End to End)": four AA batteries connected positive-to-negative in a chain (visually stacked end to end like a train), with red/orange and green terminals alternating. A voltmeter at the end reads "6V" and the label explains "1.5V + 1.5V + 1.5V + 1.5V = 6V. More voltage!" The water analogy shows four pumps stacked for higher pressure. Right panel labeled "Parallel (Side by Side)": four AA batteries placed side by side with all positives connected together (red/orange bus bar) and all negatives connected together (green bus bar). A voltmeter reads "1.5V" and the label explains "Still 1.5V but lasts 4x longer! More capacity!" The water analogy shows four tanks combined for more water volume at the same pressure. A cartoon kid scratches their head on the series side ("More push!") and nods on the parallel side ("Lasts longer!"). A summary banner reads: "Series = more voltage. Parallel = more battery life."](images/lesson-15-series-vs-parallel-batteries.png)

> "What if 1.5V is not enough? What if you need MORE voltage? Stack batteries in SERIES -- their voltages ADD UP!"

**How series batteries work:**

```
  Series = end to end (+ of one connects to - of next)

  [AA1: 1.5V] --> [AA2: 1.5V] --> [AA3: 1.5V] --> [AA4: 1.5V]
   +     -          +     -          +     -          +     -

  Total voltage = 1.5 + 1.5 + 1.5 + 1.5 = 6V!
```

> "This is EXACTLY how battery holders work! A 4-AA battery holder connects 4 batteries in series to make 6V. That is how many toys and flashlights work."

**Build it:**

If you have a battery holder:
1. Insert 2 AA batteries into the holder (correct polarity!)
2. Measure the output with the Wand

If you do not have a holder, use alligator clips:
1. Clip the + of AA1 to the - of AA2
2. Measure from the - of AA1 to the + of AA2

**Wand Check -- Series batteries:**

```
| Configuration | Predicted Voltage | Wand Reads |
|--------------|------------------|-----------|
| 1 AA battery | 1.5V | _____ V |
| 2 AA in series | 3.0V | _____ V |
| 3 AA in series | 4.5V | _____ V |
| 4 AA in series | 6.0V | _____ V |
```

> "Each battery adds its voltage. 4 batteries in series = 4 times the voltage! The voltages STACK."

**Experiment -- Power an LED from AA batteries:**

> "Can one AA battery (1.5V) light a red LED? Let us try!"

1. Connect 1 AA to a 100-ohm resistor and a red LED. Very dim or off (1.5V is barely enough for a red LED).
2. Connect 2 AA in series (3V). LED lights up!
3. Connect 4 AA in series (6V). LED is BRIGHT!

> "This is why most battery-powered gadgets use multiple batteries -- one is often not enough."

**Award: +30 XP for measuring batteries in series and lighting the LED!**

---

### Step 5: Batteries in Parallel -- Bigger Fuel Tank! (8 min)

> "What if you have ENOUGH voltage but want the battery to LAST LONGER? Wire them in PARALLEL!"

**How parallel batteries work:**

```
  Parallel = side by side (+ connects to +, - connects to -)

  [AA1: 1.5V] ---+--- (+)
  [AA2: 1.5V] ---+       Output: 1.5V
  [AA3: 1.5V] ---+       BUT capacity = 2500 + 2500 + 2500 = 7500 mAh!
                  |
  [AA1: 1.5V] ---+--- (-)
  [AA2: 1.5V] ---+
  [AA3: 1.5V] ---+
```

> "Voltage stays the SAME (1.5V). But capacity TRIPLES! The batteries share the load -- each one does less work, so they all last longer."

**IMPORTANT SAFETY RULE:**

> "Only put batteries in PARALLEL if they are the SAME type and close to the SAME charge level. Mixing old and new batteries in parallel can cause the new battery to try to charge the old one -- that makes heat and is not safe!"

**Wand Check -- Parallel batteries:**

Connect 2 AA batteries in parallel (alligator clips: + to +, - to -).

```
| Configuration | Predicted Voltage | Wand Reads |
|--------------|------------------|-----------|
| 1 AA battery | 1.5V | _____ V |
| 2 AA in parallel | 1.5V (same!) | _____ V |
```

> "See? The voltage did NOT change! Parallel does not stack voltage -- it stacks capacity. The batteries will last twice as long."

**Award: +20 XP for measuring parallel batteries and proving voltage stays the same!**

---

### Step 6: The 9V Battery Secret (3 min)

> "Here is a cool secret about the 9V battery. What do you think is INSIDE it?"

Show a picture (or if you have a dead 9V battery to carefully open):

```
  Inside a 9V battery:

  +-------+
  | AAAA  |
  | AAAA  |  <-- 6 tiny cells, each 1.5V
  | AAAA  |
  | AAAA  |  1.5 x 6 = 9V!
  | AAAA  |
  | AAAA  |
  +-------+
```

> "A 9V battery is really 6 tiny batteries wired IN SERIES inside a metal can! 6 x 1.5V = 9V. Now you know the secret!"

**Award: +10 XP for understanding the 9V battery secret!**

---

### Step 7: Battery Safety Rules (3 min)

> "Batteries are safe when used correctly. Here are the rules:"

```
  BATTERY SAFETY RULES
  ====================

  1. Never short-circuit a battery (connect + directly to -)
     -- it gets HOT and can leak or burst

  2. Never put batteries in fire
     -- they can explode

  3. Always check polarity before inserting batteries

  4. Remove batteries from devices you will not use for a long time
     -- they can leak and damage the device

  5. Do not mix old and new batteries in series
     -- the old one works too hard and can leak

  6. Dispose of dead batteries properly
     -- many stores have battery recycling bins

  7. If a battery feels hot, smells, or is swelling -- stop using it!
     -- tell an adult immediately
```

**Award: +10 XP for reciting at least 3 safety rules!**

---

## Quick Quiz -- Earn Bonus XP!

**Question 1:** A fresh AA battery measures about:
- A) 9 Volts
- B) 3 Volts
- C) 1.5 Volts

**(Correct: C -- +20 XP!)**

**Question 2:** You wire 3 AA batteries in series. What is the total voltage?
- A) 1.5V (same as one)
- B) 4.5V (1.5 x 3)
- C) 0.5V (1.5 divided by 3)

**(Correct: B -- +20 XP!)**

**Question 3:** You wire 2 identical batteries in parallel. What happens?
- A) Voltage doubles, capacity stays the same
- B) Voltage stays the same, capacity doubles
- C) Both voltage and capacity double

**(Correct: B -- +20 XP!)**

**Bonus question for older kids (10+):**
> "A 9V battery has about 500 mAh of capacity. Your circuit draws 20 mA. About how long will the battery last?"
>
> Time = Capacity / Current = 500 mAh / 20 mA = 25 hours

**(Correct: +30 XP bonus!)**

---

## Lesson 15 Complete!

```
  =============================================

     POWER SOURCE EXPERT BADGE UNLOCKED!

     Skills unlocked:
     [check] Measured all common battery types
     [check] Tested batteries for freshness
     [check] Wired batteries in series (voltage stacking)
     [check] Wired batteries in parallel (capacity stacking)
     [check] Know battery safety rules
     [check] Discovered the 9V battery secret

  =============================================
```

**XP Breakdown:**
| Activity | XP |
|----------|-----|
| Hook -- guess the strongest battery | 10 |
| Battery Lab data sheet (all batteries) | 30 |
| Voltage vs capacity understanding | 10 |
| Series batteries + LED experiment | 30 |
| Parallel batteries measurement | 20 |
| 9V battery secret | 10 |
| Battery safety rules | 10 |
| Quiz (3 questions) | 60 |
| Bonus question | 30 |
| **TOTAL POSSIBLE** | **210** |

---

## Coming Up Next...

In **Lesson 16**, it is the **Grand Finale of Module 2** -- you are going to build a working **LIGHTHOUSE** with a blinking LED! You will use EVERYTHING you have learned: breadboarding, Ohm's Law, series and parallel circuits, voltage dividers, power sources, and your Magic Measurement Wand to debug the entire project. This is going to be EPIC!

---

## Troubleshooting

| Problem | Likely Cause | Fix |
|---------|-------------|-----|
| Wand reads 0V on a battery | Probes not touching terminals | Press probe tips firmly against battery terminals |
| Wand reads negative voltage on battery | Probes reversed | Red probe on +, black probe on - |
| Series batteries give wrong total voltage | One battery is dead or reversed | Measure each battery individually; check all are oriented correctly |
| LED does not light from 2 AA batteries | LED or resistor connection issue | Check breadboard connections and LED polarity |
| Battery gets hot when connected | Short circuit | DISCONNECT IMMEDIATELY. Check for bare wires touching |
| Parallel batteries measure slightly different voltage | Batteries are at different charge levels | Use batteries of the same brand and age for parallel connections |

---

## Parent/Instructor Notes

- **Ages 6--8:** Focus on the Battery Museum and the series stacking experiment. The "count the batteries and multiply by 1.5" pattern is easy and fun. Skip the capacity/mAh concept -- just say "bigger batteries last longer."
- **Ages 9--12:** The capacity concept (mAh) and the bonus question (time = capacity / current) introduce practical engineering thinking. Encourage them to calculate how long their project circuits will run on different batteries.
- **The 9V battery teardown** is fascinating if you have a dead 9V battery. Carefully prying one open with pliers (adult only) to reveal the 6 tiny cells inside is a memorable demo. Only do this with fully dead batteries.
- **Parallel battery safety** is important. Emphasize that parallel batteries must be the same type and similar charge level. In practice, for this course, series connections are more useful and safer.
- The Battery Lab activity is a great excuse to go around the house and test every battery. Kids love finding dead batteries and reporting their findings.
- This lesson sets up the project lesson (Lesson 16) by ensuring kids understand how to choose and configure power sources.

---

## Navigation

| | |
|:---|---:|
| [← Lesson 14: Using a Multimeter -- The Deep Dive](lesson-14-using-a-multimeter.md) | [Lesson 16: Project -- The Lighthouse Circuit →](lesson-16-project-lighthouse-circuit.md) |

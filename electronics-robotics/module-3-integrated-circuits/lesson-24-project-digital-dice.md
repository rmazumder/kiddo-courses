# Lesson 24: Module 3 Project -- Digital Dice

**Module:** 3 -- Integrated Circuits (ICs) (FINAL PROJECT)
**Difficulty:** Star-3 Intermediate
**Session Time:** 60--75 minutes (longer -- it is a project!)
**Age:** 6--12 years
**XP Available:** 500 XP (the biggest XP haul of the module!)

---

## Your Mission Today

This is it, Circuit Explorer -- the **GRAND FINALE of Module 3**! You are going to build a real, working **Electronic Dice**. Press a button to "roll" and a random number from 1 to 6 will appear, shown by LEDs arranged in a dice pattern. You will use the 555 timer, the 4017 counter, logic to drive the LED patterns, and your Wand to debug it all. When you are done, you will have a game you can actually play! Let us build this!

---

## Learning Objectives

This project brings together everything from Module 3:
- 555 timer in astable mode (fast clock)
- 4017 decade counter (counting pulses)
- LED wiring and patterns
- Push button control
- Multimeter skills for debugging

---

## What You Need

| Item | Qty |
|------|-----|
| 555 timer IC | 1 |
| 4017 decade counter IC | 1 |
| LEDs (same color, preferably) | 7 |
| 330-ohm resistors | 7 |
| Resistor: 1k-ohm (R1 for 555) | 1 |
| Resistor: 10k-ohm (R2 for 555) | 1 |
| Ceramic capacitor: 0.01 microfarad (C1 for fast 555) | 1 |
| Ceramic capacitor: 0.01 microfarad (noise filter for Pin 5) | 1 |
| 1N4148 diodes (for LED pattern logic) | 6 |
| Push button (tactile switch) | 1 |
| 10k-ohm resistor (pull-up for button) | 1 |
| 9V battery + clip | 1 |
| Breadboard (830-point recommended) | 1 |
| Jumper wires | 30 |
| Multimeter (Magic Measurement Wand!) | 1 |
| Cardboard or foam board (for dice face) | 1 piece |

---

## How the Digital Dice Works

### The Big Idea

> "When you roll a real die, it tumbles randomly and lands on a number from 1 to 6. Our electronic dice does something similar -- the 555 timer runs at a VERY fast speed (thousands of times per second). The 4017 counter cycles through outputs 0, 1, 2, 3, 4, 5 so quickly that no human can tell which output is active. When you release the button, the counter stops on whichever output happens to be HIGH at that instant -- essentially a random number from 1 to 6!"

**Block diagram:**

```
  Button Press
      |
      v
  555 Timer ------> 4017 Counter ------> LED Pattern Logic ------> 7 LEDs
  (fast clock)      (cycles 1-6)          (which LEDs to             (dice face)
                    (resets at 7)          turn on for each
                                           number)
```

---

## How to Build It

### Phase 1: Plan the Dice Face (5 min)

**Standard dice LED layout:**

```
  +---+---+---+
  | A |   | B |
  +---+---+---+
  | C | G | D |
  +---+---+---+
  | E |   | F |
  +---+---+---+

  Number 1: G only
  Number 2: B, E
  Number 3: B, G, E
  Number 4: A, B, E, F
  Number 5: A, B, G, E, F
  Number 6: A, B, C, D, E, F
```

**LED assignment table:**

```
| Dice Number | LEDs On          | 4017 Output Used |
|-------------|-----------------|-----------------|
| 1           | G               | Q0 (Pin 3)      |
| 2           | B, E            | Q1 (Pin 2)      |
| 3           | B, G, E         | Q2 (Pin 4)      |
| 4           | A, B, E, F      | Q3 (Pin 7)      |
| 5           | A, B, G, E, F   | Q4 (Pin 10)     |
| 6           | A, B, C, D, E, F| Q5 (Pin 1)      |
```

**Award: +20 XP for planning the dice face layout!**

---

### Phase 2: Build the Fast 555 Clock (10 min)

> "We need the 555 to run very fast -- so fast that the counter cycles through all 6 positions hundreds of times per second. When you release the button, it stops on a random number."

**555 Astable Circuit (fast mode):**

```
  R1 = 1k-ohm
  R2 = 10k-ohm
  C1 = 0.01 microfarad (very small = very fast!)

  Frequency = 1.44 / ((1000 + 20000) x 0.00000001)
            = 1.44 / 0.00021
            = about 6,857 Hz (way too fast to see!)
```

Wire the 555 astable circuit exactly as in Lesson 18, but with C1 = 0.01 microfarad.

**Button control:** Connect the push button so that:
- When pressed: the 555 Reset (Pin 4) connects to +VCC (555 runs)
- When released: Pin 4 connects to GND through a 10k pull-down (555 stops)

```
  +VCC ---- push button ---- Pin 4 (Reset)
                              |
                             [10k]
                              |
                             GND
```

> "Press and hold the button -- the 555 runs and the counter spins. Release -- everything stops on a random number!"

**Award: +30 XP for building the fast 555 clock with button control!**

---

### Phase 3: Wire the 4017 Counter (Limited to 6) (10 min)

Wire the 4017 the same way as Lesson 23, but with one important change:

> "We only need numbers 1 through 6, not 0 through 9. So we connect the Q6 output (Pin 5) to the Reset pin (Pin 15). This makes the counter loop back to Q0 after reaching Q5 -- six outputs only!"

**4017 wiring:**
1. Pin 16 (VCC) to + rail
2. Pin 8 (GND) to - rail
3. Pin 14 (Clock) to 555 Pin 3 (Output)
4. Pin 13 (Clock Enable) to - rail
5. **Pin 5 (Q6) to Pin 15 (Reset)** -- this limits counting to 0-5 (six positions)

**Award: +20 XP for wiring the 4017 with the 6-count reset!**

---

### Phase 4: Wire the LED Dice Pattern (15 min)

> "This is the trickiest part. Each 4017 output needs to turn on the RIGHT combination of LEDs for that dice number."

**The wiring trick using diodes:**

Since multiple 4017 outputs need to control the same LED (for example, LED G turns on for numbers 1, 3, and 5), we use **1N4148 signal diodes** to combine signals without them interfering with each other.

**Simplified approach (recommended for younger builders):**

For a simpler build, you can use 6 separate groups of LEDs, each pre-wired to show the correct dice face. Each 4017 output directly drives its own set of LEDs through resistors.

```
  4017 Q0 (Pin 3)  --> [330R] --> LED G
  4017 Q1 (Pin 2)  --> [330R] --> LED B and LED E
  4017 Q2 (Pin 4)  --> [330R] --> LED B, LED G, and LED E (via diodes)
  4017 Q3 (Pin 7)  --> [330R] --> LED A, LED B, LED E, LED F (via diodes)
  4017 Q4 (Pin 10) --> [330R] --> LED A, LED B, LED G, LED E, LED F (via diodes)
  4017 Q5 (Pin 1)  --> [330R] --> LED A, LED B, LED C, LED D, LED E, LED F (via diodes)
```

**For each shared LED, connect a diode from each 4017 output that should activate it:**

Example for LED G (center dot -- used in numbers 1, 3, 5):
```
  Q0 (Pin 3)  ---[diode]--->+
  Q2 (Pin 4)  ---[diode]--->+--[330R]---LED G---GND
  Q4 (Pin 10) ---[diode]--->+
```

The diode prevents current from flowing backwards between outputs.

> "Take your time with this step. It is like solving a puzzle -- connecting the right wires to the right LEDs."

**Test each number:** Temporarily slow down the 555 (swap C1 for 47 microfarad) so the counter steps slowly. Watch each dice pattern appear one by one.

**Award: +50 XP for wiring the complete LED dice pattern!**

---

### Phase 5: Wand Check -- Debug and Verify! (10 min)

> "The moment of truth! If something is not quite right, your Magic Measurement Wand will find the problem."

**Debugging checklist:**

**1. Check the 555 clock:**
- Set Wand to DC Voltage
- Touch Pin 3 of the 555 while holding the button
- If the 555 is running fast, the Wand will show a voltage around 4-5V (it is averaging the rapid HIGH/LOW switching)

**2. Check the 4017 outputs:**
- Slow down the 555 (use bigger C1 temporarily)
- Measure each 4017 output -- only one should be HIGH at a time
- Verify that counting stops at Q5 (not continuing to Q6-Q9)

```
| 4017 Output | Pin | Should be HIGH for dice # | Wand reads HIGH? |
|-------------|-----|--------------------------|-----------------|
| Q0          | 3   | 1                        |                 |
| Q1          | 2   | 2                        |                 |
| Q2          | 4   | 3                        |                 |
| Q3          | 7   | 4                        |                 |
| Q4          | 10  | 5                        |                 |
| Q5          | 1   | 6                        |                 |
```

**3. Check each LED pattern:**
- For each counter position, verify the correct LEDs are on
- Use continuity mode to check diode connections if an LED is not lighting

**4. Battery check:**
- Measure battery voltage -- below 7V means time for a new battery

**Award: +50 XP for completing the debugging checklist!**

---

### Phase 6: Build the Dice Housing (10 min)

> "Let us make it look like a real die!"

**Using cardboard or foam board:**

1. Cut out a square piece (about 4 inches by 4 inches)
2. Poke 7 holes in the dice dot pattern:

```
  +---+---+---+
  | o |   | o |     A       B
  +---+---+---+
  | o | o | o |     C   G   D
  +---+---+---+
  | o |   | o |     E       F
  +---+---+---+
```

3. Push the 7 LEDs through the holes from behind
4. Label the back with letters (A-G) to keep track
5. Wire the LEDs to the breadboard circuit

> "Now when you press the button and release, the dice face lights up with your roll!"

**Award: +30 XP for building the dice housing!**

---

### Phase 7: Play the Dice Game! (5 min)

**How to play:**

1. Press and hold the button for at least 1 second (the counter spins)
2. Release the button -- a random number appears!
3. Take turns with a friend. Keep score!

**Game ideas:**
- Simple: highest number wins each round
- Racing game: both players roll, highest number moves that many spaces on a game board
- Dice addition: roll twice, add the numbers. Closest to 7 wins!

**Award: +30 XP for playing at least 5 rounds of the dice game!**

---

## Module 3 Final Assessment

After building the dice, have the kid answer these (no looking at notes!):

**Concept Check:**
1. "What does IC stand for?"
2. "How do you find Pin 1 on an IC?"
3. "What is the difference between astable and monostable mode on the 555?"
4. "Draw the truth table for an AND gate."
5. "What does the 4017 decade counter do?"
6. "How does the digital dice pick a random number?"

**Wand Skills Check:**
> "Measure the battery voltage for me."
> "Check if this LED is working using continuity mode."
> "Measure the voltage on Pin 8 of the 555."

**Award: +50 XP for completing the final assessment!**

---

## Quick Quiz -- Earn Bonus XP!

**Question 1:** Why does the digital dice produce a random number?
- A) The battery decides the number
- B) The 555 runs so fast that the counter position when you release the button is unpredictable
- C) The LEDs pick a random color

**(Correct: B -- +20 XP!)**

**Question 2:** Why do we connect Q6 (Pin 5) of the 4017 to the Reset pin?
- A) To make it count to 10
- B) To limit the count to 6 positions (numbers 1--6)
- C) To make it count backwards

**(Correct: B -- +20 XP!)**

**Question 3:** Why do we use diodes when connecting multiple 4017 outputs to the same LED?
- A) To make the LED brighter
- B) To prevent current from flowing backwards between outputs
- C) To slow down the circuit

**(Correct: B -- +20 XP!)**

---

## Module 3 Complete -- Grand Finale!

```
  ======================================================

     MODULE 3 CHAMPION BADGE UNLOCKED!

     _____________________ has mastered
        Integrated Circuits (ICs)

     [check] What an IC is and how to read datasheets
     [check] 555 Timer in Astable (Blinker) Mode
     [check] 555 Timer in Monostable (One-Shot) Mode
     [check] Logic Gates: AND, OR, NOT
     [check] Logic Gates: NAND, NOR, XOR
     [check] 7-Segment Display with Decoder
     [check] 4017 Decade Counter (LED Chaser)
     [check] Built the Digital Dice!

  ======================================================
```

**Lesson 24 XP Breakdown:**
| Activity | XP |
|----------|-----|
| Plan dice face layout | 20 |
| Build fast 555 clock | 30 |
| Wire 4017 with 6-count reset | 20 |
| Wire LED dice pattern | 50 |
| Wand Check debugging | 50 |
| Build dice housing | 30 |
| Play the dice game | 30 |
| Final assessment | 50 |
| Quiz (3 questions) | 60 |
| **TOTAL POSSIBLE** | **340** |

---

## Module 3 Total XP Summary

| Lesson | Title | Max XP |
|--------|-------|--------|
| 17 | What is an Integrated Circuit? | 220 |
| 18 | 555 Timer -- Blinker Mode | 200 |
| 19 | 555 Timer -- One-Shot Mode | 200 |
| 20 | Logic Gates -- AND, OR, NOT | 220 |
| 21 | Logic Gates -- NAND, NOR, XOR | 210 |
| 22 | 7-Segment Display | 200 |
| 23 | Building a Simple Counter | 230 |
| 24 | Digital Dice Project | 340 |
| **MODULE TOTAL** | | **1,820** |

**XP Ranks for Module 3:**
- 0--500 XP: IC Apprentice
- 501--900 XP: IC Explorer
- 901--1,300 XP: IC Builder
- 1,301--1,600 XP: IC Engineer
- 1,601--1,820 XP: IC Champion!

---

## All Badges Earned in Module 3

| Badge | Lesson |
|-------|--------|
| Chip Detective | 17 |
| Blink Master | 18 |
| One-Shot Wizard | 19 |
| Logic Explorer | 20 |
| Gate Master | 21 |
| Digit Decoder | 22 |
| Light Chaser Champion | 23 |
| Module 3 Champion | 24 |

---

## Reflection Questions (Talk Through Together)

> "What was the coolest circuit you built in this module?"
> "Which IC was your favorite to work with?"
> "Was there a moment where the Wand helped you find a problem?"
> "What do you think Module 4 will be about?"
> "If you could build anything with ICs, what would it be?"

---

## What's Next -- Module 4 Preview

> "You have mastered individual components, learned to build circuits, and now you can work with integrated circuits! In Module 4, we are moving into the world of PROGRAMMABLE electronics. You will meet the **Arduino** -- a tiny computer you can program to do anything. Write code, upload it, and watch your circuit come alive with your own instructions. It is like giving your circuits a brain!"

---

## Parent/Instructor Notes

- This project takes longer than a regular lesson -- plan for 60--75 minutes or split across two sessions.
- The LED pattern wiring with diodes is the most complex part. For younger kids (6--8), consider pre-wiring the diode matrix or simplifying to separate LED groups per number.
- The digital dice is a **great keepsake** and a fun game for the whole family.
- Debugging with the multimeter is extremely valuable here. Let the child work through problems rather than fixing them.
- If the dice seems to favor certain numbers, that is because the 555 frequency and the button release timing can create patterns. This is a great teachable moment about true randomness vs. pseudo-randomness!
- Consider having the child demonstrate the dice to friends or family and explain how it works -- teaching solidifies learning.
- Track XP totals across all 8 lessons on a poster or whiteboard. Celebrate reaching IC Champion rank!

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| Dice always shows the same number | 555 might not be running -- check Pin 4 button connection |
| LEDs show wrong patterns | Check diode connections and make sure each LED is wired to the correct 4017 outputs |
| Counter goes past 6 | Verify Q6 (Pin 5) is connected to Reset (Pin 15) on the 4017 |
| Some LEDs do not light | Check LED polarity and that the 330-ohm resistor is in place |
| Button does nothing | Test button with Wand continuity; check Pin 4 pull-down resistor |
| All LEDs are on at once | Diodes may be backwards -- check diode polarity (stripe = cathode = negative) |
| Circuit stops working after a while | Battery dying -- measure with Wand (should be above 7V) |

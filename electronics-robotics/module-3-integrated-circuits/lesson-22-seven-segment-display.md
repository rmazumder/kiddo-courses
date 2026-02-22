# Lesson 22: IC 7-Segment Display

**Module:** 3 -- Integrated Circuits (ICs)
**Difficulty:** Star-3 Intermediate
**Session Time:** 45--50 minutes
**Age:** 6--12 years
**XP Available:** 300 XP

---

## Your Mission Today

You have seen digital numbers everywhere -- alarm clocks, microwaves, scoreboards, elevator displays. Those glowing numbers are made from something called a **7-segment display**. Today you will learn how these displays work, wire one up by hand to show any digit you want, and then use a special decoder IC that does all the hard work for you!

---

## Learning Objectives

By the end of this lesson, you will be able to:
- Explain how a 7-segment display works (7 LEDs arranged to form digits)
- Identify segments a through g and know which ones light up for each digit
- Wire a 7-segment display manually to show a number
- Use a 7447 BCD-to-7-segment decoder IC to display digits 0--9
- Use your Magic Measurement Wand to measure which segments are active

---

## What You Need

| Item | Qty |
|------|-----|
| Common-anode 7-segment display | 1 |
| 7447 BCD-to-7-segment decoder IC | 1 |
| 330-ohm resistors | 7 |
| Push buttons or DIP switch (4 switches) | 4 |
| 10k-ohm resistors (pull-down for switches) | 4 |
| 9V battery + clip (or 5V power supply) | 1 |
| Breadboard | 1 |
| Jumper wires | 20 |
| Multimeter (Magic Measurement Wand!) | 1 |

---

## How to Teach This Lesson

### Step 1: Hook -- Numbers Are Everywhere! (5 min)

> "Look at the clock on your microwave. See those glowing numbers? Each digit is not a screen like your phone -- it is made of just 7 tiny bars of light arranged in a special pattern. By turning different bars on and off, you can make any number from 0 to 9!"

Show the kid a 7-segment display:

> "It looks like a single component, but inside it is actually 7 tiny LEDs -- one for each bar. Plus an extra one for the decimal point. Let us figure out how it works!"

```
  A 7-segment display:

     ___
    | a |
   f|   |b
    |___|
    | g |
   e|   |c
    |___|
      d    .dp
```

**Key vocabulary:**
- **7-segment display:** A component with 7 LED bars (called segments) labeled a, b, c, d, e, f, and g, arranged to display digits 0--9
- **Common anode:** All the + (anode) legs of the LEDs are connected together inside the display. You control which segments light up by grounding their individual pins
- **Common cathode:** The opposite -- all the - (cathode) legs are connected. You light segments by giving power to their individual pins
- **BCD (Binary Coded Decimal):** A way to represent digits 0--9 using 4 binary bits

**Award: +10 XP for learning about 7-segment displays!**

---

### Step 2: Which Segments Make Which Numbers? (8 min)

> "Each digit uses a different combination of the 7 segments. Let us figure out the pattern!"

**Segment Map:**

```
  To display the digit 0:  segments a, b, c, d, e, f ON  (all except g)
  To display the digit 1:  segments b, c ON
  To display the digit 2:  segments a, b, d, e, g ON
  To display the digit 3:  segments a, b, c, d, g ON
  To display the digit 4:  segments b, c, f, g ON
  To display the digit 5:  segments a, c, d, f, g ON
  To display the digit 6:  segments a, c, d, e, f, g ON
  To display the digit 7:  segments a, b, c ON
  To display the digit 8:  segments a, b, c, d, e, f, g ON  (all segments!)
  To display the digit 9:  segments a, b, c, d, f, g ON
```

**Activity -- Draw the Digits:**

Give the kid a sheet of paper with 10 blank 7-segment outlines. Have them color in the correct segments for each digit (0 through 9).

```
  BLANK TEMPLATE (draw 10 of these):

     ___
    |   |
    |   |
    |___|
    |   |
    |   |
    |___|

  Label: a (top), b (upper right), c (lower right),
         d (bottom), e (lower left), f (upper left), g (middle)
```

**Award: +20 XP for correctly drawing all 10 digits!**

---

### Step 3: Manual Wiring -- Display a Number by Hand (10 min)

> "Let us wire up the display and make it show a number manually. We will start with the number 3."

**Find the display pinout.** A common-anode 7-segment display typically has 10 pins:

```
  Common Anode 7-Segment Display -- Bottom View (pins facing you)

  Pin:   1   2   3   4   5   6   7   8   9  10
         e   d   CA  c   dp  b   a   CA  f   g

  CA = Common Anode (connect to +VCC through resistors)
```

> "The exact pinout depends on your display model -- check the datasheet or test with your Wand!"

**Wiring to display the digit 3 (segments a, b, c, d, g):**

1. Place the 7-segment display on the breadboard
2. Connect both CA (common anode) pins to the + rail
3. Connect segment pins a, b, c, d, and g each through a 330-ohm resistor to GND
4. Leave segments e and f disconnected (they stay off)

> "Did the number 3 appear? Change which segments connect to GND to show different numbers!"

**Challenge: Display your age!**

**Award: +30 XP for manually wiring a number on the display!**

---

### Step 4: The 7447 Decoder IC -- Automatic Number Display (12 min)

> "Connecting 7 wires every time you want to change a number is a lot of work! What if there was a chip that did it for you? Meet the 7447 BCD-to-7-Segment Decoder."

**How BCD works:**

> "BCD stands for Binary Coded Decimal. It is a way to tell the chip which number to display using only 4 switches (or 4 wires). Each switch represents a power of 2."

```
  BCD -- the 4 switches represent:

  Switch D | Switch C | Switch B | Switch A | Decimal
  (8)      | (4)      | (2)      | (1)      | Value
  ---------|----------|----------|----------|--------
     0     |    0     |    0     |    0     |   0
     0     |    0     |    0     |    1     |   1
     0     |    0     |    1     |    0     |   2
     0     |    0     |    1     |    1     |   3
     0     |    1     |    0     |    0     |   4
     0     |    1     |    0     |    1     |   5
     0     |    1     |    1     |    0     |   6
     0     |    1     |    1     |    1     |   7
     1     |    0     |    0     |    0     |   8
     1     |    0     |    0     |    1     |   9
```

**The 7447 IC pinout:**

```
  7447 BCD-to-7-Segment Decoder -- Top View

        Notch
          U
    +----------+
    |  1    16 | <-- Pin 16 = VCC
    |  2    15 |
    |  3    14 |
    |  4    13 |
    |  5    12 |
    |  6    11 |
    |  7    10 |
    |  8     9 |
    +----------+

  Pin 16 = VCC
  Pin 8 = GND
  Pin 7 = Input A (1s place)
  Pin 1 = Input B (2s place)
  Pin 2 = Input C (4s place)
  Pin 6 = Input D (8s place)
  Pin 13 = Output a
  Pin 12 = Output b
  Pin 11 = Output c
  Pin 10 = Output d
  Pin 9 = Output e
  Pin 15 = Output f
  Pin 14 = Output g
  Pin 3 = Lamp Test (connect to VCC for normal operation)
  Pin 4 = Blanking (connect to VCC for normal operation)
  Pin 5 = Ripple Blanking (connect to VCC for normal operation)
```

**Build the complete circuit:**

1. Place the 7447 IC on the breadboard, notch up
2. Pin 16 (VCC) to + rail, Pin 8 (GND) to - rail
3. Pin 3, Pin 4, Pin 5 to + rail (enables the chip)
4. Connect 4 push buttons (with pull-down resistors) to inputs A, B, C, D
5. Connect each output (a through g) through a 330-ohm resistor to the corresponding segment pin on the 7-segment display
6. Connect the display's common anode to + rail

**Test it -- display all digits 0 through 9:**

```
| Buttons D-C-B-A | Expected Digit | Display Shows | Correct? |
|-----------------|---------------|---------------|----------|
| 0-0-0-0         | 0             |               |          |
| 0-0-0-1         | 1             |               |          |
| 0-0-1-0         | 2             |               |          |
| 0-0-1-1         | 3             |               |          |
| 0-1-0-0         | 4             |               |          |
| 0-1-0-1         | 5             |               |          |
| 0-1-1-0         | 6             |               |          |
| 0-1-1-1         | 7             |               |          |
| 1-0-0-0         | 8             |               |          |
| 1-0-0-1         | 9             |               |          |
```

> "You just built a digital number display controlled by binary switches! This is exactly how old calculators and digital clocks worked inside."

**Award: +40 XP for building the 7447 decoder circuit and displaying all 10 digits!**

---

### Step 5: Wand Check -- Measure Segment Voltages! (8 min)

> "Time to peek behind the display with your Wand. Let us measure which segments are really getting power."

**Measurement 1: Check individual segment voltages**

1. Set the Wand to DC Voltage
2. Set the display to show the digit 3 (buttons: 0-0-1-1)
3. For each segment output pin on the 7447, measure the voltage

```
| Segment | Pin  | Digit 3 (expected) | Wand Reads | Active? |
|---------|------|-------------------|-----------|---------|
| a       | 13   | ON (LOW for CA)   |           |         |
| b       | 12   | ON                |           |         |
| c       | 11   | ON                |           |         |
| d       | 10   | ON                |           |         |
| e       | 9    | OFF               |           |         |
| f       | 15   | OFF               |           |         |
| g       | 14   | ON                |           |         |
```

> "For a common-anode display, active segments show LOW voltage (close to 0V) because the decoder sinks current through the segment. Inactive segments show HIGH voltage."

**Measurement 2: Measure across an LED segment directly**

1. Touch the red probe to the common anode pin of the display
2. Touch the black probe to one of the active segment pins (through the resistor side)
3. You should read about 2V across the LED segment -- this is the forward voltage of the LED inside!

**Award: +40 XP for measuring segment voltages and the LED forward voltage!**

---

## Fun Game: Binary Number Challenge (Optional Extension)

One person calls out a number (0--9). The other person has to figure out the binary (BCD) code and press the right buttons to display it. Race against a timer!

```
Quick reference:
0 = 0000    5 = 0101
1 = 0001    6 = 0110
2 = 0010    7 = 0111
3 = 0011    8 = 1000
4 = 0100    9 = 1001
```

---

## Quick Quiz -- Earn Bonus XP!

**Question 1:** How many LED segments make up a 7-segment display?
- A) 5
- B) 7
- C) 10

**(Correct: B -- +20 XP!)**

**Question 2:** What does the 7447 decoder IC do?
- A) Counts the number of button presses
- B) Converts a 4-bit binary input into the correct segments to display a digit
- C) Makes the display blink

**(Correct: B -- +20 XP!)**

**Question 3:** What binary (BCD) code would you enter to display the number 5?
- A) 0101
- B) 1010
- C) 0011

**(Correct: A -- +20 XP!)**

---

## Lesson 22 Complete!

```
  =============================================

     DIGIT DECODER BADGE UNLOCKED!

     Skills unlocked:
     [check] Understand how 7-segment displays work
     [check] Know which segments form each digit
     [check] Manually wired a display to show a number
     [check] Used the 7447 decoder for automatic digits
     [check] Measured segment voltages with the Wand

  =============================================
```

**XP Breakdown:**
| Activity | XP |
|----------|-----|
| Learning about 7-segment displays | 10 |
| Draw all 10 digits activity | 20 |
| Manual wiring a number | 30 |
| Build 7447 decoder circuit | 40 |
| Wand Check (segment voltages) | 40 |
| Quiz (3 questions) | 60 |
| **TOTAL POSSIBLE** | **200** |

---

## Coming Up Next...

In **Lesson 23**, you will combine the 555 timer with a **4017 decade counter IC** to build a **counting circuit**! Ten LEDs will light up one at a time in sequence -- like a light chaser from a movie. You will control the speed and watch the counter step through each number.

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| Display shows nothing | Check common anode connections to +VCC and that resistors go to GND |
| Wrong segments light up | Check wiring from 7447 output pins to display segment pins -- they must match |
| Display shows garbled numbers | Double-check BCD input wiring (A, B, C, D to correct pins) |
| Display is very dim | Reduce resistor values slightly (220-ohm instead of 330-ohm) |
| Some segments never light up | Use Wand continuity to test each LED segment individually |
| 7447 pins 3, 4, 5 not connected | These must be tied to VCC for normal operation |

---

## Navigation

| | |
|:---|---:|
| [← Lesson 21: Logic Gates -- NAND, NOR, XOR](lesson-21-logic-gates-nand-nor-xor.md) | [Lesson 23: Building a Simple Counter →](lesson-23-building-a-simple-counter.md) |

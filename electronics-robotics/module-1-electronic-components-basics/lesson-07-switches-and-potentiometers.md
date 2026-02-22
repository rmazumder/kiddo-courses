# Lesson 7: Switches and Potentiometers -- Twist, Click, Control

**Module:** 1 -- Electronic Components Basics
**Difficulty:** Star-1 Beginner
**Session Time:** 40 minutes
**Age:** 6--12 years
**XP Available:** 290 XP

---

## Your Mission Today

Circuit Explorer, today you get to play with controls! Buttons you press, switches you flip, and knobs you twist. You will build an LED dimmer that YOU control -- and use your Magic Measurement Wand to see the resistance change in real time as you turn the knob!

---

## Learning Objectives

By the end of this lesson, you will be able to:
- Know the difference between push buttons, toggle switches, and slide switches
- Explain what a potentiometer is and how it works
- Build an LED dimmer controlled by a knob
- Use the Magic Measurement Wand to measure changing resistance

---

## What You Need

| Item | Qty |
|------|-----|
| 10k-ohm potentiometer (knob type) | 1 |
| Push button (tactile) | 2 |
| Toggle switch (SPDT or SPST) | 1 |
| LEDs (bright red or yellow) | 2 |
| 100-ohm resistor | 2 |
| 9V battery + clip | 1 |
| Breadboard | 1 |
| Jumper wires | 8 |
| Multimeter (Magic Measurement Wand) | 1 |

---

## How to Teach This Lesson

### Step 1: Hook -- The Switch Hunt (3 min)

> "How many switches do you think are in this room right now?"

Let the kid count: light switches, TV remote buttons, door handles, phone buttons, keyboard keys, game controller buttons...

> "Switches are EVERYWHERE. And a potentiometer is just a fancy switch -- one that does not go on/off but smoothly changes from 0 to maximum. Let us explore them all."

**Award: +10 XP for finding at least 5 switches in the room!**

---

### Step 2: Types of Switches (8 min)

**Show each type and explain:**

**Push Button (Tactile Switch):**
```
  State:   NOT pressed        PRESSED
           --  --              --------
           open (off)          closed (on)

  Use: Doorbell, keyboard key, game controller button
  Key feature: Spring-loaded -- only ON while pressed (momentary)
```

**Toggle Switch:**
```
  State:   DOWN               UP
           --------           --  --
           closed (on)        open (off)

  Use: Light switch, power switch on old equipment
  Key feature: STAYS in position (latching)
```

**Rotary Switch:**
```
  Turns to connect to one of several positions
  Use: Fan speed (low/med/high), and... your multimeter dial!
```

> "Can you find the rotary switch in this room?" (Point to the multimeter dial!)

**Activity -- Switch Scavenger Hunt:**
Walk around the house for 2 minutes and find as many switches as possible. Categorize them:
- Momentary (only on while pressed/held)
- Latching (stays on or off)

**Award: +20 XP for finding and categorizing at least 6 switches!**

---

### Step 3: The Potentiometer -- A Variable Resistor (8 min)

**Show the potentiometer:**

```
  Three legs:

  Left leg -------- full resistance track (0 ohms to max)
  Middle leg ------  WIPER (moves as you turn)
  Right leg ------- other end of track

  Between left and right: always = max resistance (e.g., 10k ohms)
  Between left and middle: changes from 0 to 10k ohms as you turn
  Between right and middle: changes from 10k ohms to 0 as you turn
```

> "The middle leg is called the **WIPER**. It slides along a resistive strip. Turn the knob, wiper moves, resistance between middle and either end changes."

**Award: +10 XP for identifying the wiper (middle leg)!**

---

### Step 4: Wand Check -- Watch Resistance Change Live! (8 min)

> "This is SO cool. Set your Magic Measurement Wand to resistance mode (the horseshoe symbol). Now you are going to watch the numbers change AS you turn the knob!"

**Measurement 1 -- Fixed resistance:**
- Touch probes to the left and right legs
- Read the display: should be about 10k ohms
- Turn the knob... nothing changes! (These two legs always show full resistance)

**Measurement 2 -- Variable resistance:**
- Touch probes to the left leg and the MIDDLE leg
- Read the display
- Now SLOWLY turn the knob
- Watch the number go from near 0 to near 10k ohms!

**Measurement 3 -- The other direction:**
- Touch probes to the right leg and the MIDDLE leg
- Turn the knob slowly
- This time the number goes the OPPOSITE direction!

> "When one side goes up, the other side goes down. The total always adds up to the same number. That is because the knob is just sliding a contact along a fixed strip of resistive material!"

**Fill in the readings:**

```
| Knob Position    | Left-to-Middle | Right-to-Middle | Total (add both) |
|------------------|---------------|----------------|-----------------|
| All the way left |               |                |                 |
| Middle           |               |                |                 |
| All the way right|               |                |                 |
```

> "Look at the Total column. Is it always about 10k? That proves the potentiometer is just splitting the same resistance into two parts!"

**Award: +50 XP for completing all three Wand measurements and filling in the table!**

---

### Step 5: Build the LED Dimmer (10 min)

**Circuit:**

```
  9V (+) ---- [potentiometer left leg]
              [potentiometer middle leg] ---- [100-ohm] ---- LED (+) ---- LED (-) ---- 9V (-)

  The potentiometer middle leg gives variable resistance.
  Turn knob one way: more resistance -- dimmer LED
  Turn knob other way: less resistance -- brighter LED
```

**Build it:**
1. Connect 9V (+) to left leg of potentiometer
2. Middle leg to 100-ohm resistor to LED (+)
3. LED (-) to 9V (-)

**Test:**
Slowly turn the knob. The LED should smoothly brighten and dim!

> "You just built a real dimmer switch -- just like the ones used for room lighting!"

**Why the extra 100-ohm resistor?**
> "When the potentiometer is turned all the way to 0 ohms, we would have NO resistance protecting the LED. The 100 ohms is a minimum safety resistor."

**Award: +30 XP for building the dimmer!**

---

### Step 6: Add a Button Switch (5 min)

Now add a push button to turn the whole circuit on/off:

```
  9V (+) ---- [BUTTON] ---- [potentiometer left leg]
                             [potentiometer middle] ---- [100-ohm] ---- LED ---- GND
```

**Test:**
- Button not pressed: LED off (no matter what the knob says)
- Button pressed: LED brightness controlled by knob

> "You now have two controls: one that switches on/off (button) and one that controls brightness (knob). That is exactly how a professional stage lighting dimmer works!"

**Award: +20 XP for adding the button control!**

---

## Quick Quiz -- Earn Bonus XP!

**Question 1:** What is a potentiometer?
- A) A type of battery
- B) A variable resistor -- you turn a knob to change resistance
- C) A type of LED

**(Correct: B -- +20 XP!)**

**Question 2:** You measured the potentiometer with your Wand. Left-to-middle reads 3k ohms. Right-to-middle reads 7k ohms. What is the total?
- A) 3k ohms
- B) 7k ohms
- C) 10k ohms (they add up!)

**(Correct: C -- +20 XP!)**

**Question 3:** A push button is "momentary." What does that mean?
- A) It stays on forever
- B) It is only on while you are pressing it
- C) It works for one moment and then breaks

**(Correct: B -- +20 XP!)**

---

## Lesson 7 Complete!

```
  =============================================

     DIAL MASTER BADGE UNLOCKED!

     Skills unlocked:
     [check] Know push button vs toggle vs rotary switches
     [check] Understand potentiometers as variable resistors
     [check] Measured changing resistance with the Wand
     [check] Built a working LED dimmer

  =============================================
```

**XP Breakdown:**
| Activity | XP |
|----------|-----|
| Switch scavenger hunt | 20 |
| Hook (find 5 switches) | 10 |
| Identify the wiper | 10 |
| Wand Check (3 measurements + table) | 50 |
| Build the dimmer | 30 |
| Add button control | 20 |
| Quiz (3 questions) | 60 |
| **TOTAL POSSIBLE** | **200** |

---

## Real-World Connection

Ask the kid:
- "When you turn the volume knob on a speaker or TV -- that is a potentiometer!"
- "The throttle on a remote-control car? Potentiometer."
- "Old video game joysticks? Two potentiometers -- one for left/right, one for up/down."

---

## Coming Up Next...

In **Lesson 8**, we add **sound** to our toolkit with buzzers. You will build a door alarm and use your Magic Measurement Wand to explore the difference between connected and disconnected circuits using continuity mode!

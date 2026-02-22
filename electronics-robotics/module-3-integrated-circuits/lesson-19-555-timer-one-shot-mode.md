# Lesson 19: The 555 Timer -- One-Shot Mode (Monostable)

**Module:** 3 -- Integrated Circuits (ICs)
**Difficulty:** Star-3 Intermediate
**Session Time:** 40--45 minutes
**Age:** 6--12 years
**XP Available:** 280 XP

---

## Your Mission Today

Last lesson you built a blinker that keeps going forever. But what if you want something to turn on for a set amount of time and then stop? Like a hallway light that stays on for 30 seconds after you flip the switch, then turns itself off? That is **monostable mode** -- the 555's "one-shot" trick. Press a button once and the LED stays on for exactly the time YOU choose!

---

## Learning Objectives

By the end of this lesson, you will be able to:
- Explain the difference between astable (blinker) and monostable (one-shot) modes
- Build a 555 monostable circuit that triggers with a button press
- Calculate and control how long the output stays on
- Use your Magic Measurement Wand to measure the timed pulse duration

---

## What You Need

| Item | Qty |
|------|-----|
| 555 timer IC | 1 |
| Resistor: 100k-ohm (R) | 1 |
| Resistor: 47k-ohm (R swap) | 1 |
| Resistor: 10k-ohm (pull-up for trigger) | 1 |
| Electrolytic capacitor: 47 microfarad (C) | 1 |
| Electrolytic capacitor: 100 microfarad (C swap) | 1 |
| Ceramic capacitor: 0.01 microfarad (noise filter) | 1 |
| LED (any color) | 1 |
| 330-ohm resistor (for LED) | 1 |
| Push button (tactile switch) | 1 |
| 9V battery + clip | 1 |
| Breadboard | 1 |
| Jumper wires | 10 |
| Multimeter (Magic Measurement Wand!) | 1 |
| Stopwatch or phone timer | 1 |

---

## How to Teach This Lesson

### Step 1: Hook -- The Automatic Nightlight (5 min)

> "Imagine you wake up in the middle of the night and need to go to the bathroom. You slap a big button on the wall. The hallway light turns on, you walk to the bathroom and back, and by the time you are back in bed -- the light turns itself off. No switch to flip, no thinking required."

> "That is exactly what we are building today! A timed light that YOU control -- press once, it stays on for 5 seconds (or 10, or 30), then turns off by itself."

**The difference:**
- **Astable (Lesson 18):** Keeps going forever -- on, off, on, off...
- **Monostable (today):** One shot -- press the button, output goes HIGH for a set time, then goes LOW and STAYS LOW until you press again

> "Mono means one. Stable means steady. Monostable = one steady pulse."

**Award: +10 XP for understanding the difference between astable and monostable!**

---

### Step 2: How Monostable Mode Works (8 min)

**The Egg Timer Analogy:**

> "Think of an egg timer. You twist it to set the time (that is your resistor and capacitor values). When you let go, it starts counting down (the capacitor charges). When time is up, it goes DING and stops (the output goes LOW). To start it again, you have to twist it again (press the button)."

**The circuit:**

```
  +9V ----+
          |
         [R] 100k-ohm
          |
          +------------ Pin 6 (Threshold)
          |              Pin 7 (Discharge)
         [C] 47uF
          |
         GND

  Pin 8 (VCC) ---- +9V
  Pin 1 (GND) ---- GND
  Pin 4 (Reset) ---- +9V
  Pin 5 (Control) ---- 0.01uF ---- GND

  Pin 2 (Trigger) ---- [10k pull-up to +9V]
                   ---- push button ---- GND

  Pin 3 (Output) ---- [330-ohm] ---- LED ---- GND
```

**What happens when you press the button:**
1. Pin 2 (Trigger) drops below 1/3 VCC -- this triggers the 555
2. Output (Pin 3) goes HIGH -- LED turns on!
3. Capacitor C starts charging through R
4. When the capacitor voltage reaches 2/3 VCC, the 555 flips back
5. Output goes LOW -- LED turns off
6. Capacitor discharges quickly through Pin 7
7. Circuit waits for the next button press

**The timing formula:**

```
Time ON = 1.1 x R x C

Example: R = 100k, C = 47uF
T = 1.1 x 100,000 x 0.000047
T = 5.17 seconds (about 5 seconds!)
```

**Award: +10 XP for understanding how monostable timing works!**

---

### Step 3: Build the One-Shot Circuit! (12 min)

> "Let us build this! It looks a lot like the blinker from last lesson, but simpler in some ways."

**Step-by-step wiring:**

1. Place the 555 IC across the center gap, notch facing up
2. Pin 1 (GND) to - rail
3. Pin 8 (VCC) to + rail
4. Pin 4 (Reset) to + rail
5. Place R (100k-ohm) between the + rail and a row connecting to Pin 7
6. Connect Pin 6 to Pin 7 with a short jumper (they share a row connection)
7. Place C (47 microfarad) between Pin 6/7 and the - rail. **Long leg (+) to Pin 6/7 side!**
8. Place 0.01 microfarad cap between Pin 5 and - rail
9. Connect the trigger: 10k-ohm resistor from + rail to Pin 2 (pull-up), then push button from Pin 2 to - rail
10. Connect LED: Pin 3 to 330-ohm resistor to LED to - rail
11. Connect 9V battery

**Test it:**

> "Press the button quickly and let go. The LED should turn on for about 5 seconds, then turn off by itself. Press again -- another 5-second glow!"

**Award: +40 XP for building a working monostable circuit!**

---

### Step 4: Time Control Experiments (8 min)

> "Now let us play with the timing. You are the time controller!"

**Experiment: Change R and C to change the ON time**

```
| R Value  | C Value | Calculated Time | Measured Time | Close? |
|----------|---------|----------------|---------------|--------|
| 100k     | 47uF    | 5.17 sec       |               |        |
| 47k      | 47uF    | 2.43 sec       |               |        |
| 100k     | 100uF   | 11 sec         |               |        |
| 47k      | 100uF   | 5.17 sec       |               |        |
```

**How to measure:** Press the button, start the stopwatch. When the LED turns off, stop the stopwatch. Write down the time.

> "See how the formula works? Bigger R or bigger C = longer time. You are programming the chip without a computer!"

**Challenge -- The 10-Second Timer:**

> "Can you pick a resistor and capacitor combination that gives you exactly 10 seconds? Try it!"

**Award: +30 XP for testing at least 3 combinations and the 10-second challenge!**

---

### Step 5: Wand Check -- Measure the Timed Pulse! (8 min)

> "Let us see what the Wand shows during a one-shot pulse."

**Measurement 1: Output Voltage During the Pulse**

1. Set Wand to DC Voltage
2. Black probe on GND
3. Red probe on Pin 3 (Output)
4. Press the button and watch the display

> "You should see the voltage jump up to about 8V when you press the button, hold steady for the timed duration, then drop back to near 0V. That is the one-shot pulse!"

**Measurement 2: Watch the Capacitor Charge**

1. Move the red probe to the + leg of the capacitor (Pin 6/7 side)
2. Press the button and watch

> "The voltage on the capacitor slowly climbs from 0V up to about 6V. When it hits 6V (two-thirds of 9V), the 555 says 'time is up!' and flips the output off. Then the capacitor voltage drops back to 0V quickly."

**Fill in:**

```
| Measurement | Before Button | During Pulse | After Pulse |
|-------------|--------------|-------------|-------------|
| Pin 3 (Output) |           |             |             |
| Capacitor      |           |             |             |
| Pin 2 (Trigger)|           |             |             |
```

**Award: +40 XP for measuring all three signals during a pulse!**

---

### Step 6: Real-World Monostable Uses (3 min)

> "The one-shot timer is used everywhere!"

- **Hallway lights** -- press a button, light stays on for 60 seconds
- **Hand dryers in bathrooms** -- press once, blows for 30 seconds
- **Debouncing buttons** -- when you press a button, it actually bounces many times in a millisecond. A monostable 555 can clean that up into one clean signal
- **Alarms** -- trigger once, siren sounds for a set time

**Award: +10 XP for discussing real-world uses!**

---

## Quick Quiz -- Earn Bonus XP!

**Question 1:** What does "monostable" mean?
- A) Two stable states that keep switching
- B) One stable state -- it triggers once, stays on for a set time, then returns
- C) No stable states

**(Correct: B -- +20 XP!)**

**Question 2:** The formula for the ON time in monostable mode is T = 1.1 x R x C. If you DOUBLE the capacitor value, what happens to the time?
- A) It stays the same
- B) It doubles
- C) It halves

**(Correct: B -- +20 XP!)**

**Question 3:** What triggers the 555 in monostable mode?
- A) Pin 3 going HIGH
- B) Pin 2 (Trigger) dropping below 1/3 of VCC
- C) Turning off the power

**(Correct: B -- +20 XP!)**

---

## Lesson 19 Complete!

```
  =============================================

     ONE-SHOT WIZARD BADGE UNLOCKED!

     Skills unlocked:
     [check] Built a 555 monostable circuit
     [check] Controlled pulse duration with R and C
     [check] Measured the timed pulse with the Wand
     [check] Watched capacitor charging in real time
     [check] Understand monostable real-world uses

  =============================================
```

**XP Breakdown:**
| Activity | XP |
|----------|-----|
| Astable vs monostable understanding | 10 |
| How monostable works | 10 |
| Build one-shot circuit | 40 |
| Time control experiments | 30 |
| Wand Check (3 measurements) | 40 |
| Real-world uses discussion | 10 |
| Quiz (3 questions) | 60 |
| **TOTAL POSSIBLE** | **200** |

---

## Coming Up Next...

In **Lesson 20**, we leave the 555 timer and enter the world of **Logic Gates**! You will learn about AND, OR, and NOT gates -- the building blocks of every computer ever made. If two switches are both ON, the light turns on. If either switch is ON, the light turns on. These simple rules power the entire digital world!

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| LED stays on permanently | Check that Pin 2 (Trigger) has the 10k pull-up resistor to +VCC |
| LED never turns on | Check button wiring -- it should connect Pin 2 to GND when pressed |
| LED turns on but immediately turns off | Capacitor might be too small or R too small -- try bigger values |
| Timer is way off from calculated time | Battery voltage affects timing -- measure battery with Wand |
| Button press does nothing | Test the button with Wand continuity mode -- does it beep when pressed? |
| IC gets hot | Check wiring carefully -- something is likely shorted |

---

## Navigation

| | |
|:---|---:|
| [← Lesson 18: The 555 Timer -- Blinker Mode (Astable)](lesson-18-555-timer-blinker-mode.md) | [Lesson 20: Logic Gates -- AND, OR, NOT →](lesson-20-logic-gates-and-or-not.md) |

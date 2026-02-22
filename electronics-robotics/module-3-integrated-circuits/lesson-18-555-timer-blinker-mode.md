# Lesson 18: The 555 Timer -- Blinker Mode (Astable)

**Module:** 3 -- Integrated Circuits (ICs)
**Difficulty:** Star-3 Intermediate
**Session Time:** 45--50 minutes
**Age:** 6--12 years
**XP Available:** 300 XP

---

## Your Mission Today

You found Pin 1. You measured voltages. Now it is time to make the 555 timer chip DO something! Today you will build a circuit that makes an LED blink on and off all by itself -- no button pressing, no hand waving. The 555 does all the work. And you will control exactly how fast it blinks!

---

## Learning Objectives

By the end of this lesson, you will be able to:
- Explain what "astable" mode means (the 555 flips between ON and OFF forever)
- Build a working 555 blinker circuit on a breadboard
- Change the blink speed by swapping resistors and capacitors
- Use your Magic Measurement Wand to time the blinks and measure the output

---

## What You Need

| Item | Qty |
|------|-----|
| 555 timer IC | 1 |
| Resistor: 1k-ohm (R1) | 1 |
| Resistor: 10k-ohm (R2) | 1 |
| Resistor: 47k-ohm (R2 swap) | 1 |
| Resistor: 100k-ohm (R2 swap) | 1 |
| Electrolytic capacitor: 47 microfarad (C1) | 1 |
| Electrolytic capacitor: 100 microfarad (C1 swap) | 1 |
| Electrolytic capacitor: 470 microfarad (C1 swap) | 1 |
| Ceramic capacitor: 0.01 microfarad (C2, noise filter) | 1 |
| LED (any color) | 1 |
| 330-ohm resistor (for LED) | 1 |
| 9V battery + clip | 1 |
| Breadboard | 1 |
| Jumper wires | 10 |
| Multimeter (Magic Measurement Wand!) | 1 |
| Stopwatch or phone timer | 1 |

---

## How to Teach This Lesson

### Step 1: Hook -- The Heartbeat of Electronics (5 min)

> "Put your hand on your chest. Feel that? Thump... thump... thump. Your heart beats on its own, over and over, without you thinking about it. Today we are going to give the 555 timer chip a heartbeat! It will pulse on and off, on and off, forever -- just like your heart."

Show the kid the completed blinker circuit (if you built one ahead of time) or describe it:

> "When we are done, this LED will blink all by itself. No buttons, no switches. The 555 chip will be its heart."

**Key vocabulary:**

- **Astable mode:** A mode where the 555 keeps flipping between HIGH (on) and LOW (off) forever, like a heartbeat. "Astable" means "not stable" -- it never stays in one state
- **Frequency:** How fast something repeats. Measured in Hertz (Hz). 1 Hz = one blink per second
- **Oscillator:** Something that goes back and forth, on and off, over and over

**Award: +10 XP for understanding the heartbeat analogy!**

---

### Step 2: How the 555 Blinker Works (8 min)

**The Bucket Analogy:**

> "Imagine a bucket with a hole in the bottom. You fill it with water from a hose (that is the resistor letting current flow slowly). When the bucket fills up to the top line, a trap door opens and dumps the water out (that is the 555 flipping the output). Then the bucket starts filling again. Fill, dump, fill, dump -- over and over!"

**The actual circuit:**

```
  +9V ----+
          |
         [R1] 1k-ohm
          |
          +------------ Pin 7 (Discharge)
          |
         [R2] 10k-ohm
          |
          +------------ Pin 6 (Threshold)
          |              Pin 2 (Trigger)
         [C1] 47uF
          |
         GND

  Pin 8 (VCC) ---- +9V
  Pin 1 (GND) ---- GND
  Pin 4 (Reset) ---- +9V (keeps chip enabled)
  Pin 5 (Control) ---- 0.01uF cap ---- GND (noise filter)
  Pin 3 (Output) ---- [330-ohm] ---- LED ---- GND
```

**What happens inside:**
1. The capacitor C1 charges up through R1 and R2 (bucket fills)
2. When the voltage on C1 reaches 2/3 of VCC, the 555 flips -- output goes LOW
3. C1 starts discharging through R2 and Pin 7 (bucket empties)
4. When the voltage on C1 drops to 1/3 of VCC, the 555 flips again -- output goes HIGH
5. Repeat forever!

**Award: +10 XP for understanding how the 555 oscillates!**

---

### Step 3: Build the Blinker Circuit! (15 min)

> "Time to build! Follow these steps carefully. Take your time -- IC circuits have more wires than what we have built before."

**Step-by-step wiring:**

1. Place the 555 IC across the center gap of the breadboard, notch facing up
2. Connect Pin 1 (GND) to the - rail
3. Connect Pin 8 (VCC) to the + rail
4. Connect Pin 4 (Reset) to the + rail (this keeps the chip running)
5. Place R1 (1k-ohm) between the + rail and a row that connects to Pin 7
6. Place R2 (10k-ohm) between Pin 7 and Pin 6
7. Connect Pin 2 to Pin 6 with a short jumper wire (they share the same signal)
8. Place C1 (47 microfarad) between Pin 2/6 and the - rail. **Watch polarity! Long leg (+) goes to Pin 2/6 side, short leg (-) to GND rail**
9. Place the noise filter cap (0.01 microfarad) between Pin 5 and the - rail
10. Connect LED: Pin 3 to 330-ohm resistor, then to LED long leg (+), then LED short leg to GND
11. Connect 9V battery to the power rails

> "Moment of truth -- connect the battery. Does the LED blink? YES? You just built an oscillator!"

**If it does not blink:**
- Check that Pin 4 is connected to + (it resets the chip if left floating)
- Check the capacitor polarity (+ leg to the signal side, - to GND)
- Check LED polarity (long leg = +)
- Make sure Pin 2 and Pin 6 are connected together

**Award: +40 XP for building a working 555 blinker!**

---

### Step 4: Speed Control -- Change the Blink Rate (8 min)

> "Now the fun part -- you are the DJ of this circuit! By swapping resistors and capacitors, you control the speed."

**Experiment 1: Change R2**

Keep C1 at 47 microfarad. Swap R2:

```
| R2 Value | Expected Blink Speed | Actual (count blinks in 10 sec) |
|----------|---------------------|---------------------------------|
| 10k-ohm  | About 1 blink/sec   |                                 |
| 47k-ohm  | Slower              |                                 |
| 100k-ohm | Even slower         |                                 |
```

> "What pattern do you see? Bigger resistor = slower blinks!"

**Experiment 2: Change C1**

Put R2 back to 10k-ohm. Swap C1:

```
| C1 Value    | Expected Blink Speed | Actual (count blinks in 10 sec) |
|-------------|---------------------|---------------------------------|
| 47 uF       | About 1 blink/sec   |                                 |
| 100 uF      | Slower              |                                 |
| 470 uF      | Very slow           |                                 |
```

> "Bigger capacitor = slower blinks too! The capacitor is like a bigger bucket -- it takes longer to fill and empty."

**The Formula (for ages 9+):**

```
Frequency = 1.44 / ((R1 + 2 x R2) x C)

Example: R1 = 1k, R2 = 10k, C = 47uF
f = 1.44 / ((1000 + 20000) x 0.000047)
f = 1.44 / 0.987
f = about 1.46 Hz (about 1.5 blinks per second)
```

**Award: +30 XP for testing at least 3 different R/C combinations!**

---

### Step 5: Wand Check -- Measure the 555 Output! (8 min)

> "Your LED is blinking, but what does the Wand see at the output pin? Let us find out!"

**Measurement 1: DC Voltage at Pin 3 (Output)**

1. Set the Wand to **DC Voltage** mode
2. Black probe on GND rail
3. Red probe on Pin 3 (Output)
4. Watch the display -- it will jump around because the voltage is switching!

> "The Wand display is flickering! That is because Pin 3 is switching between about 0V (LOW) and about 8V (HIGH) really fast. The Wand is trying to show you a moving target!"

**Measurement 2: Timing the Blinks**

1. Use a stopwatch (or phone timer)
2. Count how many times the LED blinks in exactly 10 seconds
3. Divide by 10 to get the frequency in Hz

```
| R2 Value | C1 Value | Blinks in 10 sec | Frequency (blinks/10) |
|----------|----------|------------------|-----------------------|
| 10k      | 47uF     |                  |                       |
| 10k      | 100uF    |                  |                       |
| 47k      | 47uF     |                  |                       |
```

**Measurement 3: Capacitor Voltage**

1. Keep the Wand on DC Voltage
2. Touch the red probe to the + leg of C1 (the side connected to Pin 2/6)
3. Watch the voltage go up and down like a wave!

> "See how the voltage on the capacitor rises and falls? That is the bucket filling and emptying! It rises to about 6V, then drops to about 3V, then rises again. The 555 is watching this voltage and flipping the output based on it."

**Award: +50 XP for measuring the output, timing the blinks, and watching the capacitor voltage!**

---

## Quick Quiz -- Earn Bonus XP!

**Question 1:** What does "astable" mean for the 555 timer?
- A) It stays in one state forever
- B) It keeps switching between HIGH and LOW without stopping
- C) It only works once

**(Correct: B -- +20 XP!)**

**Question 2:** If you want the LED to blink SLOWER, what should you do?
- A) Use a bigger resistor (R2) or bigger capacitor (C1)
- B) Use a smaller resistor
- C) Remove the LED

**(Correct: A -- +20 XP!)**

**Question 3:** In the 555 blinker circuit, what does the capacitor do?
- A) Makes the LED brighter
- B) Charges and discharges to create the timing rhythm
- C) Protects the battery

**(Correct: B -- +20 XP!)**

---

## Lesson 18 Complete!

```
  =============================================

     BLINK MASTER BADGE UNLOCKED!

     Skills unlocked:
     [check] Built a 555 astable blinker circuit
     [check] Controlled blink speed with R and C
     [check] Measured output voltage with the Wand
     [check] Timed blink frequency
     [check] Watched capacitor charge/discharge

  =============================================
```

**XP Breakdown:**
| Activity | XP |
|----------|-----|
| Heartbeat analogy | 10 |
| Understanding oscillation | 10 |
| Build blinker circuit | 40 |
| Speed control experiments | 30 |
| Wand Check (3 measurements) | 50 |
| Quiz (3 questions) | 60 |
| **TOTAL POSSIBLE** | **200** |

---

## Coming Up Next...

In **Lesson 19**, you will put the 555 into **One-Shot Mode** (Monostable). Press a button once, and the LED stays on for EXACTLY 5 seconds, then turns off. You will build a timed nightlight and control how long it stays on!

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| LED does not blink -- stays on | Check that Pin 2 and Pin 6 are connected together |
| LED does not blink -- stays off | Check Pin 4 is connected to +VCC (not floating) |
| LED is very dim | Make sure the 330-ohm resistor is in the LED path, not in the timing path |
| Blinks too fast to see | Use a bigger capacitor (470uF or 1000uF) |
| Blinks too slow | Use a smaller capacitor (10uF) or smaller R2 |
| IC gets warm | Check wiring -- something may be short-circuited |
| Wand voltage jumps around on Pin 3 | That is normal! The output is switching rapidly |

---

## Navigation

| | |
|:---|---:|
| [← Lesson 17: What is an Integrated Circuit?](lesson-17-what-is-an-integrated-circuit.md) | [Lesson 19: The 555 Timer -- One-Shot Mode (Monostable) →](lesson-19-555-timer-one-shot-mode.md) |

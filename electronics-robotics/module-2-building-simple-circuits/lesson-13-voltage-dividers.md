# Lesson 13: Voltage Dividers -- Splitting Voltage on Purpose

**Module:** 2 -- Building Simple Circuits
**Difficulty:** Star-2 Medium
**Session Time:** 45--50 minutes
**Age:** 6--12 years
**XP Available:** 230 XP

---

## Your Mission Today

Circuit Explorer, what if you had a 9V battery but needed exactly 3V for a sensor? You cannot just ask the battery nicely. But you CAN use a clever trick with two resistors called a **voltage divider**. Today you will learn the formula, use it to PREDICT an exact output voltage, and then use your Magic Measurement Wand to see if the prediction is correct. It is Formula vs. Wand -- the ultimate showdown!

---

## Learning Objectives

By the end of this lesson, you will be able to:
- Explain what a voltage divider does and why it is useful
- Build a basic voltage divider with two resistors
- Use the voltage divider formula to predict the output voltage
- Verify your prediction by measuring Vout with the Wand
- Build a variable voltage divider using a potentiometer

---

## What You Need

| Item | Qty |
|------|-----|
| 9V battery + clip | 1 |
| Breadboard | 1 |
| Resistors: 1k-ohm, 2.2k-ohm, 4.7k-ohm, 10k-ohm | 2 each |
| 10k-ohm potentiometer | 1 |
| LED (red) | 1 |
| 330-ohm resistor | 1 |
| Jumper wires | 8 |
| Multimeter (Magic Measurement Wand) | 1 |
| Paper + pencil | 1 set |
| Calculator (optional) | 1 |

---

## How to Teach This Lesson

### Step 1: Hook -- The Pizza Sharing Problem (5 min)

> "Imagine you have a whole pizza (9 slices). You and your friend are sharing, but your friend is TWICE as hungry as you. How do you divide it fairly?"

Let the kid think...

> "Your friend gets 6 slices (twice as much). You get 3 slices. The hungrier person gets MORE pizza."

> "A voltage divider works the SAME way! Two resistors share the battery's voltage. The BIGGER resistor 'eats' more voltage. The smaller resistor gets less. And the voltage at the point between them is whatever is left over -- and THAT is the voltage you can use for something else!"

**Award: +10 XP for solving the pizza sharing problem!**

---

### Step 2: How a Voltage Divider Works (10 min)

**The circuit:**

```
  Voltage Divider:

  Vin (9V) ----[R1]----+----[R2]---- GND (0V)
                        |
                       Vout
                   (this is the
                   voltage we want!)
```

> "Vin is the full battery voltage (9V). The two resistors form a series circuit. The point BETWEEN them is called Vout -- the divided voltage."

**The formula:**

```
                      R2
  Vout = Vin x  ───────────
                   R1 + R2
```

> "In plain English: Vout equals the INPUT voltage multiplied by the fraction of R2 over the total resistance."

**Why does this work?**

> "Remember Kirchhoff's Voltage Law from the series lesson? The voltage across R1 plus the voltage across R2 equals 9V. Since voltage splits based on resistance (Ohm's Law), the bigger resistor gets more voltage. Vout is just the voltage across R2 -- the bottom resistor."

**Key vocabulary:**

| Word | Kid-Friendly Definition |
|------|------------------------|
| **Voltage divider** | Two resistors that split a voltage into a smaller voltage |
| **Vout** | The output voltage -- the "divided" voltage between the two resistors |
| **Vin** | The input voltage -- the battery voltage going in |

**Award: +10 XP for understanding the voltage divider concept!**

---

### Step 3: Predict the Output -- Formula Time! (10 min)

**Round 1 -- Equal Resistors (1k + 1k):**

```
  R1 = 1k ohm = 1000 ohms
  R2 = 1k ohm = 1000 ohms
  Vin = 9V

  Vout = 9 x 1000 / (1000 + 1000)
  Vout = 9 x 1000 / 2000
  Vout = 9 x 0.5
  Vout = 4.5V
```

> "Equal resistors = exactly HALF the voltage. Makes sense -- equal sharing!"

**Round 2 -- Unequal Resistors (1k + 2.2k):**

```
  R1 = 1k ohm = 1000 ohms
  R2 = 2.2k ohm = 2200 ohms
  Vin = 9V

  Vout = 9 x 2200 / (1000 + 2200)
  Vout = 9 x 2200 / 3200
  Vout = 9 x 0.6875
  Vout = 6.19V
```

> "R2 is bigger, so it gets more voltage. Vout is higher."

**Round 3 -- Big Top, Small Bottom (10k + 1k):**

```
  R1 = 10k ohm = 10000 ohms
  R2 = 1k ohm = 1000 ohms
  Vin = 9V

  Vout = 9 x 1000 / (10000 + 1000)
  Vout = 9 x 1000 / 11000
  Vout = 9 x 0.0909
  Vout = 0.82V
```

> "R1 is huge and R2 is small, so most of the voltage is eaten by R1. Vout is tiny!"

**For ages 6--8:** Do Round 1 only (equal resistors = half). Use the pizza analogy: "same size friends = equal share."

**For ages 9--12:** Do all three rounds with the calculator. Have them predict BEFORE building.

**Award: +30 XP for calculating at least 2 voltage divider outputs correctly!**

---

### Step 4: Build It and Prove It -- Formula vs. Wand! (10 min)

> "You made predictions with the formula. Now let us see if reality agrees. Build the voltage divider and let the Wand be the judge!"

**Build Round 1 on the breadboard:**

```
  On breadboard:
  1. Jumper wire: + rail to row 3
  2. R1 (1k ohm): row 3 to row 6
  3. R2 (1k ohm): row 6 to row 9
  4. Jumper wire: row 9 to - rail
  5. Vout is at row 6 (the junction between R1 and R2)
```

**Wand Check -- Measure Vout:**

1. Set Wand to **DC Volts**
2. Red probe on row 6 (the Vout point)
3. Black probe on the - rail (GND)
4. Read the display!

```
| Divider | R1 | R2 | Predicted Vout | Wand Reads | Match? |
|---------|----|----|---------------|-----------|--------|
| Round 1 | 1k | 1k | 4.5V | _____ V | |
| Round 2 | 1k | 2.2k | 6.19V | _____ V | |
| Round 3 | 10k | 1k | 0.82V | _____ V | |
```

> "How close were your predictions? If they are within 0.2V, that is excellent! Real resistors have tolerance (remember the 5% rule?), so exact matches are rare."

**Award: +50 XP for measuring all three voltage dividers and comparing to predictions!**

---

### Step 5: The Variable Voltage Divider -- Potentiometer! (8 min)

> "What if you did not want a FIXED output voltage? What if you wanted to TURN A KNOB and smoothly change Vout from 0V all the way to 9V? That is what a potentiometer does -- it is a voltage divider with an adjustable split point!"

**Build the potentiometer voltage divider:**

```
  Potentiometer has 3 pins:
  Pin 1 ---- 9V (+)
  Pin 2 ---- Vout (the wiper -- this moves when you turn the knob)
  Pin 3 ---- GND (-)

  On breadboard:
  1. Potentiometer pin 1: connect to + rail
  2. Potentiometer pin 3: connect to - rail
  3. Potentiometer pin 2: this IS Vout
```

**Wand Check -- Watch voltage change in real time:**

1. Set Wand to DC Volts
2. Red probe on pin 2 (Vout / wiper)
3. Black probe on - rail
4. SLOWLY turn the potentiometer knob
5. Watch the Wand display change!

> "As you turn the knob, you are changing the ratio of R1 to R2 inside the potentiometer. Turn all the way one direction: Vout = 0V. Turn all the way the other direction: Vout = 9V. Anywhere in between: any voltage you want!"

**Record some readings:**

```
| Knob Position | Wand Reads (Vout) |
|--------------|------------------|
| Fully left (counterclockwise) | _____ V |
| 1/4 turn | _____ V |
| Halfway | _____ V |
| 3/4 turn | _____ V |
| Fully right (clockwise) | _____ V |
```

> "The halfway position should read about 4.5V -- just like our equal-resistor divider! The potentiometer at halfway IS two equal resistors."

**Bonus -- Add an LED to Vout:**

Connect an LED + 330-ohm resistor from Vout to GND. Turn the knob.

> "When Vout is low, the LED is dim or off. When Vout is high, the LED is bright. You just built a dimmer switch using a voltage divider!"

**Award: +30 XP for building the potentiometer voltage divider and recording 5 readings!**

---

### Step 6: Why Are Voltage Dividers Useful? (3 min)

> "Voltage dividers are EVERYWHERE in electronics:"

1. **Sensors** -- Many sensors (light sensors, temperature sensors) are actually voltage dividers. When light changes the sensor's resistance, Vout changes, and a computer reads that change.

2. **Volume knobs** -- That volume control on speakers? It is a potentiometer acting as a voltage divider for the audio signal.

3. **Level shifting** -- A 5V signal needs to talk to a 3.3V device? A voltage divider steps it down safely.

4. **Battery monitoring** -- Robots check their battery level using a voltage divider to scale down the voltage to a range the microcontroller can read.

> "You will use voltage dividers with sensors in Module 3!"

**Award: +10 XP for naming one real-world use of voltage dividers!**

---

## Quick Quiz -- Earn Bonus XP!

**Question 1:** In a voltage divider with R1 = 1k and R2 = 1k, what is Vout if Vin is 10V?
- A) 10V
- B) 5V
- C) 0V

**(Correct: B -- equal resistors = half the voltage -- +20 XP!)**

**Question 2:** You increase R2 while keeping R1 the same. What happens to Vout?
- A) Vout goes up (R2 gets a bigger share)
- B) Vout goes down
- C) Vout stays the same

**(Correct: A -- bigger R2 means R2 gets more of the voltage, so Vout increases -- +20 XP!)**

**Question 3:** A potentiometer acts as a voltage divider. When the knob is exactly in the middle, what fraction of Vin appears at Vout?
- A) All of it (100%)
- B) Half (50%)
- C) None (0%)

**(Correct: B -- +20 XP!)**

**Bonus question for older kids (10+):**
> "You need exactly 3V from a 9V battery. You have a 1k-ohm resistor for R2. What value of R1 do you need?"
>
> Vout = Vin x R2/(R1+R2)
> 3 = 9 x 1000/(R1+1000)
> 3(R1+1000) = 9000
> R1 + 1000 = 3000
> R1 = 2000 ohms = 2k ohm

**(Correct: +30 XP bonus!)**

---

## Lesson 13 Complete!

```
  =============================================

     VOLTAGE DIVIDER DECODER BADGE UNLOCKED!

     Skills unlocked:
     [check] Built voltage dividers with fixed resistors
     [check] Used the formula to predict Vout
     [check] Verified predictions with the Wand
     [check] Built a variable divider with a potentiometer
     [check] Understand real-world voltage divider applications

  =============================================
```

**XP Breakdown:**
| Activity | XP |
|----------|-----|
| Hook -- pizza problem | 10 |
| Understand the concept | 10 |
| Calculate 2+ outputs | 30 |
| Formula vs Wand -- 3 dividers | 50 |
| Potentiometer divider | 30 |
| Real-world use | 10 |
| Quiz (3 questions) | 60 |
| Bonus question | 30 |
| **TOTAL POSSIBLE** | **230** |

---

## Coming Up Next...

In **Lesson 14**, you become a true **Multimeter Master**! This is the BIG lesson -- a deep dive into ALL FOUR superpowers of your Magic Measurement Wand: voltage, current, resistance, and continuity. You will learn advanced techniques, important safety rules, and become confident using your Wand in any situation!

---

## Troubleshooting

| Problem | Likely Cause | Fix |
|---------|-------------|-----|
| Vout reads 0V | R2 is disconnected | Check that R2 connects from the junction to GND |
| Vout reads 9V | R1 is disconnected | Check that R1 connects from Vin to the junction |
| Vout is way off from prediction | Wrong resistor values | Measure each resistor with the Wand in ohms mode first |
| Potentiometer does not change Vout | Wrong pins connected | Make sure pin 1 goes to +, pin 3 to -, and pin 2 is Vout |
| Vout changes when LED is connected | LED draws current, loading the divider | Use higher value resistors (10k each) or remove the LED when measuring Vout |

---

## Parent/Instructor Notes

- **Ages 6--8:** Focus on Round 1 (equal resistors = half voltage) and the potentiometer experiment. The formula is optional at this age. The key takeaway is: "two resistors can SPLIT voltage, and a knob can change the split."
- **Ages 9--12:** The formula calculations are the star. Have them predict ALL three rounds on paper, then build and measure. The thrill of the prediction matching the Wand is real scientific validation.
- **Loading effect:** When you connect an LED (or any load) to Vout, it draws current and can change the output voltage. This is called "loading" the voltage divider. For this lesson, measure Vout WITHOUT a load first (just the Wand probes), then observe the change when adding the LED. This is a subtle but important concept for advanced learners.
- The potentiometer experiment from Lesson 7 (Module 1) is revisited here with deeper understanding. Now the child knows WHY the voltage changes -- it is a variable voltage divider.
- Voltage dividers are the gateway to understanding sensor circuits in Module 3. Make sure this concept clicks before moving on.

---

## Navigation

| | |
|:---|---:|
| [← Lesson 12: Parallel Circuits -- Multiple Paths, Shared Voltage](lesson-12-parallel-circuits.md) | [Lesson 14: Using a Multimeter -- The Deep Dive →](lesson-14-using-a-multimeter.md) |

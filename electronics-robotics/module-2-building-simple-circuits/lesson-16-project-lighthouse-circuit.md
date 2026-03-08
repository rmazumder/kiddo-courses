# Lesson 16: Project -- The Lighthouse Circuit

**Module:** 2 -- Building Simple Circuits (FINAL PROJECT)
**Difficulty:** Star-2-Star-3 Medium
**Session Time:** 60--90 minutes (longer -- it is a project!)
**Age:** 6--12 years
**XP Available:** 360 XP (the biggest XP haul of Module 2!)

---

## Your Mission Today

This is it, Circuit Explorer -- the GRAND FINALE of Module 2! You are going to build a working **lighthouse** with a bright blinking LED, a hand-crafted tower, and a circuit that uses resistors, capacitors, and a transistor to flash automatically. You will use EVERYTHING you have learned: breadboarding, Ohm's Law, series and parallel knowledge, power selection, and -- most importantly -- your Magic Measurement Wand to test, verify, and debug every step. When you are done, you will have a real lighthouse you can put on your desk. Let us build something amazing!

---

## Learning Objectives

This project brings together everything from Module 2:
- Breadboard layout and wiring (Lesson 9)
- Ohm's Law for resistor selection (Lesson 10)
- Series circuit concepts -- components in a chain (Lesson 11)
- Understanding of parallel paths (Lesson 12)
- Voltage divider principles for timing (Lesson 13)
- ALL four multimeter modes for debugging (Lesson 14)
- Power source selection (Lesson 15)
- Creative building and problem-solving

---

## What You Need

| Item | Qty |
|------|-----|
| 9V battery + clip | 1 |
| Breadboard | 1 |
| Bright white or yellow LED | 1 |
| Red LED (for status indicator) | 1 |
| 2N2222 NPN transistor | 1 |
| 100-microfarad electrolytic capacitor | 1 |
| 1000-microfarad electrolytic capacitor | 1 |
| Resistors: 330-ohm, 1k-ohm, 10k-ohm, 100k-ohm | 1 each |
| Toggle switch | 1 |
| Jumper wires | 10 |
| Multimeter (Magic Measurement Wand) | 1 |
| Cardboard paper towel or toilet paper tube | 1 |
| White tissue paper or translucent plastic | 1 piece |
| Tape (electrical + masking) | 1 roll each |
| Scissors | 1 |
| Colored markers or paint (optional) | 1 set |
| Small cardboard square (for the base) | 1 |

---

## What Are We Building?

A lighthouse that:
- Blinks a bright LED on and off automatically (no manual pressing!)
- Has an on/off switch
- Is built on a breadboard and housed in a paper tube tower
- Uses a capacitor + resistor + transistor to create the blinking effect

```
  THE LIGHTHOUSE
  ==============

       (LED glows here)
      .---.
     /  O  \    <-- translucent paper diffuser
    |  LED  |
    |       |
    |  tube |   <-- paper towel tube
    |       |
    |       |
  +---------+
  | BREADBOARD | <-- circuit inside / on base
  | + battery  |
  +-----------+
```

---

## How to Build It

### Phase 1: Understand the Blinker Circuit (8 min)

![A four-stage circular diagram showing the blinker (astable multivibrator) cycle, arranged like a clock with arrows flowing clockwise. Stage 1 (top, red/orange): "Capacitor Charging" with a capacitor icon filling up (progress bar increasing), current flowing into it. Stage 2 (right, blue): "Transistor Turns ON" with the transistor gate opening, current flowing through to the LED. Stage 3 (bottom, yellow with glow): "LED Bright!" with a glowing LED at full brightness and the label "Capacitor fully charged." Stage 4 (left, green): "Capacitor Discharging" with the capacitor emptying (progress bar decreasing), transistor turning off, LED going dark. Circular arrows connect all four stages in a continuous loop with a label in the center: "This cycle repeats forever = BLINKING!" A cartoon lighthouse character winks in the center of the cycle. Each stage has a small circuit snapshot showing the state of each component.](images/lesson-16-blinker-cycle.png)

> "The secret to blinking is a CAPACITOR. Remember from Module 1 how a capacitor charges up and then releases its energy? We are going to use that charge-discharge cycle to turn a transistor ON and OFF repeatedly -- and that will blink the LED!"

**How the blinker works (simplified):**

```
  The Blinker Cycle:

  Step 1: Capacitor charges through a resistor (LED OFF)
           Voltage on capacitor rises slowly...

  Step 2: When capacitor voltage reaches about 0.7V,
           the transistor switches ON

  Step 3: Transistor ON = LED ON (lighthouse beam!)

  Step 4: Capacitor discharges through the transistor
           Voltage drops below 0.7V

  Step 5: Transistor switches OFF = LED OFF

  Step 6: Capacitor starts charging again...
           (back to Step 1 -- the cycle repeats!)
```

> "The resistor and capacitor together control HOW FAST the blinking happens. Bigger resistor or bigger capacitor = SLOWER blink. Smaller = FASTER blink."

**The time formula (for ages 9--12):**

```
  Blink time is roughly:  T = R x C

  Example:
  R = 100k ohm = 100,000 ohms
  C = 100 microfarad = 0.0001 Farads

  T = 100,000 x 0.0001 = 10 seconds per cycle

  (In reality, the charge/discharge is not perfectly symmetric,
   so the ON and OFF times may differ. That is OK!)
```

**Award: +20 XP for understanding how the blinker circuit works!**

---

### Phase 2: Build the Blinker Circuit (15 min)

![A circuit schematic where every component is drawn as a friendly cartoon character with arms, legs, and expressive faces. The battery character (red/orange, strong and smiling) pushes energy into the circuit. A switch character (a gate keeper opening and closing a door) sits at the entrance. A resistor character (wearing a crossing-guard vest, labeled with its value) slows down the flow. A capacitor character (a chubby balloon-like figure that inflates and deflates) stores and releases energy. A transistor character (a small figure with one hand on a big valve lever, labeled E-B-C) controls the main flow. An LED character (a glowing lightbulb-headed figure at the top of a lighthouse tower shape) lights up when current arrives. Colored wires connect them: red/orange from battery, blue through the main path, green to ground. Each character has a one-word role label. The overall layout forms the actual circuit topology so students can follow the connections.](images/lesson-16-cartoon-circuit-diagram.png)

**Circuit diagram:**

```
  9V (+) ----[toggle switch]----+----[1k-ohm]----LED (+)----LED (-)----+
                                |                                      |
                                +----[100k-ohm]----+                   |
                                |                  |                   |
                                |              Base (B)                |
                                |                  |                   |
                                |         [2N2222 transistor]          |
                                |              |       |               |
                                |         Collector  Emitter           |
                                |              |       |               |
                                |              +       +---- GND -----+
                                |              |
                                +----[100uF cap (+)]----cap (-)---- GND
```

**Simplified explanation:**

> "The 100k-ohm resistor slowly charges the 100-microfarad capacitor. When the capacitor gets enough charge, the transistor turns on and the LED lights up. Then the capacitor releases its charge, the transistor turns off, and the LED goes dark. This repeats forever!"

**Step-by-step breadboard build:**

```
  BREADBOARD LAYOUT:

  Row 1-2: Power
  - Toggle switch: one terminal in + rail, other terminal in row 2
  - When switch is ON, row 2 gets 9V

  Row 5: Timing resistor
  - 100k-ohm resistor: row 2 to row 5

  Row 5: Capacitor
  - 100-microfarad capacitor: (+) leg in row 5, (-) leg in - rail
  - WATCH POLARITY! Stripe (negative) goes to - rail

  Row 5: Transistor Base
  - 2N2222 transistor: Base (B) in row 5
  - Collector (C) in row 8
  - Emitter (E) in - rail (GND)

  Row 8: LED circuit
  - 1k-ohm resistor: row 2 to row 8 (connects to Collector)
  - LED: Collector row -- actually, let us wire it clearly:
    - 1k-ohm resistor: one leg in row 2, other leg in row 10
    - LED: long leg (+) in row 10, short leg (-) in row 12
    - Jumper: row 12 to Collector row of transistor (row 8)

  Battery:
  - Red wire to + rail
  - Black wire to - rail
```

> "Take your time wiring this. Every connection matters. If one wire is in the wrong row, the whole circuit will not work."

**Award: +40 XP for building the complete blinker circuit!**

---

### Phase 3: Wand Check -- Verify Before Power On! (10 min)

> "Before we flip the switch, let us make sure everything is connected correctly. Grab your Wand!"

**Pre-power continuity checks (battery DISCONNECTED):**

Set Wand to continuity mode.

```
| Test | From | To | Expected | Beep? |
|------|------|-----|----------|-------|
| 1 | Switch terminal 1 | + rail | Direct connection | YES |
| 2 | Switch terminal 2 | row 2 | Direct connection | YES |
| 3 | 100k resistor (row 2 end) | row 5 | Through resistor | YES |
| 4 | Capacitor (+) | row 5 | Direct connection | YES |
| 5 | Capacitor (-) | - rail | Direct connection | YES |
| 6 | Transistor Base | row 5 | Direct connection | YES |
| 7 | Transistor Emitter | - rail | Direct connection | YES |
| 8 | LED short leg row | Transistor Collector | Through wire | YES |
```

> "All beeps? Then the wiring is correct. No beep on any test? Check that connection -- something is loose."

**Component verification (still no power):**

1. **Measure the 100k resistor:** Set Wand to ohms. Expected: about 100,000 ohms.
2. **Measure the 1k resistor:** Expected: about 1,000 ohms.
3. **Check LED polarity:** Long leg should be on the + side (closer to the resistor).
4. **Check capacitor polarity:** Stripe (negative) should face GND (- rail).
5. **Check transistor orientation:** Flat side facing you, legs should be E-B-C from left to right.

**Award: +40 XP for completing ALL pre-power verification checks!**

---

### Phase 4: Power On and Test! (5 min)

> "Everything checked. Deep breath. Flip the switch!"

Connect the battery and flip the toggle switch ON.

**What should happen:**

The LED should start blinking! It may take a second or two for the first blink as the capacitor charges for the first time.

> "IT BLINKS! Your lighthouse beam is working!"

**Observe:**

> "How fast is it blinking? Count the blinks in 10 seconds."

If it does not blink (LED stays on or stays off), do not panic! We will debug in Phase 5.

**Award: +30 XP for a successfully blinking LED!**

---

### Phase 5: Wand-Assisted Debugging (if needed) (10 min)

> "If the LED does not blink, your Wand will find the problem. Here is your debugging workflow."

**The Debugging Flowchart:**

```
  LED does not light at all:
  |
  +-- Measure battery: is it above 8V?
  |   NO --> Replace battery
  |   YES --> Continue
  |
  +-- Check switch: Wand continuity across switch (when ON)
  |   NO BEEP --> Switch is off or broken
  |   BEEP --> Continue
  |
  +-- Measure voltage at row 2 (after switch): should be about 9V
  |   0V --> Switch wiring issue
  |   9V --> Continue
  |
  +-- Check LED polarity: is long leg on + side?
  |   NO --> Flip the LED
  |   YES --> Continue
  |
  +-- Measure voltage across LED: should show 2-3V when lit
  |   0V --> Transistor is not turning on; check base circuit
  |   2-3V --> LED might be burned out; try a new one


  LED stays ON (does not blink):
  |
  +-- Measure voltage at transistor Base (row 5) to GND
  |   About 0.7V --> Transistor is permanently ON
  |   Check capacitor polarity and 100k resistor value
  |
  +-- Is the capacitor connected correctly?
  |   (+) to row 5, (-) to GND?
  |
  +-- Is the 100k resistor really 100k?
      Measure it! Maybe it is the wrong resistor.


  LED stays OFF:
  |
  +-- Measure voltage at row 5 (base): does it rise over time?
  |   YES but never reaches 0.7V --> 100k might be too large; try smaller
  |   NO change --> Check capacitor and 100k resistor connections
```

**Debugging journal:**

```
| Symptom | Wand Mode | Measurement | Problem Found | Fix Applied |
|---------|----------|------------|--------------|-------------|
|         |          |            |              |             |
|         |          |            |              |             |
|         |          |            |              |             |
```

> "Debugging is the MOST important skill in electronics. You just used EVERY Wand mode -- voltage, continuity, resistance -- to systematically find and fix a problem. This is EXACTLY what professional engineers do every day."

**Award: +40 XP for successfully debugging (or confirming everything works)!**

---

### Phase 6: Experiment with Blink Speed (5 min)

> "Now let us play with the blink speed!"

**Experiment 1 -- Faster blink:**

Replace the 100-microfarad capacitor with a smaller value, or replace the 100k-ohm resistor with a smaller value (like 47k or 10k).

> "What happened? It blinks faster! Smaller R or C = faster charging = faster blinking."

**Experiment 2 -- Slower blink:**

Replace the 100-microfarad capacitor with the 1000-microfarad capacitor.

> "Now it blinks much slower -- like a real lighthouse! The bigger capacitor takes longer to charge."

**Record your experiments:**

```
| Resistor | Capacitor | Blink Speed (blinks per 10 sec) |
|----------|-----------|-------------------------------|
| 100k     | 100uF     |                               |
| 100k     | 1000uF    |                               |
| 10k      | 100uF     |                               |
```

**Award: +20 XP for experimenting with at least 2 different blink speeds!**

---

### Phase 7: Build the Lighthouse Tower (10 min)

![A finished lighthouse project model shown as a 3D illustration. The lighthouse tower is made from a rolled paper tube (decorated with red and white horizontal stripes like a real lighthouse), standing on a sturdy breadboard base. At the top of the paper tube, a bright LED pokes through a small hole, casting a warm yellow-orange glow with light ray lines radiating outward. The breadboard base is visible with the blinker circuit neatly wired: battery pack, switch, resistors, capacitor, and transistor are all identifiable on the board. Wires trail up inside the tube to the LED at the top. A small on/off toggle switch is accessible on the side of the base. The LED is shown mid-blink with a "flash" starburst effect. A cartoon kid stands proudly next to their creation, arms wide, with a speech bubble: "I built this!" The scene has a slightly darkened background to make the lighthouse glow stand out dramatically.](images/lesson-16-finished-lighthouse.png)

> "Now the fun part -- building the lighthouse itself!"

**Step 1: The tower**
- Take the cardboard tube (paper towel roll)
- Optional: paint it with red and white stripes, or wrap with colored tape

**Step 2: The light chamber**
- At the top of the tube, tape a piece of white tissue paper or translucent plastic over the opening
- This is the "diffuser" -- it spreads the LED light and makes it glow evenly

**Step 3: Mount the LED**
- Extend the LED wires (using jumper wires if needed) up through the tube
- Position the LED at the top, behind the tissue paper
- Tape or hot-glue the LED in place (adult helps with hot glue)

**Step 4: The base**
- Place the breadboard on a small piece of cardboard
- Stand the tube on the cardboard, next to the breadboard
- Route wires neatly from breadboard up into the tube

**Step 5: Add the status LED (optional)**
- Wire a small red LED (with 330-ohm resistor) in parallel from the + rail to - rail
- This stays ON whenever the switch is on, showing the lighthouse is "powered"

```
  Finished Lighthouse:

       .----.
      / O O  \   <-- tissue paper diffuser
     |  (LED) |       with blinking LED behind it
     |--------|
     |  tube  |   <-- decorated tower
     |  tube  |
     |  tube  |
  +--+--------+--+
  | breadboard    |
  | + battery     |
  | + switch      |
  | (red status LED) |
  +--------------+
```

**Award: +30 XP for building the lighthouse tower!**

---

### Phase 8: Final Wand Check -- The Complete Diagnostic (5 min)

> "One last mission. Prove to me that EVERYTHING in your circuit is correct by taking these measurements."

**Final diagnostic table:**

```
| Measurement | Wand Mode | Expected | My Reading |
|------------|----------|---------|-----------|
| Battery voltage | DC Volts | 8.5--9.5V | |
| Voltage at row 2 (switch ON) | DC Volts | about 9V | |
| 100k resistor value | Ohms | about 100k | |
| 1k resistor value | Ohms | about 1k | |
| Voltage across LED (when ON) | DC Volts | 2--3.5V | |
| Base voltage (when LED is ON) | DC Volts | about 0.6--0.7V | |
| Continuity: switch ON | Continuity | BEEP | |
| Continuity: + rail to - rail | Continuity | NO BEEP | |
```

> "You just ran a COMPLETE diagnostic on your lighthouse circuit. You measured voltage, resistance, and continuity. You understand every part of this circuit. You are a true Circuit Builder!"

**Award: +30 XP for completing the full diagnostic!**

---

## Module 2 Final Assessment

After building the lighthouse, have the kid answer these:

**Circuit Knowledge:**
1. "What is Ohm's Law?" (V = I x R)
2. "What is the difference between series and parallel circuits?" (Series = one path, parallel = multiple paths)
3. "In a voltage divider with equal resistors, what is Vout?" (Half of Vin)
4. "What makes the LED blink in the lighthouse?" (Capacitor charging and discharging through the transistor)

**Wand Skills Check:**
5. "Measure the battery." (DC Volts mode, probes in V/ohm and COM)
6. "Measure the 1k resistor." (Ohms mode, power off)
7. "Test this wire with continuity." (Continuity mode, listen for beep)
8. "Where would you put the probes to measure current through the LED?" (Break the circuit, insert Wand in series, red probe in mA jack)

**Award: +50 XP for completing the final assessment!**

---

## Quick Quiz -- Earn Bonus XP!

**Question 1:** Why does the LED in the lighthouse blink?
- A) The battery turns on and off
- B) A capacitor charges and discharges, turning a transistor on and off
- C) The switch has a timer inside

**(Correct: B -- +20 XP!)**

**Question 2:** You want the lighthouse to blink SLOWER. What should you change?
- A) Use a SMALLER capacitor
- B) Use a BIGGER capacitor (or bigger resistor)
- C) Use a brighter LED

**(Correct: B -- bigger capacitor or resistor = slower charging = slower blink -- +20 XP!)**

**Question 3:** Your lighthouse LED does not light at all. What is the FIRST thing you should check with your Wand?
- A) Measure the LED voltage
- B) Measure the battery voltage to make sure it is charged
- C) Measure resistance of the resistor

**(Correct: B -- always check the power source first! -- +20 XP!)**

---

## Module 2 Complete -- Grand Finale!

```
  ======================================================

     MODULE 2 CHAMPION BADGE UNLOCKED!

     _____________________ has mastered
        Building Simple Circuits

     [check] Breadboard mastery
     [check] Ohm's Law (V = I x R)
     [check] Series circuits
     [check] Parallel circuits
     [check] Voltage dividers
     [check] ALL four multimeter modes
     [check] Power sources and batteries
     [check] Built a blinking lighthouse!

  ======================================================
```

**Lesson 16 XP Breakdown:**
| Activity | XP |
|----------|-----|
| Understand blinker circuit | 20 |
| Build the blinker circuit | 40 |
| Pre-power Wand verification | 40 |
| Successful blink (power on) | 30 |
| Wand-assisted debugging | 40 |
| Blink speed experiments | 20 |
| Build the lighthouse tower | 30 |
| Final diagnostic | 30 |
| Final assessment | 50 |
| Quiz (3 questions) | 60 |
| **TOTAL POSSIBLE** | **360** |

---

## Module 2 Total XP Summary

| Lesson | Title | Max XP |
|--------|-------|--------|
| 9 | The Breadboard | 230 |
| 10 | Ohm's Law | 240 |
| 11 | Series Circuits | 220 |
| 12 | Parallel Circuits | 230 |
| 13 | Voltage Dividers | 230 |
| 14 | Using a Multimeter (Deep Dive) | 260 |
| 15 | Power Sources | 210 |
| 16 | Lighthouse Project | 360 |
| **MODULE 2 TOTAL** | | **1,980** |

**Combined with Module 1 (2,030 XP): Grand Total Available = 4,010 XP**

**XP Ranks (cumulative):**
- 0--500 XP: Circuit Apprentice
- 501--1,000 XP: Circuit Explorer
- 1,001--1,500 XP: Circuit Builder
- 1,501--2,000 XP: Circuit Engineer
- 2,001--2,500 XP: Circuit Scientist
- 2,501--3,500 XP: Circuit Wizard
- 3,501--4,010 XP: Circuit Master!

---

## All Badges Earned in Module 2

| Badge | Lesson |
|-------|--------|
| Breadboard Navigator | Lesson 9 |
| Ohm's Law Apprentice | Lesson 10 |
| Series Circuit Specialist | Lesson 11 |
| Parallel Circuit Pro | Lesson 12 |
| Voltage Divider Decoder | Lesson 13 |
| Multimeter Master | Lesson 14 |
| Power Source Expert | Lesson 15 |
| Module 2 Champion | Lesson 16 |

---

## Reflection Questions (Talk Through Together)

> "What was the coolest thing you built or discovered in Module 2?"
> "Which lesson was the hardest? What made it click?"
> "Which Wand mode are you MOST confident with now?"
> "Can you explain Ohm's Law to a friend?"
> "If you could change one thing about your lighthouse, what would it be?"
> "What do you think Module 3 will be about?"

---

## What's Next -- Module 3 Preview

> "You now know how to build real circuits, measure everything with your Wand, and debug like a pro! In Module 3, we enter the world of **integrated circuits and sensors**. You will meet the famous 555 timer chip, build a light-sensing circuit, and start connecting electronics to the real world. The journey from circuits to ROBOTS is getting closer!"

---

## Parent/Instructor Notes

- This project takes longer than a regular lesson -- plan for **60--90 minutes** or split across two sessions (build circuit in session 1, build tower + test in session 2).
- **The debugging phase (Phase 5) is the most valuable part of this lesson.** If the circuit works on the first try, consider intentionally introducing a bug (reversed LED, wrong resistor, loose wire) and having the child find it with the Wand.
- The blinker circuit described here is a simplified relaxation oscillator. It is not a perfect square wave, and blink timing may vary. That is fine -- the learning goal is understanding RC timing and transistor switching, not precision.
- For a more reliable blinker, consider using a 555 timer IC (covered in Module 3). But the transistor + capacitor version is better for learning because every component has a clear role the child already understands.
- **Ages 6--8:** Focus on building the tower and watching it blink. The debugging and measurement phases can be done together with an adult guiding. The key win is "I built a lighthouse that blinks by itself!"
- **Ages 9--12:** Challenge them to predict the blink rate using T = R x C before building. Have them adjust values to hit a target blink rate (e.g., "Can you make it blink once every 5 seconds?").
- The lighthouse makes an excellent **show-and-tell** piece. Encourage the child to explain how the circuit works to family members.
- Take a photo or video of the finished lighthouse for their portfolio!
- **Celebrate completion of Module 2!** This is a major milestone. Consider a small reward, certificate, or special outing.

---

## Navigation

| | |
|:---|---:|
| [← Lesson 15: Power Sources -- Batteries, Volts, and Energy](lesson-15-power-sources.md) | [Module Overview →](README.md) |

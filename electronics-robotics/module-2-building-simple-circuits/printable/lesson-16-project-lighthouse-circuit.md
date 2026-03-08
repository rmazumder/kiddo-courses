# Lesson 16: Project -- The Lighthouse Circuit

**Module 2 FINAL PROJECT** | **Difficulty:** Medium | **Time:** 60--90 min | **XP:** 360

---

## Your Mission

Build a working **lighthouse** with a bright blinking LED that automatically flashes on and off using a capacitor, resistor, and transistor. No pushing buttons -- the circuit does the blinking ALL ON ITS OWN!

This project combines EVERYTHING from Module 2:
✓ Breadboarding | ✓ Ohm's Law | ✓ Series/Parallel | ✓ Voltage Dividers
✓ Multimeter skills | ✓ Power sources | ✓ Creative building

---

## Understanding the Blinker: The Charge-Discharge Cycle

![A four-stage circular diagram showing the blinker cycle. Stage 1 (top): "Capacitor Charging" with a filling capacitor and current arrows. Stage 2 (right): "Transistor ON" with the transistor gate opening. Stage 3 (bottom): "LED Bright!" with a glowing LED at full brightness. Stage 4 (left): "Capacitor Discharging" with the capacitor emptying. Circular arrows show the continuous loop with "This cycle repeats forever = BLINKING!" in the center.](../images/lesson-16-blinker-cycle.png)

**How the automatic blinking works:**

```
Step 1: Capacitor charges through a resistor
        (LED stays OFF while charging)

Step 2: Capacitor reaches 0.7V threshold
        → Transistor SWITCHES ON

Step 3: LED LIGHTS UP (transistor conducts current)
        Capacitor discharges through transistor

Step 4: Capacitor voltage drops below 0.7V
        → Transistor SWITCHES OFF

Step 5: LED goes DARK
        Back to Step 1... cycle repeats!
```

**Why this works:**
- Capacitor stores and releases energy
- Transistor acts like an automatic switch (no human required!)
- Resistor controls how FAST the capacitor charges
- Result: **AUTOMATIC BLINKING!**

**Speed formula (for ages 9--12):**
```
Blink period ≈ R × C

Example:
R = 100k ohm = 100,000 ohms
C = 100 microfarad = 0.0001 Farads
Period = 100,000 × 0.0001 = 10 seconds per cycle

Bigger R or C = SLOWER blinking
Smaller R or C = FASTER blinking
```

---

## The Complete Circuit Diagram

![Circuit schematic with friendly cartoon characters: battery (strong/smiling), switch (gate keeper), resistors (crossing guards), capacitor (chubby balloon), transistor (figure at valve lever), and LED (glowing lightbulb). Colors match wire colors: red/orange for +, blue for signal paths, green for ground. Layout shows actual topology.](../images/lesson-16-cartoon-circuit-diagram.png)

**What each component does:**

| Component | Role | Value |
|-----------|------|-------|
| **Toggle Switch** | ON/OFF control | (any switch) |
| **100k-Ω resistor** | Charges capacitor slowly | 100,000 Ω |
| **100μF capacitor** | Stores charge, creates timing | 100 microfarad |
| **2N2222 transistor** | Automatic switch (controlled by capacitor) | (specific transistor) |
| **1k-Ω resistor** | Protects LED from too much current | 1,000 Ω |
| **LED** | The lighthouse beam! | White/yellow bright |

---

## Build It: Step-by-Step Breadboard Layout

**CRITICAL: Polarity matters for capacitor and LED!**

```
LAYOUT ZONES:

[+RAIL] ----[Toggle Switch]----[ROW 2]

ROW 2 branches to:
  → 100k-Ω (to ROW 5)
  → 1k-Ω (to ROW 10)

ROW 5: Junction point for timing
  → 100k-Ω resistor
  → Capacitor (+) leg
  → Transistor Base (B)

ROW 8: Transistor Collector
  → Connects to LED circuit

ROW 10-12: LED circuit
  → 1k-Ω resistor (ROW 2 to ROW 10)
  → LED long leg (+) in ROW 10
  → LED short leg (−) in ROW 12
  → ROW 12 back to Transistor Collector

[-RAIL] GND: All negative connections
  → Capacitor (−) leg
  → Transistor Emitter (E)
  → LED short leg via resistor

TRANSISTOR PIN ORIENTATION (looking at flat side):
  Left pin = Base (B)
  Middle pin = Collector (C)
  Right pin = Emitter (E)
```

**Assembly steps:**
1. Mount all components on breadboard
2. Wire step-by-step (don't rush!)
3. DOUBLE-CHECK all connections before applying power
4. Use Wand to verify before turning on

---

## Verify Before Power-On: The Wand Checks

**Set Wand to CONTINUITY (beep test):**

| Check | Should... | Wand Says... |
|-------|-----------|-------------|
| Battery + to + rail | BEEP | ✓ |
| Battery − to − rail | BEEP | ✓ |
| Switch connects to row 2 | BEEP (when ON) | ✓ |
| Capacitor polarity | Stripe to −rail | ✓ |

**Set Wand to DC VOLTAGE (circuit OFF):**

| Measurement | Before Power | Expected |
|-------------|-------------|----------|
| Battery voltage | 9V | ~9V |
| Ground continuity | 0V baseline | ✓ |

✓ **Only turn on power after ALL checks pass!**

---

## Troubleshooting Guide

| Problem | Likely Cause | Fix |
|---------|-------------|-----|
| Nothing happens (no blink) | Power not connected | Check battery, toggle switch |
| LED stays ON constantly | Transistor not switching | Check Base connection to capacitor junction |
| LED stays OFF always | Wrong LED polarity or bad transistor | Flip LED, test transistor with Wand |
| Blinks too fast | Resistor or capacitor wrong value | Check values match (100k and 100µF) |
| Blinks too slow | Same as above | Same fix |
| One corner bright, rest dim | Poor connection on LED | Check all LED circuit wires |
| Smoke/heat from any component | STOP IMMEDIATELY! | Disconnect power, check polarity, inspect |

---

## Finishing Touches: Build the Tower

**Make a lighthouse tower:**

1. Take cardboard tube (paper towel or toilet paper)
2. Wrap with colored paper (optional: paint base)
3. Cut hole near top for LED
4. Insert bright white/yellow LED through hole
5. Wrap translucent tissue paper around LED opening (diffuser)
6. Place breadboard with circuit inside or under tube base
7. Add decorative details (windows, paint, lighthouse colors)

**Result:** Real working lighthouse on your desk! 🗼✨

---

## The Complete Challenge

**By the end of this project, you will have:**
- ✓ Built an advanced circuit with transistor + capacitor
- ✓ Understood automatic switching (transistor as electronic switch)
- ✓ Used your Wand to verify everything works
- ✓ Created a physical lighthouse structure
- ✓ Mastered EVERY skill from Module 2

---

## XP Breakdown (360 total!)

| Achievement | XP |
|-------------|-----|
| Understand blinker cycle | 20 |
| Build complete circuit | 40 |
| Wand verification checks | 30 |
| Successful first power-on | 50 |
| Troubleshoot any issues | 40 |
| Physical tower construction | 30 |
| Test and refine blinking rate | 30 |
| Final demonstration | 40 |
| **BONUS: Advanced modifications** | 40 |
| **TOTAL POSSIBLE** | **360** |

---

## Advanced Modifications (Bonus XP!)

Once basic lighthouse works, try these:

**Faster/slower blinking:**
- Change 100k resistor to 10k (faster) or 1M (slower)
- Or change capacitor value
- Measure with Wand to verify timing

**Dual light:**
- Add second LED in parallel with first
- Both blink together!

**Add status indicator:**
- Red LED that's always ON when circuit has power
- Shows circuit is alive

**Different patterns:**
- Add second capacitor circuit for more complex rhythm
- Challenge: Create a sequence (fast-slow-fast)

---

## Key Takeaways from Module 2

1. **Breadboards** are your prototyping best friend
2. **Resistors** protect components and control behavior
3. **Capacitors** store energy and create timing
4. **Transistors** are electronic switches (can be controlled by voltage)
5. **Your Wand** is your debugging superpower
6. **Combining skills** = amazing projects!

---

## Celebrating Completion

🎉 **You've completed Module 2: Building Simple Circuits!**

You now know:
- How to breadboard like a pro
- Ohm's Law (V = I × R)
- Series vs. parallel circuits
- Voltage dividers
- All four multimeter modes
- Battery selection and configuration
- Automatic blinking circuits!

**Next:** Module 3 starts sensors and Arduino programming!

---

*Print this page. Keep your lighthouse working. You're a real electronics engineer now!* 🏆


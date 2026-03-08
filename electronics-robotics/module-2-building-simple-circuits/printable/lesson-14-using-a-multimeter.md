# Lesson 14: Using a Multimeter -- Quick Reference

**Age:** 6--12 years | **Time:** 45--50 min | **XP:** 240

---

## What You'll Learn

✓ Master FOUR superpowers of your Multimeter (Wand):
  1. **Voltage** - How hard the battery pushes
  2. **Resistance** - How much a component blocks electricity
  3. **Current** - How much electricity flows
  4. **Continuity** - Is the circuit complete or broken?

---

## The Four Superpowers

![Poster showing four sections. Superpower 1: Lightning bolt labeled "VOLTAGE (Volts)" - measuring battery push, ranges shown. Superpower 2: Shield labeled "RESISTANCE (Ohms)" - measuring component blocking. Superpower 3: Water flow labeled "CURRENT (Amps/mA)" - measuring electricity flow. Superpower 4: Beep symbol labeled "CONTINUITY (Ohms)" - testing if circuit is complete. Each section has color coding and emoji symbols.](../images/lesson-14-four-superpowers-poster.png)

---

## Superpower 1: VOLTAGE (DC Volts)

**What it measures:** How hard the battery pushes electricity

**How to use:**
1. Set dial to **DC V** (or 20V, 200V depending on expected voltage)
2. RED probe touches HIGH point (+)
3. BLACK probe touches LOW point (− or GND)
4. Read the display!

**Probe connections:**
- RED → **V/Ω** jack (top)
- BLACK → **COM** jack (bottom, common/ground)

| Component | Typical Voltage |
|-----------|-----------------|
| 9V battery | 9V |
| AA battery (fresh) | 1.5V |
| Battery (low) | 0.8V |
| Across LED (forward voltage) | ~2V |
| Across resistor (with current) | varies |

✓ **Never move probes while measuring — accidental short!**

---

## Superpower 2: RESISTANCE (Ohms)

**What it measures:** How much a component resists (blocks) electricity

**How to use:**
1. **DISCONNECT power first** (remove battery!)
2. Set dial to **Ω** (ohms)
3. Select range: 200Ω, 2k, 20k, 200k (start highest if unsure)
4. Touch RED probe to one end, BLACK to other end
5. Read the display!

**Probe connections:**
- RED → **V/Ω** jack
- BLACK → **COM** jack

| Component | Expected Resistance |
|-----------|-------------------|
| 330Ω resistor | ~330Ω |
| 1kΩ resistor | ~1000Ω |
| Fresh LED (no current) | very high (MΩ range) |
| Resistor's wire leads | ~0Ω (perfect conductor) |
| Broken wire | **∞ (infinite)** |

⚠️ **Key rule: Disconnect power before measuring resistance!**
(Otherwise Wand's internal battery tries to push through powered circuit)

---

## Superpower 3: CURRENT (Amps / mA)

**What it measures:** How much electricity is flowing

**How to use:**
1. Set dial to **DC A** or **mA** (milliamps)
2. Move RED probe to **A** or **mA** jack (IMPORTANT!)
3. **BREAK the circuit** - the Wand must be PART of the current flow
4. Meter probes complete the circuit
5. Read the display!

**SAFETY RULES:**
- ✓ Ammeter goes IN SERIES (part of circuit)
- ✗ Never connect ammeter ACROSS a battery directly = shorts the meter!
- Start on HIGHEST range (10A, then 200mA, then 20mA)
- If meter shows "OL", switch to higher range

**Probe connections:**
- RED → **mA** or **A** jack (depends on meter - NOT V/Ω!)
- BLACK → **COM** jack

| Circuit Element | Expected Current |
|-----------------|-----------------|
| 9V → 330Ω resistor → LED → GND | ~20mA |
| Single branch of parallel circuit | ~15-25mA |
| Whole circuit total | depends on design |
| Dead battery attempt | very small or 0mA |

✓ **This is the one skill that requires circuit modification!**

---

## Superpower 4: CONTINUITY (Beep Test)

**What it measures:** "Is this circuit complete or broken?"

**How to use:**
1. Set dial to **Ω Ω** symbol (looks like musical note or ohms with beep icon)
2. **Disconnect power**
3. Touch RED to one end, BLACK to other
4. If continuous: **BEEP!** (reads 0Ω or very low)
5. If broken: **No beep** (reads ∞ or "OL")

**Use for:**
- Testing wires (good wire = beep)
- LED polarity (short leg = cathode, long leg = anode)
- Checking component connections
- Finding a broken wire in a bundle

| Situation | Wand Does What |
|-----------|-----------------|
| Good wire end-to-end | ✓ BEEP! (0Ω) |
| Broken wire | ✗ No beep (∞) |
| LED long leg to short leg (forward) | ✓ Beep or low ohms |
| LED wrong way (reverse) | ✗ High resistance, no beep |

---

## Debugging Flowchart

![Flowchart starting with "Circuit not working?" Then branches: "Does battery have voltage?" Yes→next. No→replace battery. "Can you measure current?" Yes→next. No→open circuit (broken wire). "Is voltage where expected?" Yes→component issue. No→voltage divider problem. Multiple paths to solutions.](../images/lesson-14-debugging-flowchart.png)

**When a circuit fails, use your Wand systematically:**

1. **Check voltage** - Is battery good? (should be ~9V)
2. **Check continuity** - Are all wires connected? (should beep)
3. **Check current** - Is electricity flowing? (should show mA)
4. **Check resistance** - Do components have expected values? (compare to labels)
5. **Measure at key points** - Map voltage drops along the circuit

---

## Common Mistakes

| Mistake | Problem | Fix |
|---------|---------|-----|
| Measuring resistance with power ON | Meter gets confused or damaged | Turn OFF power first! |
| Ammeter connected across battery | Short circuit, blows fuse | Ammeter IN SERIES only |
| RED probe in wrong jack | Measures nothing or wrong value | Check: V/Ω for voltage/resistance, mA for current |
| No contact with component | Reads nothing or bounces | Press probe tips firmly |
| Wrong range selected | Shows "OL" or too small value | Start with highest range, work down |

---

## Key Takeaways

1. **VOLTAGE (V):** Battery push - RED to +, BLACK to − (or GND)
2. **RESISTANCE (Ω):** Component blocking - Power OFF first!
3. **CURRENT (mA):** Electricity flow - Ammeter goes IN SERIES
4. **CONTINUITY (beep):** Circuit complete or broken? - Beep = good, no beep = broken
5. **Systematic debugging:** Voltage → Continuity → Current → Resistance

---

## Quick Quiz (Test Yourself!)

**Q1:** You want to measure voltage across an LED. Probe positions?
✓ **Answer:** RED on + side of LED, BLACK on − side (measures forward voltage ~2V)

**Q2:** Your ammeter reads "OL" when measuring current. What do you do?
✓ **Answer:** Switch to a HIGHER current range (like 10A instead of 200mA)

**Q3:** Before measuring resistance, what's the critical step?
✓ **Answer:** Disconnect power from circuit!

---

## Master Level

Try this debugging challenge:
- Build a circuit: Battery → Resistor → LED → GND
- LED doesn't light
- Use your Wand to find the problem:
  - Is battery voltage OK?
  - Is current flowing?
  - Is any component broken?

---

*Print this page. You are now a Circuit Detective!*

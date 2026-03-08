# Lesson 18: 555 Timer Astable -- The Blinker Mode

**Age:** 6--12 years | **Time:** 45--50 min | **XP:** 220

---

## What You'll Learn

✓ How the 555 timer blinks automatically (without pushing a button!)
✓ Astable mode = "free-running" oscillator
✓ Use resistors + capacitor to control blink speed
✓ Build a circuit that pulses forever and ever
✓ Calculate blink frequency from resistor/capacitor values

---

## The Heartbeat Analogy

**The 555 in Astable mode is like your heart:**

```
Your Heart:
- Beats automatically (you don't think about it)
- Beats at a steady rhythm
- Keeps beating forever (until you stop!)

555 Astable:
- Pulses automatically (charging/discharging)
- Pulses at a steady rhythm (controlled by R and C)
- Keeps pulsing forever (until power OFF!)
```

**Output pulse = LED blinks**
- HIGH (charging) = LED ON
- LOW (discharging) = LED OFF
- Repeats automatically!

---

## How the Blinker Circuit Works: 4-Step Cycle

### Step 1: Capacitor Charging (LED OFF)
```
Battery pushes current through R1 + R2
         ↓
Capacitor slowly fills up with charge
         ↓
LED stays OFF while charging
         ↓
Continue until capacitor reaches 2/3 VCC (6V)
```

### Step 2: Threshold Reached! (555 Switches ON!)
```
Capacitor voltage = 2/3 VCC (6V)
         ↓
Pin 6 detects threshold → sends signal to 555 brain
         ↓
Internal switch FLIPS ON
         ↓
Output goes HIGH → LED LIGHTS UP!
```

### Step 3: Capacitor Discharging (LED ON)
```
Internal discharge switch opens
         ↓
Capacitor drains through R2 (faster than charging!)
         ↓
LED stays ON while discharging
         ↓
Continue until capacitor drops to 1/3 VCC (3V)
```

### Step 4: Lower Threshold Reached! (555 Switches OFF!)
```
Capacitor voltage = 1/3 VCC (3V)
         ↓
Pin 2 detects trigger → sends signal to 555 brain
         ↓
Internal switch FLIPS OFF
         ↓
Output goes LOW → LED goes DARK!
         ↓
Back to Step 1... cycle repeats FOREVER!
```

---

## The Bucket Analogy: Fill, Empty, Repeat!

Imagine a magical bucket with a trap door:

```
FILLING PHASE (capacitor charges):
  ┌─────────────┐
  │    ▒▒▒      │ ← Narrow fill hose = slow
  │ ▒▒▒ ▒▒▒     │ (R1 + R2 resistors)
  │▒▒▒▒▒ ▒▒▒▒   │
  │▒▒▒▒▒▒▒▒▒▒───→ 2/3 full = TRAP DOOR OPENS!
  └─────────────┘

EMPTYING PHASE (capacitor discharges):
  ┌─────────────┐
  │      ▒▒▒▒   │ ← Wide drain pipe = fast
  │    ▒▒▒▒▒    │ (R2 resistor only)
  │  ▒▒▒▒▒▒     │
  │▒▒───────────→ 1/3 empty = DOOR CLOSES!
  └─────────────┘
  (back to filling...)
```

---

## The 555 Astable Circuit

```
Simple Astable Blinker:

        +9V
         |
      ┌──┴──┐
      │  R1 │ 1k-ohm
      └──┬──┘
         ├─────────→ Pin 7 (DISCHARGE)
      ┌──┴──┐
      │  R2 │ 10k-ohm
      └──┬──┘
         ├─────────→ Pin 6 (THRESHOLD)
         │          & Pin 2 (TRIGGER)
      ┌──┴──┐
      │ C1  │ 47µF capacitor
      └──┬──┘
         │
        GND

Pin 3 (OUTPUT) → 330Ω resistor → LED → GND
Pin 1 → GND
Pin 8 → +9V
```

---

## Blink Speed Formula

```
Frequency (how fast it blinks):
f = 1.44 / ((R1 + 2×R2) × C)

Time ON:
T_on = 0.693 × (R1 + R2) × C

Time OFF:
T_off = 0.693 × R2 × C

Period (total):
T = T_on + T_off

Example:
R1 = 1k, R2 = 10k, C = 47µF

f = 1.44 / ((1000 + 2×10000) × 0.000047)
f = 1.44 / (21000 × 0.000047)
f ≈ 1.45 Hz = blink about once per second ✓
```

---

## Component Values & Their Effects

| Component | Value | Effect on Blinking |
|-----------|-------|-------------------|
| R1 | Small (1k) | Charges FASTER → faster overall |
| R1 | Large (100k) | Charges SLOWER → slower overall |
| R2 | Small (1k) | Discharges FASTER → asymmetrical |
| R2 | Large (100k) | Discharges SLOWER → longer ON time |
| C (capacitor) | Small (10µF) | Fast charge/discharge → fast blink |
| C (capacitor) | Large (100µF) | Slow charge/discharge → slow blink |

**Rules of thumb:**
- **Want faster blinking?** Use smaller R and C values
- **Want slower blinking?** Use larger R and C values
- **Want equal ON/OFF time?** Make R1 ≈ R2

---

## Common Astable Circuits

### Fast Blinker (like a heartbeat):
```
R1 = 1k, R2 = 1k, C = 10µF
Frequency ≈ 7 Hz (blinks 7 times per second)
```

### Medium Blinker (normal lighthouse):
```
R1 = 1k, R2 = 10k, C = 47µF
Frequency ≈ 1.5 Hz (blinks once per second)
```

### Slow Blinker (like a warning beacon):
```
R1 = 10k, R2 = 100k, C = 100µF
Frequency ≈ 0.07 Hz (blinks every ~15 seconds)
```

---

## Building the Astable Circuit

**Step-by-step:**
1. Mount 555 IC on breadboard (notch UP!)
2. Wire Pin 8 to +9V rail
3. Wire Pin 1 to GND rail
4. Place R1 (1k): +9V → Pin 7
5. Place R2 (10k): Pin 7 → Pin 6/2 junction
6. Place C1 (47µF): Pin 6/2 junction → GND
7. Small capacitor C2 (0.01µF): Pin 5 → GND (noise reduction)
8. Wire Pin 4 (RESET) to +9V
9. Wire Pin 3 (OUTPUT) through 330Ω resistor to LED
10. LED other leg to GND

✓ **Power ON → watch it blink!**

---

## Troubleshooting

| Problem | Likely Cause | Fix |
|---------|-------------|-----|
| No blinking (LED always OFF) | Capacitor polarity wrong or pin connections | Check C1 polarity (+), verify Pin 6/2 junction |
| No blinking (LED always ON) | Pin 2 not connected to capacitor | Connect Pin 2 to the capacitor junction |
| Blinks too fast | Resistor or capacitor value too small | Use larger values (R1/R2 or C) |
| Blinks too slow | Resistor or capacitor value too large | Use smaller values |
| LED very dim | Resistor before LED too big | Use 220Ω or 330Ω, not 1k+ |

---

## Key Takeaways

1. **Astable = automatic, continuous oscillation** (no user input needed!)
2. **Charging up to 2/3 VCC** → Output goes HIGH
3. **Discharging to 1/3 VCC** → Output goes LOW
4. **R1 + R2 control charge time** (affects ON/OFF duration)
5. **C (capacitor) is your timer** (bigger C = slower blink)
6. **Use formula to calculate frequency** if you need exact timing

---

## Challenge Projects

**Vary the blink speed:**
- Measure voltage on Pin 3 with your Wand (should pulse 0V to 9V)
- Change R values and watch blink speed change
- Calculate predicted frequency, compare to actual

**Next project:**
- Monostable mode (one-shot pulse)
- Logic gates for counting
- LED chaser patterns!

---

*Print this page. Keep the circuit diagram handy for reference!* ⚡

